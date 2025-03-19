from .base import BaseModel
from .centres import Centre
from .statut import Statut
from .types_offre import TypeOffre
from .formations import Formation, FormationManager
from .commentaires import Commentaire
from .evenements import Evenement
from .documents import Document
from .historique_formations import HistoriqueFormation
from .recherches import Recherche
from .partenaires import Partenaire
from .rapports import Rapport  # Ajoutez cette ligne

__all__ = [
    'BaseModel',
    'Centre',
    'Statut',
    'TypeOffre',
    'Formation',
    'FormationManager',
    'Commentaire',
    'Partenaire',
    'Evenement',
    'Document',
    'HistoriqueFormation',
    'Recherche',
    'Rapport',  # Ajoutez cette ligne
]