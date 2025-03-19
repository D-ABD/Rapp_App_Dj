from django.urls import reverse_lazy
from django.db.models import Count, Q
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect

from ..models.partenaires import Partenaire

from ..models import  Formation
from .base_views import BaseListView, BaseDetailView, BaseCreateView, BaseUpdateView, BaseDeleteView


class PartenaireListView(BaseListView):
    """Vue listant toutes les partenaires avec des statistiques"""
    model = Partenaire
    context_object_name = 'partenaires'
    template_name = 'partenaires/partenaire_list.html'
    
    def get_queryset(self):
        """
        Récupère la liste des partenaires en annotant des statistiques :
        - Nombre de formations associées à chaque partenaire
        """
        queryset = super().get_queryset().annotate(
            nb_formations=Count('formations')
        )
        
        # Filtrage par nom de l'partenaire
        q = self.request.GET.get('q')
        if q:
            queryset = queryset.filter(nom__icontains=q)
            
        # Filtrage par secteur d'activité
        secteur = self.request.GET.get('secteur')
        if secteur:
            queryset = queryset.filter(secteur_activite__icontains=secteur)
            
        return queryset
    
    def get_context_data(self, **kwargs):
        """
        Ajoute des statistiques générales et les filtres appliqués au contexte de la page.
        """
        context = super().get_context_data(**kwargs)
        context['total_partenaires_avec_formations'] = Partenaire.objects.filter(formations__isnull=False).distinct().count()

        
        # Statistiques globales
        context['total_partenaires'] = Partenaire.objects.count()
        context['total_formations'] = Formation.objects.count()
        
        # Secteurs d'activité uniques pour le filtre
        secteurs = Partenaire.objects.exclude(secteur_activite__isnull=True).exclude(secteur_activite='').values_list('secteur_activite', flat=True).distinct()
        context['secteurs'] = secteurs
        
        # Filtres actuellement appliqués
        context['filters'] = {
            'q': self.request.GET.get('q', ''),
            'secteur': self.request.GET.get('secteur', ''),
        }
        
        return context


class PartenaireDetailView(BaseDetailView):
    """Vue affichant les détails d'une partenaire"""
    model = Partenaire
    context_object_name = 'partenaire'
    template_name = 'partenaires/partenaire_detail.html'

    def get_context_data(self, **kwargs):
        """Ajoute au contexte les formations associées à l'partenaire"""
        context = super().get_context_data(**kwargs)
        
        # Récupération des formations associées à l'partenaire
        formations = self.object.formations.select_related('type_offre', 'statut', 'centre').order_by('-start_date')

        # Filtrage des formations par type d'offre
        type_offre = self.request.GET.get('type_offre')
        if type_offre:
            formations = formations.filter(type_offre_id=type_offre)

        # Filtrage des formations par statut
        statut = self.request.GET.get('statut')
        if statut:
            formations = formations.filter(statut_id=statut)

        context['formations'] = formations
        
        return context


class PartenaireCreateView(PermissionRequiredMixin, BaseCreateView):
    """Vue permettant de créer une nouvelle partenaire"""
    model = Partenaire
    permission_required = 'rap_app.add_partenaire'
    fields = ['nom', 'secteur_activite', 'contact_nom', 'contact_poste', 
              'contact_telephone', 'contact_email', 'description']
    success_url = reverse_lazy('partenaire-list')
    template_name = 'partenaires/partenaire_form.html'

    def form_valid(self, form):
        partenaire = form.save()
        messages.success(self.request, "✅ Partenaire ajouté avec succès.")
        return redirect('partenaire-list')  # 🔹 Rediriger après succès
    
    def get_context_data(self, **kwargs):
        """
        Ajoute un titre personnalisé au contexte.
        """
        context = super().get_context_data(**kwargs)
        context['titre'] = "Ajouter un partenaire"
        return context
    
class PartenaireCreateViewFormation(PermissionRequiredMixin, BaseCreateView):
    """Vue permettant de créer une partenaire et de l'associer à une formation"""
    model = Partenaire
    permission_required = 'rap_app.add_partenaire'
    fields = ['nom', 'secteur_activite', 'contact_nom', 'contact_poste', 
              'contact_telephone', 'contact_email', 'description']
    template_name = 'partenaires/partenaire_formation_form.html'

    def form_valid(self, form):
        print("✅ form_valid exécuté")  # Vérifie si cette ligne s'affiche dans la console
        formation_id = self.kwargs.get('formation_id')

        if not formation_id:
            print("❌ Aucun ID de formation fourni !")
            messages.error(self.request, "❌ Erreur : Aucun ID de formation fourni.")
            return HttpResponseRedirect(reverse_lazy('formation-list'))  

        formation = get_object_or_404(Formation, pk=formation_id)
        print(f"📌 Formation trouvée : {formation.nom} (ID: {formation.id})")

        self.object = form.save()
        print(f"✅ Partenaire créé : {self.object.nom}")

        formation.partenaires.add(self.object)
        formation.save()
        print("✅ Partenaire ajouté à la formation avec succès !")

        messages.success(self.request, "Le partenaire a été créé et associé à la formation avec succès.")
        return HttpResponseRedirect(reverse_lazy('formation-detail', kwargs={'pk': formation_id}))

    def get_context_data(self, **kwargs):
        """Ajoute un titre dynamique au contexte"""
        context = super().get_context_data(**kwargs)
        formation_id = self.kwargs.get('formation_id')
        formation = get_object_or_404(Formation, pk=formation_id)
        context['titre'] = f"Ajouter un partenaire à la formation : {formation.nom} - { formation.num_offre}"
        return context


class PartenaireUpdateView(PermissionRequiredMixin, BaseUpdateView):
    """Vue permettant de modifier une partenaire existante"""
    model = Partenaire
    permission_required = 'rap_app.change_partenaire'
    fields = ['nom', 'secteur_activite', 'contact_nom', 'contact_poste', 
              'contact_telephone', 'contact_email', 'description']
    template_name = 'partenaires/partenaire_form.html'
    
    def get_success_url(self):
        """Redirige vers le détail du partenaire après modification"""
        return reverse_lazy('partenaire-detail', kwargs={'pk': self.object.pk})
    
    def get_context_data(self, **kwargs):
        """
        Ajoute un titre dynamique au contexte en fonction du partenaire modifié.
        """
        context = super().get_context_data(**kwargs)
        context['titre'] = f"Modifier le partenaire : {self.object.nom}"
        return context

class PartenaireDeleteView(PermissionRequiredMixin, BaseDeleteView):
    """Vue permettant de supprimer une partenaire"""
    model = Partenaire
    permission_required = 'rap_app.delete_partenaire'
    success_url = reverse_lazy('partenaire-list')
    template_name = 'partenaires/partenaire_confirm_delete.html'