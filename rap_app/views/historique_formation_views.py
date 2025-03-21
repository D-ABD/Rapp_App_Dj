from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.utils.timezone import datetime

from ..models.formations import Formation
from ..models import HistoriqueFormation

class HistoriqueFormationListView(ListView):
    model = HistoriqueFormation
    template_name = 'historiqueformation/historiqueformation_list.html'
    context_object_name = 'historiques'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        formation_id = self.request.GET.get("formation")
        date = self.request.GET.get("date")

        if formation_id:
            queryset = queryset.filter(formation__id=formation_id)
        if date:
            try:
                parsed_date = datetime.strptime(date, "%Y-%m-%d")
                queryset = queryset.filter(date_modification__date=parsed_date)
            except ValueError:
                pass  # Ignore mauvaise date

        return queryset.select_related("formation", "modifie_par")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['formations'] = Formation.objects.all().order_by("nom")
        return context

class HistoriqueFormationDetailView( DetailView):
    model = HistoriqueFormation
    template_name = 'historiqueformation/historiqueformation_detail.html'
    context_object_name = 'historique'

class HistoriqueFormationDeleteView(DeleteView):
    model = HistoriqueFormation
    template_name = "historiqueformation/historiqueformation_confirm_delete.html"
    success_url = reverse_lazy("historique-formation-list")

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "✅ Entrée historique supprimée avec succès.")
        return super().delete(request, *args, **kwargs)
