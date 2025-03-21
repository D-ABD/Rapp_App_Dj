from django.db import models
from django.core.validators import RegexValidator
from django.utils import timezone
from django.contrib.auth import get_user_model
import logging

# Configuration du logger
logger = logging.getLogger(__name__)

# Expression régulière pour les numéros de téléphone français
phone_regex = RegexValidator(
    regex=r'^(0[1-9]\d{8})$|^(?:\+33|0033)[1-9]\d{8}$',
    message="Entrez un numéro de téléphone français valide commençant par 01, 02, ..., 06 ou 07."
)

CHOICES_TYPE_OF_ACTION = [
    ('accueil_stagiaires', 'Accueil de stagiaires'),
    ('recrutement_cdi', 'Recrutement - CDI'),
    ('recrutement_cdd', 'Recrutement - CDD'),
    ('recrutement_stage', 'Recrutement - Stage'),
    ('recrutement_formation', 'Recrutement Formation'),
    ('recrutement_apprentissage', 'Recrutement - Apprentissage'),
    ('presentation_metier_entreprise', 'Présentation de métier(s)/entreprise'),
    ('enquete_metier', 'Enquête métier'),
    ('visite_entreprise', 'Visite de l’entreprise'),
    ('coaching', 'Coaching'),
    ('autre', 'Autre'),
    ('partenariat', 'Partenariat'),
    ('taxe_apprentissage', 'Taxe apprentissage'),
    ('non_definie', 'Non définie')
]

CHOICES_SOCIAL_NETWORK = [
    ("facebook", "Facebook"),
    ("twitter", "Twitter"),
    ("instagram", "Instagram"),
    ("linkedin", "LinkedIn"),
    ("tiktok", "TikTok"),
]

class Company(models.Model):
    objects = models.Manager()

    # INFORMATIONS GENERALES
    name = models.CharField(max_length=100, null=True, blank=True, verbose_name="Nom")

    # Adresse
    street_name = models.CharField(max_length=200, null=True, blank=True, verbose_name="Numéro et nom de la rue")
    zip_code = models.CharField(
        max_length=5,
        validators=[RegexValidator(regex=r'^[0-9]{5}$', message="Le code postal doit être composé de 5 chiffres.")],
        verbose_name="Code postal",
        blank=True,
        null=True,
    )
    city = models.CharField(max_length=100, verbose_name="Ville", blank=True, null=True)
    country = models.CharField(max_length=100, default="France", verbose_name="Pays", blank=True, null=True)

    # Contact principal (Sans relation avec `Person`)
    contact_name = models.CharField(max_length=255, null=True, blank=True, verbose_name="Nom du contact")
    contact_email = models.EmailField(null=True, blank=True, verbose_name="Adresse email du contact")
    contact_phone_number = models.CharField(
        max_length=20, verbose_name='Numéro de téléphone du contact', blank=True, null=True, validators=[phone_regex]
    )
    contact_job = models.CharField(max_length=255, null=True, blank=True, verbose_name="Métier du contact")

    # Informations complémentaires
    sector_name = models.CharField(max_length=200, null=True, blank=True, verbose_name="Secteur d'activité")

    # Opportunités
    actions = models.CharField(max_length=50, null=True, blank=True, choices=CHOICES_TYPE_OF_ACTION, verbose_name="Actions")
    action_description = models.CharField(max_length=5000, null=True, blank=True, verbose_name="Description de l'action")

    # Informations numériques
    website = models.URLField(null=True, blank=True, validators=[RegexValidator(regex='^(http|https)://')])
    social_network_url = models.CharField(max_length=200, verbose_name="URL du réseau social", null=True, blank=True)

    # Création et mise à jour
    created_by = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now, editable=False, verbose_name="Contact créé le")
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name="Date de MAJ")

    class Meta:
        verbose_name = 'entreprise'
        verbose_name_plural = 'entreprises'
        db_table = 'companies'

    def __str__(self):
        return f"{self.name} ({self.city}) - {self.sector_name or 'Secteur inconnu'}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
