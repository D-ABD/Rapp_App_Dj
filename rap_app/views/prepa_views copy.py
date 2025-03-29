# prepa/views/prepa_views.py
import logging
from datetime import datetime, timedelta
from django.views.generic import CreateView, TemplateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import Sum
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django import forms
from django.utils.timezone import now

from ..models.centres import Centre
from ..models.prepacomp import NOMS_MOIS, Semaine, PrepaCompGlobal
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
        centre = Centre.objects.first()
        objectif_global = PrepaCompGlobal.objectif_annuel_global()
        adhesions_globales = PrepaCompGlobal.objects.filter(annee=annee).aggregate(total=Sum('adhesions'))['total'] or 0



        try:
            context['semaine_courante'] = Semaine.creer_semaine_courante(centre)
            context['bilan_global'] = get_object_or_404(PrepaCompGlobal, annee=annee, centre=centre)
            context['mois_annee'] = PrepaCompGlobal.stats_par_mois(annee, centre)
            context['objectif_annuel_global'] = PrepaCompGlobal.objectif_annuel_global()
            context['objectif_hebdo_global'] = PrepaCompGlobal.objectif_hebdo_global(annee)
            context['adhesions_globales'] = adhesions_globales
            context['taux_objectif_global'] = round((adhesions_globales / objectif_global) * 100, 1) if objectif_global else 0
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
            messages.error(self.request, "Erreur lors du chargement du tableau de bord.")
        return context



# ---- Semaines ----
class PrepaSemaineListView(BaseListView):
    model = Semaine
    template_name = 'prepa/prepa_semaine_list.html'
    context_object_name = 'semaines'
    ordering = ['-date_debut']
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
        return qs

    def get_context_data(self, **kwargs):  # <- doit être DANS la classe
        context = super().get_context_data(**kwargs)
        annee = self.request.GET.get('annee') or timezone.now().year

        context['centres'] = Centre.objects.all()
        context['annees'] = Semaine.objects.values_list('annee', flat=True).distinct().order_by('-annee')
        context['objectif_annuel_global'] = PrepaCompGlobal.objectif_annuel_global()
        context['objectif_hebdo_global'] = PrepaCompGlobal.objectif_hebdo_global(annee)
        context['objectifs_par_centre'] = PrepaCompGlobal.objectifs_par_centre(annee)

        return context



class PrepaSemaineDetailView(BaseDetailView):
    model = Semaine
    template_name = 'prepa/prepa_semaine_detail.html'
    context_object_name = 'semaine'

class PrepaSemaineCreateView(CreateView):
    model = Semaine
    template_name = 'prepa/prepa_semaine_form.html'
    fields = ['centre', 'objectif_hebdo_prepa', 'nombre_candidats', 'nombre_prescriptions',
              'nombre_adhesions', 'nombre_presents', 'nombre_places_ouvertes']
    success_url = reverse_lazy('prepa_semaine_list')

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
        return form

    def get_initial(self):
        initial = super().get_initial()
        centre_id = self.request.POST.get('centre') or self.request.GET.get('centre')
        try:
            centre = Centre.objects.get(pk=int(centre_id))
            initial['objectif_hebdo_prepa'] = centre.objectif_hebdomadaire_prepa or 0
        except:
            initial['objectif_hebdo_prepa'] = 0
        return initial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        annee = now().year
        context['objectif_annuel_global'] = PrepaCompGlobal.objectif_annuel_global()
        context['objectif_hebdo_global'] = PrepaCompGlobal.objectif_hebdo_global(annee)
        context['objectifs_par_centre'] = PrepaCompGlobal.objectifs_par_centre(annee)
        num_semaine = self.request.POST.get('numero_semaine')
        if num_semaine:
            lundi, dimanche = get_dates_from_week(annee, int(num_semaine))
            context['date_debut_calculee'] = lundi
            context['date_fin_calculee'] = dimanche
        return context

    def form_valid(self, form):
        numero = int(form.cleaned_data['numero_semaine'])
        centre = form.cleaned_data['centre']
        annee = now().year
        lundi, dimanche = get_dates_from_week(annee, numero)

        form.instance.numero_semaine = numero
        form.instance.date_debut = lundi
        form.instance.date_fin = dimanche
        form.instance.mois = lundi.month
        form.instance.annee = annee

        return super().form_valid(form)

class PrepaSemaineUpdateView(BaseUpdateView):
    model = Semaine
    template_name = 'prepa/prepa_semaine_form.html'
    context_object_name = 'semaine'
    fields = ['centre', 'nombre_candidats', 'nombre_prescriptions',
              'nombre_adhesions', 'nombre_presents', 'nombre_places_ouvertes']
    success_url = reverse_lazy('prepa_semaine_list')

class PrepaSemaineDeleteView(BaseDeleteView):
    model = Semaine
    template_name = 'prepa/prepa_semaine_confirm_delete.html'
    context_object_name = 'semaine'
    success_url = reverse_lazy('prepa_semaine_list')

# ---- Bilan Global ----
class PrepaGlobalListView(BaseListView):
    model = PrepaCompGlobal
    template_name = 'prepa/prepacompglobal_list.html'
    context_object_name = 'bilans'
    ordering = ['-annee']

class PrepaGlobalDetailView(BaseDetailView):
    model = PrepaCompGlobal
    template_name = 'prepa/prepacompglobal_detail.html'
    context_object_name = 'bilan'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        annee = self.object.annee

        context['objectif_annuel_global'] = PrepaCompGlobal.objectif_annuel_global()
        context['mois'] = PrepaCompGlobal.stats_par_mois(
            annee=annee,
            centre=self.object.centre
        )
        context['objectif_hebdo_global'] = PrepaCompGlobal.objectif_hebdo_global(annee)
        context['objectifs_par_centre'] = PrepaCompGlobal.objectifs_par_centre(annee)

        return context



class PrepaGlobalCreateView(BaseCreateView):
    model = PrepaCompGlobal
    template_name = 'prepa/prepacompglobal_form.html'
    fields = ['centre', 'annee', 'total_candidats', 'total_prescriptions',
              'adhesions', 'total_presents', 'total_places_ouvertes']
    success_url = reverse_lazy('prepa_global_list')
