from django.contrib import admin
from ..models.company import Company

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_name', 'contact_email', 'phone_number', 'city', 'sector_name', 'created_at')
    search_fields = ('name', 'contact_name', 'contact_email', 'phone_number', 'sector_name')
    list_filter = ('sector_name', 'city', 'created_at')
    ordering = ('-created_at',)
