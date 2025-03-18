from django.views.generic import ListView, DetailView, FormView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
import logging
import json

from ..models.rapports import Rapport
from ..models import Centre, TypeOffre, Statut
from ..services.generateur_rapports import GenerateurRapport
from ..forms.rapports_forms import RapportCreationForm

logger = logging.getLogger(__name__)

class RapportListView(LoginRequiredMixin, ListView):
    """Vue pour afficher la liste des rapports générés."""
    model = Rapport
    template_name = 'rapports/rapport_list.html'
    context_object_name = 'rapports'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()

        # Filtres
        type_rapport = self.request.GET.get('type_rapport')
        periode = self.request.GET.get('periode')

        if type_rapport:
            queryset = queryset.filter(type_rapport=type_rapport)
        if periode:
            queryset = queryset.filter(periode=periode)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type_choices'] = Rapport.TYPE_CHOICES
        context['periode_choices'] = Rapport.PERIODE_CHOICES
        return context


import logging

logger = logging.getLogger(__name__)

class RapportDetailView(LoginRequiredMixin, DetailView):
    model = Rapport
    template_name = 'rapports/rapport_detail.html'
    context_object_name = 'rapport'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        rapport = self.get_object()

        try:
            if isinstance(rapport.donnees, str):
                rapport.donnees = json.loads(rapport.donnees)  # ✅ Convertir JSON string en dict

            logger.info(f"📊 Données envoyées au template : {rapport.donnees}")
            context['donnees'] = rapport.donnees

        except json.JSONDecodeError as e:
            logger.error(f"❌ Erreur de décodage JSON pour le rapport {rapport.id}: {e}")
            context['donnees'] = {}  # S'assurer qu'on ne passe pas None

        # Gestion des graphiques pour les rapports d'occupation
        if rapport.type_rapport == Rapport.TYPE_OCCUPATION:
            context['chart_data'] = self._prepare_occupation_chart_data(rapport)

        return context


    def _prepare_occupation_chart_data(self, rapport):
        """Prépare les données pour le graphique d'occupation."""
        formations = rapport.donnees.get('formations', [])

        labels = [f['nom'] for f in formations]
        taux_remplissage = [f['taux_remplissage'] for f in formations]

        return {
            'labels': labels,
            'datasets': [{
                'label': 'Taux de remplissage (%)',
                'data': taux_remplissage,
                'backgroundColor': [
                    '#4CAF50' if rate >= 90 else '#FFC107' if rate >= 70 else '#F44336'
                    for rate in taux_remplissage
                ]
            }]
        }


class RapportCreationView(LoginRequiredMixin, FormView):
    """Vue pour créer un nouveau rapport."""
    template_name = 'rapports/rapport_form.html'
    form_class = RapportCreationForm
    success_url = reverse_lazy('rapport-list')

    def form_valid(self, form):
        """Génère un rapport basé sur les paramètres saisis."""
        try:
            rapport = GenerateurRapport.generer_rapport(
                type_rapport=form.cleaned_data['type_rapport'],
                date_debut=form.cleaned_data['date_debut'],
                date_fin=form.cleaned_data['date_fin'],
                centre=form.cleaned_data.get('centre'),
                type_offre=form.cleaned_data.get('type_offre'),
                statut=form.cleaned_data.get('statut'),
                format=form.cleaned_data.get('format', Rapport.FORMAT_HTML),
                utilisateur=self.request.user,
                periode=form.cleaned_data.get('periode')
            )

            if rapport:
                messages.success(self.request, f'✅ Rapport "{rapport.nom}" généré avec succès.')
            else:
                messages.error(self.request, "❌ Erreur lors de la génération du rapport.")

        except Exception as e:
            logger.exception(f"Erreur lors de la création du rapport: {str(e)}")
            messages.error(self.request, f'Erreur lors de la génération du rapport: {str(e)}')

        return super().form_valid(form)


class RapportDeleteView(LoginRequiredMixin, DeleteView):
    """Vue pour supprimer un rapport."""
    model = Rapport
    template_name = 'rapports/rapport_confirm_delete.html'
    success_url = reverse_lazy('rapport-list')

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Rapport supprimé avec succès.')
        return super().delete(request, *args, **kwargs)


class RapportExportView(LoginRequiredMixin, DetailView):
    """Vue pour exporter un rapport dans différents formats."""
    model = Rapport

    def get(self, request, *args, **kwargs):
        rapport = self.get_object()
        format_export = request.GET.get('format', rapport.format)

        if format_export == Rapport.FORMAT_PDF:
            return self._export_pdf(rapport)
        elif format_export == Rapport.FORMAT_EXCEL:
            return self._export_excel(rapport)
        elif format_export == Rapport.FORMAT_CSV:
            return self._export_csv(rapport)
        else:
            # Format HTML par défaut, rediriger vers la vue détaillée
            return redirect('rapport-detail', pk=rapport.pk)

    def _export_pdf(self, rapport):
        """Logique d'export PDF"""
        try:
            from io import BytesIO
            from reportlab.lib.pagesizes import letter
            from reportlab.pdfgen import canvas

            buffer = BytesIO()
            p = canvas.Canvas(buffer, pagesize=letter)
            p.drawString(100, 750, f"Rapport: {rapport.nom}")
            p.drawString(100, 730, f"Type: {rapport.get_type_rapport_display()}")
            p.drawString(100, 710, f"Date: {rapport.date_debut} - {rapport.date_fin}")
            p.drawString(100, 690, f"Généré par: {rapport.utilisateur}")

            y_position = 670
            for formation in rapport.donnees.get('formations', []):
                p.drawString(100, y_position, f"Formation: {formation['nom']} - {formation['taux_remplissage']}%")
                y_position -= 20

            p.showPage()
            p.save()
            buffer.seek(0)

            response = HttpResponse(buffer, content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="{rapport.nom}.pdf"'
            return response
        except Exception as e:
            logger.exception(f"Erreur lors de l'export PDF: {str(e)}")
            messages.error(self.request, "Erreur lors de l'export PDF.")
            return redirect('rapport-detail', pk=rapport.pk)

    def _export_excel(self, rapport):
        """Logique d'export Excel"""
        try:
            import pandas as pd

            formations_data = rapport.donnees.get('formations', [])
            df = pd.DataFrame(formations_data)

            response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Content-Disposition'] = f'attachment; filename="{rapport.nom}.xlsx"'
            df.to_excel(response, index=False)
            return response
        except Exception as e:
            logger.exception(f"Erreur lors de l'export Excel: {str(e)}")
            messages.error(self.request, "Erreur lors de l'export Excel.")
            return redirect('rapport-detail', pk=rapport.pk)

    def _export_csv(self, rapport):
        """Logique d'export CSV"""
        try:
            import csv
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = f'attachment; filename="{rapport.nom}.csv"'

            writer = csv.writer(response)
            formations_data = rapport.donnees.get('formations', [])
            if formations_data:
                writer.writerow(formations_data[0].keys())
                for formation in formations_data:
                    writer.writerow(formation.values())

            return response
        except Exception as e:
            logger.exception(f"Erreur lors de l'export CSV: {str(e)}")
            messages.error(self.request, "Erreur lors de l'export CSV.")
            return redirect('rapport-detail', pk=rapport.pk)
