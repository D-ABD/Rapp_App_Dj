from django import template
from django.utils.http import urlencode

register = template.Library()

@register.filter
def get_value(queryset, key):
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
    query_params = request_get.copy()
    query_params.pop(key, None)
    return '?' + urlencode(query_params)

# ✅ Manquait ce décorateur ici :
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
