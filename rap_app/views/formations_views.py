import csv
from django.contrib.auth import get_user_model
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.db.models import Q, F, ExpressionWrapper, IntegerField, FloatField
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.utils import timezone
from django.db import transaction
from django.shortcuts import get_object_or_404, redirect
from datetime import datetime, date  # ✅ Ajoute cette ligne en haut du fichier
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
from django.views import View
from django.views.decorators.http import require_POST
from datetime import datetime

from django.contrib import messages
from django.http import HttpResponseBadRequest

from ..models.partenaires import Partenaire
from ..models import Formation


from ..models.centres import Centre
from ..models.statut import Statut
from ..models.types_offre import TypeOffre

from ..models.commentaires import Commentaire, User
from ..models import Formation, HistoriqueFormation
from .base_views import BaseListView, BaseDetailView, BaseCreateView, BaseUpdateView, BaseDeleteView

User = get_user_model()


class FormationListView(BaseListView):
    """Vue listant toutes les formations avec options de filtrage et indicateurs dynamiques."""
    model = Formation
    context_object_name = 'formations'
    template_name = 'formations/formation_list.html'
    paginate_by = 10  # ✅ Ajout de la pagination

    def get_queryset(self):
        """Récupère la liste des formations avec options de filtrage et recherche par mots-clés."""
        today = timezone.now().date()

        queryset = Formation.objects.select_related('centre', 'type_offre', 'statut').annotate(
            total_places=ExpressionWrapper(
                F('prevus_crif') + F('prevus_mp'), output_field=IntegerField()
            ),
            total_inscrits=ExpressionWrapper(
                F('inscrits_crif') + F('inscrits_mp'), output_field=IntegerField()
            ),
            places_restantes_crif=ExpressionWrapper(
                F('prevus_crif') - F('inscrits_crif'), output_field=IntegerField()
            ),
            places_restantes_mp=ExpressionWrapper(
                F('prevus_mp') - F('inscrits_mp'), output_field=IntegerField()
            ),
            taux_saturation=ExpressionWrapper(
                100.0 * (F('inscrits_crif') + F('inscrits_mp')) / 
                (F('prevus_crif') + F('prevus_mp')), output_field=FloatField()
            ),
            taux_transformation=ExpressionWrapper(
                100.0 * (F('inscrits_crif') + F('inscrits_mp')) / 
                (F('nombre_candidats') + 0.0001), output_field=FloatField()
            ),
        )

        # 🔍 Recherche et filtres
        mot_cle = self.request.GET.get('q', '').strip()
        if mot_cle:
            queryset = queryset.filter(
                Q(nom__icontains=mot_cle) |
                Q(num_offre__icontains=mot_cle) |
                Q(centre__nom__icontains=mot_cle) |
                Q(type_offre__nom__icontains=mot_cle) |
                Q(statut__nom__icontains=mot_cle)
            )

        centre_id = self.request.GET.get('centre', '').strip()
        type_offre_id = self.request.GET.get('type_offre', '').strip()
        statut_id = self.request.GET.get('statut', '').strip()
        periode = self.request.GET.get('periode', '').strip()

        if centre_id:
            queryset = queryset.filter(centre_id=centre_id)
        if type_offre_id:
            queryset = queryset.filter(type_offre_id=type_offre_id)
        if statut_id:
            queryset = queryset.filter(statut_id=statut_id)
        if periode:
            if periode == 'active':
                queryset = queryset.filter(start_date__lte=today, end_date__gte=today)
            elif periode == 'a_venir':
                queryset = queryset.filter(start_date__gt=today)
            elif periode == 'terminee':
                queryset = queryset.filter(end_date__lt=today)
            elif periode == 'a_recruter':
                queryset = queryset.filter(total_places__gt=F('total_inscrits'))

        return queryset

    def get_context_data(self, **kwargs):
        """Ajoute les statistiques, les centres, types d'offres et statuts au contexte pour le template."""
        context = super().get_context_data(**kwargs)

        context['stats'] = [
            (Formation.objects.count(), "Total formations", "primary", "fa-graduation-cap"),
            (Formation.objects.formations_actives().count(), "Formations Actives", "success", "fa-check-circle"),
            (Formation.objects.formations_a_venir().count(), "Formations À venir", "info", "fa-clock"),
            (Formation.objects.formations_terminees().count(), "Formations Terminées", "secondary", "fa-times-circle"),
            (Formation.objects.formations_a_recruter().count(), "Formations À recruter", "warning", "fa-users"),
        ]

        context['centres'] = Centre.objects.all()
        context['types_offre'] = TypeOffre.objects.all()
        context['statuts'] = Statut.objects.all()

        context['filters'] = {
            'centre': self.request.GET.get('centre', ''),
            'type_offre': self.request.GET.get('type_offre', ''),
            'statut': self.request.GET.get('statut', ''),
            'periode': self.request.GET.get('periode', ''),
            'q': self.request.GET.get('q', ''),
        }

        return context
        




class ModifierInscritsView(View):
    """Vue pour modifier les inscrits CRIF, MP, nombre de candidats, entretiens et prévus CRIF/MP via AJAX."""

    def post(self, request, formation_id, *args, **kwargs):  
        try:
            data = json.loads(request.body)
            field = data.get("field")
            value = data.get("value")

            # ✅ Ajout des nouveaux champs autorisés
            if field not in ["inscrits_crif", "inscrits_mp", "nombre_candidats", "nombre_entretiens", "prevus_crif", "prevus_mp"]:
                return JsonResponse({"success": False, "error": "Champ invalide"}, status=400)

            formation = Formation.objects.get(pk=formation_id)

            # ✅ Vérifier la permission de modification
            if not request.user.has_perm("rap_app.change_formation"):
                return JsonResponse({"success": False, "error": "Permission refusée"}, status=403)

            # ✅ Mettre à jour la valeur du champ
            setattr(formation, field, int(value))
            formation.save()

            return JsonResponse({"success": True, "message": "Mise à jour réussie", "new_value": value})

        except Formation.DoesNotExist:
            return JsonResponse({"success": False, "error": "Formation non trouvée"}, status=404)
        except json.JSONDecodeError:
            return JsonResponse({"success": False, "error": "Format JSON invalide"}, status=400)
        except Exception as e:
            return JsonResponse({"success": False, "error": str(e)}, status=500)

class FormationDetailView(BaseDetailView):
    """Vue affichant les détails d'une formation"""
    model = Formation
    context_object_name = 'formation'
    template_name = 'formations/formation_detail.html'

    def get_context_data(self, **kwargs):
        """Ajoute les commentaires, evenements et autres données au contexte"""
        context = super().get_context_data(**kwargs)
        formation = self.object

    # Récupération du dernier commentaire avec toutes ses infos
        dernier_commentaire = formation.get_commentaires().order_by('-created_at').first()

    # ✅ Partenaires associées
        context['partenaires'] = formation.partenaires.all()

        # ✅ Partenaires disponibles (celles qui ne sont pas encore associées)
        context['partenaires_disponibles'] = Partenaire.objects.exclude(id__in=formation.partenaires.values_list('id', flat=True))


        context['dernier_commentaire'] = dernier_commentaire  # ✅ Ajout du dernier commentaire complet
        context['commentaires'] = formation.get_commentaires().order_by('-created_at')
        context['evenements'] = formation.get_evenements().order_by('-event_date')
        context['documents'] = formation.documents.all().order_by('-created_at')
        context['partenaires'] = formation.get_partenaires()
        context['historique'] = formation.historique_formations.order_by('-created_at')[:10]

        # ✅ Ajout des valeurs calculées pour affichage
        context['places_restantes_crif'] = formation.get_places_restantes_crif()
        context['places_restantes_mp'] = formation.get_places_restantes_mp()
        context['taux_saturation'] = formation.get_taux_saturation()

        return context
    
    def post(self, request, *args, **kwargs):
            """
            Gère l'ajout de commentaires, événements, documents et partenaires via POST.
            L'action est déterminée par le champ `action` du formulaire.
            """
            formation = self.get_object()
            action = request.POST.get('action')

            if action == 'add_commentaire':
                return self.add_commentaire(request, formation)

            elif action == 'add_evenement':
                return self.add_evenement(request, formation)

            elif action == 'add_document':
                return self.add_document(request, formation)

            elif action == 'add_partenaire':
                return self.add_partenaire(request, formation)

            return HttpResponseBadRequest("Action non valide.")

    def add_commentaire(self, request, formation):
        """Ajoute un commentaire à la formation"""
        contenu = request.POST.get('contenu', '').strip()

        if not contenu:
            return HttpResponseBadRequest("Le commentaire ne peut pas être vide.")

        formation.add_commentaire(request.user, contenu)
        messages.success(request, "Commentaire ajouté avec succès.")
        return redirect(self.request.path)
        

    def add_evenement(self, request, formation):
        """Ajoute un événement à la formation"""
        type_evenement = request.POST.get('type_evenement', '').strip()
        date = request.POST.get('date')
        details = request.POST.get('details', '').strip()
        description_autre = request.POST.get('description_autre', '').strip()

        if not type_evenement or not date:
            return HttpResponseBadRequest("Le type et la date de l'événement sont obligatoires.")

    # ✅ On appelle la méthode avec les bons arguments (4 au total)
        formation.add_evenement(type_evenement, date, details, description_autre)
        messages.success(request, "Événement ajouté avec succès.")
        return redirect(self.request.path)

    def add_document(self, request, formation):
        """Ajoute un document à la formation."""
        nom = request.POST.get('nom', '').strip()
        fichier = request.FILES.get('fichier')

        if not nom or not fichier:
            return HttpResponseBadRequest("Le nom et le fichier sont obligatoires.")

        # ✅ Ajout du document directement avec `.create()`
        formation.documents.create(
            utilisateur=request.user, 
            nom_fichier=nom, 
            fichier=fichier
        )

        messages.success(request, "Document ajouté avec succès.")
        return redirect(self.request.path)

class FormationCreateView(PermissionRequiredMixin, BaseCreateView):
    """Vue permettant de créer une nouvelle formation"""
    model = Formation
    permission_required = 'rap_app.add_formation'
    template_name = 'formations/formation_form.html'
    fields = [
        'nom', 'centre', 'type_offre', 'statut', 'start_date', 'end_date',
        'num_kairos', 'num_offre', 'num_produit', 'prevus_crif', 'prevus_mp',
        'inscrits_crif', 'inscrits_mp', 'assistante', 'cap', 'convocation_envoie',
        'entresformation', 'nombre_candidats', 'nombre_entretiens'
    ]

    def form_valid(self, form):
        """Associe l'utilisateur connecté à la formation et crée un historique"""
        with transaction.atomic():
            form.instance.utilisateur = self.request.user
            response = super().form_valid(form)

            # 📌 Création d'un historique
            HistoriqueFormation.objects.create(
                formation=self.object,
                utilisateur=self.request.user,
                action='création',
                details={'nom': self.object.nom}
            )

            return response

    def get_success_url(self):
        return reverse_lazy('formation-detail', kwargs={'pk': self.object.pk})


class FormationUpdateView(PermissionRequiredMixin, BaseUpdateView):
    """Vue permettant de modifier une formation existante"""
    model = Formation
    permission_required = 'rap_app.change_formation'
    template_name = 'formations/formation_form.html'
    fields = FormationCreateView.fields  # ✅ Réutilisation des champs

    def form_valid(self, form):
        """Détecte les modifications et met à jour l'historique"""
        with transaction.atomic():
            old_obj = Formation.objects.get(pk=self.object.pk)
            response = super().form_valid(form)

            # ✅ Comparaison des champs modifiés
            changes = {}
            for field in self.fields:
                old_value, new_value = getattr(old_obj, field), getattr(self.object, field)

                # 🔹 Si la valeur est une date, la convertir en string au format ISO
                # ✅ Correction de la conversion des dates dans form_valid()
                if isinstance(old_value, (datetime, date)):  
                    old_value = old_value.isoformat() if old_value else None
                if isinstance(new_value, (datetime, date)):  
                    new_value = new_value.isoformat() if new_value else None

                if old_value != new_value:
                    changes[field] = {'ancien': old_value, 'nouveau': new_value}

            # 📌 Enregistre l'historique si des changements ont été détectés
            if changes:
                HistoriqueFormation.objects.create(
                    formation=self.object,
                    utilisateur=self.request.user,
                    action='modification',
                    details=changes
                )

            return response

    def get_success_url(self):
        return reverse_lazy('formation-detail', kwargs={'pk': self.object.pk})


class FormationDeleteView(PermissionRequiredMixin, BaseDeleteView):
    """Vue permettant de supprimer une formation"""
    model = Formation
    permission_required = 'rap_app.delete_formation'
    success_url = reverse_lazy('formation-list')
    template_name = 'formations/formation_confirm_delete.html'


class FormationAddCommentView(BaseCreateView):
    """Vue permettant d'ajouter un commentaire à une formation"""
    model = Commentaire
    fields = ['contenu']
    template_name = 'formations/formation_add_comment.html'

    def dispatch(self, request, *args, **kwargs):
        """Vérifie que la formation existe avant d'ajouter un commentaire"""
        self.formation = get_object_or_404(Formation, pk=self.kwargs['pk'])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        """Associe le commentaire à la formation et à l'utilisateur"""
        form.instance.formation = self.formation
        form.instance.utilisateur = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('formation-detail', kwargs={'pk': self.formation.pk})

class ExportFormationsExcelView(View):
    def get(self, request, *args, **kwargs):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="formations_export.csv"'

        writer = csv.writer(response)
        writer.writerow([
            "Nom", "Centre", "num_offre", "Type d'offre", "Statut", "N° Kairos", 
            "Dates", "Assistante", "Candidats", "Entretiens",
            "Prévus CRIF", "Prévus MP", "Inscrits CRIF", "Inscrits MP",
            "Places restantes CRIF", "Places restantes MP",
            "Transformation", "Saturation"
        ])

        formations = Formation.objects.all()
        for formation in formations:
            writer.writerow([
                formation.nom, 
                formation.centre.nom if formation.centre else "-",
                formation.num_offre if formation.num_offre else "-",
                formation.type_offre.nom if formation.type_offre else "-",
                formation.statut.nom if formation.statut else "-",
                formation.num_kairos if formation.num_kairos else "-",
                f"{formation.start_date} - {formation.end_date}",
                formation.assistante if formation.assistante else "-",
                formation.nombre_candidats,
                formation.nombre_entretiens,
                formation.prevus_crif,
                formation.prevus_mp,
                formation.inscrits_crif,
                formation.inscrits_mp,
                formation.get_places_restantes_crif(),  # ✅ Appel correct
                formation.get_places_restantes_mp(),  # ✅ Appel correct
                formation.get_taux_saturation(),  # ✅ Ajout du taux de saturation
                formation.get_taux_saturation()  # ✅ Transformation (ajuster si différent)
            ])

        return response
    



