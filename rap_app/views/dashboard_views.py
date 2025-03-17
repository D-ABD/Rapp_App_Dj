from django.http import HttpRequest  # ✅ Import correct de HttpRequest
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.db.models import Count, Sum, Avg, F, Q, Case, When, IntegerField, Value
from django.utils import timezone
from datetime import timedelta
from django.db.models.functions import TruncMonth
from django.http import JsonResponse
from django.views import View
from django.db.models import Count, Avg, F, Value, Sum, FloatField
from django.db.models.functions import Coalesce, TruncMonth
from django.db import models

from ..views.base_views import BaseListView

from ..models.partenaires import Partenaire


from ..models import Formation, Centre, Commentaire, TypeOffre, Statut, Evenement, HistoriqueFormation, Recherche


from ..models import Formation, Statut

from ..models import Formation, Centre, Commentaire, TypeOffre, Statut, Evenement, HistoriqueFormation


class DashboardView(BaseListView):
    model = Formation  # Spécifiez le modèle à afficher
    template_name = 'dashboard.html'  # Spécifiez le template
    context_object_name = 'formations'  # Nom de la variable dans le template

    def get_context_data(self, **kwargs):
        # Appelez la méthode parente pour obtenir le contexte de base
        context = super().get_context_data(**kwargs)

        # ✅ Nombre total de formations par centre
        context['formations_par_centre'] = (
            Centre.objects.annotate(total_formations=Count('formations'))
            .order_by('-total_formations')
        )

        # ✅ Formations par type d'offre
        context['formations_par_type_offre'] = (
            TypeOffre.objects.annotate(total=Count('formations'))
            .order_by('-total')
        )

        # ✅ Formations par statut
        context['formations_par_statut'] = (
            Statut.objects.annotate(total=Count('formations'))
            .order_by('-total')
        )

        # ✅ Statistiques globales
        context['total_formations'] = Formation.objects.count()
        context['formations_actives'] = Formation.objects.formations_actives().count()
        context['formations_a_venir'] = Formation.objects.formations_a_venir().count()
        context['formations_terminees'] = Formation.objects.formations_terminees().count()
        context['formations_a_recruter'] = Formation.objects.formations_a_recruter().count()

        # ✅ Places prévues et disponibles
        context['total_places_prevues'] = Formation.objects.aggregate(
            total=Sum(F('prevus_crif') + F('prevus_mp'))
        )['total'] or 0

        context['total_places_prevues_crif'] = Formation.objects.aggregate(
            total=Sum('prevus_crif')
        )['total'] or 0

        context['total_places_prevues_mp'] = Formation.objects.aggregate(
            total=Sum('prevus_mp')
        )['total'] or 0

        context['total_places_restantes'] = Formation.objects.aggregate(
            total=Sum(F('prevus_crif') + F('prevus_mp') - F('inscrits_crif') - F('inscrits_mp'))
        )['total'] or 0

        context['total_places_restantes_crif'] = Formation.objects.aggregate(
            total=Sum(F('prevus_crif') - F('inscrits_crif'))
        )['total'] or 0

        context['total_places_restantes_mp'] = Formation.objects.aggregate(
            total=Sum(F('prevus_mp') - F('inscrits_mp'))
        )['total'] or 0

        # ✅ Recrutement et inscriptions
        context['total_candidats'] = Formation.objects.aggregate(total=Sum('nombre_candidats'))['total'] or 0
        context['total_entretiens'] = Formation.objects.aggregate(total=Sum('nombre_entretiens'))['total'] or 0
        context['total_inscrits'] = Formation.objects.aggregate(total=Sum(F('inscrits_crif') + F('inscrits_mp')))['total'] or 0
        context['total_inscrits_crif'] = Formation.objects.aggregate(total=Sum('inscrits_crif'))['total'] or 0
        context['total_inscrits_mp'] = Formation.objects.aggregate(total=Sum('inscrits_mp'))['total'] or 0

        # ✅ Calcul des taux moyens avec gestion d'erreur (évite division par zéro)
        try:
            context['taux_transformation_moyen'] = Formation.objects.aggregate(
                taux=Avg(100 * (F('inscrits_crif') + F('inscrits_mp')) / Coalesce(F('nombre_candidats'), Value(1)))
            )['taux'] or 0
        except ZeroDivisionError:
            context['taux_transformation_moyen'] = 0

        try:
            context['taux_saturation_moyen'] = Formation.objects.aggregate(
                taux=Avg(100 * (F('inscrits_crif') + F('inscrits_mp')) / Coalesce(F('prevus_crif') + F('prevus_mp'), Value(1)))
            )['taux'] or 0
        except ZeroDivisionError:
            context['taux_saturation_moyen'] = 0

        # ✅ Nombre de partenaires
        context['total_partenaires'] = Partenaire.objects.count()

        # ✅ Derniers commentaires des formations
        context['derniers_commentaires'] = (
            Commentaire.objects.select_related('formation', 'utilisateur')
            .order_by('-created_at')[:5]
        )

        # ✅ Candidats et Entretiens par Centre
        candidats_par_centre = (
            Centre.objects.annotate(
                total_candidats=Sum('formations__nombre_candidats'),
                total_entretiens=Sum('formations__nombre_entretiens')
            )
            .filter(Q(total_candidats__gt=0) | Q(total_entretiens__gt=0))
            .order_by('-total_candidats')
        )
        context['candidats_par_centre'] = candidats_par_centre

        # ✅ Places prévues et Inscrits par Centre
        places_par_centre = (
            Centre.objects.annotate(
                total_places_prevues=Sum(F('formations__prevus_crif') + F('formations__prevus_mp')),
                total_inscrits=Sum(F('formations__inscrits_crif') + F('formations__inscrits_mp')),
                places_prevues_crif=Sum('formations__prevus_crif'),
                places_prevues_mp=Sum('formations__prevus_mp'),
                inscrits_crif=Sum('formations__inscrits_crif'),
                inscrits_mp=Sum('formations__inscrits_mp')
            )
            .filter(total_places_prevues__gt=0)
            .order_by('-total_places_prevues')
        )
        context['places_par_centre'] = places_par_centre

        # ✅ Taux de transformation et saturation par Centre
        taux_par_centre = (
            Centre.objects.annotate(
                total_formations=Count('formations'),  # Ajout du total des formations
                total_candidats=Sum('formations__nombre_candidats'),
                total_entretiens=Sum('formations__nombre_entretiens'), 
                places_prevues_crif=Sum('formations__prevus_crif'),  # ✅ Ajout des places CRIF
                inscrits_crif=Sum('formations__inscrits_crif'),  # ✅ Ajout des inscrits CRIF
                places_prevues_mp=Sum('formations__prevus_mp'),  # ✅ Ajout des places MP
                inscrits_mp=Sum('formations__inscrits_mp'),  # ✅ Ajout des inscrits MP
                total_inscrits=Sum(F('formations__inscrits_crif') + F('formations__inscrits_mp')),
                total_places_prevues=Sum(F('formations__prevus_crif') + F('formations__prevus_mp')),
                taux_transformation=Case(
                    When(total_candidats__gt=0, 
                        then=100.0 * Sum(F('formations__inscrits_crif') + F('formations__inscrits_mp')) / Coalesce(Sum('formations__nombre_candidats'), Value(1))),
                    default=Value(0.0)
                ),
                taux_saturation=Case(
                    When(total_places_prevues__gt=0, 
                        then=100.0 * Sum(F('formations__inscrits_crif') + F('formations__inscrits_mp')) / Coalesce(Sum(F('formations__prevus_crif') + F('formations__prevus_mp')), Value(1))),
                    default=Value(0.0)
                )
            )
            .filter(Q(total_candidats__gt=0) | Q(total_places_prevues__gt=0))
            .order_by('-taux_saturation')
        )
        context['taux_par_centre'] = taux_par_centre

        # ✅ Préparation des stats pour l'affichage en haut du tableau de bord
        context['stats'] = [
            (context['total_formations'], "Formations", "primary", "fa-graduation-cap"),
            (context['total_candidats'], "Candidats", "secondary", "fa-users"),
            (context['total_entretiens'], "Entretiens", "warning", "fa-handshake"),
            (context['total_inscrits'], "Inscrits", "success", "fa-user-check"),
            (context['total_places_prevues'], "Places prévues", "info", "fa-calendar-alt"),
            (context['total_places_restantes'], "Places restantes", "danger", "fa-calendar-times"),
        ]

        # ✅ Événements par type
        context['evenements_par_type'] = (
            Evenement.objects.values('type_evenement')
            .annotate(total=Count('id'))
            .order_by('-total')
        )

        # ✅ Récupération du nombre total d'événements par centre + détails par type
        evenements_par_centre = (
            Centre.objects.annotate(
                total_evenements=Count('formations__evenements', distinct=True)  # Utilisation du related_name
            )
        )

        details_evenements_par_centre = []
        for centre in evenements_par_centre:
            evenements = (
                Evenement.objects.filter(formation__centre=centre)
                .values('type_evenement')
                .annotate(total=Count('id'))
                .order_by('-total')
            )

            details_evenements_par_centre.append({
                'centre': centre,
                'total_evenements': centre.total_evenements,  # Total des événements pour ce centre
                'evenements': evenements
            })

        # ✅ Ajout au contexte
        context['evenements_par_centre'] = details_evenements_par_centre

        return context  # ✅ Retourne correctement le contexte sans écrasement





class StatsAPIView(View):
    """API pour récupérer les statistiques du Dashboard"""

    def get(self, request, *args, **kwargs):
        action = request.GET.get('action')

        if action == 'formations_par_statut':
            return self.formations_par_statut()
        elif action == 'evolution_formations':
            return self.evolution_formations()
        elif action == 'formations_par_type':
            return self.formations_par_type()
        else:
            return JsonResponse({'error': 'Action non reconnue'}, status=400)

    def formations_par_statut(self):
        """Renvoie le nombre de formations par statut"""
        statuts = Statut.objects.annotate(
            nb_formations=Count('formations'),
            taux_moyen=Coalesce(
                Avg(
                    100.0 * (F('formations__inscrits_crif') + F('formations__inscrits_mp')) /
                    Coalesce(F('formations__prevus_crif') + F('formations__prevus_mp'), Value(1))
                ),
                Value(0.0),
                output_field=FloatField()
            )
        ).values('nom', 'nb_formations', 'taux_moyen', 'couleur')

        return JsonResponse({'statuts': list(statuts)})

    def evolution_formations(self):
        """Renvoie l'évolution du nombre de formations et d'inscrits par période"""
        date_limite = timezone.now().date() - timedelta(days=365)
        periode = self.request.GET.get('periode', 'mois')
        
        # Récupérer l'historique des formations
        query = HistoriqueFormation.objects.filter(created_at__gte=date_limite)
        
        # Définir comment obtenir la période selon le choix
        result = {}
        for historique in query:
            created_at = historique.created_at
            
            if periode == 'semaine':
                # Obtenir année et semaine
                year, week_num, _ = created_at.isocalendar()
                key = f"{year}-{week_num:02d}"
                label = f"Sem {week_num}, {year}"
            elif periode == 'annee':
                # Obtenir année
                year = created_at.year
                key = str(year)
                label = str(year)
            else:  # mois par défaut
                # Obtenir année et mois
                year = created_at.year
                month = created_at.month
                key = f"{year}-{month:02d}"
                label = f"{month:02d}/{year}"
            
            if key not in result:
                result[key] = {
                    'periode_evolution': key,
                    'label': label,
                    'nb_formations': 0,
                    'nb_inscrits': 0,
                    'total_candidats': 0,
                    'total_entretiens': 0,
                    'taux_saturation': 0,
                    'taux_transformation': 0,
                    'count': 0  # Pour calculer des moyennes
                }
            
            # Incrémenter les compteurs
            result[key]['nb_formations'] += 1
            
            # Traiter les champs qui peuvent être None
            if historique.inscrits_total is not None:
                result[key]['nb_inscrits'] += historique.inscrits_total
            
            if historique.formation is not None:
                # Candidats et entretiens de la formation
                candidats = getattr(historique.formation, 'nombre_candidats', 0) or 0
                entretiens = getattr(historique.formation, 'nombre_entretiens', 0) or 0
                result[key]['total_candidats'] += candidats
                result[key]['total_entretiens'] += entretiens
            
            if historique.saturation is not None:
                result[key]['taux_saturation'] += historique.saturation
                result[key]['count'] += 1
            
            # Transformation: calculer le rapport inscrits/candidats
            if candidats > 0 and historique.inscrits_total is not None:
                transformation = (historique.inscrits_total / candidats) * 100
                result[key]['taux_transformation'] += transformation
                # Ne pas incrémenter count à nouveau, nous utiliserons le même compte pour les deux moyennes
        
        # Calculer les moyennes
        evolution_list = []
        for key, data in result.items():
            if data['count'] > 0:
                data['taux_saturation'] = round(data['taux_saturation'] / data['count'], 1)
                data['taux_transformation'] = round(data['taux_transformation'] / data['count'], 1)
            del data['count']
            evolution_list.append(data)
        
        # Trier par période
        evolution_list.sort(key=lambda x: x['periode_evolution'])
        
        print(f"Données d'évolution réelles: {len(evolution_list)} périodes trouvées pour {periode}")
        return JsonResponse({'evolution': evolution_list})