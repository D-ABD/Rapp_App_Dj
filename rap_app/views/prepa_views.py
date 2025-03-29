import logging
from datetime import datetime, timedelta
from django.views.generic import CreateView, TemplateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import Sum
from django.shortcuts import get_object_or_404, redirect
from django.utils import timezone
from django import forms
from django.utils.timezone import now
from django.db.models import F, IntegerField, ExpressionWrapper

from ..models.prepacomp import NOMS_ATELIERS, NOMS_MOIS, Semaine, PrepaCompGlobal
from ..models.centres import Centre
from ..views.base_views import (
    BaseListView, BaseDetailView, BaseCreateView,
    BaseUpdateView, BaseDeleteView, CustomLoginRequiredMixin
)

logger = logging.getLogger(__name__)

def get_dates_from_week(annee, semaine):
    try:
        lundi = datetime.strptime(f'{annee}-W{semaine}-1', "%G-W%V-%u").date()
        dimanche = lundi + timedelta(days=6)
        return lundi, dimanche
    except Exception:
        return None, None

# ---- Dashboard ----
class PrepaHomeView(CustomLoginRequiredMixin, TemplateView):
    template_name = 'prepa/prepa_home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        annee = timezone.now().year
        context['annee_courante'] = annee  # Ajout de l'année courante au contexte
        
        centre = Centre.objects.first()
        objectif_global = PrepaCompGlobal.objectif_annuel_global()
        adhesions_globales = PrepaCompGlobal.objects.filter(
            annee=annee
        ).aggregate(total=Sum('adhesions'))['total'] or 0

        try:
            context['semaine_courante'] = Semaine.creer_semaine_courante(centre)
            
            # Récupérer ou créer le bilan global pour l'année en cours
            try:
                bilan_global = PrepaCompGlobal.objects.get(annee=annee, centre=centre)
            except PrepaCompGlobal.DoesNotExist:
                # Créer un bilan global par défaut s'il n'existe pas
                bilan_global = PrepaCompGlobal(
                    annee=annee,
                    centre=centre,
                    total_candidats=0,
                    total_prescriptions=0,
                    adhesions=0,
                    total_presents=0,
                    total_places_ouvertes=0
                )
                bilan_global.save()
                logger.info(f"Création automatique d'un bilan global pour {annee} et le centre {centre}")
            
            context['bilan_global'] = bilan_global
            context['mois_annee'] = PrepaCompGlobal.stats_par_mois(annee, centre)
            context['objectif_annuel_global'] = objectif_global
            context['objectif_hebdo_global'] = PrepaCompGlobal.objectif_hebdo_global(annee)
            context['adhesions_globales'] = adhesions_globales
            context['stats_ateliers'] = Semaine.stats_globales_par_atelier(annee)

            context['taux_objectif_global'] = round(
                (adhesions_globales / objectif_global) * 100, 1
            ) if objectif_global else 0

            context['objectifs_par_centre'] = [
                {
                    **o,
                    'ecart': (o['objectif_calculé'] or 0) - (o['objectif_annuel_defini'] or 0),
                    'pourcentage': round((o['objectif_calculé'] or 0) / (o['objectif_annuel_defini'] or 1) * 100, 0)
                    if o['objectif_annuel_defini'] else 0
                }
                for o in PrepaCompGlobal.objectifs_par_centre(annee)
            ]

        except Exception as e:
            logger.error(f"Erreur chargement PrepaHomeView : {e}")
            messages.error(self.request, f"Erreur lors du chargement du tableau de bord : {e}")
            
            # Valeurs par défaut pour éviter les erreurs dans le template
            context['semaine_courante'] = None
            context['bilan_global'] = None
            context['mois_annee'] = []
            context['objectif_annuel_global'] = 0
            context['objectif_hebdo_global'] = 0
            context['adhesions_globales'] = 0
            context['taux_objectif_global'] = 0
            context['objectifs_par_centre'] = []
            context['stats_ateliers'] = []

        return context
    
# ---- Semaines ----
class PrepaSemaineListView(BaseListView):
    model = Semaine
    template_name = 'prepa/prepa_semaine_list.html'
    context_object_name = 'semaines'
    ordering = ['-date_debut_semaine']
    paginate_by = 10

    def get_queryset(self):
        qs = super().get_queryset()
        filtre = self.request.GET
        if filtre.get('centre'):
            qs = qs.filter(centre__id=filtre.get('centre'))
        if filtre.get('annee'):
            qs = qs.filter(annee=filtre.get('annee'))
        if filtre.get('mois'):
            qs = qs.filter(mois=filtre.get('mois'))
        if filtre.get('semaine'):
            qs = qs.filter(numero_semaine=filtre.get('semaine'))
            
        # Enrichissement des semaines avec des données calculées
        semaines = []
        for semaine in qs:
            # Calcul du taux d'adhésion (nombre_adhesions / nombre_presents_ic)
            taux_adhesion = 0
            if semaine.nombre_presents_ic > 0:
                taux_adhesion = (semaine.nombre_adhesions / semaine.nombre_presents_ic) * 100
            
            # Préparation des seuils pour les badges
            seuil_80_pourcent = 0
            seuil_50_pourcent = 0
            if semaine.nombre_presents_ic > 0:
                seuil_80_pourcent = semaine.nombre_presents_ic * 0.8
                seuil_50_pourcent = semaine.nombre_presents_ic * 0.5
            
            # Attacher ces données calculées à la semaine
            semaine.taux_adhesion = taux_adhesion
            semaine.seuil_80_pourcent = seuil_80_pourcent
            semaine.seuil_50_pourcent = seuil_50_pourcent
            
            semaines.append(semaine)
        
        return semaines

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        annee = self.request.GET.get('annee') or timezone.now().year
        context['centres'] = Centre.objects.all()
        context['annees'] = Semaine.objects.values_list('annee', flat=True).distinct().order_by('-annee')
        context['NOMS_MOIS'] = NOMS_MOIS
        context['objectif_annuel_global'] = PrepaCompGlobal.objectif_annuel_global()
        context['objectif_hebdo_global'] = PrepaCompGlobal.objectif_hebdo_global(annee)

        # Nouvelle version : suppression des doublons en Python
        semaines_raw = Semaine.objects.order_by('annee', 'numero_semaine', 'date_debut_semaine')
        semaines_uniques = {}
        for s in semaines_raw:
            if s.numero_semaine not in semaines_uniques:
                semaines_uniques[s.numero_semaine] = {
                    'numero_semaine': s.numero_semaine,
                    'date_debut_semaine': s.date_debut_semaine,
                    'date_fin_semaine': s.date_fin_semaine,
                }
        context["semaines_disponibles"] = list(semaines_uniques.values())


        
        # Obtenir et enrichir les objectifs par centre
        objectifs_par_centre = PrepaCompGlobal.objectifs_par_centre(annee)
        
        # Calculer le total des objectifs (à faire ici plutôt que dans le template)
        total_objectif_annuel = sum(o['objectif_annuel_defini'] for o in objectifs_par_centre)
        total_objectif_hebdo = sum(o['objectif_hebdo'] for o in objectifs_par_centre)
        total_objectif_mensuel = total_objectif_hebdo * 4  # Calculer l'objectif mensuel ici
        
        context['objectifs_par_centre'] = objectifs_par_centre
        context['total_objectif_annuel'] = total_objectif_annuel
        context['total_objectif_hebdo'] = total_objectif_hebdo
        context['total_objectif_mensuel'] = total_objectif_mensuel
        
        return context
    
class PrepaSemaineDetailView(BaseDetailView):
    model = Semaine
    template_name = 'prepa/prepa_semaine_detail.html'
    context_object_name = 'semaine'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        semaine = self.get_object()
        context['taux_transformation'] = semaine.taux_transformation()
        context['pourcentage_objectif'] = semaine.pourcentage_objectif()
        context['ateliers'] = semaine.ateliers_nommés
        context['nom_mois'] = semaine.nom_mois()
        return context


class PrepaSemaineCreateView(BaseCreateView):
    model = Semaine
    template_name = 'prepa/prepa_semaine_form.html'
    success_url = reverse_lazy('prepa_semaine_list')

    # Retirer les champs JSON du formulaire
    fields = [
        'centre', 'objectif_annuel_prepa', 'objectif_mensuel_prepa', 'objectif_hebdo_prepa',
        'nombre_places_ouvertes', 'nombre_prescriptions', 'nombre_adhesions',
        'nombre_presents_ic'
        # Retirez 'departements' et 'nombre_par_atelier'
    ]

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        annee = now().year
        semaines = [
            (str(num), f"Semaine {num} (du {get_dates_from_week(annee, num)[0].strftime('%d/%m')} au {get_dates_from_week(annee, num)[1].strftime('%d/%m')})")
            for num in range(1, 54) if get_dates_from_week(annee, num)[0]
        ]
        form.fields['numero_semaine'] = forms.ChoiceField(
            choices=semaines,
            label="Numéro de semaine",
            widget=forms.Select(attrs={'class': 'form-select'})
        )
        
        # Cacher les champs d'objectifs
        form.fields['objectif_annuel_prepa'].widget = forms.HiddenInput()
        form.fields['objectif_mensuel_prepa'].widget = forms.HiddenInput()
        form.fields['objectif_hebdo_prepa'].widget = forms.HiddenInput()
        
        # Ajouter des champs pour les départements
        DEPARTEMENTS_IDF = ['75', '77', '78', '91', '92', '93', '94', '95']
        for dept in DEPARTEMENTS_IDF:
            field_name = f'dept_{dept}'
            form.fields[field_name] = forms.IntegerField(
                label=f'Département {dept}',
                required=False,
                min_value=0,
                initial=0,
                widget=forms.NumberInput(attrs={'class': 'form-control'})
            )
        
        # Ajouter des champs pour les ateliers
        for code, nom in NOMS_ATELIERS.items():
            field_name = f'atelier_{code}'
            form.fields[field_name] = forms.IntegerField(
                label=nom,
                required=False,
                min_value=0,
                initial=0,
                widget=forms.NumberInput(attrs={'class': 'form-control'})
            )
            
        return form

    def form_valid(self, form):
        # Traiter les données du formulaire normalement
        result = super().form_valid(form)
        
        # Collecter les données des départements
        DEPARTEMENTS_IDF = ['75', '77', '78', '91', '92', '93', '94', '95']
        departements_data = {}
        for dept in DEPARTEMENTS_IDF:
            field_name = f'dept_{dept}'
            value = self.request.POST.get(field_name)
            if value and int(value) > 0:
                departements_data[dept] = int(value)
        
        # Collecter les données des ateliers
        ateliers_data = {}
        for code in NOMS_ATELIERS.keys():
            field_name = f'atelier_{code}'
            value = self.request.POST.get(field_name)
            if value and int(value) > 0:
                ateliers_data[code] = int(value)
        
        # Mettre à jour l'instance avec les données JSON
        self.object.departements = departements_data
        self.object.nombre_par_atelier = ateliers_data
        self.object.save()
        
        return result

    def get_initial(self):
        initial = super().get_initial()
        # Initialiser les objectifs
        centre_id = self.request.POST.get('centre') or self.request.GET.get('centre')
        try:
            centre = Centre.objects.get(pk=int(centre_id))
            initial['objectif_annuel_prepa'] = centre.objectif_annuel_prepa or 0
            initial['objectif_hebdo_prepa'] = centre.objectif_hebdomadaire_prepa or 0
            initial['objectif_mensuel_prepa'] = (centre.objectif_hebdomadaire_prepa or 0) * 4
        except:
            initial['objectif_annuel_prepa'] = 0
            initial['objectif_hebdo_prepa'] = 0
            initial['objectif_mensuel_prepa'] = 0
        return initial

class PrepaSemaineUpdateView(BaseUpdateView):
    model = Semaine
    template_name = 'prepa/prepa_semaine_form.html'
    context_object_name = 'semaine'
    success_url = reverse_lazy('prepa_semaine_list')

    # Retirer les champs JSON du formulaire
    fields = [
        'centre', 'objectif_annuel_prepa', 'objectif_mensuel_prepa', 'objectif_hebdo_prepa',
        'nombre_places_ouvertes', 'nombre_prescriptions', 'nombre_adhesions',
        'nombre_presents_ic'
        # Retirez 'departements' et 'nombre_par_atelier'
    ]
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        
        # Cacher les champs d'objectifs
        form.fields['objectif_annuel_prepa'].widget = forms.HiddenInput()
        form.fields['objectif_mensuel_prepa'].widget = forms.HiddenInput()
        form.fields['objectif_hebdo_prepa'].widget = forms.HiddenInput()
        
        # Ajouter des champs pour les départements
        DEPARTEMENTS_IDF = ['75', '77', '78', '91', '92', '93', '94', '95']
        semaine = self.get_object()
        departements_data = semaine.departements or {}
        
        for dept in DEPARTEMENTS_IDF:
            field_name = f'dept_{dept}'
            form.fields[field_name] = forms.IntegerField(
                label=f'Département {dept}',
                required=False,
                min_value=0,
                initial=departements_data.get(dept, 0),
                widget=forms.NumberInput(attrs={'class': 'form-control'})
            )
        
        # Ajouter des champs pour les ateliers
        ateliers_data = semaine.nombre_par_atelier or {}
        for code, nom in NOMS_ATELIERS.items():
            field_name = f'atelier_{code}'
            form.fields[field_name] = forms.IntegerField(
                label=nom,
                required=False,
                min_value=0,
                initial=ateliers_data.get(code, 0),
                widget=forms.NumberInput(attrs={'class': 'form-control'})
            )
            
        return form
    
    def form_valid(self, form):
        # Traiter les données du formulaire normalement
        result = super().form_valid(form)
        
        # Collecter les données des départements
        DEPARTEMENTS_IDF = ['75', '77', '78', '91', '92', '93', '94', '95']
        departements_data = {}
        for dept in DEPARTEMENTS_IDF:
            field_name = f'dept_{dept}'
            value = self.request.POST.get(field_name)
            if value and int(value) > 0:
                departements_data[dept] = int(value)
        
        # Collecter les données des ateliers
        ateliers_data = {}
        for code in NOMS_ATELIERS.keys():
            field_name = f'atelier_{code}'
            value = self.request.POST.get(field_name)
            if value and int(value) > 0:
                ateliers_data[code] = int(value)
        
        # Mettre à jour l'instance avec les données JSON
        self.object.departements = departements_data
        self.object.nombre_par_atelier = ateliers_data
        self.object.save()
        
        return result

class PrepaSemaineUpdateView(BaseUpdateView):
    model = Semaine
    template_name = 'prepa/prepa_semaine_form.html'
    context_object_name = 'semaine'
    success_url = reverse_lazy('prepa_semaine_list')

    fields = [
        'centre', 'objectif_annuel_prepa', 'objectif_mensuel_prepa', 'objectif_hebdo_prepa',
        'nombre_places_ouvertes', 'nombre_prescriptions', 'nombre_adhesions',
        'nombre_presents_ic', 'departements', 'nombre_par_atelier'
    ]
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        
        # Cacher les champs d'objectifs
        form.fields['objectif_annuel_prepa'].widget = forms.HiddenInput()
        form.fields['objectif_mensuel_prepa'].widget = forms.HiddenInput()
        form.fields['objectif_hebdo_prepa'].widget = forms.HiddenInput()
        
        return form
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        annee = now().year
        context['objectif_annuel_global'] = PrepaCompGlobal.objectif_annuel_global()
        context['objectif_hebdo_global'] = PrepaCompGlobal.objectif_hebdo_global(annee)
        
        # Obtenir et enrichir les objectifs par centre
        objectifs_par_centre = PrepaCompGlobal.objectifs_par_centre(annee)
        
        # Calculer le total des objectifs
        total_objectif_annuel = sum(o['objectif_annuel_defini'] for o in objectifs_par_centre)
        total_objectif_hebdo = sum(o['objectif_hebdo'] for o in objectifs_par_centre)
        total_objectif_mensuel = total_objectif_hebdo * 4
        
        context['objectifs_par_centre'] = objectifs_par_centre
        context['total_objectif_annuel'] = total_objectif_annuel
        context['total_objectif_hebdo'] = total_objectif_hebdo
        context['total_objectif_mensuel'] = total_objectif_mensuel
        
        return context
    

class PrepaSemaineDeleteView(BaseDeleteView):
    model = Semaine
    template_name = 'prepa/prepa_semaine_confirm_delete.html'
    context_object_name = 'semaine'
    success_url = reverse_lazy('prepa_semaine_list')


# ---- Bilan Global ----
from django.db.models import F, IntegerField, ExpressionWrapper

class PrepaGlobalListView(BaseListView):
    model = PrepaCompGlobal
    template_name = 'prepa/prepacompglobal_list.html'
    context_object_name = 'bilans'
    ordering = ['-annee']

    def get_queryset(self):
        # On ajoute un accès direct au centre lié
        qs = super().get_queryset().select_related("centre")
        
        # On annote avec :
        # - objectif_annuel : récupéré depuis Centre
        # - ecart : différence entre objectif et adhésions
        return qs.annotate(
            objectif_annuel=F("centre__objectif_annuel_prepa"),
            ecart=ExpressionWrapper(
                F("centre__objectif_annuel_prepa") - F("adhesions"),
                output_field=IntegerField()
            )
        )



class PrepaGlobalDetailView(BaseDetailView):
    model = PrepaCompGlobal
    template_name = 'prepa/prepacompglobal_detail.html'
    context_object_name = 'bilan'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        bilan = self.object
        centre = bilan.centre
        annee = bilan.annee

        # Objectifs globaux
        context['objectif_annuel_global'] = PrepaCompGlobal.objectif_annuel_global()
        context['objectif_hebdo_global'] = PrepaCompGlobal.objectif_hebdo_global(annee)
        context['objectif_annuel_centre'] = getattr(centre, 'objectif_annuel_prepa', 0)

        # Données mensuelles déjà enrichies avec 'mois_nom'
        context['mois'] = PrepaCompGlobal.stats_par_mois(annee=annee, centre=centre)

        # Synthèse annuelle pour ce centre
        context['total_adhesions'] = bilan.adhesions
        context['taux_objectif'] = bilan.taux_objectif_annee
        context['taux_transformation'] = bilan.taux_transformation

        # Objectifs par centre (utile pour comparaison ou affichage)
        context['objectifs_par_centre'] = PrepaCompGlobal.objectifs_par_centre(annee)

        return context



class PrepaGlobalCreateView(BaseCreateView):
    model = PrepaCompGlobal
    template_name = 'prepa/prepacompglobal_form.html'
    fields = ['centre', 'annee', 'total_candidats', 'total_prescriptions',
              'adhesions', 'total_presents', 'total_places_ouvertes']
    success_url = reverse_lazy('prepa_global_list')

class PrepaObjectifsView(CustomLoginRequiredMixin, TemplateView):
    """Vue pour gérer les objectifs des centres Prépa Comp"""
    template_name = 'prepa/prepa_objectifs_form.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        annee = self.kwargs.get('annee') or timezone.now().year
        
        # Liste des centres
        context['centres'] = Centre.objects.all().order_by('nom')
        context['annee_courante'] = annee
        
        # Objectifs globaux
        context['objectif_annuel_global'] = PrepaCompGlobal.objectif_annuel_global()
        context['objectif_hebdo_global'] = PrepaCompGlobal.objectif_hebdo_global(annee)
        
        # Données de réalisation
        adhesions_globales = Semaine.objects.filter(
            annee=annee
        ).aggregate(total=Sum('nombre_adhesions'))['total'] or 0
        
        context['adhesions_globales'] = adhesions_globales
        context['taux_objectif_global'] = (
            (adhesions_globales / context['objectif_annuel_global']) * 100
            if context['objectif_annuel_global'] else 0
        )
        
        # Réalisations par centre
        realisations_centres = {}
        for centre in context['centres']:
            adhesions = Semaine.objects.filter(
                centre=centre,
                annee=annee
            ).aggregate(total=Sum('nombre_adhesions'))['total'] or 0
            
            pourcentage = 0
            if centre.objectif_annuel_prepa:
                pourcentage = (adhesions / centre.objectif_annuel_prepa) * 100
                
            realisations_centres[centre.id] = {
                'adhesions': adhesions,
                'pourcentage': pourcentage
            }
            
        context['realisations_centres'] = realisations_centres
        
        return context
    
    def post(self, request, *args, **kwargs):
        """Traitement du formulaire pour enregistrer les objectifs"""
        centres = Centre.objects.all()
        
        for centre in centres:
            # Récupération des valeurs du formulaire
            objectif_annuel = request.POST.get(f'objectif_annuel_{centre.id}', 0)
            objectif_hebdo = request.POST.get(f'objectif_hebdo_{centre.id}', 0)
            
            # Conversion en entiers (avec valeur par défaut à 0)
            try:
                objectif_annuel = int(objectif_annuel)
            except (ValueError, TypeError):
                objectif_annuel = 0
                
            try:
                objectif_hebdo = int(objectif_hebdo)
            except (ValueError, TypeError):
                objectif_hebdo = 0
            
            # Si l'objectif hebdomadaire est vide, le calculer automatiquement
            if objectif_hebdo == 0 and objectif_annuel > 0:
                objectif_hebdo = objectif_annuel // 52
            
            # Mise à jour du centre
            centre.objectif_annuel_prepa = objectif_annuel
            centre.objectif_hebdomadaire_prepa = objectif_hebdo
            centre.save()
        
        messages.success(request, "Les objectifs ont été mis à jour avec succès.")
        return redirect('prepa_objectifs')