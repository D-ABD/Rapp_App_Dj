from django import template

register = template.Library()

@register.filter
def get_value(dictionary, key):
    """
    Récupère une valeur dans un dictionnaire à partir d'une clé.
    Exemple d'utilisation dans un template :
    {{ mon_dict|get_value:"ma_cle" }}
    """
    if isinstance(dictionary, dict):
        return dictionary.get(key, "Inconnu")  # Retourne "Inconnu" si la clé n'existe pas
    return "Invalide"
