from django.urls import reverse_lazy
from django.db.models import Q
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views import View
from django.shortcuts import get_list_or_404
from django.contrib.auth import get_user_model
from django.views.generic import ListView
import csv
from django.http import HttpResponse
from ..models.commentaires import User

from ..models import Commentaire, Formation
from .base_views import BaseListView, BaseDetailView, BaseCreateView, BaseUpdateView, BaseDeleteView

User = get_user_model()

class CommentaireListView(BaseListView):
    """Vue listant tous les commentaires avec options de filtrage"""
    model = Commentaire
    context_object_name = 'commentaires'
    template_name = 'commentaires/commentaire_list.html'
    paginate_by = 20  # ✅ Ajout de la pagination

    def get_queryset(self):
        """
        Récupère la liste des commentaires avec possibilité de filtrage par :
        - Formation associée
        - Utilisateur
        - Contenu (recherche textuelle)
        """
        queryset = super().get_queryset().select_related('formation', 'utilisateur')

        # 🔍 Filtrage dynamique
        formation_id = self.request.GET.get('formation')
        utilisateur_id = self.request.GET.get('utilisateur')
        search_query = self.request.GET.get('q')

        if formation_id:
            queryset = queryset.filter(formation_id=formation_id)

        if utilisateur_id:
            queryset = queryset.filter(utilisateur_id=utilisateur_id)

        if search_query:
            queryset = queryset.filter(contenu__icontains=search_query)

        print(f"DEBUG: {queryset.count()} commentaires trouvés")  # ✅ Debugging

        return queryset  # ✅ Ajout du return pour éviter une erreur 500

    def get_context_data(self, **kwargs):
        """Ajoute les options de filtre au contexte pour le template"""
        context = super().get_context_data(**kwargs)

        # Ajout des filtres et options de filtrage
        context['filters'] = {
            'formation': self.request.GET.get('formation', ''),
            'utilisateur': self.request.GET.get('utilisateur', ''),
            'q': self.request.GET.get('q', ''),
        }

        # Liste des formations et utilisateurs pour les filtres
        context['formations'] = Formation.objects.all()
        context['utilisateurs'] = User.objects.all()  # ✅ Ajout de la liste des utilisateurs

        return context



class CommentaireDetailView(BaseDetailView):
    """Vue affichant les détails d'un commentaire"""
    model = Commentaire
    context_object_name = 'commentaire'
    template_name = 'commentaires/commentaire_detail.html'


class CommentaireCreateView(BaseCreateView):
    """Vue permettant de créer un nouveau commentaire"""
    model = Commentaire
    fields = ['formation', 'contenu', 'saturation']
    template_name = 'commentaires/commentaire_form.html'
    
    def get_initial(self):
        """Pré-remplit le formulaire avec la formation si spécifiée dans l'URL"""
        initial = super().get_initial()
        formation_id = self.request.GET.get('formation')
        if formation_id:
            initial['formation'] = formation_id
        return initial
    
    def form_valid(self, form):
        """Associe automatiquement l'utilisateur connecté au commentaire"""
        form.instance.utilisateur = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        """Redirige vers la formation associée après création"""
        return reverse_lazy('formation-detail', kwargs={'pk': self.object.formation.pk})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titre'] = "Ajouter un commentaire"
        return context


class CommentaireUpdateView(PermissionRequiredMixin, BaseUpdateView):
    """Vue permettant de modifier un commentaire existant"""
    model = Commentaire
    permission_required = 'rap_app.change_commentaire'
    fields = ['contenu', 'saturation']
    template_name = 'commentaires/commentaire_form.html'
    
    def get_success_url(self):
        """Redirige vers la formation associée après modification"""
        return reverse_lazy('formation-detail', kwargs={'pk': self.object.formation.pk})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titre'] = f"Modifier le commentaire du {self.object.created_at.strftime('%d/%m/%Y')}"
        return context


class CommentaireDeleteView(PermissionRequiredMixin, BaseDeleteView):
    """Vue permettant de supprimer un commentaire"""
    model = Commentaire
    permission_required = 'rap_app.delete_commentaire'
    template_name = 'commentaires/commentaire_confirm_delete.html'
    
    def get_success_url(self):
        """Redirige vers la formation associée après suppression"""
        formation_id = self.object.formation.id
        return reverse_lazy('formation-detail', kwargs={'pk': formation_id})
    



class AllCommentairesView(ListView):
    model = Commentaire
    template_name = 'formations/commentaires_tous.html'
    context_object_name = 'commentaires'
    paginate_by = 20  # Pagination

    def get_queryset(self):
        """Récupère tous les commentaires avec les filtres appliqués."""
        queryset = Commentaire.objects.select_related('formation', 'utilisateur').order_by('-created_at')

        formation_id = self.request.GET.get('formation')
        utilisateur_id = self.request.GET.get('utilisateur')
        search_query = self.request.GET.get('q')
        order_by = self.request.GET.get('order_by', '-created_at')

        filters = Q()

        if formation_id:
            filters &= Q(formation_id=formation_id)

        if utilisateur_id:
            filters &= Q(utilisateur_id=utilisateur_id)

        if search_query:
            filters &= Q(contenu__icontains=search_query)

        if order_by:
            queryset = queryset.order_by(order_by)

        queryset = queryset.filter(filters)


        return queryset

    def get_context_data(self, **kwargs):
        """Ajoute la liste des formations et utilisateurs pour le filtrage."""
        context = super().get_context_data(**kwargs)
        context['formations'] = Formation.objects.all()
        context['utilisateurs'] = User.objects.all()
        return context

class ExportCommentairesView(View):
    """Vue permettant d'exporter les commentaires sélectionnés en CSV."""

    def post(self, request, *args, **kwargs):
        commentaire_ids = request.POST.getlist('commentaire_ids')  # Récupération des IDs sélectionnés
        
        if not commentaire_ids:
            return HttpResponse("Aucun commentaire sélectionné.", status=400)

        commentaires = get_list_or_404(Commentaire, id__in=commentaire_ids)

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="commentaires_export.csv"'

        writer = csv.writer(response)
        writer.writerow(["ID", "Utilisateur", "Date", "Formation", "Num Offre", "Commentaire"])

        for commentaire in commentaires:
            writer.writerow([
                commentaire.id,
                commentaire.utilisateur.username if commentaire.utilisateur else "Anonyme",
                commentaire.created_at.strftime("%d/%m/%Y %H:%M"),
                commentaire.formation.nom if commentaire.formation else "N/A",
                commentaire.formation.num_offre if commentaire.formation else "N/A",
                commentaire.contenu
            ])

        return response