# models/statut.py
from django.db import models
from django.core.exceptions import ValidationError
from .base import BaseModel

def get_default_color(statut_nom):
    """
    Retourne une couleur prédéfinie selon le type de statut.
    """
    COULEURS_PREDEFINIES = {
        'non_defini': "#FFEB3B",  # 🟡 Jaune (texte noir lisible)
        'recrutement_en_cours': "#4CAF50", # Vert
        'formation_en_cours': "#2196F3",  # Bleu
        'formation_a_annuler': "#FF9800", # Orange
        'formation_a_repousser': "#FFEB3B", # Jaune
        'formation_annulee': "#F44336",   # Rouge
        'pleine': "#9C27B0",             # Violet
        'quasi_pleine': "#3F51B5",       # Indigo
        'autre': "#795548",              # Marron
    }
    return COULEURS_PREDEFINIES.get(statut_nom, "#607D8B")  # Bleu-gris par défaut

class Statut(BaseModel):
    """
    Modèle représentant les statuts des formations.

    Ce modèle définit les différents états possibles d'une formation (ex: "Recrutement en cours", 
    "Formation en cours", "Formation annulée", etc.). Il permet également d'ajouter une couleur 
    pour une meilleure visibilité et un statut personnalisé si nécessaire.

    ✅ Utilisation principale :
    - Assigner un statut à une formation.
    - Permettre l'affichage du statut sous forme colorée sur l'interface utilisateur.
    - Offrir une flexibilité avec un statut "Autre" personnalisable.
    """

    # Constantes pour les choix de statut
    NON_DEFINI = 'non_defini'
    RECRUTEMENT_EN_COURS = 'recrutement_en_cours'
    FORMATION_EN_COURS = 'formation_en_cours'
    FORMATION_A_ANNULER = 'formation_a_annuler'
    FORMATION_A_REPOUSSER = 'formation_a_repousser'
    FORMATION_ANNULEE = 'formation_annulee'
    PLEINE = 'pleine'
    QUASI_PLEINE = 'quasi_pleine'
    AUTRE = 'autre'
    
    STATUT_CHOICES = [
        (NON_DEFINI, 'Non défini'),
        (RECRUTEMENT_EN_COURS, 'Recrutement en cours'),
        (FORMATION_EN_COURS, 'Formation en cours'),
        (FORMATION_A_ANNULER, 'Formation à annuler'),
        (FORMATION_A_REPOUSSER, 'Formation à repousser'),
        (FORMATION_ANNULEE, 'Formation annulée'),
        (PLEINE, 'Pleine'),
        (QUASI_PLEINE, 'Quasi-pleine'),
        (AUTRE, 'Autre'),
    ]
    
    nom = models.CharField(
        max_length=100, 
        choices=STATUT_CHOICES, 
        verbose_name="Nom du statut"
    )
    """
    Nom du statut, avec des choix prédéfinis.
    """

    couleur = models.CharField(
        max_length=7,  # Format #RRGGBB
        verbose_name="Couleur", 
        help_text="Couleur hexadécimale (ex: #FF5733)",
        blank=True  # Permet d'assigner une couleur par défaut si vide
    )
    """
    Code couleur associé au statut.
    Exemple : `#FF0000` pour rouge, `#00FF00` pour vert.
    Si ce champ est vide, une couleur prédéfinie selon le type de statut sera attribuée.
    """

    description_autre = models.CharField(
        max_length=255, 
        blank=True, 
        null=True, 
        verbose_name="Description personnalisée"
    )
    """
    Permet de renseigner une description si le statut sélectionné est "Autre".
    Obligatoire si le statut est `AUTRE`.
    """

    def clean(self):
        """
        Validation personnalisée :
        - Si le statut est 'Autre', alors `description_autre` doit être rempli.
        """
        if self.nom == self.AUTRE and not self.description_autre:
            raise ValidationError({
                'description_autre': "Le champ 'description_autre' doit être renseigné lorsque le statut est 'autre'."
            })

    def get_nom_display(self):
        """
        Retourne le nom du statut. Si le statut est 'Autre', affiche la description à la place.
        """
        if self.nom == self.AUTRE and self.description_autre:
            return self.description_autre  # ✅ Retourne la description si le statut est "Autre"
        return dict(self.STATUT_CHOICES).get(self.nom, self.nom)  # ✅ Sinon, retourne le nom normal

    def get_badge_html(self):
        return f'<span class="badge" style="background-color:{self.couleur}">{self.get_nom_display()}</span>'

    def save(self, *args, **kwargs):
        """
        Sauvegarde avec validation :
        - Assigne une couleur prédéfinie si aucune couleur n'est spécifiée.
        - Appelle `clean()` avant l'enregistrement en base de données.
        """
        if not self.couleur:
            self.couleur = get_default_color(self.nom)
        
        self.full_clean()  # Applique les validations avant l'enregistrement
        super().save(*args, **kwargs)

    def __str__(self):
        """
        Représentation textuelle du modèle dans l'admin Django et les logs.
        """
        if self.nom == self.AUTRE and self.description_autre:
            return f"{self.description_autre} - {self.couleur}"
        return f"{self.get_nom_display()} "

    class Meta:
        verbose_name = "Statut"
        verbose_name_plural = "Statuts"
        ordering = ['nom']