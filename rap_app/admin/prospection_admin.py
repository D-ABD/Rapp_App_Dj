from django.contrib import admin

from ..models import Prospection



@admin.register(Prospection)
class ProspectionAdmin(admin.ModelAdmin):
    list_display = ('company', 'formation', 'statut', 'objectif', 'date_prospection', 'responsable')
    list_filter = ('statut', 'objectif', 'date_prospection')
    search_fields = ('company__name', 'formation__nom', 'statut', 'objectif')
