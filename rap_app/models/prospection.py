from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

from ..models.formations import Formation
from .company import Company

# ✅ Statuts possibles pour une prospection
PROSPECTION_STATUS_CHOICES = [
    ('a_faire', 'À faire'),
    ('en_cours', 'En cours'),
    ('a_relancer', 'À relancer'),
    ('acceptee', 'Acceptée'),
    ('refusee', 'Refusée'),
    ('annulee', 'Annulée'),
    ('Non renséigné', 'Non renséigné'),

]

# ✅ Objectifs de prospection
PROSPECTION_OBJECTIF_CHOICES = [
    ('prise_contact', 'Prise de contact'),
    ('rendez_vous', 'Obtenir un rendez-vous'),
    ('presentation_offre', 'Présentation d’une offre'),
    ('contrat', 'Signer un contrat'),
    ('partenariat', 'Établir un partenariat'),
    ('autre', 'Autre'),
]

# ✅ Motifs pour lesquels on fait la prospection
PROSPECTION_MOTIF_CHOICES = [
    ('POEI', 'POEI'),
    ('Apprentissage', 'Apprentissage'),
    ('VAE', 'VAE'),
    ('partenariat', 'Établir un partenariat'),
    ('autre', 'Autre'),
]

# ===============================
# 🔵 Modèle principal : Prospection
# ===============================
class Prospection(models.Model):
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE,
        related_name="prospections",
        verbose_name="Entreprise"
    )
    formation = models.ForeignKey(
        Formation, on_delete=models.CASCADE,
        null=True, blank=True,
        related_name="prospections",
        verbose_name="Formation en lien"
    )
    date_prospection = models.DateTimeField(
        default=timezone.now,
        verbose_name="Date de la prospection"
    )
    motif = models.CharField(
        max_length=30,
        choices=PROSPECTION_MOTIF_CHOICES,
        default='prise_contact',
        verbose_name="Motif de la prospection"
    )
    statut = models.CharField(
        max_length=20,
        choices=PROSPECTION_STATUS_CHOICES,
        default='a_faire',
        verbose_name="Statut de la prospection"
    )
    objectif = models.CharField(
        max_length=30,
        choices=PROSPECTION_OBJECTIF_CHOICES,
        default='prise_contact',
        verbose_name="Objectif de la prospection"
    )
    commentaire = models.TextField(
        blank=True, null=True,
        verbose_name="Commentaires de la prospection"
    )
    responsable = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_NULL,
        null=True, blank=True,
        verbose_name="Responsable de la prospection"
    )

    class Meta:
        verbose_name = "Suivi de la prospection"
        verbose_name_plural = "Suivis des prospections"
        ordering = ['-date_prospection']

    def __str__(self):
        return f"{self.company.name} - {self.formation.nom if self.formation else 'Sans formation'} - {self.get_statut_display()} - {self.get_objectif_display()}"

    # 🔁 Méthode save() personnalisée pour historiser les changements
    def save(self, *args, **kwargs):
        is_new = self.pk is None
        old_prospection = None

        # ⚠️ Si la prospection existe déjà, on récupère l'ancienne version pour détecter les changements
        if not is_new:
            try:
                old_prospection = Prospection.objects.get(pk=self.pk)
            except Prospection.DoesNotExist:
                pass

        # 💾 On sauvegarde d'abord la prospection
        super().save(*args, **kwargs)

        # 🕓 Ensuite, on vérifie s'il y a des changements à historiser
        if old_prospection:
            changement_statut = old_prospection.statut != self.statut
            changement_objectif = old_prospection.objectif != self.objectif
            changement_commentaire = old_prospection.commentaire != self.commentaire

            if changement_statut or changement_objectif or changement_commentaire:
                # 📚 Création d'un enregistrement d'historique
                HistoriqueProspection.objects.create(
                    prospection=self,
                    ancien_statut=old_prospection.statut,
                    nouveau_statut=self.statut,
                    modifie_par=self.responsable,
                    commentaire=self.commentaire or "",
                    resultat=(
                        f"Objectif modifié : {old_prospection.objectif} → {self.objectif}"
                        if changement_objectif else ""
                    ),
                    prochain_contact=timezone.now().date() + timezone.timedelta(days=7),  # ⏳ J+7 pour relancer
                )

# ===============================
# 🔵 Historique des changements
# ===============================
class HistoriqueProspection(models.Model):
    prospection = models.ForeignKey(
        Prospection, on_delete=models.CASCADE,
        related_name="historiques"
    )
    date_modification = models.DateTimeField(auto_now_add=True)
    ancien_statut = models.CharField(max_length=20, choices=PROSPECTION_STATUS_CHOICES)
    nouveau_statut = models.CharField(max_length=20, choices=PROSPECTION_STATUS_CHOICES)
    commentaire = models.TextField(null=True, blank=True)
    modifie_par = models.ForeignKey(
        get_user_model(), on_delete=models.SET_NULL,
        null=True
    )
    prochain_contact = models.DateField(
        null=True, blank=True,
        verbose_name="Date de relance"
    )
    resultat = models.TextField(
        null=True, blank=True,
        verbose_name="Résultat ou retour de la prospection"
    )
    moyen_contact = models.CharField(
        max_length=50,
        choices=[('email', 'Email'), ('telephone', 'Téléphone'), ('visite', 'Visite'), ('réseaux', 'Réseaux sociaux')],
        null=True, blank=True,
        verbose_name="Moyen de contact"
    )

    class Meta:
        ordering = ['-date_modification']
        verbose_name = "Historique de prospection"

    def __str__(self):
        return f"{self.date_modification} - {self.prospection.company.name} - {self.nouveau_statut}"
