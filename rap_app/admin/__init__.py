"""
Importe les classes admin pour l'interface d'administration Django.
L'importation des classes admin enregistre automatiquement les modèles avec admin.site.
"""

from .centres_admin import CentreAdmin
from .statuts_admin import StatutAdmin
from .types_offre_admin import TypeOffreAdmin
from .formations_admin import FormationAdmin
from .commentaires_admin import CommentaireAdmin
from .recherches_admin import RechercheAdmin
from .partenaires_admin import PartenaireAdmin  # Nouveau
from .evenements_admin import EvenementAdmin    # Nouveau
from .documents_admin import DocumentAdmin      # Nouveau

