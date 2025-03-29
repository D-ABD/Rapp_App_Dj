from django.db import models, transaction
from django.utils import timezone
from django.db.models import Sum

from datetime import timedelta
from django.core.exceptions import ValidationError
from django.db import IntegrityError

from ..models.centres import Centre 

import logging
logger = logging.getLogger(__name__)

# Constante pour l'affichage des noms de mois
NOMS_MOIS = {
    1: 'Janvier', 2: 'Février', 3: 'Mars', 4: 'Avril',
    5: 'Mai', 6: 'Juin', 7: 'Juillet', 8: 'Août',
    9: 'Septembre', 10: 'Octobre', 11: 'Novembre', 12: 'Décembre'
}





class Semaine(models.Model):
    """
    Suivi hebdomadaire d’un centre pour une année donnée
    """
    centre = models.ForeignKey(Centre, on_delete=models.CASCADE, null=True, blank=True)
    date_debut = models.DateField()
    date_fin = models.DateField()
    numero_semaine = models.PositiveIntegerField()
    mois = models.PositiveIntegerField()
    annee = models.PositiveIntegerField()
    objectif_hebdo_prepa = models.PositiveIntegerField(default=0)

    nombre_candidats = models.PositiveIntegerField(default=0)
    nombre_prescriptions = models.PositiveIntegerField(default=0)
    nombre_adhesions = models.PositiveIntegerField(default=0)
    nombre_presents = models.PositiveIntegerField(default=0)
    nombre_places_ouvertes = models.PositiveIntegerField(default=0)

    # Nouveau : pour suivre les adhésions par département (ex: {"92": 10, "95": 3})
    departements = models.JSONField(default=dict, blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.pk:
            logger.info(f"🔁 Semaine modifiée : semaine {self.numero_semaine} ({self.date_debut} - {self.date_fin}) - Centre: {self.centre}")
        else:
            logger.info(f"🆕 Semaine créée : semaine {self.numero_semaine} ({self.date_debut} - {self.date_fin}) - Centre: {self.centre}")
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        logger.warning(f"🗑️ Semaine supprimée : semaine {self.numero_semaine} ({self.date_debut} - {self.date_fin}) - Centre: {self.centre}")
        super().delete(*args, **kwargs)


    class Meta:
        ordering = ['-date_debut']
        unique_together = ['numero_semaine', 'annee', 'centre']
        verbose_name = "Semaine"
        verbose_name_plural = "Semaines"

    def __str__(self):
        centre_nom = self.centre.nom if self.centre else "Sans centre"
        return f"Semaine {self.numero_semaine} ({self.date_debut} au {self.date_fin}) - {centre_nom}"

    def clean(self):
        if self.date_debut and self.date_fin and self.date_debut > self.date_fin:
            raise ValidationError("La date de début doit être avant la date de fin.")

        # Vérifie si une autre semaine existe déjà pour le même centre / année / numéro
        if Semaine.objects.exclude(pk=self.pk).filter(
            centre=self.centre,
            annee=self.annee,
            numero_semaine=self.numero_semaine
        ).exists():
            raise ValidationError("Une semaine avec ce numéro existe déjà pour ce centre et cette année.")

        super().clean()



    @property
    def taux_transformation(self):
        if self.nombre_candidats == 0:
            return 0
        return (self.nombre_adhesions / self.nombre_candidats) * 100

    @property
    def pourcentage_objectif_hebdomadaire(self):
        return (self.nombre_adhesions / self.objectif_hebdo_prepa) * 100 if self.objectif_hebdo_prepa else 0


    @classmethod
    def creer_semaine_courante(cls, centre):
        """
        Crée automatiquement la semaine courante pour un centre donné
        """
        aujourd_hui = timezone.now().date()
        debut_semaine = aujourd_hui - timedelta(days=aujourd_hui.weekday())
        fin_semaine = debut_semaine + timedelta(days=6)
        numero_semaine = debut_semaine.isocalendar()[1]
        mois = debut_semaine.month
        annee = debut_semaine.year

        semaine, _ = cls.objects.get_or_create(
            numero_semaine=numero_semaine,
            annee=annee,
            centre=centre,
            defaults={
                'date_debut': debut_semaine,
                'date_fin': fin_semaine,
                'mois': mois,
            }
        )
        return semaine




class PrepaCompGlobal(models.Model):
    """
    Statistiques annuelles cumulées d’un centre
    """
    centre = models.ForeignKey(Centre, on_delete=models.CASCADE, null=True, blank=True)
    annee = models.PositiveIntegerField()
    total_candidats = models.PositiveIntegerField(default=0)
    total_prescriptions = models.PositiveIntegerField(default=0)
    total_presents = models.PositiveIntegerField(default=0)
    total_places_ouvertes = models.PositiveIntegerField(default=0)
    adhesions= models.PositiveIntegerField(default=0)


    class Meta:
        verbose_name = "Prépa Comp Global"
        verbose_name_plural = "Prépas Comp Global"
        unique_together = ['annee', 'centre']

    def __str__(self):
        return f"Prépa Comp - {self.centre} ({self.annee})"

    def save(self, *args, **kwargs):
        if self.pk:
            logger.info(f"🔁 PrepaCompGlobal modifié : {self.annee} - Centre: {self.centre}")
        else:
            logger.info(f"🆕 PrepaCompGlobal créé : {self.annee} - Centre: {self.centre}")
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        logger.warning(f"🗑️ PrepaCompGlobal supprimé : {self.annee} - Centre: {self.centre}")
        super().delete(*args, **kwargs)

    def taux_transformation(self):
        return (self.adhesions / self.total_candidats) * 100 if self.total_candidats else 0

    def taux_objectif_annee(self):
        objectif = self.centre.objectif_annuel_prepa if self.centre and self.centre.objectif_annuel_prepa else 0
        return (self.adhesions / objectif) * 100 if objectif else 0

    # ---- Méthodes de stats globales ----

    @classmethod
    def total_adhesions(cls, annee):
        """
        Total des adhésions enregistrées dans PrepaCompGlobal pour une année donnée
        """
        return cls.objects.filter(annee=annee).aggregate(total=Sum('adhesions'))['total'] or 0

    @classmethod
    def objectif_annuel_global(cls):
        """
        Somme des objectifs annuels de tous les centres
        """
        return Centre.objects.aggregate(total=Sum('objectif_annuel_prepa'))['total'] or 0

    @classmethod
    def objectif_hebdo_global(cls, annee=None):
        """
        Somme des objectifs hebdomadaires de toutes les semaines (via Semaine)
        """
        queryset = Semaine.objects.all()
        if annee:
            queryset = queryset.filter(annee=annee)
        return queryset.aggregate(total=Sum('objectif_hebdo_prepa'))['total'] or 0

    # ---- Objectifs par centre ----

    @staticmethod
    def objectif_calcule_centre(centre, annee=None):
        """
        Total des objectifs hebdomadaires déclarés pour un centre sur une année
        """
        queryset = Semaine.objects.filter(centre=centre)
        if annee:
            queryset = queryset.filter(annee=annee)
        return queryset.aggregate(total=Sum('objectif_hebdo_prepa'))['total'] or 0

    @classmethod
    def objectifs_par_centre(cls, annee=None):
        """
        Liste des objectifs définis et calculés pour tous les centres
        """
        centres = Centre.objects.all()
        resultats = []
        for centre in centres:
            objectif_calcule = cls.objectif_calcule_centre(centre, annee)
            resultats.append({
                'centre': centre,
                'objectif_annuel_defini': centre.objectif_annuel_prepa or 0,
                'objectif_calculé': objectif_calcule
            })
        return resultats

    # ---- Statistiques mensuelles ----

    @classmethod
    def stats_par_mois(cls, annee, centre):
        """
        Statistiques mensuelles par centre, basées sur les semaines
        """
        stats = []
        for mois in range(1, 13):
            semaines = Semaine.objects.filter(annee=annee, mois=mois, centre=centre)
            total = semaines.aggregate(
                adhesions=Sum('nombre_adhesions'),
                total_candidats=Sum('nombre_candidats')
            )
            stats.append({
                'mois': mois,
                'mois_nom': NOMS_MOIS.get(mois, f"Mois {mois}"),
                'adhesions': total['adhesions'] or 0,
                'candidats': total['total_candidats'] or 0,
                'taux_transformation': (
                    (total['adhesions'] / total['total_candidats']) * 100
                    if total['total_candidats'] else 0
                )
            })
        return stats

    @classmethod
    def stats_mensuelles(cls, annee, mois, centre):
        """
        Statistiques pour un seul mois précis d’un centre
        """
        semaines = Semaine.objects.filter(annee=annee, mois=mois, centre=centre)
        total = semaines.aggregate(
            adhesions=Sum('nombre_adhesions'),
            total_candidats=Sum('nombre_candidats')
        )
        return {
            'adhesions': total['adhesions'] or 0,
            'candidats': total['total_candidats'] or 0,
            'taux_transformation': (
                total['adhesions'] / total['total_candidats'] * 100
                if total['total_candidats'] else 0
            ),
            'objectif': (centre.objectif_annuel_prepa or 0) / 12 if centre else 0
        }