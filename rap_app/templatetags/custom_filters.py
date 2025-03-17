from django import template
from django.utils.http import urlencode

register = template.Library()

@register.filter
def get_value(queryset, key):
    """
    Récupère le nom d'un objet à partir de son ID dans un QuerySet.
    Utilisation dans un template :
    {{ centres|get_value:filters.centre }}
    """
    try:
        if not key:  # Vérifier si key est vide ou None
            return "Inconnu"
        
        key = int(key)  # Convertir en entier
        obj = queryset.filter(id=key).first()  # Utiliser filter().first() pour éviter DoesNotExist
        return obj.nom if obj else "Inconnu"  # Retourne le nom si l'objet est trouvé, sinon "Inconnu"
    
    except (ValueError, AttributeError):
        return "Inconnu"  # Retourne "Inconnu" si l'ID est invalide
@register.filter
def remove_filter(request_get, key):
    """
    Supprime un paramètre spécifique de la requête GET et renvoie l'URL mise à jour.
    Permet de retirer un filtre actif dans l'interface.
    
    Utilisation dans un template :
    <a href="?{{ request.GET|remove_filter:'q' }}">✖</a>
    """
    query_params = request_get.copy()  # Copie des paramètres actuels
    query_params.pop(key, None)  # Supprime le filtre sans erreur si absent

    return '?' + urlencode(query_params)  # Reconstruit l'URL