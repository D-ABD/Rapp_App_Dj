from django import template
from django.utils.http import urlencode

register = template.Library()

@register.filter
def get_value(queryset, key):
    """
    Retourne le nom de l'objet d'un queryset selon sa clé primaire.
    """
    try:
        if not key:
            return "Inconnu"
        key = int(key)
        obj = queryset.filter(id=key).first()
        return obj.nom if obj else "Inconnu"
    except (ValueError, AttributeError):
        return "Inconnu"

@register.filter
def remove_filter(request_get, key):
    """
    Supprime un paramètre de l'URL GET pour le bouton "réinitialiser un filtre".
    """
    query_params = request_get.copy()
    query_params.pop(key, None)
    return '?' + urlencode(query_params)

@register.filter
def get_statut_color(statuts, statut_id):
    """
    Retourne la couleur du statut à partir de son ID.
    Fonctionne avec une liste ou un dictionnaire de statuts.
    """
    try:
        statut_id = int(statut_id)
        if hasattr(statuts, "get"):
            statut = statuts.get(id=statut_id)
        else:
            statut = next((s for s in statuts if s.id == statut_id), None)
        return statut.couleur if statut and statut.couleur else "#000000"
    except (ValueError, AttributeError):
        return "#000000"

@register.filter
def get_type_offre_color(types_offre, type_offre_id):
    """
    Retourne la couleur du type d'offre à partir de son ID.
    Fonctionne avec une liste ou un dictionnaire de types d'offre.
    """
    try:
        type_offre_id = int(type_offre_id)
        if hasattr(types_offre, "get"):
            type_offre = types_offre.get(id=type_offre_id)
        else:
            type_offre = next((t for t in types_offre if t.id == type_offre_id), None)
        return type_offre.couleur if type_offre and type_offre.couleur else "#6c757d"
    except (ValueError, AttributeError):
        return "#6c757d"
