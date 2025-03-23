from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DeleteView, DetailView, CreateView, UpdateView, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from ..models.prepa_comp import Semaine, Mois, Candidat, Entree, Departement, ObjectifAnnuel
from ..forms.prepa_comp_form import CandidatForm, EntreeForm, ObjectifAnnuelForm
import json
from django.contrib import messages
from django.db.models import Count


class TableauDeBordView(LoginRequiredMixin, TemplateView):
    """Vue pour le tableau de bord principal"""
    template_name = 'prepacomp/tableau_de_bord.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Récupérer l'onglet actif (semaine, mois ou année)
        onglet = self.request.GET.get('onglet', 'semaine')
        context['onglet_actif'] = onglet
        
        if onglet == 'semaine':
            # Statistiques de la semaine courante
            semaine_courante = Semaine.creer_semaine_courante()
            context['periode_courante'] = semaine_courante
            context['stats_semaines'] = self.get_stats_semaines()
            
        elif onglet == 'mois':
            # Statistiques du mois courant
            mois_courant = Mois.creer_mois_courant()
            context['periode_courante'] = mois_courant
            context['stats_mois'] = self.get_stats_mois()
            
        else:  # onglet == 'annee'
            # Statistiques de l'année courante
            annee_courante = timezone.now().year
            objectif_annuel = ObjectifAnnuel.get_current_year_objectif()
            context['annee_courante'] = annee_courante
            context['objectif_annuel'] = objectif_annuel
            context['stats_annees'] = self.get_stats_annees()
        
        # Ajouter les données pour les graphiques
        context['chart_data'] = self.prepare_chart_data(onglet)
        
        return context
    
    def get_stats_semaines(self):
        """Récupère les statistiques des dernières semaines"""
        from ..queries import get_stats_historiques_semaines
        return get_stats_historiques_semaines(10)
    
    def get_stats_mois(self):
        """Récupère les statistiques des derniers mois"""
        from ..queries import get_stats_historiques_mois
        return get_stats_historiques_mois(12)
    
    def get_stats_annees(self):
        """Récupère les statistiques des dernières années"""
        from ..queries import get_stats_historiques_annees
        return get_stats_historiques_annees(5)
    
    def prepare_chart_data(self, onglet):
        """Prépare les données pour les graphiques en fonction de l'onglet actif"""
        if onglet == 'semaine':
            return self.prepare_chart_data_semaines()
        elif onglet == 'mois':
            return self.prepare_chart_data_mois()
        else:  # onglet == 'annee'
            return self.prepare_chart_data_annees()
    
    def prepare_chart_data_semaines(self):
        """Prépare les données pour les graphiques des semaines"""
        stats = self.get_stats_semaines()
        
        # Inversons l'ordre pour l'affichage chronologique
        stats.reverse()
        
        labels = [s['semaine'] for s in stats]
        entrees = [s['entrees'] for s in stats]
        candidats = [s['candidats'] for s in stats]
        objectifs = [s['objectif'] for s in stats]
        
        # Données pour le graphique par département (semaine courante)
        semaine_courante = Semaine.creer_semaine_courante()
        stats_depts = semaine_courante.stats_par_departement()
        labels_depts = [stat['departement__code'] for stat in stats_depts]
        values_depts = [stat['total'] for stat in stats_depts]
        
        return {
            'labels': json.dumps(labels),
            'entrees': json.dumps(entrees),
            'candidats': json.dumps(candidats),
            'objectifs': json.dumps(objectifs),
            'labels_depts': json.dumps(labels_depts),
            'values_depts': json.dumps(values_depts)
        }
    
    def prepare_chart_data_mois(self):
        """Prépare les données pour les graphiques des mois"""
        stats = self.get_stats_mois()
        
        # Inversons l'ordre pour l'affichage chronologique
        stats.reverse()
        
        labels = [f"{s['mois']} {s['annee']}" for s in stats]
        entrees = [s['entrees'] for s in stats]
        candidats = [s['candidats'] for s in stats]
        objectifs = [s['objectif'] for s in stats]
        
        # Données pour le graphique par département (mois courant)
        mois_courant = Mois.creer_mois_courant()
        stats_depts = mois_courant.stats_par_departement()
        labels_depts = [stat['departement__code'] for stat in stats_depts]
        values_depts = [stat['total'] for stat in stats_depts]
        
        return {
            'labels': json.dumps(labels),
            'entrees': json.dumps(entrees),
            'candidats': json.dumps(candidats),
            'objectifs': json.dumps(objectifs),
            'labels_depts': json.dumps(labels_depts),
            'values_depts': json.dumps(values_depts)
        }
    
    def prepare_chart_data_annees(self):
        """Prépare les données pour les graphiques des années"""
        stats = self.get_stats_annees()
        
        # Inversons l'ordre pour l'affichage chronologique
        stats.reverse()
        
        labels = [str(s['annee']) for s in stats]
        entrees = [s['entrees'] for s in stats]
        candidats = [s['candidats'] for s in stats]
        objectifs = [s['objectif'] for s in stats]
        
        # Statistiques par mois pour l'année courante
        from ..queries import get_stats_annee_courante
        stats_annee = get_stats_annee_courante()
        labels_mois = [s['nom_mois'] for s in stats_annee['stats_mois']]
        entrees_mois = [s['entrees'] for s in stats_annee['stats_mois']]
        objectifs_mois = [s['objectif'] for s in stats_annee['stats_mois']]
        
        # Données pour le graphique par département (année courante)
        stats_depts = stats_annee['stats_departements']
        labels_depts = [stat['departement__code'] for stat in stats_depts]
        values_depts = [stat['total'] for stat in stats_depts]
        
        return {
            'labels': json.dumps(labels),
            'entrees': json.dumps(entrees),
            'candidats': json.dumps(candidats),
            'objectifs': json.dumps(objectifs),
            'labels_mois': json.dumps(labels_mois),
            'entrees_mois': json.dumps(entrees_mois),
            'objectifs_mois': json.dumps(objectifs_mois),
            'labels_depts': json.dumps(labels_depts),
            'values_depts': json.dumps(values_depts)
        }


class SemaineDetailView(LoginRequiredMixin, DetailView):
    """Vue détaillée d'une semaine"""
    model = Semaine
    template_name = 'prepacomp/semaine_detail.html'
    context_object_name = 'semaine'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        semaine = self.object
        
        # Ajouter les statistiques par département
        context['stats_departements'] = semaine.stats_par_departement()
        
        # Liste des entrées de la semaine
        context['entrees'] = Entree.objects.filter(semaine=semaine)
        
        return context


class MoisDetailView(LoginRequiredMixin, DetailView):
    """Vue détaillée d'un mois"""
    model = Mois
    template_name = 'prepacomp/mois_detail.html'
    context_object_name = 'mois'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mois = self.object
        
        # Ajouter les statistiques par département
        context['stats_departements'] = mois.stats_par_departement()
        
        # Liste des semaines de ce mois
        context['semaines'] = mois.get_semaines()
        
        # Liste des candidats du mois
        context['candidats'] = Candidat.objects.filter(
            semaine__mois=mois.mois, 
            semaine__annee=mois.annee
        )
        
        # Liste des entrées du mois
        context['entrees'] = Entree.objects.filter(
            semaine__mois=mois.mois, 
            semaine__annee=mois.annee
        )
        
        return context


class AnneeDetailView(LoginRequiredMixin, TemplateView):
    """Vue détaillée d'une année"""
    template_name = 'prepacomp/annee_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        annee = self.kwargs.get('annee', timezone.now().year)
        
        # Objectif annuel
        try:
            objectif_annuel = ObjectifAnnuel.objects.get(annee=annee)
        except ObjectifAnnuel.DoesNotExist:
            objectif_annuel = ObjectifAnnuel.objects.create(annee=annee, objectif=430)
        
        context['annee'] = annee
        context['objectif_annuel'] = objectif_annuel
        
        # Statistiques par mois
        stats_mois = []
        for mois_num in range(1, 13):
            try:
                mois_obj = Mois.objects.get(mois=mois_num, annee=annee)
                entrees_mois = mois_obj.nombre_entrees
                candidats_mois = mois_obj.nombre_candidats
                taux = mois_obj.taux_transformation
            except Mois.DoesNotExist:
                entrees_mois = 0
                candidats_mois = 0
                taux = 0
                
            stats_mois.append({
                'mois': mois_num,
                'nom_mois': Mois.get_nom_mois(mois_num),
                'entrees': entrees_mois,
                'candidats': candidats_mois,
                'taux': taux,
                'objectif': objectif_annuel.objectif_mensuel()
            })
        
        context['stats_mois'] = stats_mois
        
        # Statistiques par département
        context['stats_departements'] = Entree.objects.filter(
            semaine__annee=annee
        ).values(
            'departement__code', 'departement__nom'
        ).annotate(
            total=Count('id')
        ).order_by('departement__code')
        
        # Calcul des totaux annuels
        nombre_entrees = Entree.objects.filter(semaine__annee=annee).count()
        nombre_candidats = Candidat.objects.filter(semaine__annee=annee).count()
        
        context['nombre_entrees'] = nombre_entrees
        context['nombre_candidats'] = nombre_candidats
        context['taux_transformation'] = (nombre_entrees / nombre_candidats * 100) if nombre_candidats > 0 else 0
        context['pourcentage_objectif'] = (nombre_entrees / objectif_annuel.objectif * 100) if objectif_annuel.objectif > 0 else 0
        
        return context


class CandidatCreateView(LoginRequiredMixin, CreateView):
    """Vue pour créer un candidat"""
    model = Candidat
    form_class = CandidatForm
    template_name = 'prepacomp/candidat_form.html'
    success_url = reverse_lazy('prepacomp:tableau_de_bord')
    
    def form_valid(self, form):
        # Assigner automatiquement la semaine courante
        form.instance.semaine = Semaine.creer_semaine_courante()
        return super().form_valid(form)


class EntreeCreateView(LoginRequiredMixin, CreateView):
    """Vue pour créer une entrée"""
    model = Entree
    form_class = EntreeForm
    template_name = 'prepacomp/entree_form.html'
    success_url = reverse_lazy('prepacomp:tableau_de_bord')
    
    def form_valid(self, form):
        # Assigner automatiquement la semaine courante
        form.instance.semaine = Semaine.creer_semaine_courante()
        
        # Si l'entrée est liée à un candidat, mettre à jour son statut
        if form.instance.candidat:
            form.instance.candidat.a_adhere = True
            form.instance.candidat.save(update_fields=['a_adhere'])
            
        return super().form_valid(form)


class ObjectifAnnuelUpdateView(LoginRequiredMixin, UpdateView):
    """Vue pour modifier l'objectif annuel"""
    model = ObjectifAnnuel
    form_class = ObjectifAnnuelForm
    template_name = 'prepacomp/objectif_form.html'
    success_url = reverse_lazy('prepacomp:tableau_de_bord')
    
    def get_object(self):
        annee = self.kwargs.get('annee', timezone.now().year)
        return get_object_or_404(ObjectifAnnuel, annee=annee) 
        context['candidats'] = Candidat.objects.filter(semaine=semaine)
        

from ..models.prepa_comp import Candidat, Entree, Departement, Semaine, Mois, ObjectifAnnuel


class CandidatListView(LoginRequiredMixin, ListView):
    """Vue pour lister tous les candidats"""
    model = Candidat
    template_name = 'prepacomp/candidat_list.html'
    context_object_name = 'candidats'
    paginate_by = 20
    
    def get_queryset(self):
        queryset = super().get_queryset().order_by('-date_candidature')
        
        # Filtrage par département si spécifié
        departement = self.request.GET.get('departement')
        if departement:
            queryset = queryset.filter(departement__code=departement)
            
        # Filtrage par statut d'adhésion si spécifié
        statut = self.request.GET.get('statut')
        if statut == 'adherent':
            queryset = queryset.filter(a_adhere=True)
        elif statut == 'non_adherent':
            queryset = queryset.filter(a_adhere=False)
            
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Ajouter les filtres actifs au contexte
        context['departement_filtre'] = self.request.GET.get('departement', '')
        context['statut_filtre'] = self.request.GET.get('statut', '')
        
        # Ajouter la liste des départements pour le filtre
        context['departements'] = Departement.objects.all().order_by('code')
        
        # Ajouter les statistiques
        context['total_candidats'] = Candidat.objects.count()
        context['total_adherents'] = Candidat.objects.filter(a_adhere=True).count()
        context['taux_global'] = (context['total_adherents'] / context['total_candidats'] * 100) if context['total_candidats'] > 0 else 0
        
        return context


class CandidatDeleteView(LoginRequiredMixin, DeleteView):
    """Vue pour supprimer un candidat"""
    model = Candidat
    template_name = 'prepacomp/candidat_confirm_delete.html'
    success_url = reverse_lazy('prepacomp:candidat_list')
    
    def delete(self, request, *args, **kwargs):
        candidat = self.get_object()
        try:
            # Vérifier si le candidat a une entrée associée
            if hasattr(candidat, 'entree'):
                messages.error(request, "Ce candidat a déjà une entrée associée et ne peut pas être supprimé.")
                return redirect('prepacomp:candidat_list')
            
            # Supprimer le candidat
            response = super().delete(request, *args, **kwargs)
            messages.success(request, f"Le candidat {candidat.prenom} {candidat.nom} a été supprimé avec succès.")
            return response
        except Exception as e:
            messages.error(request, f"Erreur lors de la suppression : {str(e)}")
            return redirect('prepacomp:candidat_list')


class EntreeListView(LoginRequiredMixin, ListView):
    """Vue pour lister toutes les entrées"""
    model = Entree
    template_name = 'prepacomp/entree_list.html'
    context_object_name = 'entrees'
    paginate_by = 20
    
    def get_queryset(self):
        queryset = super().get_queryset().order_by('-date_entree')
        
        # Filtrage par département si spécifié
        departement = self.request.GET.get('departement')
        if departement:
            queryset = queryset.filter(departement__code=departement)
            
        # Filtrage par période si spécifié
        annee = self.request.GET.get('annee')
        mois = self.request.GET.get('mois')
        semaine = self.request.GET.get('semaine')
        
        if annee:
            queryset = queryset.filter(semaine__annee=annee)
            
        if mois and annee:
            queryset = queryset.filter(semaine__mois=mois, semaine__annee=annee)
            
        if semaine and annee:
            queryset = queryset.filter(semaine__numero_semaine=semaine, semaine__annee=annee)
            
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Ajouter les filtres actifs au contexte
        context['departement_filtre'] = self.request.GET.get('departement', '')
        context['annee_filtre'] = self.request.GET.get('annee', '')
        context['mois_filtre'] = self.request.GET.get('mois', '')
        context['semaine_filtre'] = self.request.GET.get('semaine', '')
        
        # Ajouter les listes pour les filtres
        context['departements'] = Departement.objects.all().order_by('code')
        context['annees'] = Semaine.objects.values('annee').distinct().order_by('-annee')
        
        if context['annee_filtre']:
            context['mois_disponibles'] = Semaine.objects.filter(
                annee=context['annee_filtre']
            ).values('mois').distinct().order_by('mois')
            
            context['semaines_disponibles'] = Semaine.objects.filter(
                annee=context['annee_filtre']
            ).values('numero_semaine').distinct().order_by('numero_semaine')
        
        # Ajouter les statistiques
        context['total_entrees'] = Entree.objects.count()
        context['stats_par_departement'] = Entree.objects.values(
            'departement__code', 'departement__nom'
        ).annotate(
            total=Count('id')
        ).order_by('departement__code')
        
        return context


class DepartementStatsView(LoginRequiredMixin, DetailView):
    """Vue détaillée des statistiques par département"""
    model = Departement
    template_name = 'prepacomp/departement_stats.html'
    context_object_name = 'departement'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        departement = self.object
        
        # Statistiques globales
        context['total_entrees'] = Entree.objects.filter(departement=departement).count()
        context['total_candidats'] = Candidat.objects.filter(departement=departement).count()
        context['taux_transformation'] = (context['total_entrees'] / context['total_candidats'] * 100) if context['total_candidats'] > 0 else 0
        
        # Statistiques par année
        stats_annees = []
        annees = Semaine.objects.filter(
            entree__departement=departement
        ).values('annee').distinct().order_by('-annee')
        
        for annee_dict in annees:
            annee = annee_dict['annee']
            entrees = Entree.objects.filter(departement=departement, semaine__annee=annee).count()
            candidats = Candidat.objects.filter(departement=departement, semaine__annee=annee).count()
            taux = (entrees / candidats * 100) if candidats > 0 else 0
            
            try:
                objectif_annuel = ObjectifAnnuel.objects.get(annee=annee)
                objectif = objectif_annuel.objectif
            except ObjectifAnnuel.DoesNotExist:
                objectif = 430
                
            # Calculer la part du département dans l'objectif global (proportion par rapport aux autres départements)
            total_entrees_annee = Entree.objects.filter(semaine__annee=annee).count()
            part_departement = (entrees / total_entrees_annee * 100) if total_entrees_annee > 0 else 0
            objectif_departement = objectif * (part_departement / 100)
            
            stats_annees.append({
                'annee': annee,
                'entrees': entrees,
                'candidats': candidats,
                'taux': taux,
                'part_departement': part_departement,
                'objectif_departement': objectif_departement,
                'pourcentage_objectif': (entrees / objectif_departement * 100) if objectif_departement > 0 else 0
            })
        
        context['stats_annees'] = stats_annees
        
        # Statistiques par mois de l'année courante
        stats_mois = []
        annee_courante = timezone.now().year
        
        for mois_num in range(1, 13):
            entrees = Entree.objects.filter(
                departement=departement, 
                semaine__annee=annee_courante,
                semaine__mois=mois_num
            ).count()
            
            candidats = Candidat.objects.filter(
                departement=departement, 
                semaine__annee=annee_courante,
                semaine__mois=mois_num
            ).count()
            
            stats_mois.append({
                'mois': mois_num,
                'nom_mois': Mois.get_nom_mois(mois_num),
                'entrees': entrees,
                'candidats': candidats,
                'taux': (entrees / candidats * 100) if candidats > 0 else 0
            })
        
        context['stats_mois'] = stats_mois
        context['annee_courante'] = annee_courante
        
        return context