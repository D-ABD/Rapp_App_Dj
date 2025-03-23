import logging
import re
from django.db import models, transaction
from django.core.exceptions import ValidationError
from django.utils.text import slugify
from .base import BaseModel

# Configuration du logger
logger = logging.getLogger("application.typeoffre")

class TypeOffre(BaseModel):
    """
    Modèle représentant les types d'offres de formation.

    Ce modèle définit les différents types d'offres disponibles dans l'application, 
    comme CRIF, Alternance, POEC, POEI, etc. Il permet également d'ajouter un type personnalisé 
    via l'option "Autre".

    Attributes:
        nom: Type d'offre sélectionné parmi les choix prédéfinis
        autre: Description personnalisée si le type est "Autre"
        couleur: Code couleur hexadécimal pour l'affichage visuel
        created_at: Date de création (de BaseModel)
        updated_at: Date de dernière modification (de BaseModel)
    
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
    
    # Mapping des couleurs par défaut pour chaque type d'offre
    COULEURS_PAR_DEFAUT = {
        CRIF: "#4e73df",         # Bleu
        ALTERNANCE: "#1cc88a",   # Vert
        POEC: "#f6c23e",         # Jaune
        POEI: "#e74a3b",         # Rouge
        TOSA: "#6f42c1",         # Violet
        AUTRE: "#20c997",        # Turquoise
        NON_DEFINI: "#6c757d",   # Gris
    }
    
    nom = models.CharField(
        max_length=100, 
        choices=TYPE_OFFRE_CHOICES, 
        default=NON_DEFINI, 
        verbose_name="Type d'offre",
        help_text="Sélectionnez le type d'offre de formation parmi les choix prédéfinis"
    )
    
    autre = models.CharField(
        max_length=255, 
        blank=True,
        verbose_name="Autre (personnalisé)",
        help_text="Si vous avez choisi 'Autre', précisez le type d'offre personnalisé"
    )
    
    couleur = models.CharField(
        max_length=7,
        default='#6c757d',
        verbose_name="Couleur associée (hexadécimal)",
        help_text="Code couleur hexadécimal (ex: #FF5733) pour l'affichage visuel"
    )

    def clean(self):
        """
        Validation personnalisée des données avant sauvegarde.
        
        Vérifications:
        - Si le type d'offre est 'Autre', alors `autre` doit être rempli
        - Format valide pour le code couleur hexadécimal
        - Unicité du champ 'autre' pour les types personnalisés
        
        Raises:
            ValidationError: Si les conditions de validation ne sont pas remplies
        """
        super().clean()
        
        # Validation du type "Autre"
        if self.nom == self.AUTRE and not self.autre:
            raise ValidationError({
                'autre': "Le champ 'autre' doit être renseigné lorsque le type d'offre est 'Autre'."
            })
        
        # Validation du format du code couleur
        if self.couleur:
            # Vérification du format hexadécimal (#RRGGBB ou #RGB)
            if not re.match(r'^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$', self.couleur):
                raise ValidationError({
                    'couleur': "Le format de couleur doit être un code hexadécimal valide (ex: #FF5733)."
                })
        
        # Vérification de l'unicité du champ 'autre' pour les types personnalisés
        if self.nom == self.AUTRE and self.autre:
            # Vérifier si un autre objet avec le même 'autre' existe déjà
            # Exclure l'objet actuel si on est en train de le modifier
            queryset = TypeOffre.objects.filter(nom=self.AUTRE, autre=self.autre)
            if self.pk:
                queryset = queryset.exclude(pk=self.pk)
            
            if queryset.exists():
                raise ValidationError({
                    'autre': f"Un type d'offre personnalisé avec le nom '{self.autre}' existe déjà."
                })

    def save(self, *args, **kwargs):
        """
        Personnalisation de la sauvegarde:
        - Validation des données
        - Attribution automatique d'une couleur par défaut
        - Journalisation des actions
        
        Args:
            *args, **kwargs: Arguments à passer à la méthode save() de base
        """
        is_new = self.pk is None
        old_instance = None
        
        # Si modification, récupérer l'instance avant les changements
        if not is_new:
            try:
                old_instance = TypeOffre.objects.get(pk=self.pk)
            except TypeOffre.DoesNotExist:
                pass
        
        # Normalisation des données
        if self.autre:
            self.autre = self.autre.strip()
        self.couleur = self.couleur.lower() if self.couleur else '#6c757d'
        
        # Validation complète
        self.full_clean()
        
        # Attribution d'une couleur par défaut si nécessaire
        self.assign_default_color()
        
        # Utilisation d'une transaction pour garantir l'intégrité
        with transaction.atomic():
            # Sauvegarde
            super().save(*args, **kwargs)
            
            # Journalisation
            if is_new:
                logger.info(f"Création d'un nouveau type d'offre: {self}")
            elif old_instance:
                changes = []
                if old_instance.nom != self.nom:
                    changes.append(f"nom: {old_instance.get_nom_display()} → {self.get_nom_display()}")
                if old_instance.autre != self.autre:
                    changes.append(f"autre: {old_instance.autre} → {self.autre}")
                if old_instance.couleur != self.couleur:
                    changes.append(f"couleur: {old_instance.couleur} → {self.couleur}")
                
                if changes:
                    logger.info(f"Modification du type d'offre {self.pk}: {', '.join(changes)}")

    def assign_default_color(self):
        """
        Assigne une couleur par défaut selon le type d'offre si aucune 
        couleur personnalisée n'est définie.
        """
        # On affecte seulement si aucune couleur personnalisée ou si c'est la couleur grise par défaut
        if not self.couleur or self.couleur == "#6c757d":
            self.couleur = self.COULEURS_PAR_DEFAUT.get(self.nom, "#6c757d")
            logger.debug(f"Couleur par défaut assignée au type d'offre {self}: {self.couleur}")

    def __str__(self):
        """
        Représentation textuelle du modèle dans l'admin Django et les logs.
        
        Returns:
            str: Nom personnalisé si le type est "Autre", sinon le nom standard
        """
        if self.nom == self.AUTRE and self.autre:
            return self.autre
        return self.get_nom_display()
    
    def is_personnalise(self):
        """
        Vérifie si le type d'offre est personnalisé (Autre).
        
        Returns:
            bool: True si le type est "Autre", False sinon
        """
        return self.nom == self.AUTRE
    
    def get_badge_html(self):
        """
        Génère le HTML pour afficher un badge avec la couleur du type d'offre.
        
        Returns:
            str: Code HTML pour afficher un badge formaté
        """
        text_color = self.text_color()
        return f'<span class="badge" style="background-color:{self.couleur};color:{text_color};">{self}</span>'
    
    def text_color(self):
        """
        Détermine la couleur de texte adaptée (blanc ou noir) en fonction de la couleur de fond.
        
        Utilise une heuristique simple: les couleurs claires (jaune) ont un texte noir,
        les autres ont un texte blanc pour assurer la lisibilité.
        
        Returns:
            str: 'black' pour les fonds clairs, 'white' pour les fonds foncés
        """
        # Couleurs claires qui nécessitent un texte noir
        couleurs_claires = ['#ffff00', '#ffeb3b', '#fff176', '#fff59d', '#fffde7', '#ffffcc']
        
        if self.couleur.lower() in couleurs_claires:
            return 'black'
        
        # Heuristique avancée: calculer la luminosité de la couleur
        # Si la luminosité est élevée, utiliser du texte noir
        try:
            # Convertir le code hexadécimal en valeurs RGB
            hex_color = self.couleur.lstrip('#')
            if len(hex_color) == 3:
                # Convertir les formats courts (#RGB) en format long (#RRGGBB)
                hex_color = ''.join([c*2 for c in hex_color])
            
            r, g, b = [int(hex_color[i:i+2], 16) for i in (0, 2, 4)]
            
            # Calculer la luminosité (formule standard)
            luminance = (0.299 * r + 0.587 * g + 0.114 * b) / 255
            
            # Si la luminosité est supérieure à 0.5, la couleur est considérée comme claire
            if luminance > 0.5:
                return 'black'
        except Exception as e:
            # En cas d'erreur, revenir à la logique simple
            logger.warning(f"Erreur lors du calcul de la luminosité pour {self.couleur}: {str(e)}")
        
        # Par défaut, utiliser du texte blanc
        return 'white'
    
    def get_formations_count(self):
        """
        Retourne le nombre de formations associées à ce type d'offre.
        
        Returns:
            int: Nombre de formations utilisant ce type d'offre
        """
        return self.formations.count()

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
        ]
        # Ajout d'index pour optimiser les requêtes fréquentes
        indexes = [
            models.Index(fields=['nom']),
            models.Index(fields=['autre']),
        ]
    def get_badge_html(self):
        """
        Retourne un badge HTML avec la couleur associée au type d'offre.
        """
        color = self.couleur or "#6c757d"  # couleur par défaut si absente
        return f'<span class="badge" style="background-color: {color}; color: white;">{self.nom}</span>'
