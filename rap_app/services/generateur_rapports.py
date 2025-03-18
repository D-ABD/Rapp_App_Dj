# services/generateur_rapports.py
import time
from django.db.models import Count, Avg, Sum, F, Q, FloatField
from django.db.models.functions import TruncMonth, TruncYear
from django.utils import timezone
from datetime import timedelta, date

from ..models.rapports import Rapport

from ..models import (
     Formation, Centre, Statut, TypeOffre, Evenement, 
    Commentaire, HistoriqueFormation, Recherche
)

import logging

logger = logging.getLogger(__name__)

class GenerateurRapport:
    """Service de génération des différents types de rapports."""

    def generer_rapport(type_rapport, date_debut, date_fin, **kwargs):
        debut_generation = time.time()

        logger.info(f"📊 Génération du rapport {type_rapport} ({date_debut} → {date_fin})")

        # Création du rapport
        rapport = Rapport(
            nom=f"Rapport {dict(Rapport.TYPE_CHOICES).get(type_rapport, 'Inconnu')} du {date_debut} au {date_fin}",
            type_rapport=type_rapport,
            date_debut=date_debut,
            date_fin=date_fin,
            **{k: v for k, v in kwargs.items() if k in ['centre', 'type_offre', 'statut', 'format', 'utilisateur', 'periode']}
        )

        try:
            generateur = getattr(GenerateurRapport, f"_generer_{type_rapport}", None)
            if not generateur:
                logger.error(f"❌ Aucun générateur trouvé pour {type_rapport}")
                return None

            rapport.donnees = generateur(date_debut, date_fin, **kwargs)

            # Sauvegarde du rapport
            rapport.temps_generation = time.time() - debut_generation
            rapport.save()

            logger.info(f"✅ Rapport {rapport.nom} généré et sauvegardé en {rapport.temps_generation:.2f}s")

        except Exception as e:
            logger.error(f"❌ Erreur lors de la génération du rapport {type_rapport} : {str(e)}")
            return None

        return rapport
    
    @staticmethod
    def _generer_occupation(date_debut, date_fin, **kwargs):
        """Génère un rapport d'occupation des formations."""
        formations = Formation.objects.filter(
            Q(start_date__gte=date_debut) | Q(end_date__gte=date_debut),
            Q(start_date__lte=date_fin) | Q(start_date__isnull=True),
        )
        
        if 'centre' in kwargs and kwargs['centre']:
            formations = formations.filter(centre=kwargs['centre'])
        if 'type_offre' in kwargs and kwargs['type_offre']:
            formations = formations.filter(type_offre=kwargs['type_offre'])
        if 'statut' in kwargs and kwargs['statut']:
            formations = formations.filter(statut=kwargs['statut'])
        
        # Statistiques générales
        total_formations = formations.count()
        total_places = formations.aggregate(
            total=Sum(F('prevus_crif') + F('prevus_mp'))
        )['total'] or 0
        total_inscrits = formations.aggregate(
            total=Sum(F('inscrits_crif') + F('inscrits_mp'))
        )['total'] or 0
        
        taux_moyen = 0
        if total_places > 0:
            taux_moyen = (total_inscrits / total_places) * 100
        
        # Données par formation
        formations_data = []
        for formation in formations:
            places_totales = formation.prevus_crif + formation.prevus_mp
            inscrits_totaux = formation.inscrits_crif + formation.inscrits_mp
            taux_remplissage = 0
            if places_totales > 0:
                taux_remplissage = (inscrits_totaux / places_totales) * 100
                
            formations_data.append({
                'id': formation.id,
                'nom': formation.nom,
                'centre': formation.centre.nom,
                'type_offre': formation.type_offre.get_nom_display(),
                'statut': formation.statut.get_nom_display(),
                'start_date': formation.start_date.strftime('%Y-%m-%d') if formation.start_date else None,
                'end_date': formation.end_date.strftime('%Y-%m-%d') if formation.end_date else None,
                'places_totales': places_totales,
                'inscrits_totaux': inscrits_totaux,
                'places_disponibles': places_totales - inscrits_totaux,
                'taux_remplissage': round(taux_remplissage, 2)
            })
        
        return {
            'statistiques': {
                'total_formations': total_formations,
                'total_places': total_places,
                'total_inscrits': total_inscrits,
                'taux_moyen': round(taux_moyen, 2),
                'formations_pleines': len([f for f in formations_data if f['taux_remplissage'] >= 95]),
                'formations_sous_remplies': len([f for f in formations_data if f['taux_remplissage'] < 70])
            },
            'formations': formations_data
        }
    
    @staticmethod
    def _generer_centre(date_debut, date_fin, **kwargs):
        """Génère un rapport de performance par centre."""
        # On pourrait ajouter ici le reste du code pour les 10 types de rapports
        # par souci de concision, je montre juste le principe

# Répéter pour les autres méthodes de génération de rapports