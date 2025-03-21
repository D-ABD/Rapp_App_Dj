from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from ..forms.ProspectionForm import ProspectionForm
from ..models.prospection import HistoriqueProspection, Prospection


def ProspectionHomeView(request):
    return render(request, 'prospection/prospection_home.html')  # ✅ Indiquer que le template est dans prospection/

class ProspectionListView( ListView):
    """Affiche la liste des prospections"""
    model = Prospection
    template_name = 'prospection/prospection_list.html'
    context_object_name = 'prospections'
    ordering = ['-date_prospection']
    paginate_by = 10  # Pagination


    def get_queryset(self):
        queryset = super().get_queryset()
        statut = self.request.GET.get('statut')
        formation = self.request.GET.get('formation')
        entreprise = self.request.GET.get('entreprise')

        if statut:
            queryset = queryset.filter(statut=statut)
        if formation:
            queryset = queryset.filter(formation_id=formation)
        if entreprise:
            queryset = queryset.filter(company_id=entreprise)

        return queryset

class ProspectionDetailView( DetailView):
    """Affiche le détail d'une prospection"""
    model = Prospection
    template_name = 'prospection/prospection_detail.html'
    context_object_name = 'prospection'

class ProspectionCreateView (CreateView):
    """Vue pour créer une prospection"""
    model = Prospection
    form_class = ProspectionForm
    template_name = 'prospection/prospection_form.html'
    success_url = reverse_lazy('prospection-list')

    def form_valid(self, form):
        messages.success(self.request, "✅ Prospection ajoutée avec succès.")
        return super().form_valid(form)
    
    def get_initial(self):
        initial = super().get_initial()
        formation_id = self.request.GET.get('formation')
        if formation_id:
            initial['formation'] = formation_id
        return initial


class ProspectionUpdateView( UpdateView):
    """Permet de modifier une prospection"""
    model = Prospection
    form_class = ProspectionForm
    template_name = 'prospection/prospection_form.html'
    success_url = reverse_lazy('prospection-list')

    def form_valid(self, form):
        messages.success(self.request, "✅ Prospection mise à jour avec succès.")
        return super().form_valid(form)

class ProspectionDeleteView(DeleteView):
    """Permet de supprimer une prospection"""
    model = Prospection
    template_name = 'prospection/prospection_confirm_delete.html'
    success_url = reverse_lazy('prospection-list')

    def delete(self, request, *args, **kwargs):
        messages.success(request, "✅ Prospection supprimée avec succès.")
        return super().delete(request, *args, **kwargs)

class HistoriqueProspectionListView(ListView):
    model = HistoriqueProspection
    template_name = 'prospection/historiqueprospection_list.html'
    context_object_name = 'historiques'
    paginate_by = 20

    def get_queryset(self):
        queryset = super().get_queryset()
        prospection_id = self.request.GET.get("prospection")

        if prospection_id:
            queryset = queryset.filter(prospection_id=prospection_id)

        return queryset.select_related('prospection', 'modifie_par')


class HistoriqueProspectionDetailView(DetailView):
    model = HistoriqueProspection
    template_name = 'prospection/historiqueprospection_detail.html'
    context_object_name = 'historique'