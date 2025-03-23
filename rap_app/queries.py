# Exemple de code pour obtenir les statistiques

from django.db.models import Count, F, Sum, FloatField, ExpressionWrapper
from django.utils import timezone
from datetime import datetime

from .models.prepa_comp import Candidat, Departement, Entree, Mois, ObjectifAnnuel, Semaine


def get_stats_semaine_courante():
    """Récupère les statistiques pour la semaine courante"""
    semaine = Semaine.creer_semaine_courante()
    
    # Nombre d'entrées et de candidats pour la semaine
    nombre_entrees = semaine.nombre_entrees
    nombre_candidats = semaine.nombre_candidats
    
    # Taux de transformation
    taux = semaine.taux_transformation
    
    # Pourcentage d'atteinte de l'objectif hebdomadaire
    pourcentage_objectif = semaine.pourcentage_objectif_hebdomadaire
    
    # Objectif hebdomadaire
    objectif_hebdo = semaine.objectif_annuel.objectif_hebdomadaire()
    
    # Statistiques par département
    stats_departements = semaine.stats_par_departement()
    
    return {
        'semaine': semaine,
        'nombre_entrees': nombre_entrees,
        'nombre_candidats': nombre_candidats,
        'taux_transformation': taux,
        'pourcentage_objectif': pourcentage_objectif,
        'objectif_hebdo': objectif_hebdo,
        'stats_departements': stats_departements
    }


def get_stats_mois_courant():
    """Récupère les statistiques pour le mois courant"""
    mois = Mois.creer_mois_courant()
    
    # Nombre d'entrées et de candidats pour le mois
    nombre_entrees = mois.nombre_entrees
    nombre_candidats = mois.nombre_candidats
    
    # Taux de transformation
    taux = mois.taux_transformation
    
    # Pourcentage d'atteinte de l'objectif mensuel
    pourcentage_objectif = mois.pourcentage_objectif_mensuel
    
    # Objectif mensuel
    objectif_mensuel = mois.objectif_annuel.objectif_mensuel()
    
    # Statistiques par département
    stats_departements = mois.stats_par_departement()
    
    # Liste des semaines du mois
    semaines = mois.get_semaines()
    
    return {
        'mois': mois,
        'nombre_entrees': nombre_entrees,
        'nombre_candidats': nombre_candidats,
        'taux_transformation': taux,
        'pourcentage_objectif': pourcentage_objectif,
        'objectif_mensuel': objectif_mensuel,
        'stats_departements': stats_departements,
        'semaines': semaines
    }


def get_stats_annee_courante():
    """Récupère les statistiques pour l'année courante"""
    annee_courante = timezone.now().year
    objectif_annuel = ObjectifAnnuel.get_current_year_objectif()
    
    # Nombre total d'entrées et de candidats pour l'année
    nombre_entrees = Entree.objects.filter(semaine__annee=annee_courante).count()
    nombre_candidats = Candidat.objects.filter(semaine__annee=annee_courante).count()
    
    # Taux de transformation
    taux = (nombre_entrees / nombre_candidats * 100) if nombre_candidats > 0 else 0
    
    # Pourcentage d'atteinte de l'objectif annuel
    pourcentage_objectif = (nombre_entrees / objectif_annuel.objectif * 100) if objectif_annuel.objectif > 0 else 0
    
    # Statistiques par département
    stats_departements = Entree.objects.filter(
        semaine__annee=annee_courante
    ).values(
        'departement__code', 'departement__nom'
    ).annotate(
        total=Count('id')
    ).order_by('departement__code')
    
    # Statistiques par mois
    stats_mois = []
    for mois_num in range(1, 13):
        try:
            mois_obj = Mois.objects.get(mois=mois_num, annee=annee_courante)
            entrees_mois = mois_obj.nombre_entrees
        except Mois.DoesNotExist:
            entrees_mois = 0
            
        stats_mois.append({
            'mois': mois_num,
            'nom_mois': Mois.get_nom_mois(mois_num),
            'entrees': entrees_mois,
            'objectif': objectif_annuel.objectif_mensuel()
        })
    
    return {
        'annee': annee_courante,
        'objectif_annuel': objectif_annuel,
        'nombre_entrees': nombre_entrees,
        'nombre_candidats': nombre_candidats,
        'taux_transformation': taux,
        'pourcentage_objectif': pourcentage_objectif,
        'stats_departements': stats_departements,
        'stats_mois': stats_mois
    }


def get_stats_historiques_semaines(nb_semaines=10):
    """Récupère les statistiques sur les n dernières semaines"""
    semaines = Semaine.objects.all().order_by('-date_debut')[:nb_semaines]
    
    resultats = []
    for semaine in semaines:
        resultats.append({
            'semaine': f"S{semaine.numero_semaine}",
            'periode': f"{semaine.date_debut} au {semaine.date_fin}",
            'entrees': semaine.nombre_entrees,
            'candidats': semaine.nombre_candidats,
            'taux_transformation': semaine.taux_transformation,
            'pourcentage_objectif': semaine.pourcentage_objectif_hebdomadaire,
            'objectif': semaine.objectif_annuel.objectif_hebdomadaire(),
            'departements': {
                stat['departement__code']: stat['total'] 
                for stat in semaine.stats_par_departement()
            }
        })
    
    return resultats


def get_stats_historiques_mois(nb_mois=12):
    """Récupère les statistiques sur les n derniers mois"""
    mois = Mois.objects.all().order_by('-annee', '-mois')[:nb_mois]
    
    resultats = []
    for m in mois:
        resultats.append({
            'mois': m.nom_mois,
            'annee': m.annee,
            'entrees': m.nombre_entrees,
            'candidats': m.nombre_candidats,
            'taux_transformation': m.taux_transformation,
            'pourcentage_objectif': m.pourcentage_objectif_mensuel,
            'objectif': m.objectif_annuel.objectif_mensuel(),
            'departements': {
                stat['departement__code']: stat['total'] 
                for stat in m.stats_par_departement()
            }
        })
    
    return resultats


def get_stats_historiques_annees(nb_annees=5):
    """Récupère les statistiques sur les n dernières années"""
    annee_courante = timezone.now().year
    annees = list(range(annee_courante, annee_courante - nb_annees, -1))
    
    resultats = []
    for annee in annees:
        try:
            objectif = ObjectifAnnuel.objects.get(annee=annee)
        except ObjectifAnnuel.DoesNotExist:
            # Si pas d'objectif défini pour cette année, passer à la suivante
            continue
            
        nombre_entrees = Entree.objects.filter(semaine__annee=annee).count()
        nombre_candidats = Candidat.objects.filter(semaine__annee=annee).count()
        
        taux = (nombre_entrees / nombre_candidats * 100) if nombre_candidats > 0 else 0
        pourcentage_objectif = (nombre_entrees / objectif.objectif * 100) if objectif.objectif > 0 else 0
        
        stats_departements = Entree.objects.filter(
            semaine__annee=annee
        ).values(
            'departement__code', 'departement__nom'
        ).annotate(
            total=Count('id')
        ).order_by('departement__code')
        
        resultats.append({
            'annee': annee,
            'entrees': nombre_entrees,
            'candidats': nombre_candidats,
            'taux_transformation': taux,
            'pourcentage_objectif': pourcentage_objectif,
            'objectif': objectif.objectif,
            'departements': {
                stat['departement__code']: stat['total'] 
                for stat in stats_departements
            }
        })
    
    return resultats


def initialiser_departements():
    """Initialise les départements de la région parisienne"""
    departements = [
        {'code': '75', 'nom': 'Paris'},
        {'code': '77', 'nom': 'Seine-et-Marne'},
        {'code': '78', 'nom': 'Yvelines'},
        {'code': '91', 'nom': 'Essonne'},
        {'code': '92', 'nom': 'Hauts-de-Seine'},
        {'code': '93', 'nom': 'Seine-Saint-Denis'},
        {'code': '94', 'nom': 'Val-de-Marne'},
        {'code': '95', 'nom': "Val-d'Oise"}
    ]
    
    for dept in departements:
        Departement.objects.get_or_create(
            code=dept['code'],
            defaults={'nom': dept['nom']}
        )