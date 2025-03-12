from django.contrib import admin
from django.apps import apps

Partenaire = apps.get_model('rap_app', 'Partenaire')

@admin.register(Partenaire)
class PartenaireAdmin(admin.ModelAdmin):
    list_display = ('nom', 'secteur_activite', 'contact_nom', 'contact_poste', 
                    'contact_telephone', 'contact_email' )
    list_filter = ('secteur_activite',)  # Ajout de la virgule pour éviter une erreur de tuple
    search_fields = ('nom', 'contact_nom', 'contact_email', 'contact_telephone')
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('Informations générales', {
            'fields': ('nom', 'secteur_activite', 'description')
        }),
        ('Contact', {
            'fields': ('contact_nom', 'contact_poste', 'contact_telephone', 'contact_email')
        }),
        ('Métadonnées', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
