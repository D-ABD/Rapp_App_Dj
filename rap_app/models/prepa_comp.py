from django.db import models
from django.utils import timezone
from django.db.models import Sum, Count, F, FloatField, ExpressionWrapper
from datetime import datetime, timedelta


class Departement(models.Model):
    """Modèle pour les départements"""
    code = models.CharField(max_length=3, unique=True)
    nom = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.code} - {self.nom}"


class ObjectifAnnuel(models.Model):
    """Modèle pour définir les objectifs annuels"""
    annee = models.PositiveIntegerField(unique=True)
    objectif = models.IntegerField(default=430)
    
    def __str__(self):
        return f"Objectif {self.annee}: {self.objectif} entrées"
    
    @classmethod
    def get_current_year_objectif(cls):
        """Récupère ou crée l'objectif de l'année en cours"""
        annee_courante = timezone.now().year
        obj, created = cls.objects.get_or_create(
            annee=annee_courante,
            defaults={'objectif': 430}
        )
        return obj
    
    def objectif_hebdomadaire(self):
        """Calcule l'objectif hebdomadaire basé sur l'objectif annuel"""
        # Nombre approximatif de semaines dans l'année
        return round(self.objectif / 52, 1)
    
    def objectif_mensuel(self):
        """Calcule l'objectif mensuel basé sur l'objectif annuel"""
        return round(self.objectif / 12, 1)


class Semaine(models.Model):
    """Modèle pour suivre les données par semaine"""
    date_debut = models.DateField()
    date_fin = models.DateField()
    numero_semaine = models.PositiveIntegerField()
    mois = models.PositiveIntegerField()
    annee = models.PositiveIntegerField()
    objectif_annuel = models.ForeignKey(ObjectifAnnuel, on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['-date_debut']
        unique_together = ['numero_semaine', 'annee']
    
    def __str__(self):
        return f"Semaine {self.numero_semaine} ({self.date_debut} au {self.date_fin})"
    
    @property
    def taux_transformation(self):
        """Calcule le taux de transformation candidats vs adhésions"""
        if self.nombre_candidats == 0:
            return 0
        return (self.nombre_entrees / self.nombre_candidats) * 100
    
    @property
    def nombre_entrees(self):
        """Nombre total d'entrées pour la semaine"""
        return self.entree_set.count()
    
    @property
    def nombre_candidats(self):
        """Nombre total de candidats pour la semaine"""
        return self.candidat_set.count()
    
    @property
    def pourcentage_objectif_hebdomadaire(self):
        """Pourcentage d'atteinte de l'objectif hebdomadaire"""
        objectif_hebdo = self.objectif_annuel.objectif_hebdomadaire()
        return (self.nombre_entrees / objectif_hebdo) * 100 if objectif_hebdo else 0
    
    @classmethod
    def creer_semaine_courante(cls):
        """Crée une entrée pour la semaine courante si elle n'existe pas"""
        aujourd_hui = timezone.now().date()
        # Calcul du lundi et dimanche de la semaine courante
        debut_semaine = aujourd_hui - timedelta(days=aujourd_hui.weekday())
        fin_semaine = debut_semaine + timedelta(days=6)
        
        # Récupérer l'objectif annuel courant
        objectif_annuel = ObjectifAnnuel.get_current_year_objectif()
        
        # Déterminer le numéro de semaine et le mois
        numero_semaine = debut_semaine.isocalendar()[1]
        mois = debut_semaine.month
        annee = debut_semaine.year
        
        semaine, created = cls.objects.get_or_create(
            numero_semaine=numero_semaine,
            annee=annee,
            defaults={
                'date_debut': debut_semaine,
                'date_fin': fin_semaine,
                'mois': mois,
                'objectif_annuel': objectif_annuel
            }
        )
        return semaine

    def stats_par_departement(self):
        """Retourne les statistiques par département"""
        return Entree.objects.filter(semaine=self).values(
            'departement__code', 'departement__nom'
        ).annotate(
            total=Count('id')
        ).order_by('departement__code')


class Mois(models.Model):
    """Modèle pour suivre les données par mois"""
    mois = models.PositiveIntegerField()
    annee = models.PositiveIntegerField()
    objectif_annuel = models.ForeignKey(ObjectifAnnuel, on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['-annee', '-mois']
        unique_together = ['mois', 'annee']
    
    def __str__(self):
        return f"{self.get_nom_mois()} {self.annee}"
    
    @staticmethod
    def get_nom_mois(mois_numero=None):
        """Retourne le nom du mois à partir du numéro"""
        noms_mois = [
            'Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin',
            'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre'
        ]
        if mois_numero is None:
            return noms_mois
        return noms_mois[mois_numero - 1]
    
    @property
    def nom_mois(self):
        """Retourne le nom du mois"""
        return self.get_nom_mois(self.mois)
    
    @classmethod
    def creer_mois_courant(cls):
        """Crée une entrée pour le mois courant si elle n'existe pas"""
        aujourd_hui = timezone.now().date()
        mois = aujourd_hui.month
        annee = aujourd_hui.year
        
        # Récupérer l'objectif annuel courant
        objectif_annuel = ObjectifAnnuel.get_current_year_objectif()
        
        mois_obj, created = cls.objects.get_or_create(
            mois=mois,
            annee=annee,
            defaults={'objectif_annuel': objectif_annuel}
        )
        return mois_obj
    
    def get_semaines(self):
        """Récupère toutes les semaines de ce mois"""
        return Semaine.objects.filter(mois=self.mois, annee=self.annee)
    
    @property
    def nombre_entrees(self):
        """Nombre total d'entrées pour le mois"""
        return Entree.objects.filter(
            semaine__mois=self.mois, 
            semaine__annee=self.annee
        ).count()
    
    @property
    def nombre_candidats(self):
        """Nombre total de candidats pour le mois"""
        return Candidat.objects.filter(
            semaine__mois=self.mois, 
            semaine__annee=self.annee
        ).count()
    
    @property
    def taux_transformation(self):
        """Calcule le taux de transformation candidats vs adhésions pour le mois"""
        if self.nombre_candidats == 0:
            return 0
        return (self.nombre_entrees / self.nombre_candidats) * 100
    
    @property
    def pourcentage_objectif_mensuel(self):
        """Pourcentage d'atteinte de l'objectif mensuel"""
        objectif_mensuel = self.objectif_annuel.objectif_mensuel()
        return (self.nombre_entrees / objectif_mensuel) * 100 if objectif_mensuel else 0
    
    def stats_par_departement(self):
        """Retourne les statistiques par département pour le mois"""
        return Entree.objects.filter(
            semaine__mois=self.mois, 
            semaine__annee=self.annee
        ).values(
            'departement__code', 'departement__nom'
        ).annotate(
            total=Count('id')
        ).order_by('departement__code')


class Candidat(models.Model):
    """Modèle pour les candidats"""
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telephone = models.CharField(max_length=20, blank=True, null=True)
    date_candidature = models.DateTimeField(auto_now_add=True)
    semaine = models.ForeignKey(Semaine, on_delete=models.CASCADE)
    departement = models.ForeignKey(Departement, on_delete=models.CASCADE)
    a_adhere = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.prenom} {self.nom}"
    
    def save(self, *args, **kwargs):
        """Surcharge de la méthode save pour mettre à jour le statut d'adhésion"""
        if not self.semaine_id:
            self.semaine = Semaine.creer_semaine_courante()
        super().save(*args, **kwargs)
        
        # Si le candidat a adhéré, créer une entrée automatiquement
        if self.a_adhere and not Entree.objects.filter(candidat=self).exists():
            Entree.objects.create(
                candidat=self,
                semaine=self.semaine,
                departement=self.departement,
                date_entree=timezone.now()
            )


class Entree(models.Model):
    """Modèle pour les entrées dans le dispositif"""
    candidat = models.OneToOneField(Candidat, on_delete=models.CASCADE, null=True, blank=True)
    semaine = models.ForeignKey(Semaine, on_delete=models.CASCADE)
    departement = models.ForeignKey(Departement, on_delete=models.CASCADE)
    date_entree = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        if self.candidat:
            return f"Entrée de {self.candidat} le {self.date_entree}"
        return f"Entrée le {self.date_entree} (Dépt: {self.departement.code})"
    
    def save(self, *args, **kwargs):
        """Surcharge de la méthode save pour mettre à jour le statut d'adhésion du candidat"""
        if not self.semaine_id:
            self.semaine = Semaine.creer_semaine_courante()
        
        super().save(*args, **kwargs)
        
        # Si l'entrée est liée à un candidat, mettre à jour son statut
        if self.candidat:
            self.candidat.a_adhere = True
            self.candidat.save(update_fields=['a_adhere'])