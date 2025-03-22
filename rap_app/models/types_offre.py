# models/types_offre.py
from django.db import models
from django.core.exceptions import ValidationError
from .base import BaseModel


class TypeOffre(BaseModel):
    """
    Modèle représentant les types d'offres de formation.

    Ce modèle définit les différents types d'offres disponibles dans l'application, 
    comme CRIF, Alternance, POEC, POEI, etc. Il permet également d'ajouter un type personnalisé 
    via l'option "Autre".

    ✅ Utilisation principale :
    - Associer un type d'offre à une formation.
    - Filtrer les formations par type d'offre.
    - Permettre l'ajout d'un type personnalisé si besoin.
    """

    # Constantes pour les choix de types d'offre
    CRIF = 'crif'
    ALTERNANCE = 'alternance'
    POEC = 'poec'
    POEI = 'poei'
    TOSA = 'tosa'
    AUTRE = 'autre'
    NON_DEFINI = 'non_defini'
    
    TYPE_OFFRE_CHOICES = [
        (CRIF, 'CRIF'),
        (ALTERNANCE, 'Alternance'),
        (POEC, 'POEC'),
        (POEI, 'POEI'),
        (TOSA, 'TOSA'),
        (AUTRE, 'Autre'),
        (NON_DEFINI, 'Non défini'),
    ]
    
    nom = models.CharField(
        max_length=100, 
        choices=TYPE_OFFRE_CHOICES, 
        default=NON_DEFINI, 
        verbose_name="Type d'offre"
    )
    """
    Nom du type d'offre, avec une liste de choix prédéfinis.
    """

    autre = models.CharField(
        max_length=255, 
        blank=True,  # Suppression de null=True pour éviter les valeurs NULL sur un CharField
        verbose_name="Autre (personnalisé)"
    )
    """
    Champ permettant de spécifier un type personnalisé si "Autre" est sélectionné.
    """
    
    couleur = models.CharField(
    max_length=7,
    default='#6c757d',  # Gris Bootstrap par défaut
    verbose_name="Couleur associée (hexadécimal)"
)
    """
    Champ permettant d'ajouter une couleur aux types d'offres.
    """
    def clean(self):
        """
        Validation personnalisée :
        - Si le type d'offre est 'Autre', alors `autre` doit être rempli.
        """
        if self.nom == self.AUTRE and not self.autre:
            raise ValidationError({
                'autre': "Le champ 'autre' doit être renseigné lorsque le type d'offre est 'autre'."
            })

    def save(self, *args, **kwargs):
        self.full_clean()
        self.assign_default_color()  # 🎨 Assigne la couleur
        super().save(*args, **kwargs)


    def __str__(self):
        """
        Représentation textuelle du modèle dans l'admin Django et les logs.
        """
        return self.autre if self.nom == self.AUTRE and self.autre else self.get_nom_display()
    
    def is_personnalise(self):
        """
        Vérifie si le type d'offre est personnalisé (Autre).
        """
        return self.nom == self.AUTRE
    
    def assign_default_color(self):
        """Assigne une couleur par défaut selon le type d'offre"""
        couleurs = {
        self.CRIF: "#4e73df",         # Bleu
        self.ALTERNANCE: "#1cc88a",   # Vert
        self.POEC: "#f6c23e",         # Jaune
        self.POEI: "#e74a3b",         # Rouge
        self.TOSA: "#6f42c1",         # Violet
        self.AUTRE: "#20c997",        # Turquoise
        self.NON_DEFINI: "#6c757d",   # Gris
    }
    # On affecte seulement si aucune couleur personnalisée
        if not self.couleur or self.couleur == "#6c757d":
            self.couleur = couleurs.get(self.nom, "#6c757d")
    def get_badge_html(self):
        return f'<span class="badge" style="background-color:{self.couleur}">{self.get_nom_display()}</span>'


    class Meta:
        verbose_name = "Type d'offre"
        verbose_name_plural = "Types d'offres"
        ordering = ['nom']
        constraints = [
            models.UniqueConstraint(
                fields=['autre'],
                name='unique_autre_non_null',
                condition=models.Q(nom='autre', autre__isnull=False)
            )
        ]  # Empêche d'avoir plusieurs fois la même valeur personnalisée 'Autre'
    def text_color(self):
        """Retourne 'black' ou 'white' selon la couleur de fond"""
        if self.couleur.lower() in ['#ffff00', '#ffeb3b']:
            return 'black'
        return 'white'
