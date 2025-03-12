from django.db import models
from .base import BaseModel

class Partenaire(BaseModel):
    """
    Modèle représentant une partenaire.

    Ajout d'une relation avec `Formation` pour que les partenaires puissent être utilisées comme ressources.
    """

    nom = models.CharField(max_length=255, verbose_name="Nom du partenaire", unique=True )
    secteur_activite = models.CharField(max_length=255, verbose_name="Secteur d'activité",blank=True,null=True)
    contact_nom = models.CharField(max_length=255,verbose_name="Nom du contact",blank=True,null=True)
    contact_poste = models.CharField(max_length=255,verbose_name="Poste du contact",blank=True,null=True)
    contact_telephone = models.CharField(max_length=20, verbose_name="Téléphone du contact", blank=True, null=True)
    contact_email = models.EmailField(verbose_name="Email du contact", blank=True, null=True)
    description = models.TextField(verbose_name="Description de la relation", blank=True, null=True)

    # Manager par défaut (si PartenaireManager est supprimé)
    objects = models.Manager()

    def __str__(self):
        """Représentation lisible du partenaire."""
        return self.nom

    class Meta:
        verbose_name = "Partenaire"
        verbose_name_plural = "Partenaires"
        ordering = ['nom']
        indexes = [
            models.Index(fields=['nom']),  # Index pour optimiser la recherche par nom.
        ]
