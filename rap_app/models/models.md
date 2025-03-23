(Files content cropped to 300k characters, download full ingest to see more)
================================================
File: README.md
================================================
# Rapp_App_Dj


================================================
File: __init__.py
================================================



================================================
File: db.sqlite3
================================================
[Non-text file]


================================================
File: fichier
================================================



================================================
File: formation.js
================================================



================================================
File: manage.py
================================================
#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rap_app_project.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()



================================================
File: requirements.txt
================================================
asgiref==3.8.1
attrs==25.1.0
chardet==5.2.0
Django==4.2.7
django-cors-headers==4.7.0
django-filter==25.1
django-guardian==2.4.0
djangorestframework==3.14.0
drf-spectacular==0.28.0
et_xmlfile==2.0.0
inflection==0.5.1
jsonschema==4.23.0
jsonschema-specifications==2024.10.1
lxml==5.3.1
numpy==2.2.3
openpyxl==3.1.5
pandas==2.2.3
pillow==11.1.0
psycopg2-binary==2.9.10
python-dateutil==2.9.0.post0
python-docx==1.1.2
python-dotenv==1.0.1
pytz==2025.1
PyYAML==6.0.2
referencing==0.36.2
reportlab==4.3.1
rpds-py==0.23.1
six==1.17.0
sqlparse==0.5.3
typing_extensions==4.12.2
tzdata==2025.1
uritemplate==4.1.1



================================================
File: un
================================================



================================================
File: vide
================================================



================================================
File: .!63787!db.sqlite3
================================================



================================================
File: .!63801!db.sqlite3
================================================




================================================
File: rap_app/__init__.py
================================================



================================================
File: rap_app/apps.py
================================================
from django.apps import AppConfig


class RapAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'rap_app'



================================================
File: rap_app/urls.py
================================================
from django.urls import path

from .views.historique_formation_views import HistoriqueFormationDeleteView, HistoriqueFormationDetailView, HistoriqueFormationListView

from .views.prospection_views import HistoriqueProspectionDetailView, HistoriqueProspectionListView, ProspectionCreateView, ProspectionDeleteView, ProspectionDetailView, ProspectionHomeView, ProspectionListView, ProspectionUpdateView

from .views.company_views import CompanyCreateView, CompanyDeleteView, CompanyDetailView, CompanyListView, CompanyUpdateView

from .views.rapport_views import RapportCreationView, RapportDeleteView, RapportDetailView, RapportExportView, RapportListView


from .views.parametres_views import parametres


from .views.users_views import (UserDeleteView, UserDetailView, UserListView, UserUpdateView, 
user_login, register, user_logout, user_profile, change_password,reset_password, 
)

from .views import (
    home_views, DashboardView, centres_views, statuts_views, types_offre_views,
    commentaires_views, documents_views, partenaires_views, evenements_views, formations_views
)  # Import des vues

urlpatterns = [
    # Page d'accueil
    path('', home_views.home, name='home'),

    # Rapports
    # Liste des rapports
    path('rapports/', RapportListView.as_view(), name='rapport-list'),
    path('rapports/creer/', RapportCreationView.as_view(), name='rapport-create'),
    path('rapports/<int:pk>/', RapportDetailView.as_view(), name='rapport-detail'),
    path('rapports/<int:pk>/supprimer/', RapportDeleteView.as_view(), name='rapport-delete'),
    path('rapports/<int:pk>/export/', RapportExportView.as_view(), name='rapport-export'),

    # USERS
    path("register/", register, name="register"),
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
    path("profile/", user_profile, name="user-profile"),
    path("password_change/", change_password, name="password_change"),
    path("password_reset/", reset_password, name="password_reset"),
    
    path("users/", UserListView.as_view(), name="user-list"),
    path("users/<int:pk>/", UserDetailView.as_view(), name="user-detail"),
    path("users/<int:pk>/update/", UserUpdateView.as_view(), name="user-update"),
    path("users/<int:pk>/delete/", UserDeleteView.as_view(), name="user-delete"),


    # Dashboard
    path('dashboard/', DashboardView.as_view(), name='dashboard'),


    # Centres de formation
    path('centres/', centres_views.CentreListView.as_view(), name='centre-list'),
    path('centres/<int:pk>/', centres_views.CentreDetailView.as_view(), name='centre-detail'),
    path('centres/ajouter/', centres_views.CentreCreateView.as_view(), name='centre-create'),
    path('centres/<int:pk>/modifier/', centres_views.CentreUpdateView.as_view(), name='centre-update'),
    path('centres/<int:pk>/supprimer/', centres_views.CentreDeleteView.as_view(), name='centre-delete'),

    # Statuts des formations
    path('statuts/', statuts_views.StatutListView.as_view(), name='statut-list'),
    path('statuts/<int:pk>/', statuts_views.StatutDetailView.as_view(), name='statut-detail'),
    path('statuts/ajouter/', statuts_views.StatutCreateView.as_view(), name='statut-create'),
    path('statuts/<int:pk>/modifier/', statuts_views.StatutUpdateView.as_view(), name='statut-update'),
    path('statuts/<int:pk>/supprimer/', statuts_views.StatutDeleteView.as_view(), name='statut-delete'),

    # Types d'offres
    path('types-offres/', types_offre_views.TypeOffreListView.as_view(), name='type-offre-list'),
    path('types-offres/<int:pk>/', types_offre_views.TypeOffreDetailView.as_view(), name='type-offre-detail'),
    path('types-offres/ajouter/', types_offre_views.TypeOffreCreateView.as_view(), name='type-offre-create'),
    path('types-offres/<int:pk>/modifier/', types_offre_views.TypeOffreUpdateView.as_view(), name='type-offre-update'),
    path('types-offres/<int:pk>/supprimer/', types_offre_views.TypeOffreDeleteView.as_view(), name='type-offre-delete'),

    # Commentaires
    path('commentaires/', commentaires_views.CommentaireListView.as_view(), name='commentaire-list'),
    path('commentaires/<int:pk>/', commentaires_views.CommentaireDetailView.as_view(), name='commentaire-detail'),
    path('commentaires/ajouter/', commentaires_views.CommentaireCreateView.as_view(), name='commentaire-create'),
    path('commentaires/<int:pk>/modifier/', commentaires_views.CommentaireUpdateView.as_view(), name='commentaire-update'),
    path('commentaires/<int:pk>/supprimer/', commentaires_views.CommentaireDeleteView.as_view(), name='commentaire-delete'),
    path('commentaires_all/', commentaires_views.AllCommentairesView.as_view(), name='all-commentaires'),
    path('export-commentaires/', commentaires_views.ExportCommentairesView.as_view(), name='export-commentaires'),

    # Documents
    path('documents/', documents_views.DocumentListView.as_view(), name='document-list'),
    path('documents/<int:pk>/', documents_views.DocumentDetailView.as_view(), name='document-detail'),
    path('documents/ajouter/', documents_views.DocumentCreateView.as_view(), name='document-create'),
    path('documents/ajouter/<int:formation_id>/', documents_views.DocumentCreateView.as_view(), name='document-create-formation'),
    path('documents/<int:pk>/modifier/', documents_views.DocumentUpdateView.as_view(), name='document-update'),
    path('documents/<int:pk>/supprimer/', documents_views.DocumentDeleteView.as_view(), name='document-delete'),
    
    # Partenaires
    path('partenaires/', partenaires_views.PartenaireListView.as_view(), name='partenaire-list'),
    path('partenaires/<int:pk>/', partenaires_views.PartenaireDetailView.as_view(), name='partenaire-detail'),
    path('partenaires/ajouter/', partenaires_views.PartenaireCreateView.as_view(), name='partenaire-create'),
    path('partenaires/<int:pk>/modifier/', partenaires_views.PartenaireUpdateView.as_view(), name='partenaire-update'),
    path('partenaires/<int:pk>/supprimer/', partenaires_views.PartenaireDeleteView.as_view(), name='partenaire-delete'),
    path('partenaires/ajouter/formation/<int:formation_id>/', partenaires_views.PartenaireCreateViewFormation.as_view(), name='partenaire-add-formation'),

    # Événements
    path('evenements/', evenements_views.EvenementListView.as_view(), name='evenement-list'),
    path('evenements/<int:pk>/', evenements_views.EvenementDetailView.as_view(), name='evenement-detail'),
    path('evenements/ajouter/', evenements_views.EvenementCreateView.as_view(), name='evenement-create'),
    path('evenements/<int:pk>/modifier/', evenements_views.EvenementUpdateView.as_view(), name='evenement-update'),
    path('evenements/<int:pk>/supprimer/', evenements_views.EvenementDeleteView.as_view(), name='evenement-delete'),
    
    # Formations
    path('formations/', formations_views.FormationListView.as_view(), name='formation-list'),
    path('formations/modifier-inscrits/<int:formation_id>/', formations_views.ModifierInscritsView.as_view(), name='modifier-inscrits'),
    path('formations/<int:pk>/', formations_views.FormationDetailView.as_view(), name='formation-detail'),
    path('formations/ajouter/', formations_views.FormationCreateView.as_view(), name='formation-create'),
    path('formations/<int:pk>/modifier/', formations_views.FormationUpdateView.as_view(), name='formation-update'),
    path('formations/<int:pk>/supprimer/', formations_views.FormationDeleteView.as_view(), name='formation-delete'),
    path('formations/<int:pk>/commentaire/', formations_views.FormationAddCommentView.as_view(), name='formation-add-comment'),
    path("formations/export-excel/", formations_views.ExportFormationsExcelView.as_view(), name="export-formations-excel"),
    
        # Historique des Formations
    path('historique-formations/', HistoriqueFormationListView.as_view(), name='historique-formation-list'),
    path('historique-formations/<int:pk>/', HistoriqueFormationDetailView.as_view(), name='historique-formation-detail'),
    path("historique-formations/<int:pk>/delete/", HistoriqueFormationDeleteView.as_view(), name="historique-formation-delete"),

    # Company
    path('companies/', CompanyListView.as_view(), name='company-list'),
    path('companies/<int:pk>/', CompanyDetailView.as_view(), name='company-detail'),
    path('companies/add/', CompanyCreateView.as_view(), name='company-create'),
    path('companies/<int:pk>/edit/', CompanyUpdateView.as_view(), name='company-update'),
    path('companies/<int:pk>/delete/', CompanyDeleteView.as_view(), name='company-delete'),

    # Paramètres
    path('parametres/', parametres, name='parametres'),

    # Prospections
    path('prospection_home', ProspectionHomeView, name='prospection-home'),
    path('prospections/', ProspectionListView.as_view(), name='prospection-list'),
    path('prospections/<int:pk>/', ProspectionDetailView.as_view(), name='prospection-detail'),
    path('prospections/add/', ProspectionCreateView.as_view(), name='prospection-add'),
    path('prospections/<int:pk>/edit/', ProspectionUpdateView.as_view(), name='prospection-update'),
    path('prospections/<int:pk>/delete/', ProspectionDeleteView.as_view(), name='prospection-delete'),
    path('historique-prospections/', HistoriqueProspectionListView.as_view(), name='historique-prospection-list'),
    path('historique-prospections/<int:pk>/', HistoriqueProspectionDetailView.as_view(), name='historique-prospection-detail'),
]


================================================
File: rap_app/.DS_Store
================================================
[Non-text file]



================================================
File: rap_app/admin/__init__.py
================================================
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
from .prospection_admin import ProspectionAdmin



================================================
File: rap_app/admin/centres_admin.py
================================================
from django.contrib import admin
from ..models import Centre


@admin.register(Centre)
class CentreAdmin(admin.ModelAdmin):
    list_display = ('nom', 'code_postal', 'created_at', 'updated_at')
    list_filter = ('code_postal',)
    search_fields = ('nom', 'code_postal')
    ordering = ('nom',)
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Informations', {
            'fields': ('nom', 'code_postal')
        }),
        ('Métadonnées', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


================================================
File: rap_app/admin/commentaires_admin.py
================================================
from django.contrib import admin
from django.contrib.auth import get_user_model
from ..models.commentaires import Commentaire


Utilisateur = get_user_model()

@admin.register(Commentaire)
class CommentaireAdmin(admin.ModelAdmin):
    """
    Interface d'administration pour la gestion des commentaires liés aux formations.
    """

    # Affichage des principales informations
    list_display = ("formation", "utilisateur", "contenu", "saturation", "created_at")

    # Ajout de filtres pour faciliter la recherche
    list_filter = ("formation", "utilisateur", "saturation", "created_at")

    # Recherche rapide sur certains champs
    search_fields = ("formation__nom", "utilisateur__username", "contenu")

    # Rendre certains champs en lecture seule
    readonly_fields = ("utilisateur", "created_at")

    # Organisation des champs
    fieldsets = (
        ("Informations générales", {
            "fields": ("formation", "utilisateur")
        }),
        ("Contenu du commentaire", {
            "fields": ("contenu",)
        }),
        ("Données complémentaires", {
            "fields": ("saturation",),
        }),
        ("Métadonnées", {
            "fields": ("created_at",),
            "classes": ("collapse",)
        }),
    )

    ordering = ("-created_at",)
    list_per_page = 20

    def save_model(self, request, obj, form, change):
        """
        Assigne l'utilisateur connecté à l'ajout d'un commentaire.
        """
        if not obj.utilisateur:
            # Vérifie que request.user est bien du bon type
            if isinstance(request.user, Utilisateur):
                obj.utilisateur = request.user
            else:
                obj.utilisateur = Utilisateur.objects.get(pk=request.user.pk)  # Convertit en `Utilisateur`
        
        obj.save()


================================================
File: rap_app/admin/company_admin.py
================================================
from django.contrib import admin
from ..models.company import Company

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_name', 'contact_email', 'phone_number', 'city', 'sector_name', 'created_at')
    search_fields = ('name', 'contact_name', 'contact_email', 'phone_number', 'sector_name')
    list_filter = ('sector_name', 'city', 'created_at')
    ordering = ('-created_at',)



================================================
File: rap_app/admin/documents_admin.py
================================================
from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from ..models import Document, Formation


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    """
    Interface d'administration pour la gestion des documents associés aux formations.
    """
    
    # Affichage des principales informations
    list_display = ('nom_fichier', 'formation_link', 'type_document', 'taille_fichier', 'file_link', 'created_at')
    
    # Ajout de filtres pour faciliter la navigation
    list_filter = ('type_document', 'formation__centre', 'created_at')
    
    # Recherche rapide sur certains champs
    search_fields = ('nom_fichier', 'formation__nom', 'source')

    # Rendre certains champs en lecture seule pour éviter toute modification accidentelle
    readonly_fields = ('created_at', 'updated_at', 'taille_fichier', 'file_link', 'image_preview', 'formation_link')

    # Organisation des champs dans l'interface d'administration
    fieldsets = (
        ('Informations générales', {
            'fields': ('formation', 'formation_link', 'nom_fichier', 'type_document', 'taille_fichier')
        }),
        ('Fichier', {
            'fields': ('fichier', 'file_link', 'source', 'image_preview'),
        }),
        ('Métadonnées', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)  # Masquer cette section par défaut
        }),
    )

    ### ✅ **Ajouts de méthodes utiles**
    
    def formation_link(self, obj):
        """
        Affiche un lien vers la formation associée dans l'interface d'administration.
        """
        if obj.formation:
            url = reverse('admin:rap_app_formation_change', args=[obj.formation.id])
            return format_html('<a href="{}">{}</a>', url, obj.formation.nom)
        return "Aucune formation"
    
    formation_link.short_description = 'Formation'
    formation_link.admin_order_field = 'formation__nom'

    
    def file_link(self, obj):
        """
        Ajoute un lien pour télécharger le fichier directement depuis l'admin Django.
        """
        if obj.fichier:
            return format_html('<a href="{}" target="_blank">Télécharger</a>', obj.fichier.url)
        return "-"
    
    file_link.short_description = "Téléchargement"

    
    def image_preview(self, obj):
        """
        Affiche un aperçu de l'image si le document est de type `image`.
        """
        if obj.type_document == Document.IMAGE and obj.fichier:
            return format_html('<img src="{}" width="150" style="border:1px solid #ddd; padding:5px;"/>', obj.fichier.url)
        return "Aperçu non disponible"
    
    image_preview.short_description = "Aperçu"

    
    def taille_fichier(self, obj):
        """
        Affiche la taille du fichier en Ko pour plus d'informations.
        """
        if obj.taille_fichier:
            return f"{obj.taille_fichier:.2f} Ko"
        return "-"

    
    # Ajout de fonctionnalités supplémentaires à l'admin
    ordering = ("-created_at", "nom_fichier")  # Trie les documents par date de création descendante
    list_per_page = 20  # Nombre de documents affichés par page



================================================
File: rap_app/admin/evenements_admin.py
================================================
from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from ..models import Evenement


@admin.register(Evenement)
class EvenementAdmin(admin.ModelAdmin):
    list_display = ('type_evenement_display', 'event_date', 'formation_link', 
                   'details_preview', 'created_at', 'event_date')
    list_filter = ('type_evenement', 'event_date', 'formation__centre')
    search_fields = ('formation__nom', 'details', 'description_autre')
    readonly_fields = ('created_at', 'updated_at')
    date_hierarchy = 'event_date'
    
    fieldsets = (
        ('Informations générales', {
            'fields': ('formation', 'type_evenement', 'description_autre', 'event_date')
        }),
        ('Détails', {
            'fields': ('details',)
        }),
        ('Métadonnées', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def formation_link(self, obj):
        if obj.formation and obj.formation.id:
            url = reverse('admin:rap_app_formation_change', args=[obj.formation.id])
            return format_html('<a href="{}">{}</a>', url, obj.formation)
        return "Aucune formation"


    def type_evenement_display(self, obj):
        if obj.type_evenement == Evenement.AUTRE and obj.description_autre:
            return obj.description_autre
        return obj.get_type_evenement_display()
    type_evenement_display.short_description = "Type d'événement"
    type_evenement_display.admin_order_field = 'type_evenement'

    def details_preview(self, obj):
        if obj.details:
            # Tronquer les détails s'ils sont trop longs
            preview = obj.details[:50] + ('...' if len(obj.details) > 50 else '')
            return preview
        return "-"
    details_preview.short_description = 'Détails'


================================================
File: rap_app/admin/formations_admin.py
================================================
from django.contrib import admin
from django.utils.html import format_html
from django.db.models import F, Sum

from ..models.formations import Formation

@admin.register(Formation)
class FormationAdmin(admin.ModelAdmin):
    """
    Administration du modèle Formation avec fonctionnalités avancées
    """
    # Champs affichés dans la liste des formations
    list_display = (
        'nom', 
        'centre', 
        'type_offre', 
        'statut', 
        'start_date', 
        'end_date', 
        'places_dispo_display', 
        'taux_saturation_display'
    )
    
    # Filtres dans la barre latérale
    list_filter = (
        'centre', 
        'statut', 
        'type_offre', 
        'start_date', 
        'end_date', 
        'convocation_envoie'
    )
    
    # Champs de recherche
    search_fields = (
        'nom', 
        'num_kairos', 
        'num_offre', 
        'num_produit', 
        'assistante'
    )
    
    # Actions personnalisées
    actions = [
        'marquer_convocation_envoyee', 
        'reset_convocation_envoyee'
    ]
    
    # Champs pour édition rapide depuis la liste
    list_editable = (
        'statut',
    )
    
    # Champs cliquables dans la liste
    list_display_links = (
        'nom',
    )
    
    # Pagination pour la liste des formations
    list_per_page = 20
    
    # Filtres date dans le panneau latéral
    date_hierarchy = 'start_date'
    
    # Groupes de champs dans le formulaire d'édition
    fieldsets = (
        ('Informations générales', {
            'fields': (
                'nom', 
                'centre', 
                'type_offre', 
                'statut',
                'utilisateur'
            )
        }),
        ('Dates et identifiants', {
            'fields': (
                'start_date', 
                'end_date', 
                'num_kairos', 
                'num_offre', 
                'num_produit'
            )
        }),
        ('Gestion des places', {
            'fields': (
                ('prevus_crif', 'inscrits_crif'),
                ('prevus_mp', 'inscrits_mp'),
                'cap',
                'entresformation'
            )
        }),
        ('Recrutement', {
            'fields': (
                'nombre_candidats', 
                'nombre_entretiens', 
                'convocation_envoie'
            )
        }),
        ('Informations supplémentaires', {
            'fields': (
                'assistante', 
                'nombre_evenements',
                'dernier_commentaire',
                'partenaires'
            ),
            'classes': ('collapse',)  # Cette section est rétractable
        })
    )
    
    # Sauvegarde automatique des ManyToMany relations
    save_on_top = True
    
    # Relations many-to-many dans un widget filtrable
    filter_horizontal = ('partenaires',)
    
    # Méthodes pour les champs personnalisés dans l'affichage en liste
    
    def places_dispo_display(self, obj):
        """Affiche le nombre de places disponibles avec formatage"""
        places = obj.get_places_disponibles()
        color = 'green' if places > 5 else 'orange' if places > 0 else 'red'
        return format_html('<span style="color: {};">{}</span>', color, places)
    places_dispo_display.short_description = "Places disponibles"
    places_dispo_display.admin_order_field = 'places_disponibles'
    
    def taux_saturation_display(self, obj):
        """Affiche le taux de saturation avec une barre de progression"""
        taux = obj.get_taux_saturation()
        color = 'green' if taux < 70 else 'orange' if taux < 95 else 'red'
        return format_html(
            '<div style="width:100px; border:1px solid #ccc;">'
            '<div style="width:{}px; height:10px; background-color:{};">&nbsp;</div>'
            '</div> {}%',
            min(int(taux), 100), color, round(taux, 1)
        )
    taux_saturation_display.short_description = "Taux de saturation"
    taux_saturation_display.admin_order_field = 'taux_saturation'
    
    # Actions personnalisées
    
    def marquer_convocation_envoyee(self, request, queryset):
        """Marque les convocations comme envoyées pour les formations sélectionnées"""
        updated = queryset.update(convocation_envoie=True)
        self.message_user(request, f"{updated} formations marquées avec convocations envoyées.")
    marquer_convocation_envoyee.short_description = "Marquer les convocations comme envoyées"
    
    def reset_convocation_envoyee(self, request, queryset):
        """Réinitialise le statut d'envoi des convocations"""
        updated = queryset.update(convocation_envoie=False)
        self.message_user(request, f"Statut d'envoi des convocations réinitialisé pour {updated} formations.")
    reset_convocation_envoyee.short_description = "Réinitialiser statut d'envoi des convocations"
    
    # Surcharge pour ajouter des annotations
    def get_queryset(self, request):
        """Surcharge pour ajouter des calculs agrégés à la requête"""
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(
            places_disponibles=F('prevus_crif') + F('prevus_mp') - F('inscrits_crif') - F('inscrits_mp'),
            taux_saturation=100 * (F('inscrits_crif') + F('inscrits_mp')) / 
                           (F('prevus_crif') + F('prevus_mp'))
        )
        return queryset

    # Statistiques personnalisées
    def changelist_view(self, request, extra_context=None):
        """Ajout de statistiques en haut de la liste des formations"""
        response = super().changelist_view(request, extra_context)
        
        # Uniquement si nous ne faisons pas face à une erreur 404
        if hasattr(response, 'context_data'):
            queryset = self.get_queryset(request)
            
            # Calculer les statistiques globales
            stats = queryset.aggregate(
                total_formations=Sum('id', distinct=True),
                total_places=Sum(F('prevus_crif') + F('prevus_mp')),
                total_inscrits=Sum(F('inscrits_crif') + F('inscrits_mp')),
            )
            
            # Ajouter les statistiques au contexte
            if not extra_context:
                extra_context = {}
            
            # Vérifier que les valeurs ne sont pas None avant de calculer
            if stats['total_places'] and stats['total_inscrits']:
                taux_remplissage = (stats['total_inscrits'] / stats['total_places']) * 100
                extra_context['taux_remplissage_global'] = round(taux_remplissage, 1)
            else:
                extra_context['taux_remplissage_global'] = 0
                
            extra_context.update(stats)
            response.context_data.update(extra_context)
            
        return response
    
    # Esthétique et optimisation des chargements
    
    class Media:
        """Ressources CSS et JS pour l'interface d'admin"""
        css = {
            'all': ('css/admin/formation_admin.css',)
        }
        js = ('js/admin/formation_admin.js',)


================================================
File: rap_app/admin/partenaires_admin.py
================================================
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



================================================
File: rap_app/admin/prospection_admin.py
================================================
from django.contrib import admin

from ..models import Prospection



@admin.register(Prospection)
class ProspectionAdmin(admin.ModelAdmin):
    list_display = ('company', 'formation', 'statut', 'objectif', 'date_prospection', 'responsable')
    list_filter = ('statut', 'objectif', 'date_prospection')
    search_fields = ('company__name', 'formation__nom', 'statut', 'objectif')



================================================
File: rap_app/admin/recherches_admin.py
================================================
from django.contrib import admin
from ..models.recherches import Recherche


@admin.register(Recherche)
class RechercheAdmin(admin.ModelAdmin):
    """
    Interface d'administration pour la gestion des recherches effectuées par les utilisateurs.
    """

    # ✅ Affichage des principales informations dans la liste
    list_display = (
        "terme_recherche", "filtre_centre", "filtre_type_offre", 
        "filtre_statut", "date_debut", "date_fin", 
        "nombre_resultats", "temps_execution", "created_at"
    )

    # ✅ Ajout de filtres pour affiner les recherches dans l'admin
    list_filter = (
        "filtre_centre", "filtre_type_offre", "filtre_statut", 
        "date_debut", "date_fin", "created_at"
    )

    # ✅ Recherche rapide sur certains champs
    search_fields = ("terme_recherche", "filtre_centre__nom", "filtre_type_offre__nom", "filtre_statut__nom")

    # ✅ Champs en lecture seule pour éviter des modifications involontaires
    readonly_fields = ("nombre_resultats", "temps_execution", "created_at", "updated_at")

    # ✅ Organisation des champs dans l'interface d'administration
    fieldsets = (
        ("Détails de la recherche", {
            "fields": ("terme_recherche",)
        }),
        ("Filtres appliqués", {
            "fields": ("filtre_centre", "filtre_type_offre", "filtre_statut", "date_debut", "date_fin")
        }),
        ("Informations sur les résultats", {
            "fields": ("nombre_resultats", "temps_execution"),
            "classes": ("collapse",)  # Permet de masquer cette section par défaut
        }),
        ("Métadonnées", {
            "fields": ("created_at", "updated_at"),
            "classes": ("collapse",)
        }),
    )

    # ✅ Configuration de l'affichage dans l'admin
    ordering = ("-created_at",)  # Trie les recherches du plus récent au plus ancien
    list_per_page = 25  # Nombre de recherches affichées par page


    def a_trouve_resultats_display(self, obj):
        """
        Affiche un ✅ si la recherche a trouvé des résultats, sinon ❌.
        """
        return "✅ Oui" if obj.a_trouve_resultats else "❌ Non"
    a_trouve_resultats_display.short_description = "Résultats trouvés"




================================================
File: rap_app/admin/statuts_admin.py
================================================
from django.contrib import admin
from django.utils.html import format_html
from ..models import Statut


@admin.register(Statut)
class StatutAdmin(admin.ModelAdmin):
    list_display = ('get_nom_display', 'couleur_display', 'description_autre', 'created_at')
    list_filter = ('nom',)
    search_fields = ('nom', 'description_autre')
    readonly_fields = ('created_at', 'updated_at', 'couleur_display')
    fieldsets = (
        ('Informations', {
            'fields': ('nom', 'couleur', 'couleur_display', 'description_autre')
        }),
        ('Métadonnées', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def get_nom_display(self, obj):
        return obj.get_nom_display()
    get_nom_display.short_description = 'Statut'
    get_nom_display.admin_order_field = 'nom'
    
    def couleur_display(self, obj):
        """Affiche un échantillon visuel de la couleur."""
        if obj.couleur:
            return format_html(
                '<div style="display:inline-block; width:100px; height:25px; background-color:{}; '
                'border:1px solid #ddd; border-radius:3px;"></div>', 
                obj.couleur
            )
        return "-"
    couleur_display.short_description = 'Aperçu de la couleur'


================================================
File: rap_app/admin/types_offre_admin.py
================================================
from django.contrib import admin
from ..models import TypeOffre


@admin.register(TypeOffre)
class TypeOffreAdmin(admin.ModelAdmin):
    list_display = ('get_nom_display', 'autre', 'created_at')
    list_filter = ('nom',)
    search_fields = ('nom', 'autre')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Informations', {
            'fields': ('nom', 'autre')
        }),
        ('Métadonnées', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def get_nom_display(self, obj):
        return obj.get_nom_display()
    get_nom_display.short_description = "Type d'offre"
    get_nom_display.admin_order_field = 'nom'


================================================
File: rap_app/admin/utilisateurs_admin.py
================================================
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from ..models import Utilisateur


@admin.register(Utilisateur)
class UtilisateurAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'role', 'is_staff')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Informations personnelles', {'fields': ('first_name', 'last_name', 'email', 'role')}),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        ('Dates importantes', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'role'),
        }),
    )
    search_fields = ('username', 'email', 'first_name', 'last_name', 'role')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    ordering = ('username',)



================================================
File: rap_app/forms/ProspectionForm.py
================================================
from django import forms
from ..models.prospection import Prospection

class ProspectionForm(forms.ModelForm):
    class Meta:
        model = Prospection
        fields = ['company', 'formation', 'statut', 'objectif', 'commentaire', 'responsable']
        widgets = {
            'commentaire': forms.Textarea(attrs={'rows': 3}),
        }



================================================
File: rap_app/forms/__init__.py
================================================
from rap_app.forms import ProspectionForm



================================================
File: rap_app/forms/company_form.py
================================================
from django import forms
from ..models.company import Company

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = [
            'name', 'street_name', 'zip_code', 'city', 'country',
            'contact_name', 'contact_email', 'contact_phone_number', 'contact_job',
            'sector_name', 'actions', 'action_description',
            'website', 'social_network_url'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_name': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'contact_phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'sector_name': forms.TextInput(attrs={'class': 'form-control'}),
        }



================================================
File: rap_app/forms/rapports_forms.py
================================================
from django import forms
from django.utils import timezone
from datetime import timedelta

from ..models.rapports import Rapport
from ..models import Centre, TypeOffre, Statut

class RapportCreationForm(forms.Form):
    """Formulaire pour créer un nouveau rapport."""
    
    type_rapport = forms.ChoiceField(
        choices=Rapport.TYPE_CHOICES,
        label="Type de rapport",
        widget=forms.Select(attrs={'class': 'form-select'}),
        help_text="Sélectionnez le type de rapport à générer."
    )
    
    periode = forms.ChoiceField(
        choices=[("", "Aucune période sélectionnée")] + Rapport.PERIODE_CHOICES,
        label="Périodicité (optionnelle)",
        required=False,
        widget=forms.Select(attrs={'class': 'form-select'}),
        initial=Rapport.PERIODE_MENSUEL,
        help_text="Choisissez la période du rapport (optionnel)."
    )
    
    date_debut = forms.DateField(
        label="Date de début",
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        help_text="La date de début de la période du rapport."
    )
    
    date_fin = forms.DateField(
        label="Date de fin",
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        help_text="La date de fin de la période du rapport."
    )
    
    centre = forms.ModelChoiceField(
        queryset=Centre.objects.none(),
        label="Centre (optionnel)",
        required=False,
        widget=forms.Select(attrs={'class': 'form-select'}),
        help_text="Filtrer par centre (optionnel)."
    )

    type_offre = forms.ModelChoiceField(
        queryset=TypeOffre.objects.none(),
        label="Type d'offre (optionnel)",
        required=False,
        widget=forms.Select(attrs={'class': 'form-select'}),
        help_text="Filtrer par type d'offre (optionnel)."
    )
    
    statut = forms.ModelChoiceField(
        queryset=Statut.objects.none(),
        label="Statut (optionnel)",
        required=False,
        widget=forms.Select(attrs={'class': 'form-select'}),
        help_text="Filtrer par statut (optionnel)."
    )
    
    format = forms.ChoiceField(
        choices=Rapport.FORMAT_CHOICES,
        label="Format d'export",
        initial=Rapport.FORMAT_HTML,
        widget=forms.Select(attrs={'class': 'form-select'}),
        help_text="Choisissez le format d'export du rapport."
    )

    description = forms.CharField(
        label="Description (optionnelle)",
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        required=False,
        help_text="Ajoutez une description pour ce rapport (optionnel)."
    )

    def __init__(self, *args, **kwargs):
        """Initialisation dynamique des choix de centres, types d'offres et statuts."""
        super().__init__(*args, **kwargs)

        # Récupérer les données dynamiquement
        self.fields['centre'].queryset = Centre.objects.all().order_by('nom')
        self.fields['type_offre'].queryset = TypeOffre.objects.all().order_by('nom')
        self.fields['statut'].queryset = Statut.objects.all().order_by('nom')

        # Initialisation des dates
        self.fields['date_debut'].initial = timezone.now().date() - timedelta(days=30)
        self.fields['date_fin'].initial = timezone.now().date()

    def clean(self):
        """Validation des dates et autres champs."""
        cleaned_data = super().clean()
        date_debut = cleaned_data.get('date_debut')
        date_fin = cleaned_data.get('date_fin')

        # Vérifier que la date de début est bien avant la date de fin
        if date_debut and date_fin:
            if date_debut > date_fin:
                self.add_error('date_debut', "⚠ La date de début doit être antérieure à la date de fin.")
                self.add_error('date_fin', "⚠ La date de fin doit être postérieure à la date de début.")

            if date_fin > timezone.now().date():
                self.add_error('date_fin', "⚠ La date de fin ne peut pas être dans le futur.")

        return cleaned_data




================================================
File: rap_app/migrations/0001_initial.py
================================================
# Generated by Django 4.2.7 on 2025-03-11 20:00

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Centre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Date de création')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Dernière mise à jour')),
                ('nom', models.CharField(max_length=255, unique=True, verbose_name='Nom du centre')),
                ('code_postal', models.CharField(blank=True, max_length=5, null=True, validators=[django.core.validators.RegexValidator(message='Le code postal doit contenir exactement 5 chiffres', regex='^\\d{5}$')], verbose_name='Code postal')),
            ],
            options={
                'verbose_name': 'Centre',
                'verbose_name_plural': 'Centres',
                'ordering': ['nom'],
            },
        ),
        migrations.CreateModel(
            name='Commentaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Date de création')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Dernière mise à jour')),
                ('contenu', models.TextField(verbose_name='Contenu du commentaire')),
                ('saturation', models.PositiveIntegerField(blank=True, null=True, verbose_name='Niveau de saturation (%)')),
            ],
            options={
                'verbose_name': 'Commentaire',
                'verbose_name_plural': 'Commentaires',
                'ordering': ['formation', '-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Date de création')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Dernière mise à jour')),
                ('nom_fichier', models.CharField(db_index=True, max_length=255, verbose_name='Nom du fichier')),
                ('fichier', models.FileField(upload_to='formations/documents/', verbose_name='Fichier')),
                ('source', models.TextField(blank=True, null=True, verbose_name='Source du document')),
                ('type_document', models.CharField(choices=[('pdf', 'PDF'), ('image', 'Image'), ('contrat', 'Contrat signé'), ('autre', 'Autre')], default='autre', max_length=20, verbose_name='Type de document')),
                ('taille_fichier', models.PositiveIntegerField(blank=True, null=True, verbose_name='Taille du fichier (Ko)')),
            ],
            options={
                'verbose_name': 'Document',
                'verbose_name_plural': 'Documents',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Evenement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Date de création')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Dernière mise à jour')),
                ('type_evenement', models.CharField(choices=[('info_collective_presentiel', 'Information collective présentiel'), ('info_collective_distanciel', 'Information collective distanciel'), ('job_dating', 'Job dating'), ('evenement_emploi', 'Événement emploi'), ('forum', 'Forum'), ('jpo', 'Journée Portes Ouvertes (JPO)'), ('autre', 'Autre')], db_index=True, max_length=100, verbose_name="Type d'événement")),
                ('details', models.TextField(blank=True, null=True, verbose_name="Détails de l'événement")),
                ('event_date', models.DateField(blank=True, null=True, verbose_name="Date de l'événement")),
                ('description_autre', models.CharField(blank=True, max_length=255, null=True, verbose_name="Description pour 'Autre' événement")),
            ],
            options={
                'verbose_name': 'Événement',
                'verbose_name_plural': 'Événements',
                'ordering': ['-event_date'],
            },
        ),
        migrations.CreateModel(
            name='Formation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Date de création')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Dernière mise à jour')),
                ('nom', models.CharField(max_length=255, verbose_name='Nom de la formation')),
                ('start_date', models.DateField(blank=True, null=True, verbose_name='Date de début')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='Date de fin')),
                ('num_kairos', models.CharField(blank=True, max_length=50, null=True, verbose_name='Numéro Kairos')),
                ('num_offre', models.CharField(blank=True, max_length=50, null=True, verbose_name="Numéro de l'offre")),
                ('num_produit', models.CharField(blank=True, max_length=50, null=True, verbose_name='Numéro du produit')),
                ('prevus_crif', models.PositiveIntegerField(default=0, verbose_name='Places prévues CRIF')),
                ('prevus_mp', models.PositiveIntegerField(default=0, verbose_name='Places prévues MP')),
                ('inscrits_crif', models.PositiveIntegerField(default=0, verbose_name='Inscrits CRIF')),
                ('inscrits_mp', models.PositiveIntegerField(default=0, verbose_name='Inscrits MP')),
                ('assistante', models.CharField(blank=True, max_length=255, null=True, verbose_name='Assistante')),
                ('cap', models.PositiveIntegerField(blank=True, null=True, verbose_name='Capacité maximale')),
                ('convocation_envoie', models.BooleanField(default=False, verbose_name='Convocation envoyée')),
                ('entresformation', models.PositiveIntegerField(default=0, verbose_name='Entrées en formation')),
                ('nombre_candidats', models.PositiveIntegerField(default=0, verbose_name='Nombre de candidats')),
                ('nombre_entretiens', models.PositiveIntegerField(default=0, verbose_name="Nombre d'entretiens")),
                ('nombre_evenements', models.PositiveIntegerField(default=0, verbose_name="Nombre d'événements")),
                ('dernier_commentaire', models.TextField(blank=True, null=True, verbose_name='Dernier commentaire')),
            ],
            options={
                'verbose_name': 'Formation',
                'verbose_name_plural': 'Formations',
                'ordering': ['-start_date', 'nom'],
            },
        ),
        migrations.CreateModel(
            name='HistoriqueFormation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Date de création')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Dernière mise à jour')),
                ('action', models.CharField(max_length=255, verbose_name='Action effectuée')),
                ('ancien_statut', models.CharField(blank=True, max_length=100, null=True, verbose_name='Statut avant modification')),
                ('nouveau_statut', models.CharField(blank=True, max_length=100, null=True, verbose_name='Statut après modification')),
                ('details', models.JSONField(blank=True, null=True, verbose_name='Détails des modifications')),
                ('inscrits_total', models.PositiveIntegerField(blank=True, null=True, verbose_name='Total inscrits')),
                ('inscrits_crif', models.PositiveIntegerField(blank=True, null=True, verbose_name='Inscrits CRIF')),
                ('inscrits_mp', models.PositiveIntegerField(blank=True, null=True, verbose_name='Inscrits MP')),
                ('total_places', models.PositiveIntegerField(blank=True, null=True, verbose_name='Total places')),
                ('saturation', models.FloatField(blank=True, null=True, verbose_name='Niveau de saturation (%)')),
                ('taux_remplissage', models.FloatField(blank=True, null=True, verbose_name='Taux de remplissage (%)')),
                ('semaine', models.PositiveIntegerField(blank=True, null=True, verbose_name='Numéro de la semaine')),
                ('mois', models.PositiveIntegerField(blank=True, null=True, verbose_name='Mois')),
                ('annee', models.PositiveIntegerField(blank=True, null=True, verbose_name='Année')),
            ],
            options={
                'verbose_name': 'Historique de formation',
                'verbose_name_plural': 'Historiques des formations',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Parametre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Date de création')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Dernière mise à jour')),
                ('cle', models.CharField(max_length=100, unique=True, verbose_name='Clé du paramètre')),
                ('valeur', models.TextField(verbose_name='Valeur du paramètre')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description du paramètre')),
            ],
            options={
                'verbose_name': 'Paramètre',
                'verbose_name_plural': 'Paramètres',
                'ordering': ['cle'],
            },
        ),
        migrations.CreateModel(
            name='Partenaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Date de création')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Dernière mise à jour')),
                ('nom', models.CharField(max_length=255, unique=True, verbose_name="Nom de l'partenaire")),
                ('secteur_activite', models.CharField(blank=True, max_length=255, null=True, verbose_name="Secteur d'activité")),
                ('contact_nom', models.CharField(blank=True, max_length=255, null=True, verbose_name='Nom du contact')),
                ('contact_poste', models.CharField(blank=True, max_length=255, null=True, verbose_name='Poste du contact')),
                ('contact_telephone', models.CharField(blank=True, max_length=20, null=True, verbose_name='Téléphone du contact')),
                ('contact_email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email du contact')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description de la relation')),
            ],
            options={
                'verbose_name': 'Partenaire',
                'verbose_name_plural': 'Partenaires',
                'ordering': ['nom'],
            },
        ),
        migrations.CreateModel(
            name='Rapport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Date de création')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Dernière mise à jour')),
                ('periode', models.CharField(choices=[('Hebdomadaire', 'Hebdomadaire'), ('Mensuel', 'Mensuel'), ('Annuel', 'Annuel')], max_length=50, verbose_name='Période du rapport')),
                ('date_debut', models.DateField(verbose_name='Date de début de la période')),
                ('date_fin', models.DateField(verbose_name='Date de fin de la période')),
                ('total_inscrits', models.PositiveIntegerField(default=0, verbose_name='Total des inscrits')),
                ('inscrits_crif', models.PositiveIntegerField(default=0, verbose_name='Inscrits CRIF')),
                ('inscrits_mp', models.PositiveIntegerField(default=0, verbose_name='Inscrits MP')),
                ('total_places', models.PositiveIntegerField(default=0, verbose_name='Total des places')),
                ('nombre_evenements', models.PositiveIntegerField(default=0, verbose_name="Nombre d'événements")),
                ('nombre_candidats', models.PositiveIntegerField(default=0, verbose_name='Nombre de candidats')),
                ('nombre_entretiens', models.PositiveIntegerField(default=0, verbose_name="Nombre d'entretiens")),
            ],
            options={
                'verbose_name': 'Rapport de formation',
                'verbose_name_plural': 'Rapports de formation',
                'ordering': ['-date_fin'],
            },
        ),
        migrations.CreateModel(
            name='Recherche',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Date de création')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Dernière mise à jour')),
                ('terme_recherche', models.CharField(blank=True, max_length=255, null=True, verbose_name='Terme de recherche')),
                ('date_debut', models.DateField(blank=True, null=True, verbose_name='Date de début filtrée')),
                ('date_fin', models.DateField(blank=True, null=True, verbose_name='Date de fin filtrée')),
                ('nombre_resultats', models.PositiveIntegerField(default=0, verbose_name='Nombre de résultats obtenus')),
                ('temps_execution', models.FloatField(blank=True, null=True, verbose_name="Temps d'exécution (ms)")),
            ],
            options={
                'verbose_name': 'Recherche',
                'verbose_name_plural': 'Recherches',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Statut',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Date de création')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Dernière mise à jour')),
                ('nom', models.CharField(choices=[('non_defini', 'Non défini'), ('recrutement_en_cours', 'Recrutement en cours'), ('formation_en_cours', 'Formation en cours'), ('formation_a_annuler', 'Formation à annuler'), ('formation_a_repousser', 'Formation à repousser'), ('formation_annulee', 'Formation annulée'), ('pleine', 'Pleine'), ('quasi_pleine', 'Quasi-pleine'), ('autre', 'Autre')], max_length=100, verbose_name='Nom du statut')),
                ('couleur', models.CharField(blank=True, help_text='Couleur hexadécimale (ex: #FF5733)', max_length=7, verbose_name='Couleur')),
                ('description_autre', models.CharField(blank=True, max_length=255, null=True, verbose_name='Description personnalisée')),
            ],
            options={
                'verbose_name': 'Statut',
                'verbose_name_plural': 'Statuts',
                'ordering': ['nom'],
            },
        ),
        migrations.CreateModel(
            name='TypeOffre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Date de création')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Dernière mise à jour')),
                ('nom', models.CharField(choices=[('crif', 'CRIF'), ('alternance', 'Alternance'), ('poec', 'POEC'), ('poei', 'POEI'), ('tosa', 'TOSA'), ('autre', 'Autre'), ('non_defini', 'Non défini')], default='non_defini', max_length=100, verbose_name="Type d'offre")),
                ('autre', models.CharField(blank=True, max_length=255, verbose_name='Autre (personnalisé)')),
            ],
            options={
                'verbose_name': "Type d'offre",
                'verbose_name_plural': "Types d'offres",
                'ordering': ['nom'],
            },
        ),
        migrations.AddConstraint(
            model_name='typeoffre',
            constraint=models.UniqueConstraint(condition=models.Q(('autre__isnull', False), ('nom', 'autre')), fields=('autre',), name='unique_autre_non_null'),
        ),
        migrations.AddField(
            model_name='recherche',
            name='filtre_centre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='recherches', to='rap_app.centre', verbose_name='Centre filtré'),
        ),
        migrations.AddField(
            model_name='recherche',
            name='filtre_statut',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='recherches', to='rap_app.statut', verbose_name='Statut filtré'),
        ),
        migrations.AddField(
            model_name='recherche',
            name='filtre_type_offre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='recherches', to='rap_app.typeoffre', verbose_name="Type d'offre filtré"),
        ),
        migrations.AddField(
            model_name='rapport',
            name='formation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rapports', to='rap_app.formation', verbose_name='Formation associée'),
        ),
        migrations.AddIndex(
            model_name='partenaire',
            index=models.Index(fields=['nom'], name='rap_app_par_nom_983061_idx'),
        ),
        migrations.AddField(
            model_name='historiqueformation',
            name='formation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='historique_formations', to='rap_app.formation', verbose_name='Formation concernée'),
        ),
        migrations.AddField(
            model_name='historiqueformation',
            name='utilisateur',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='historique_utilisateurs', to=settings.AUTH_USER_MODEL, verbose_name='Utilisateur ayant modifié'),
        ),
        migrations.AddField(
            model_name='formation',
            name='centre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='formations', to='rap_app.centre', verbose_name='Centre de formation'),
        ),
        migrations.AddField(
            model_name='formation',
            name='partenaires',
            field=models.ManyToManyField(blank=True, related_name='formations', to='rap_app.partenaire', verbose_name='Partenaires'),
        ),
        migrations.AddField(
            model_name='formation',
            name='statut',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='formations', to='rap_app.statut', verbose_name='Statut de la formation'),
        ),
        migrations.AddField(
            model_name='formation',
            name='type_offre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='formations', to='rap_app.typeoffre', verbose_name="Type d'offre"),
        ),
        migrations.AddField(
            model_name='formation',
            name='utilisateur',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='formations_creees', to=settings.AUTH_USER_MODEL, verbose_name='Créé par'),
        ),
        migrations.AddField(
            model_name='evenement',
            name='formation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='evenements', to='rap_app.formation', verbose_name='Formation associée'),
        ),
        migrations.AddField(
            model_name='document',
            name='formation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='documents', to='rap_app.formation', verbose_name='Formation associée'),
        ),
        migrations.AddField(
            model_name='document',
            name='utilisateur',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='commentaire',
            name='formation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commentaires', to='rap_app.formation', verbose_name='Formation'),
        ),
        migrations.AddField(
            model_name='commentaire',
            name='utilisateur',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='commentaires', to=settings.AUTH_USER_MODEL, verbose_name='Utilisateur associé'),
        ),
        migrations.AddIndex(
            model_name='centre',
            index=models.Index(fields=['nom'], name='rap_app_cen_nom_671da5_idx'),
        ),
        migrations.AddIndex(
            model_name='centre',
            index=models.Index(fields=['code_postal'], name='rap_app_cen_code_po_c9960c_idx'),
        ),
        migrations.AddIndex(
            model_name='recherche',
            index=models.Index(fields=['terme_recherche'], name='rap_app_rec_terme_r_3f5d4d_idx'),
        ),
        migrations.AddIndex(
            model_name='recherche',
            index=models.Index(fields=['created_at'], name='rap_app_rec_created_e5edf0_idx'),
        ),
        migrations.AddIndex(
            model_name='recherche',
            index=models.Index(fields=['nombre_resultats'], name='rap_app_rec_nombre__2090c2_idx'),
        ),
        migrations.AddIndex(
            model_name='rapport',
            index=models.Index(fields=['date_debut'], name='rap_app_rap_date_de_392072_idx'),
        ),
        migrations.AddIndex(
            model_name='rapport',
            index=models.Index(fields=['date_fin'], name='rap_app_rap_date_fi_a3dd0d_idx'),
        ),
        migrations.AddIndex(
            model_name='rapport',
            index=models.Index(fields=['periode'], name='rap_app_rap_periode_db57b2_idx'),
        ),
        migrations.AddIndex(
            model_name='historiqueformation',
            index=models.Index(fields=['created_at'], name='rap_app_his_created_c1d4f1_idx'),
        ),
        migrations.AddIndex(
            model_name='historiqueformation',
            index=models.Index(fields=['action'], name='rap_app_his_action_40c15f_idx'),
        ),
        migrations.AddIndex(
            model_name='historiqueformation',
            index=models.Index(fields=['formation'], name='rap_app_his_formati_aa2815_idx'),
        ),
        migrations.AddIndex(
            model_name='formation',
            index=models.Index(fields=['start_date'], name='rap_app_for_start_d_4c1834_idx'),
        ),
        migrations.AddIndex(
            model_name='formation',
            index=models.Index(fields=['end_date'], name='rap_app_for_end_dat_e7d2c9_idx'),
        ),
        migrations.AddIndex(
            model_name='formation',
            index=models.Index(fields=['nom'], name='rap_app_for_nom_27c494_idx'),
        ),
        migrations.AddIndex(
            model_name='evenement',
            index=models.Index(fields=['event_date'], name='rap_app_eve_event_d_758395_idx'),
        ),
        migrations.AddIndex(
            model_name='evenement',
            index=models.Index(fields=['type_evenement'], name='rap_app_eve_type_ev_11d24c_idx'),
        ),
        migrations.AddIndex(
            model_name='document',
            index=models.Index(fields=['nom_fichier'], name='rap_app_doc_nom_fic_b4d61d_idx'),
        ),
        migrations.AddIndex(
            model_name='commentaire',
            index=models.Index(fields=['created_at'], name='rap_app_com_created_aad49b_idx'),
        ),
        migrations.AddIndex(
            model_name='commentaire',
            index=models.Index(fields=['formation'], name='rap_app_com_formati_0c3422_idx'),
        ),
    ]



================================================
File: rap_app/migrations/0002_alter_partenaire_nom.py
================================================
# Generated by Django 4.2.7 on 2025-03-11 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rap_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partenaire',
            name='nom',
            field=models.CharField(max_length=255, unique=True, verbose_name='Nom du partenaire'),
        ),
    ]



================================================
File: rap_app/migrations/0003_alter_rapport_options_remove_rapport_created_at_and_more.py
================================================
# Generated by Django 4.2.7 on 2025-03-11 23:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rap_app', '0002_alter_partenaire_nom'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rapport',
            options={'ordering': ['-date_fin']},
        ),
        migrations.RemoveField(
            model_name='rapport',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='rapport',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='rapport',
            name='centre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='rap_app.centre'),
        ),
        migrations.AddField(
            model_name='rapport',
            name='derniers_commentaires',
            field=models.JSONField(default=list),
        ),
        migrations.AddField(
            model_name='rapport',
            name='entrees_formation',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='rapport',
            name='nombre_partenaires',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='rapport',
            name='prevus_crif',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='rapport',
            name='prevus_mp',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='rapport',
            name='saturation_moyenne',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='rapport',
            name='saturation_par_formation',
            field=models.JSONField(default=dict),
        ),
        migrations.AddField(
            model_name='rapport',
            name='statut',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='rap_app.statut'),
        ),
        migrations.AddField(
            model_name='rapport',
            name='type_offre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='rap_app.typeoffre'),
        ),
        migrations.AlterField(
            model_name='rapport',
            name='date_debut',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='rapport',
            name='date_fin',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='rapport',
            name='formation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rapports', to='rap_app.formation'),
        ),
        migrations.AlterField(
            model_name='rapport',
            name='inscrits_crif',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='rapport',
            name='inscrits_mp',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='rapport',
            name='nombre_candidats',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='rapport',
            name='nombre_entretiens',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='rapport',
            name='nombre_evenements',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='rapport',
            name='periode',
            field=models.CharField(choices=[('Hebdomadaire', 'Hebdomadaire'), ('Mensuel', 'Mensuel'), ('Annuel', 'Annuel')], max_length=50),
        ),
        migrations.AlterField(
            model_name='rapport',
            name='total_inscrits',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='rapport',
            name='total_places',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddIndex(
            model_name='rapport',
            index=models.Index(fields=['centre'], name='rap_app_rap_centre__cf0208_idx'),
        ),
        migrations.AddIndex(
            model_name='rapport',
            index=models.Index(fields=['type_offre'], name='rap_app_rap_type_of_e4b013_idx'),
        ),
        migrations.AddIndex(
            model_name='rapport',
            index=models.Index(fields=['statut'], name='rap_app_rap_statut__098b07_idx'),
        ),
    ]



================================================
File: rap_app/migrations/0004_alter_rapport_options_and_more.py
================================================
# Generated by Django 4.2.7 on 2025-03-12 01:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rap_app', '0003_alter_rapport_options_remove_rapport_created_at_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rapport',
            options={},
        ),
        migrations.RemoveIndex(
            model_name='rapport',
            name='rap_app_rap_date_de_392072_idx',
        ),
        migrations.RemoveIndex(
            model_name='rapport',
            name='rap_app_rap_date_fi_a3dd0d_idx',
        ),
        migrations.RemoveIndex(
            model_name='rapport',
            name='rap_app_rap_periode_db57b2_idx',
        ),
        migrations.RemoveIndex(
            model_name='rapport',
            name='rap_app_rap_centre__cf0208_idx',
        ),
        migrations.RemoveIndex(
            model_name='rapport',
            name='rap_app_rap_type_of_e4b013_idx',
        ),
        migrations.RemoveIndex(
            model_name='rapport',
            name='rap_app_rap_statut__098b07_idx',
        ),
        migrations.AlterField(
            model_name='rapport',
            name='formation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rapports', to='rap_app.formation'),
        ),
    ]



================================================
File: rap_app/migrations/0005_alter_rapport_options_remove_rapport_centre_and_more.py
================================================
# Generated by Django 4.2.7 on 2025-03-12 19:13

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('rap_app', '0004_alter_rapport_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rapport',
            options={'ordering': ['-date_fin'], 'verbose_name': 'Rapport de formation', 'verbose_name_plural': 'Rapports de formation'},
        ),
        migrations.RemoveField(
            model_name='rapport',
            name='centre',
        ),
        migrations.RemoveField(
            model_name='rapport',
            name='derniers_commentaires',
        ),
        migrations.RemoveField(
            model_name='rapport',
            name='entrees_formation',
        ),
        migrations.RemoveField(
            model_name='rapport',
            name='nombre_partenaires',
        ),
        migrations.RemoveField(
            model_name='rapport',
            name='prevus_crif',
        ),
        migrations.RemoveField(
            model_name='rapport',
            name='prevus_mp',
        ),
        migrations.RemoveField(
            model_name='rapport',
            name='saturation_moyenne',
        ),
        migrations.RemoveField(
            model_name='rapport',
            name='saturation_par_formation',
        ),
        migrations.RemoveField(
            model_name='rapport',
            name='statut',
        ),
        migrations.RemoveField(
            model_name='rapport',
            name='type_offre',
        ),
        migrations.AddField(
            model_name='rapport',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Date de création'),
        ),
        migrations.AddField(
            model_name='rapport',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Dernière mise à jour'),
        ),
        migrations.AlterField(
            model_name='rapport',
            name='date_debut',
            field=models.DateField(verbose_name='Date de début de la période'),
        ),
        migrations.AlterField(
            model_name='rapport',
            name='date_fin',
            field=models.DateField(verbose_name='Date de fin de la période'),
        ),
        migrations.AlterField(
            model_name='rapport',
            name='formation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rapports', to='rap_app.formation', verbose_name='Formation associée'),
        ),
        migrations.AlterField(
            model_name='rapport',
            name='inscrits_crif',
            field=models.PositiveIntegerField(default=0, verbose_name='Inscrits CRIF'),
        ),
        migrations.AlterField(
            model_name='rapport',
            name='inscrits_mp',
            field=models.PositiveIntegerField(default=0, verbose_name='Inscrits MP'),
        ),
        migrations.AlterField(
            model_name='rapport',
            name='nombre_candidats',
            field=models.PositiveIntegerField(default=0, verbose_name='Nombre de candidats'),
        ),
        migrations.AlterField(
            model_name='rapport',
            name='nombre_entretiens',
            field=models.PositiveIntegerField(default=0, verbose_name="Nombre d'entretiens"),
        ),
        migrations.AlterField(
            model_name='rapport',
            name='nombre_evenements',
            field=models.PositiveIntegerField(default=0, verbose_name="Nombre d'événements"),
        ),
        migrations.AlterField(
            model_name='rapport',
            name='periode',
            field=models.CharField(choices=[('Hebdomadaire', 'Hebdomadaire'), ('Mensuel', 'Mensuel'), ('Annuel', 'Annuel')], max_length=50, verbose_name='Période du rapport'),
        ),
        migrations.AlterField(
            model_name='rapport',
            name='total_inscrits',
            field=models.PositiveIntegerField(default=0, verbose_name='Total des inscrits'),
        ),
        migrations.AlterField(
            model_name='rapport',
            name='total_places',
            field=models.PositiveIntegerField(default=0, verbose_name='Total des places'),
        ),
        migrations.AddIndex(
            model_name='rapport',
            index=models.Index(fields=['date_debut'], name='rap_app_rap_date_de_392072_idx'),
        ),
        migrations.AddIndex(
            model_name='rapport',
            index=models.Index(fields=['date_fin'], name='rap_app_rap_date_fi_a3dd0d_idx'),
        ),
        migrations.AddIndex(
            model_name='rapport',
            index=models.Index(fields=['periode'], name='rap_app_rap_periode_db57b2_idx'),
        ),
    ]



================================================
File: rap_app/migrations/0006_delete_rapport.py
================================================
# Generated by Django 4.2.7 on 2025-03-12 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rap_app', '0005_alter_rapport_options_remove_rapport_centre_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Rapport',
        ),
    ]



================================================
File: rap_app/migrations/0007_rapport_delete_parametre.py
================================================
# Generated by Django 4.2.7 on 2025-03-18 18:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rap_app', '0006_delete_rapport'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rapport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Date de création')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Dernière mise à jour')),
                ('nom', models.CharField(max_length=255, verbose_name='Nom du rapport')),
                ('type_rapport', models.CharField(choices=[('occupation', "Rapport d'occupation des formations"), ('centre', 'Rapport de performance par centre'), ('statut', 'Rapport de suivi des statuts'), ('evenement', "Rapport d'efficacité des événements"), ('recrutement', 'Rapport de suivi du recrutement'), ('partenaire', "Rapport d'activité des partenaires"), ('repartition', 'Rapport de répartition des partenaires'), ('periodique', 'Rapport périodique'), ('annuel', 'Rapport annuel consolidé'), ('utilisateur', "Rapport d'activité utilisateurs")], max_length=50, verbose_name='Type de rapport')),
                ('periode', models.CharField(choices=[('quotidien', 'Quotidien'), ('hebdomadaire', 'Hebdomadaire'), ('mensuel', 'Mensuel'), ('trimestriel', 'Trimestriel'), ('annuel', 'Annuel'), ('personnalise', 'Période personnalisée')], max_length=50, verbose_name='Périodicité')),
                ('date_debut', models.DateField(verbose_name='Date de début')),
                ('date_fin', models.DateField(verbose_name='Date de fin')),
                ('format', models.CharField(choices=[('pdf', 'PDF'), ('excel', 'Excel'), ('csv', 'CSV'), ('html', 'HTML')], default='html', max_length=10, verbose_name='Format')),
                ('donnees', models.JSONField(default=dict, verbose_name='Données du rapport')),
                ('date_generation', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date de génération')),
                ('temps_generation', models.FloatField(blank=True, null=True, verbose_name='Temps de génération (s)')),
                ('centre', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='rap_app.centre', verbose_name='Centre')),
                ('statut', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='rap_app.statut', verbose_name='Statut')),
                ('type_offre', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='rap_app.typeoffre', verbose_name="Type d'offre")),
                ('utilisateur', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Généré par')),
            ],
            options={
                'verbose_name': 'Rapport',
                'verbose_name_plural': 'Rapports',
                'ordering': ['-date_generation'],
            },
        ),
        migrations.DeleteModel(
            name='Parametre',
        ),
    ]



================================================
File: rap_app/migrations/0008_company_prospection.py
================================================
# Generated by Django 4.2.7 on 2025-03-19 22:39

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rap_app', '0007_rapport_delete_parametre'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Nom')),
                ('street_name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Numéro et nom de la rue')),
                ('zip_code', models.CharField(blank=True, max_length=5, null=True, validators=[django.core.validators.RegexValidator(message='Le code postal doit être composé de 5 chiffres.', regex='^[0-9]{5}$')], verbose_name='Code postal')),
                ('city', models.CharField(blank=True, max_length=100, null=True, verbose_name='Ville')),
                ('country', models.CharField(blank=True, default='France', max_length=100, null=True, verbose_name='Pays')),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True, validators=[django.core.validators.RegexValidator(message='Entrez un numéro de téléphone français valide commençant par 01, 02, ..., 06 ou 07.', regex='^(0[1-9]\\d{8})$|^(?:\\+33|0033)[1-9]\\d{8}$')], verbose_name='Numéro de téléphone')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Adresse email')),
                ('sector_name', models.CharField(blank=True, max_length=200, null=True, verbose_name="Secteur d'activité")),
                ('actions', models.CharField(blank=True, choices=[('accueil_stagiaires', 'Accueil de stagiaires'), ('recrutement_cdi', 'Recrutement - CDI'), ('recrutement_cdd', 'Recrutement - CDD'), ('recrutement_stage', 'Recrutement - Stage'), ('recrutement_formation', 'Recrutement Formation'), ('recrutement_apprentissage', 'Recrutement - Apprentissage'), ('presentation_metier_entreprise', 'Présentation de métier(s)/entreprise'), ('enquete_metier', 'Enquête métier'), ('visite_entreprise', 'Visite de l’entreprise'), ('coaching', 'Coaching'), ('autre', 'Autre'), ('partenariat', 'Partenariat'), ('taxe_apprentissage', 'Taxe apprentissage'), ('non_definie', 'Non définie')], max_length=50, null=True, verbose_name='Actions')),
                ('action_description', models.CharField(blank=True, max_length=5000, null=True, verbose_name="Description de l'action")),
                ('website', models.URLField(blank=True, null=True, validators=[django.core.validators.RegexValidator(regex='^(http|https)://')])),
                ('social_network_url', models.CharField(blank=True, max_length=200, null=True, verbose_name='URL du réseau social')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Contact créé le')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Date de MAJ')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'entreprise',
                'verbose_name_plural': 'entreprises',
                'db_table': 'companies',
            },
        ),
        migrations.CreateModel(
            name='Prospection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_prospection', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date de la prospection')),
                ('statut', models.CharField(choices=[('a_faire', 'À faire'), ('en_cours', 'En cours'), ('a_relancer', 'À relancer'), ('acceptee', 'Acceptée'), ('refusee', 'Refusée'), ('annulee', 'Annulée')], default='a_faire', max_length=20, verbose_name='Statut')),
                ('objectif', models.CharField(choices=[('prise_contact', 'Prise de contact'), ('rendez_vous', 'Obtenir un rendez-vous'), ('presentation_offre', 'Présentation d’une offre'), ('contrat', 'Signer un contrat'), ('partenariat', 'Établir un partenariat'), ('autre', 'Autre')], default='prise_contact', max_length=30, verbose_name='Objectif')),
                ('commentaire', models.TextField(blank=True, null=True, verbose_name='Commentaire')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prospections', to='rap_app.company', verbose_name='Entreprise')),
                ('formation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prospections', to='rap_app.formation', verbose_name='Formation')),
                ('responsable', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Responsable')),
            ],
            options={
                'verbose_name': 'Suivi de prospection',
                'verbose_name_plural': 'Suivis de prospection',
                'ordering': ['-date_prospection'],
            },
        ),
    ]



================================================
File: rap_app/migrations/0009_remove_company_email_remove_company_phone_number_and_more.py
================================================
# Generated by Django 4.2.7 on 2025-03-19 22:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rap_app', '0008_company_prospection'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='email',
        ),
        migrations.RemoveField(
            model_name='company',
            name='phone_number',
        ),
        migrations.AddField(
            model_name='company',
            name='contact_email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='Adresse email du contact'),
        ),
        migrations.AddField(
            model_name='company',
            name='contact_job',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Métier du contact'),
        ),
        migrations.AddField(
            model_name='company',
            name='contact_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Nom du contact'),
        ),
        migrations.AddField(
            model_name='company',
            name='contact_phone_number',
            field=models.CharField(blank=True, max_length=20, null=True, validators=[django.core.validators.RegexValidator(message='Entrez un numéro de téléphone français valide commençant par 01, 02, ..., 06 ou 07.', regex='^(0[1-9]\\d{8})$|^(?:\\+33|0033)[1-9]\\d{8}$')], verbose_name='Numéro de téléphone du contact'),
        ),
    ]



================================================
File: rap_app/migrations/0010_historiqueprospection_and_more.py
================================================
# Generated by Django 4.2.7 on 2025-03-21 16:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rap_app', '0009_remove_company_email_remove_company_phone_number_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoriqueProspection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_modification', models.DateTimeField(auto_now_add=True)),
                ('ancien_statut', models.CharField(choices=[('a_faire', 'À faire'), ('en_cours', 'En cours'), ('a_relancer', 'À relancer'), ('acceptee', 'Acceptée'), ('refusee', 'Refusée'), ('annulee', 'Annulée')], max_length=20)),
                ('nouveau_statut', models.CharField(choices=[('a_faire', 'À faire'), ('en_cours', 'En cours'), ('a_relancer', 'À relancer'), ('acceptee', 'Acceptée'), ('refusee', 'Refusée'), ('annulee', 'Annulée')], max_length=20)),
                ('commentaire', models.TextField(blank=True, null=True)),
                ('prochain_contact', models.DateField(blank=True, null=True, verbose_name='Date de relance')),
                ('resultat', models.TextField(blank=True, null=True, verbose_name='Résultat ou retour de la prospection')),
                ('moyen_contact', models.CharField(blank=True, choices=[('email', 'Email'), ('telephone', 'Téléphone'), ('visite', 'Visite'), ('réseaux', 'Réseaux sociaux')], max_length=50, null=True, verbose_name='Moyen de contact')),
            ],
            options={
                'verbose_name': 'Historique de prospection',
                'ordering': ['-date_modification'],
            },
        ),
        migrations.AlterModelOptions(
            name='historiqueformation',
            options={'ordering': ['-date_modification'], 'verbose_name': 'Historique de modification de formation'},
        ),
        migrations.AlterModelOptions(
            name='prospection',
            options={'ordering': ['-date_prospection'], 'verbose_name': 'Suivi de la prospection', 'verbose_name_plural': 'Suivis des prospections'},
        ),
        migrations.RemoveIndex(
            model_name='historiqueformation',
            name='rap_app_his_created_c1d4f1_idx',
        ),
        migrations.RemoveIndex(
            model_name='historiqueformation',
            name='rap_app_his_action_40c15f_idx',
        ),
        migrations.RemoveIndex(
            model_name='historiqueformation',
            name='rap_app_his_formati_aa2815_idx',
        ),
        migrations.RemoveField(
            model_name='historiqueformation',
            name='action',
        ),
        migrations.RemoveField(
            model_name='historiqueformation',
            name='ancien_statut',
        ),
        migrations.RemoveField(
            model_name='historiqueformation',
            name='annee',
        ),
        migrations.RemoveField(
            model_name='historiqueformation',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='historiqueformation',
            name='details',
        ),
        migrations.RemoveField(
            model_name='historiqueformation',
            name='inscrits_crif',
        ),
        migrations.RemoveField(
            model_name='historiqueformation',
            name='inscrits_mp',
        ),
        migrations.RemoveField(
            model_name='historiqueformation',
            name='inscrits_total',
        ),
        migrations.RemoveField(
            model_name='historiqueformation',
            name='mois',
        ),
        migrations.RemoveField(
            model_name='historiqueformation',
            name='nouveau_statut',
        ),
        migrations.RemoveField(
            model_name='historiqueformation',
            name='saturation',
        ),
        migrations.RemoveField(
            model_name='historiqueformation',
            name='semaine',
        ),
        migrations.RemoveField(
            model_name='historiqueformation',
            name='taux_remplissage',
        ),
        migrations.RemoveField(
            model_name='historiqueformation',
            name='total_places',
        ),
        migrations.RemoveField(
            model_name='historiqueformation',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='historiqueformation',
            name='utilisateur',
        ),
        migrations.AddField(
            model_name='historiqueformation',
            name='ancienne_valeur',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='historiqueformation',
            name='champ_modifie',
            field=models.CharField(default='non_specifié', max_length=100, verbose_name='Champ modifié'),
        ),
        migrations.AddField(
            model_name='historiqueformation',
            name='commentaire',
            field=models.TextField(blank=True, null=True, verbose_name='Commentaire lié à la modification'),
        ),
        migrations.AddField(
            model_name='historiqueformation',
            name='date_modification',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='historiqueformation',
            name='modifie_par',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historiqueformation',
            name='nouvelle_valeur',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='prospection',
            name='motif',
            field=models.CharField(choices=[('POEI', 'POEI'), ('Apprentissage', 'Apprentissage'), ('VAE', 'VAE'), ('partenariat', 'Établir un partenariat'), ('autre', 'Autre')], default='prise_contact', max_length=30, verbose_name='Motif de la prospection'),
        ),
        migrations.AlterField(
            model_name='historiqueformation',
            name='formation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='historiques', to='rap_app.formation'),
        ),
        migrations.AlterField(
            model_name='prospection',
            name='commentaire',
            field=models.TextField(blank=True, null=True, verbose_name='Commentaires de la prospection'),
        ),
        migrations.AlterField(
            model_name='prospection',
            name='formation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='prospections', to='rap_app.formation', verbose_name='Formation en lien'),
        ),
        migrations.AlterField(
            model_name='prospection',
            name='objectif',
            field=models.CharField(choices=[('prise_contact', 'Prise de contact'), ('rendez_vous', 'Obtenir un rendez-vous'), ('presentation_offre', 'Présentation d’une offre'), ('contrat', 'Signer un contrat'), ('partenariat', 'Établir un partenariat'), ('autre', 'Autre')], default='prise_contact', max_length=30, verbose_name='Objectif de la prospection'),
        ),
        migrations.AlterField(
            model_name='prospection',
            name='responsable',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Responsable de la prospection'),
        ),
        migrations.AlterField(
            model_name='prospection',
            name='statut',
            field=models.CharField(choices=[('a_faire', 'À faire'), ('en_cours', 'En cours'), ('a_relancer', 'À relancer'), ('acceptee', 'Acceptée'), ('refusee', 'Refusée'), ('annulee', 'Annulée')], default='a_faire', max_length=20, verbose_name='Statut de la prospection'),
        ),
        migrations.AddField(
            model_name='historiqueprospection',
            name='modifie_par',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historiqueprospection',
            name='prospection',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='historiques', to='rap_app.prospection'),
        ),
    ]



================================================
File: rap_app/migrations/0011_historiqueformation_action_and_more.py
================================================
# Generated by Django 4.2.7 on 2025-03-21 22:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rap_app', '0010_historiqueprospection_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='historiqueformation',
            name='action',
            field=models.CharField(default='modification', max_length=100),
        ),
        migrations.AddField(
            model_name='historiqueformation',
            name='details',
            field=models.JSONField(blank=True, default=dict),
        ),
        migrations.AddField(
            model_name='historiqueformation',
            name='utilisateur',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='historiques_utilisateur', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='historiqueprospection',
            name='ancien_statut',
            field=models.CharField(choices=[('a_faire', 'À faire'), ('en_cours', 'En cours'), ('a_relancer', 'À relancer'), ('acceptee', 'Acceptée'), ('refusee', 'Refusée'), ('annulee', 'Annulée'), ('Non renséigné', 'Non renséigné')], max_length=20),
        ),
        migrations.AlterField(
            model_name='historiqueprospection',
            name='nouveau_statut',
            field=models.CharField(choices=[('a_faire', 'À faire'), ('en_cours', 'En cours'), ('a_relancer', 'À relancer'), ('acceptee', 'Acceptée'), ('refusee', 'Refusée'), ('annulee', 'Annulée'), ('Non renséigné', 'Non renséigné')], max_length=20),
        ),
        migrations.AlterField(
            model_name='prospection',
            name='statut',
            field=models.CharField(choices=[('a_faire', 'À faire'), ('en_cours', 'En cours'), ('a_relancer', 'À relancer'), ('acceptee', 'Acceptée'), ('refusee', 'Refusée'), ('annulee', 'Annulée'), ('Non renséigné', 'Non renséigné')], default='a_faire', max_length=20, verbose_name='Statut de la prospection'),
        ),
    ]



================================================
File: rap_app/migrations/0012_typeoffre_couleur.py
================================================
# Generated by Django 4.2.7 on 2025-03-22 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rap_app', '0011_historiqueformation_action_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='typeoffre',
            name='couleur',
            field=models.CharField(default='#6c757d', max_length=7, verbose_name='Couleur associée (hexadécimal)'),
        ),
    ]



================================================
File: rap_app/migrations/__init__.py
================================================




================================================
File: rap_app/models/__init__.py
================================================
from .base import BaseModel
from .centres import Centre
from .statut import Statut
from .types_offre import TypeOffre
from .formations import Formation, FormationManager
from .commentaires import Commentaire
from .evenements import Evenement
from .documents import Document
from .recherches import Recherche
from .partenaires import Partenaire
from .rapports import Rapport  
from .company import Company
from .prospection import Prospection
from .formations import HistoriqueFormation

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
    'Rapport',  
    'Prospection',
    'Company',
]


================================================
File: rap_app/models/base.py
================================================
from django.db import models
from django.utils.timezone import now  # Utilise Django timezone pour éviter les problèmes UTC

class BaseModel(models.Model):
    """
    Modèle de base pour tous les modèles de l'application.
    Il inclut la gestion automatique de `created_at` et `updated_at`.
    """

    created_at = models.DateTimeField(default=now, editable=False, verbose_name="Date de création")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Dernière mise à jour")

    class Meta:
        abstract = True  # Empêche Django de créer une table pour ce modèle



================================================
File: rap_app/models/centres.py
================================================
# models/centres.py
from django.db import models
from django.core.validators import RegexValidator
from django.urls import reverse
from .base import BaseModel


class Centre(BaseModel):
    """
    Modèle représentant un centre de formation.

    Hérite de `BaseModel` qui ajoute les champs :
    - `created_at` : Date et heure de création de l'enregistrement.
    - `updated_at` : Date et heure de la dernière modification.

    Champs spécifiques :
    - `nom` : Nom du centre de formation (obligatoire et unique).
    - `code_postal` : Code postal du centre (optionnel).
      * Doit contenir exactement 5 chiffres (validation par regex).
    
    Méthodes :
    - `__str__` : Retourne le nom du centre.
    - `get_absolute_url` : Retourne l'URL du détail du centre.
    - `full_address` : Retourne l'adresse complète (utile pour affichage futur).

    Options du modèle :
    - `verbose_name` : Nom affiché au singulier dans l'interface d'administration.
    - `verbose_name_plural` : Nom affiché au pluriel dans l'interface d'administration.
    - `ordering` : Trie les centres par nom par défaut.
    - `indexes` : Ajoute des index sur `nom` et `code_postal` pour optimiser les recherches.
    """

    nom = models.CharField(
        max_length=255,
        unique=True,  # 🔹 Garantit qu'un centre a un nom unique
        verbose_name="Nom du centre"
    )

    code_postal = models.CharField(
        max_length=5,  # 🔹 Limité à 5 caractères au lieu de 10
        null=True,
        blank=True,
        verbose_name="Code postal",
        validators=[
            RegexValidator(
                regex=r'^\d{5}$',
                message="Le code postal doit contenir exactement 5 chiffres"
            )
        ]
    )

    def __str__(self):
        """Retourne le nom du centre pour une meilleure lisibilité."""
        return self.nom

    def get_absolute_url(self):
        """
        Retourne l'URL du détail du centre.
        Utile pour les vues génériques et les redirections après une création/modification.
        """
        return reverse('centre-detail', kwargs={'pk': self.pk})

    def full_address(self):
        """
        Retourne une version complète de l'adresse (utile si d'autres champs d'adresse sont ajoutés).
        """
        address = self.nom
        if self.code_postal:
            address += f" ({self.code_postal})"
        return address

    class Meta:
        verbose_name = "Centre"
        verbose_name_plural = "Centres"
        ordering = ['nom']
        indexes = [
            models.Index(fields=['nom']),  # 🔹 Index pour optimiser les recherches par nom
            models.Index(fields=['code_postal']),  # 🔹 Index pour les recherches par code postal
        ]



================================================
File: rap_app/models/commentaires.py
================================================
from django.db import models
from django.db.models import Q

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .base import BaseModel
from .formations import Formation
from django.contrib.auth import get_user_model
User = get_user_model()


class Commentaire(BaseModel):
    """
    Modèle représentant un commentaire associé à une formation.
    """

    formation = models.ForeignKey(Formation, on_delete=models.CASCADE, related_name="commentaires", verbose_name="Formation")
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="commentaires", verbose_name="Utilisateur associé")
    contenu = models.TextField(verbose_name="Contenu du commentaire")
    saturation = models.PositiveIntegerField(null=True, blank=True,verbose_name="Niveau de saturation (%)")

    def __str__(self):
        """
        Retourne une représentation lisible du commentaire.
        """
        return f"Commentaire de {self.utilisateur} sur {self.formation.nom} ({self.created_at.strftime('%d/%m/%Y')})"

    class Meta:
        verbose_name = "Commentaire"
        verbose_name_plural = "Commentaires"
        ordering = ['formation', '-created_at']
        indexes = [
            models.Index(fields=['created_at']),
            models.Index(fields=['formation']),
        ]


    @classmethod
    def get_all_commentaires(cls, formation_id=None, utilisateur_id=None, search_query=None, order_by="-created_at"):
        """
        Récupère tous les commentaires avec options de filtres.
        """
        queryset = cls.objects.select_related('formation', 'utilisateur').order_by(order_by)

        filters = Q()
        if formation_id:
            filters &= Q(formation_id=formation_id)
        if utilisateur_id:
            filters &= Q(utilisateur_id=utilisateur_id)
        if search_query:
            filters &= Q(contenu__icontains=search_query)

        queryset = queryset.filter(filters)
        return queryset if queryset.exists() else cls.objects.none()  # ✅ Évite l'erreur avec un queryset vide




@receiver(post_save, sender=Commentaire)
def update_formation_saturation(sender, instance, **kwargs):
    """
    Met à jour la saturation et le dernier commentaire après un ajout.
    """
    if instance.formation:
        updates = {}

        if instance.saturation is not None:
            updates['saturation'] = instance.saturation

        dernier_commentaire = Commentaire.objects.filter(formation=instance.formation).order_by('-created_at').first()
        updates['dernier_commentaire'] = dernier_commentaire.contenu if dernier_commentaire else ""

        if updates:
            Formation.objects.filter(id=instance.formation.id).update(**updates)

@receiver(post_delete, sender=Commentaire)
def handle_commentaire_delete(sender, instance, **kwargs):
    """
    Met à jour la formation après la suppression d'un commentaire.
    """
    if instance.formation:
        dernier_commentaire = Commentaire.objects.filter(formation=instance.formation).order_by('-created_at').first()
        Formation.objects.filter(id=instance.formation.id).update(
            dernier_commentaire=dernier_commentaire.contenu if dernier_commentaire else ""
        )



================================================
File: rap_app/models/company.py
================================================
from django.db import models
from django.core.validators import RegexValidator
from django.utils import timezone
from django.contrib.auth import get_user_model
import logging

# Configuration du logger
logger = logging.getLogger(__name__)

# Expression régulière pour les numéros de téléphone français
phone_regex = RegexValidator(
    regex=r'^(0[1-9]\d{8})$|^(?:\+33|0033)[1-9]\d{8}$',
    message="Entrez un numéro de téléphone français valide commençant par 01, 02, ..., 06 ou 07."
)

CHOICES_TYPE_OF_ACTION = [
    ('accueil_stagiaires', 'Accueil de stagiaires'),
    ('recrutement_cdi', 'Recrutement - CDI'),
    ('recrutement_cdd', 'Recrutement - CDD'),
    ('recrutement_stage', 'Recrutement - Stage'),
    ('recrutement_formation', 'Recrutement Formation'),
    ('recrutement_apprentissage', 'Recrutement - Apprentissage'),
    ('presentation_metier_entreprise', 'Présentation de métier(s)/entreprise'),
    ('enquete_metier', 'Enquête métier'),
    ('visite_entreprise', 'Visite de l’entreprise'),
    ('coaching', 'Coaching'),
    ('autre', 'Autre'),
    ('partenariat', 'Partenariat'),
    ('taxe_apprentissage', 'Taxe apprentissage'),
    ('non_definie', 'Non définie')
]

CHOICES_SOCIAL_NETWORK = [
    ("facebook", "Facebook"),
    ("twitter", "Twitter"),
    ("instagram", "Instagram"),
    ("linkedin", "LinkedIn"),
    ("tiktok", "TikTok"),
]

class Company(models.Model):
    objects = models.Manager()

    # INFORMATIONS GENERALES
    name = models.CharField(max_length=100, null=True, blank=True, verbose_name="Nom")

    # Adresse
    street_name = models.CharField(max_length=200, null=True, blank=True, verbose_name="Numéro et nom de la rue")
    zip_code = models.CharField(
        max_length=5,
        validators=[RegexValidator(regex=r'^[0-9]{5}$', message="Le code postal doit être composé de 5 chiffres.")],
        verbose_name="Code postal",
        blank=True,
        null=True,
    )
    city = models.CharField(max_length=100, verbose_name="Ville", blank=True, null=True)
    country = models.CharField(max_length=100, default="France", verbose_name="Pays", blank=True, null=True)

    # Contact principal (Sans relation avec `Person`)
    contact_name = models.CharField(max_length=255, null=True, blank=True, verbose_name="Nom du contact")
    contact_email = models.EmailField(null=True, blank=True, verbose_name="Adresse email du contact")
    contact_phone_number = models.CharField(
        max_length=20, verbose_name='Numéro de téléphone du contact', blank=True, null=True, validators=[phone_regex]
    )
    contact_job = models.CharField(max_length=255, null=True, blank=True, verbose_name="Métier du contact")

    # Informations complémentaires
    sector_name = models.CharField(max_length=200, null=True, blank=True, verbose_name="Secteur d'activité")

    # Opportunités
    actions = models.CharField(max_length=50, null=True, blank=True, choices=CHOICES_TYPE_OF_ACTION, verbose_name="Actions")
    action_description = models.CharField(max_length=5000, null=True, blank=True, verbose_name="Description de l'action")

    # Informations numériques
    website = models.URLField(null=True, blank=True, validators=[RegexValidator(regex='^(http|https)://')])
    social_network_url = models.CharField(max_length=200, verbose_name="URL du réseau social", null=True, blank=True)

    # Création et mise à jour
    created_by = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now, editable=False, verbose_name="Contact créé le")
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name="Date de MAJ")

    class Meta:
        verbose_name = 'entreprise'
        verbose_name_plural = 'entreprises'
        db_table = 'companies'

    def __str__(self):
        return f"{self.name} ({self.city}) - {self.sector_name or 'Secteur inconnu'}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)



================================================
File: rap_app/models/documents.py
================================================
from django.db import models
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver
import os
from django.conf import settings
from django.core.exceptions import ValidationError
from .base import BaseModel
from .formations import Formation, User


class Document(BaseModel):
    """
    Modèle représentant un document associé à une formation.
    Permet de stocker et gérer différents types de documents (PDF, images, contrats...).
    """

    # Types de documents possibles
    PDF = 'pdf'
    IMAGE = 'image'
    CONTRAT = 'contrat'
    AUTRE = 'autre'

    TYPE_DOCUMENT_CHOICES = [
        (PDF, 'PDF'),
        (IMAGE, 'Image'),
        (CONTRAT, 'Contrat signé'),
        (AUTRE, 'Autre'),
    ]

    formation = models.ForeignKey(Formation, on_delete=models.CASCADE, related_name="documents",  verbose_name="Formation associée")
    nom_fichier = models.CharField(max_length=255, verbose_name="Nom du fichier",db_index=True)
    fichier = models.FileField(upload_to='formations/documents/', verbose_name="Fichier")
    source = models.TextField(null=True, blank=True, verbose_name="Source du document")
    type_document = models.CharField( max_length=20, choices=TYPE_DOCUMENT_CHOICES, default=AUTRE,verbose_name="Type de document")
    taille_fichier = models.PositiveIntegerField(null=True,blank=True, verbose_name="Taille du fichier (Ko)")
    utilisateur = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        """
        Retourne une représentation lisible du document avec un nom tronqué si nécessaire.
        Exemple : "Guide utilisateur.pdf"
        """
        nom_tronque = self.nom_fichier[:50] + ('...' if len(self.nom_fichier) > 50 else '')
        return f"{nom_tronque} ({self.get_type_document_display()})"
    
    def clean(self):
        """Validation personnalisée pour vérifier la correspondance entre type et extension."""
        super().clean()
        if self.fichier and self.type_document:
            validate_file_extension(self.fichier, self.type_document)

    def save(self, *args, **kwargs):
        """
        - Vérifie les règles de validation avant la sauvegarde (`full_clean()`).
        - Met à jour automatiquement la taille du fichier en Ko.
        """
        self.full_clean()  # Exécute la validation avant la sauvegarde.

        if self.fichier and hasattr(self.fichier, 'size'):
            self.taille_fichier = max(1, self.fichier.size // 1024)  # Au moins 1 Ko pour éviter les zeros
        
        super().save(*args, **kwargs)
    class Meta:
        verbose_name = "Document"
        verbose_name_plural = "Documents"
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['nom_fichier']),  # Index pour la recherche rapide
        ]


### 🚀 Validation : Empêcher l'upload d'un fichier invalide
def validate_file_extension(value, type_doc=None):
    """
    Vérifie que le fichier téléchargé correspond bien au type déclaré.
    Le paramètre type_doc peut être passé à la validation.
    """
    ext = os.path.splitext(value.name)[1].lower()
    valid_extensions = {
        'pdf': ['.pdf'],
        'image': ['.jpg', '.jpeg', '.png', '.gif'],
        'contrat': ['.pdf', '.doc', '.docx'],
        'autre': []  # Autorise tout pour "Autre"
    }
    
    # Si aucun type n'est fourni ou si c'est "autre", on accepte le fichier
    if not type_doc or type_doc == Document.AUTRE:
        return
        
    # Vérifie si l'extension correspond au type fourni
    if ext not in valid_extensions.get(type_doc, []):
        raise ValidationError(f"Le fichier {value.name} ne correspond pas au type {dict(Document.TYPE_DOCUMENT_CHOICES).get(type_doc, type_doc)}.")

### 🚀 Suppression automatique des anciens fichiers avant mise à jour
@receiver(pre_save, sender=Document)
def supprimer_fichier_ancien(sender, instance, **kwargs):
    """
    Supprime l'ancien fichier si un nouveau fichier est uploadé pour éviter l'accumulation de fichiers inutiles.
    """
    if instance.pk:
        ancien_document = Document.objects.get(pk=instance.pk)
        if ancien_document.fichier and ancien_document.fichier != instance.fichier:
            ancien_fichier_path = os.path.join(settings.MEDIA_ROOT, ancien_document.fichier.name)
            if os.path.exists(ancien_fichier_path):
                os.remove(ancien_fichier_path)


### 🚀 Suppression automatique du fichier après suppression d'un Document
@receiver(post_delete, sender=Document)
def supprimer_fichier_apres_suppression(sender, instance, **kwargs):
    """
    Supprime le fichier du stockage lorsque l'objet `Document` est supprimé.
    Évite les erreurs si le fichier a déjà été supprimé.
    """
    if instance.fichier:
        fichier_path = os.path.join(settings.MEDIA_ROOT, instance.fichier.name)
        try:
            if os.path.exists(fichier_path):
                os.remove(fichier_path)
        except Exception as e:
            print(f"Erreur lors de la suppression du fichier {fichier_path}: {e}")



================================================
File: rap_app/models/evenements.py
================================================
from django.db import models
from django.core.exceptions import ValidationError
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.db.models import F
from .base import BaseModel
from .formations import Formation

class Evenement(BaseModel):
    """
    Modèle représentant un événement lié à une formation.
    """

    # Constantes pour les types d'événements
    INFO_PRESENTIEL = 'info_collective_presentiel'
    INFO_DISTANCIEL = 'info_collective_distanciel'
    JOB_DATING = 'job_dating'
    EVENEMENT_EMPLOI = 'evenement_emploi'
    FORUM = 'forum'
    JPO = 'jpo'
    AUTRE = 'autre'

    TYPE_EVENEMENT_CHOICES = [
        (INFO_PRESENTIEL, 'Information collective présentiel'),
        (INFO_DISTANCIEL, 'Information collective distanciel'),
        (JOB_DATING, 'Job dating'),
        (EVENEMENT_EMPLOI, 'Événement emploi'),
        (FORUM, 'Forum'),
        (JPO, 'Journée Portes Ouvertes (JPO)'),
        (AUTRE, 'Autre'),
    ]

    formation = models.ForeignKey(Formation, on_delete=models.CASCADE, null=True, blank=True,  related_name="evenements",verbose_name="Formation associée")
    type_evenement = models.CharField(max_length=100, choices=TYPE_EVENEMENT_CHOICES, verbose_name="Type d'événement",db_index=True)
    details = models.TextField(null=True,  blank=True, verbose_name="Détails de l'événement")
    event_date = models.DateField(null=True, blank=True, verbose_name="Date de l'événement")
    description_autre = models.CharField(max_length=255,  null=True,  blank=True,  verbose_name="Description pour 'Autre' événement")

    def clean(self):
        """
        Validation personnalisée :
        - Si l'événement est de type "Autre", la description doit être remplie.
        """
        if self.type_evenement == self.AUTRE and not self.description_autre:
            raise ValidationError({
                'description_autre': "Veuillez fournir une description pour l'événement de type 'Autre'."
            })

    def save(self, *args, **kwargs):
        """
        Personnalisation de la sauvegarde :
        - Vérifie les règles de validation (`full_clean()`).
        """
        self.full_clean()  # Exécute la validation avant la sauvegarde.
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Événement"
        verbose_name_plural = "Événements"
        ordering = ['-event_date']
        indexes = [
            models.Index(fields=['event_date']),  # Optimisation des recherches par date.
            models.Index(fields=['type_evenement']),  # Ajout d'un index sur le type d'événement.
        ]

    def __str__(self):
        """
        Retourne une représentation lisible de l'événement.
        Exemple : "Job dating - 2025-03-10"
        """
        type_event = self.get_type_evenement_display() if self.type_evenement else "Type inconnu"
        return f"{type_event} - {self.event_date.strftime('%d/%m/%Y')}" if self.event_date else f"{type_event} - Date inconnue"



# 🚀 Signaux pour mettre à jour `nombre_evenements` dans `Formation`
@receiver(post_save, sender=Evenement)
def update_nombre_evenements(sender, instance, **kwargs):
    """Met à jour le nombre d'événements dans la formation associée."""
    if instance.formation:
        # Recalcule le nombre total d'événements à chaque modification
        count = Evenement.objects.filter(formation=instance.formation).count()
        Formation.objects.filter(id=instance.formation.id).update(nombre_evenements=count)
        # Rafraîchir la formation
        if hasattr(instance, 'formation'):
            instance.formation.refresh_from_db()

@receiver(post_delete, sender=Evenement)
def update_nombre_evenements_after_delete(sender, instance, **kwargs):
    """Met à jour le nombre d'événements après suppression."""
    if hasattr(instance, 'formation') and instance.formation:
        # Recalcule le nombre après suppression
        count = Evenement.objects.filter(formation=instance.formation).count()
        Formation.objects.filter(id=instance.formation.id).update(nombre_evenements=count)


================================================
File: rap_app/models/formations.py
================================================
import datetime
from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils import timezone
from jsonschema import ValidationError

from .partenaires import Partenaire

from .centres import Centre
from .types_offre import TypeOffre
from .base import BaseModel
from .statut import Statut, get_default_color

User = get_user_model()  # Récupère le modèle User


class FormationManager(models.Manager):
    """
    Manager personnalisé pour optimiser les requêtes sur les formations.
    Ajoute des méthodes pour filtrer les formations selon leur état.
    """
        
    def formations_actives(self):
        """
        Retourne uniquement les formations actives :
        - La date de début est passée (<= aujourd’hui)
        - La date de fin est future ou aujourd’hui (>= aujourd’hui)
        """
        today = timezone.now().date()
        return self.filter(start_date__lte=today, end_date__gte=today)

    def formations_a_venir(self):
        """Retourne uniquement les formations qui commencent dans le futur."""
        return self.filter(start_date__gt=timezone.now().date())

    def formations_terminees(self):
        """Retourne uniquement les formations terminées (date de fin dépassée)."""
        return self.filter(end_date__lt=timezone.now().date())

    def formations_a_recruter(self):
        """Retourne les formations qui ont encore des places disponibles."""
        return self.annotate(
            total_places=models.F('prevus_crif') + models.F('prevus_mp'),
            total_inscrits=models.F('inscrits_crif') + models.F('inscrits_mp')
        ).filter(total_places__gt=models.F('total_inscrits'))

    def formations_toutes(self):
        """Retourne **toutes** les formations, sans filtre."""
        return self.all()

    def trier_par(self, champ_tri):
        """Trie les formations selon un champ donné, si autorisé."""
        champs_autorises = [
            "centre", "-centre",
            "statut", "-statut",
            "type_offre", "-type_offre",
            "start_date", "-start_date",
            "end_date", "-end_date"
        ]
        return self.get_queryset().order_by(champ_tri) if champ_tri in champs_autorises else self.get_queryset()


class Formation(BaseModel):
    """
    Modèle représentant une formation.
    """

    # Informations générales
    nom = models.CharField(max_length=255, verbose_name="Nom de la formation")
    centre = models.ForeignKey(Centre, on_delete=models.CASCADE, related_name='formations', verbose_name="Centre de formation")
    type_offre = models.ForeignKey(TypeOffre, on_delete=models.CASCADE, related_name="formations", verbose_name="Type d'offre")
    statut = models.ForeignKey(Statut, on_delete=models.CASCADE, related_name="formations", verbose_name="Statut de la formation")

    # Dates et identifiants
    start_date = models.DateField(null=True, blank=True, verbose_name="Date de début")
    end_date = models.DateField(null=True, blank=True, verbose_name="Date de fin")
    num_kairos = models.CharField(max_length=50, null=True, blank=True, verbose_name="Numéro Kairos")
    num_offre = models.CharField(max_length=50, null=True, blank=True, verbose_name="Numéro de l'offre")
    num_produit = models.CharField(max_length=50, null=True, blank=True, verbose_name="Numéro du produit")

    # Gestion des places et inscriptions
    prevus_crif = models.PositiveIntegerField(default=0, verbose_name="Places prévues CRIF")
    prevus_mp = models.PositiveIntegerField(default=0, verbose_name="Places prévues MP")
    inscrits_crif = models.PositiveIntegerField(default=0, verbose_name="Inscrits CRIF")
    inscrits_mp = models.PositiveIntegerField(default=0, verbose_name="Inscrits MP")

    # Informations supplémentaires
    assistante = models.CharField(max_length=255, null=True, blank=True, verbose_name="Assistante")
    cap = models.PositiveIntegerField(null=True, blank=True, verbose_name="Capacité maximale")
    convocation_envoie = models.BooleanField(default=False, verbose_name="Convocation envoyée")
    entresformation = models.PositiveIntegerField(default=0, verbose_name="Entrées en formation")

    # Statistiques de recrutement
    nombre_candidats = models.PositiveIntegerField(default=0, verbose_name="Nombre de candidats")
    nombre_entretiens = models.PositiveIntegerField(default=0, verbose_name="Nombre d'entretiens")

    # Nombre d'événements liés
    nombre_evenements = models.PositiveIntegerField(default=0, verbose_name="Nombre d'événements")

    # Commentaires et logs
    dernier_commentaire = models.TextField(null=True, blank=True, verbose_name="Dernier commentaire")

    # Relation avec les partenaires
    partenaires = models.ManyToManyField(Partenaire, related_name="formations", verbose_name="Partenaires", blank=True)

    # Créateur de la formation
    utilisateur = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,related_name="formations_creees",verbose_name="Créé par" )

    # Manager personnalisé
    objects = FormationManager()

    def save(self, *args, **kwargs):
        is_new = self.pk is None
        old_instance = None

        if not is_new:
            try:
                old_instance = Formation.objects.get(pk=self.pk)
            except Formation.DoesNotExist:
                pass

        super().save(*args, **kwargs)  # Sauvegarde classique

        if old_instance:
            fields_to_track = [
                'nom', 'centre', 'type_offre', 'statut',
                'start_date', 'end_date', 'num_kairos',
                'num_offre', 'num_produit', 'prevus_crif',
                'prevus_mp', 'inscrits_crif', 'inscrits_mp',
                'assistante', 'cap', 'convocation_envoie',
                'entresformation', 'nombre_candidats', 'nombre_entretiens',
                'dernier_commentaire'
            ]

            for field in fields_to_track:
                old_value = getattr(old_instance, field)
                new_value = getattr(self, field)

                if old_value != new_value:
                    HistoriqueFormation.objects.create(
                        formation=self,
                        champ_modifie=field,
                        ancienne_valeur=str(old_value),
                        nouvelle_valeur=str(new_value),
                        modifie_par=self.utilisateur  # ou `kwargs.get('user')` selon ton besoin
                    )

    ### ✅ Méthode pour sérialiser les données avant enregistrement dans JSONField
    def to_serializable_dict(self):
        """
        Retourne un dictionnaire JSON-sérialisable des valeurs de la formation,
        en convertissant les dates en chaînes de caractères.
        """
        def convert_value(value):
            if isinstance(value, (datetime.date, datetime.datetime)):
                return value.strftime('%Y-%m-%d')  # ✅ Convertit les dates en format JSON
            elif isinstance(value, models.Model):
                return str(value)  # ✅ Convertit les objets Django en string
            return value 

        return {key: convert_value(getattr(self, key)) for key in [
            "nom", "centre", "type_offre", "statut", "start_date", "end_date", "num_kairos", "num_offre", "num_produit",
            "prevus_crif", "prevus_mp", "inscrits_crif", "inscrits_mp", "assistante", "cap", "convocation_envoie",
            "entresformation", "nombre_candidats", "nombre_entretiens", "nombre_evenements", "dernier_commentaire"
        ]}

    ### ✅ Méthodes calculées (remplaçant `@property`)

    def get_total_places(self):
        """Retourne le nombre total de places prévues (CRIF + MP)."""
        return self.prevus_crif + self.prevus_mp

    def get_total_inscrits(self):
        """Retourne le nombre total d'inscrits (CRIF + MP)."""
        return self.inscrits_crif + self.inscrits_mp

    def get_places_restantes_crif(self):
        """Retourne le nombre de places restantes pour CRIF."""
        return max(0, self.prevus_crif - self.inscrits_crif)

    def get_places_restantes_mp(self):
        """Retourne le nombre de places restantes pour MP."""
        return max(0, self.prevus_mp - self.inscrits_mp)

    def get_places_disponibles(self):
        """Retourne le nombre de places encore disponibles pour la formation."""
        return max(0, self.get_total_places() - self.get_total_inscrits())

    def get_a_recruter(self):
        """Retourne le nombre de places encore disponibles pour le recrutement."""
        return self.get_places_disponibles()

    def get_taux_saturation(self):
        """Calcule le taux de saturation de la formation en fonction des inscriptions."""
        total_places = self.get_total_places()
        return (self.get_total_inscrits() / total_places) * 100 if total_places > 0 else 0

    def is_a_recruter(self):
        """Renvoie `True` si la formation a encore des places disponibles, sinon `False`."""
        return self.get_a_recruter() > 0
    

### ✅ Méthodes d'ajout d'éléments associés

# ✅ Ajout d'un commentaire en utilisant la relation inverse
    def add_commentaire(self, utilisateur, contenu):
        """
        Ajoute un commentaire à la formation via la relation inverse.
        """
        commentaire = self.commentaires.create(
            utilisateur=utilisateur,
            contenu=contenu
        )
        self.dernier_commentaire = contenu  # Mettre à jour le dernier commentaire affiché
        self.save()
        return commentaire

    # ✅ Ajout d'un événement en utilisant la relation inverse
    def add_evenement(self, type_evenement, event_date, details=None, description_autre=None):
        """
        Ajoute un événement à la formation via la relation inverse.
        """
        from .evenements import Evenement  # ✅ Import local pour éviter la relation circulaire

        if type_evenement == Evenement.AUTRE and not description_autre:
            raise ValidationError("Veuillez fournir une description pour un événement de type 'Autre'.")

        evenement = Evenement.objects.create(
            formation=self,
            type_evenement=type_evenement,
            event_date=event_date,
            details=details,
            description_autre=description_autre if type_evenement == Evenement.AUTRE else None
        )

        self.nombre_evenements += 1  # ✅ Mise à jour du compteur d'événements
        self.save()
        return evenement



    ### ✅ Autres méthodes utiles

    def get_status_color(self):
        """
        Retourne la couleur associée au statut de la formation.
        Si le statut n’a pas de couleur définie, il prend une couleur par défaut.
        """
        return self.statut.couleur if self.statut.couleur else get_default_color(self.statut.nom)
    
    def get_absolute_url(self):
        """Retourne l'URL de détail de la formation."""
        return reverse('formation-detail', kwargs={'pk': self.pk})
    
    def get_commentaires(self):
        """Retourne tous les commentaires associés à cette formation, en incluant les utilisateurs."""
        return self.commentaires.select_related("utilisateur").all()  # ✅ Optimisation SQL


    def get_evenements(self):
        """Retourne tous les événements associés à cette formation."""
        return self.evenements.all()

    def get_documents(self):
        """Retourne tous les documents associés à cette formation."""
        return self.documents.all()

    def get_partenaires(self):
        """Retourne les partenaires associés (optimisé avec prefetch)."""
        return self.partenaires.all().prefetch_related()

    def __str__(self):
        """Affiche une représentation textuelle de la formation."""
        return f"{self.nom} ({self.centre.nom if self.centre else 'Centre inconnu'})"

    class Meta:
        verbose_name = "Formation"
        verbose_name_plural = "Formations"
        ordering = ['-start_date', 'nom']
        indexes = [
            models.Index(fields=['start_date']),
            models.Index(fields=['end_date']),
            models.Index(fields=['nom']),
        ]

class HistoriqueFormation(models.Model):
    formation = models.ForeignKey('Formation', on_delete=models.CASCADE, related_name="historiques")
    utilisateur = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='historiques_utilisateur')
    action = models.CharField(max_length=100, default='modification')
    details = models.JSONField(default=dict, blank=True)
    date_modification = models.DateTimeField(default=timezone.now)
    champ_modifie = models.CharField(max_length=100, default="non_specifié" , verbose_name="Champ modifié")
    ancienne_valeur = models.TextField(null=True, blank=True)
    nouvelle_valeur = models.TextField(null=True, blank=True)
    modifie_par = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)
    commentaire = models.TextField(null=True, blank=True, verbose_name="Commentaire lié à la modification")

    class Meta:
        ordering = ['-date_modification']
        verbose_name = "Historique de modification de formation"



================================================
File: rap_app/models/models.md
================================================
from django.db import models
from django.utils.timezone import now  # Utilise Django timezone pour éviter les problèmes UTC

class BaseModel(models.Model):
    """
    Modèle de base pour tous les modèles de l'application.
    Il inclut la gestion automatique de `created_at` et `updated_at`.
    """

    created_at = models.DateTimeField(default=now, editable=False, verbose_name="Date de création")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Dernière mise à jour")

    class Meta:
        abstract = True  # Empêche Django de créer une table pour ce modèle
# models/centres.py
from django.db import models
from django.core.validators import RegexValidator
from django.urls import reverse
from .base import BaseModel


class Centre(BaseModel):
    """
    Modèle représentant un centre de formation.

    Hérite de `BaseModel` qui ajoute les champs :
    - `created_at` : Date et heure de création de l'enregistrement.
    - `updated_at` : Date et heure de la dernière modification.

    Champs spécifiques :
    - `nom` : Nom du centre de formation (obligatoire et unique).
    - `code_postal` : Code postal du centre (optionnel).
      * Doit contenir exactement 5 chiffres (validation par regex).
    
    Méthodes :
    - `__str__` : Retourne le nom du centre.
    - `get_absolute_url` : Retourne l'URL du détail du centre.
    - `full_address` : Retourne l'adresse complète (utile pour affichage futur).

    Options du modèle :
    - `verbose_name` : Nom affiché au singulier dans l'interface d'administration.
    - `verbose_name_plural` : Nom affiché au pluriel dans l'interface d'administration.
    - `ordering` : Trie les centres par nom par défaut.
    - `indexes` : Ajoute des index sur `nom` et `code_postal` pour optimiser les recherches.
    """

    nom = models.CharField(
        max_length=255,
        unique=True,  # 🔹 Garantit qu'un centre a un nom unique
        verbose_name="Nom du centre"
    )

    code_postal = models.CharField(
        max_length=5,  # 🔹 Limité à 5 caractères au lieu de 10
        null=True,
        blank=True,
        verbose_name="Code postal",
        validators=[
            RegexValidator(
                regex=r'^\d{5}$',
                message="Le code postal doit contenir exactement 5 chiffres"
            )
        ]
    )

    def __str__(self):
        """Retourne le nom du centre pour une meilleure lisibilité."""
        return self.nom

    def get_absolute_url(self):
        """
        Retourne l'URL du détail du centre.
        Utile pour les vues génériques et les redirections après une création/modification.
        """
        return reverse('centre-detail', kwargs={'pk': self.pk})

    def full_address(self):
        """
        Retourne une version complète de l'adresse (utile si d'autres champs d'adresse sont ajoutés).
        """
        address = self.nom
        if self.code_postal:
            address += f" ({self.code_postal})"
        return address

    class Meta:
        verbose_name = "Centre"
        verbose_name_plural = "Centres"
        ordering = ['nom']
        indexes = [
            models.Index(fields=['nom']),  # 🔹 Index pour optimiser les recherches par nom
            models.Index(fields=['code_postal']),  # 🔹 Index pour les recherches par code postal
        ]
from django.db import models
from django.db.models import Q

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .base import BaseModel
from .formations import Formation
from django.contrib.auth import get_user_model
User = get_user_model()


class Commentaire(BaseModel):
    """
    Modèle représentant un commentaire associé à une formation.
    """

    formation = models.ForeignKey(Formation, on_delete=models.CASCADE, related_name="commentaires", verbose_name="Formation")
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="commentaires", verbose_name="Utilisateur associé")
    contenu = models.TextField(verbose_name="Contenu du commentaire")
    saturation = models.PositiveIntegerField(null=True, blank=True,verbose_name="Niveau de saturation (%)")

    def __str__(self):
        """
        Retourne une représentation lisible du commentaire.
        """
        return f"Commentaire de {self.utilisateur} sur {self.formation.nom} ({self.created_at.strftime('%d/%m/%Y')})"

    class Meta:
        verbose_name = "Commentaire"
        verbose_name_plural = "Commentaires"
        ordering = ['formation', '-created_at']
        indexes = [
            models.Index(fields=['created_at']),
            models.Index(fields=['formation']),
        ]


    @classmethod
    def get_all_commentaires(cls, formation_id=None, utilisateur_id=None, search_query=None, order_by="-created_at"):
        """
        Récupère tous les commentaires avec options de filtres.
        """
        queryset = cls.objects.select_related('formation', 'utilisateur').order_by(order_by)

        filters = Q()
        if formation_id:
            filters &= Q(formation_id=formation_id)
        if utilisateur_id:
            filters &= Q(utilisateur_id=utilisateur_id)
        if search_query:
            filters &= Q(contenu__icontains=search_query)

        queryset = queryset.filter(filters)
        return queryset if queryset.exists() else cls.objects.none()  # ✅ Évite l'erreur avec un queryset vide




@receiver(post_save, sender=Commentaire)
def update_formation_saturation(sender, instance, **kwargs):
    """
    Met à jour la saturation et le dernier commentaire après un ajout.
    """
    if instance.formation:
        updates = {}

        if instance.saturation is not None:
            updates['saturation'] = instance.saturation

        dernier_commentaire = Commentaire.objects.filter(formation=instance.formation).order_by('-created_at').first()
        updates['dernier_commentaire'] = dernier_commentaire.contenu if dernier_commentaire else ""

        if updates:
            Formation.objects.filter(id=instance.formation.id).update(**updates)

@receiver(post_delete, sender=Commentaire)
def handle_commentaire_delete(sender, instance, **kwargs):
    """
    Met à jour la formation après la suppression d'un commentaire.
    """
    if instance.formation:
        dernier_commentaire = Commentaire.objects.filter(formation=instance.formation).order_by('-created_at').first()
        Formation.objects.filter(id=instance.formation.id).update(
            dernier_commentaire=dernier_commentaire.contenu if dernier_commentaire else ""
        )
from django.db import models
from django.db.models import Q

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .base import BaseModel
from .formations import Formation
from django.contrib.auth import get_user_model
User = get_user_model()


class Commentaire(BaseModel):
    """
    Modèle représentant un commentaire associé à une formation.
    """

    formation = models.ForeignKey(Formation, on_delete=models.CASCADE, related_name="commentaires", verbose_name="Formation")
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="commentaires", verbose_name="Utilisateur associé")
    contenu = models.TextField(verbose_name="Contenu du commentaire")
    saturation = models.PositiveIntegerField(null=True, blank=True,verbose_name="Niveau de saturation (%)")

    def __str__(self):
        """
        Retourne une représentation lisible du commentaire.
        """
        return f"Commentaire de {self.utilisateur} sur {self.formation.nom} ({self.created_at.strftime('%d/%m/%Y')})"

    class Meta:
        verbose_name = "Commentaire"
        verbose_name_plural = "Commentaires"
        ordering = ['formation', '-created_at']
        indexes = [
            models.Index(fields=['created_at']),
            models.Index(fields=['formation']),
        ]


    @classmethod
    def get_all_commentaires(cls, formation_id=None, utilisateur_id=None, search_query=None, order_by="-created_at"):
        """
        Récupère tous les commentaires avec options de filtres.
        """
        queryset = cls.objects.select_related('formation', 'utilisateur').order_by(order_by)

        filters = Q()
        if formation_id:
            filters &= Q(formation_id=formation_id)
        if utilisateur_id:
            filters &= Q(utilisateur_id=utilisateur_id)
        if search_query:
            filters &= Q(contenu__icontains=search_query)

        queryset = queryset.filter(filters)
        return queryset if queryset.exists() else cls.objects.none()  # ✅ Évite l'erreur avec un queryset vide




@receiver(post_save, sender=Commentaire)
def update_formation_saturation(sender, instance, **kwargs):
    """
    Met à jour la saturation et le dernier commentaire après un ajout.
    """
    if instance.formation:
        updates = {}

        if instance.saturation is not None:
            updates['saturation'] = instance.saturation

        dernier_commentaire = Commentaire.objects.filter(formation=instance.formation).order_by('-created_at').first()
        updates['dernier_commentaire'] = dernier_commentaire.contenu if dernier_commentaire else ""

        if updates:
            Formation.objects.filter(id=instance.formation.id).update(**updates)

@receiver(post_delete, sender=Commentaire)
def handle_commentaire_delete(sender, instance, **kwargs):
    """
    Met à jour la formation après la suppression d'un commentaire.
    """
    if instance.formation:
        dernier_commentaire = Commentaire.objects.filter(formation=instance.formation).order_by('-created_at').first()
        Formation.objects.filter(id=instance.formation.id).update(
            dernier_commentaire=dernier_commentaire.contenu if dernier_commentaire else ""
        )
from django.db import models
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver
import os
from django.conf import settings
from django.core.exceptions import ValidationError
from .base import BaseModel
from .formations import Formation, User


class Document(BaseModel):
    """
    Modèle représentant un document associé à une formation.
    Permet de stocker et gérer différents types de documents (PDF, images, contrats...).
    """

    # Types de documents possibles
    PDF = 'pdf'
    IMAGE = 'image'
    CONTRAT = 'contrat'
    AUTRE = 'autre'

    TYPE_DOCUMENT_CHOICES = [
        (PDF, 'PDF'),
        (IMAGE, 'Image'),
        (CONTRAT, 'Contrat signé'),
        (AUTRE, 'Autre'),
    ]

    formation = models.ForeignKey(Formation, on_delete=models.CASCADE, related_name="documents",  verbose_name="Formation associée")
    nom_fichier = models.CharField(max_length=255, verbose_name="Nom du fichier",db_index=True)
    fichier = models.FileField(upload_to='formations/documents/', verbose_name="Fichier")
    source = models.TextField(null=True, blank=True, verbose_name="Source du document")
    type_document = models.CharField( max_length=20, choices=TYPE_DOCUMENT_CHOICES, default=AUTRE,verbose_name="Type de document")
    taille_fichier = models.PositiveIntegerField(null=True,blank=True, verbose_name="Taille du fichier (Ko)")
    utilisateur = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        """
        Retourne une représentation lisible du document avec un nom tronqué si nécessaire.
        Exemple : "Guide utilisateur.pdf"
        """
        nom_tronque = self.nom_fichier[:50] + ('...' if len(self.nom_fichier) > 50 else '')
        return f"{nom_tronque} ({self.get_type_document_display()})"
    
    def clean(self):
        """Validation personnalisée pour vérifier la correspondance entre type et extension."""
        super().clean()
        if self.fichier and self.type_document:
            validate_file_extension(self.fichier, self.type_document)

    def save(self, *args, **kwargs):
        """
        - Vérifie les règles de validation avant la sauvegarde (`full_clean()`).
        - Met à jour automatiquement la taille du fichier en Ko.
        """
        self.full_clean()  # Exécute la validation avant la sauvegarde.

        if self.fichier and hasattr(self.fichier, 'size'):
            self.taille_fichier = max(1, self.fichier.size // 1024)  # Au moins 1 Ko pour éviter les zeros
        
        super().save(*args, **kwargs)
    class Meta:
        verbose_name = "Document"
        verbose_name_plural = "Documents"
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['nom_fichier']),  # Index pour la recherche rapide
        ]


### 🚀 Validation : Empêcher l'upload d'un fichier invalide
def validate_file_extension(value, type_doc=None):
    """
    Vérifie que le fichier téléchargé correspond bien au type déclaré.
    Le paramètre type_doc peut être passé à la validation.
    """
    ext = os.path.splitext(value.name)[1].lower()
    valid_extensions = {
        'pdf': ['.pdf'],
        'image': ['.jpg', '.jpeg', '.png', '.gif'],
        'contrat': ['.pdf', '.doc', '.docx'],
        'autre': []  # Autorise tout pour "Autre"
    }
    
    # Si aucun type n'est fourni ou si c'est "autre", on accepte le fichier
    if not type_doc or type_doc == Document.AUTRE:
        return
        
    # Vérifie si l'extension correspond au type fourni
    if ext not in valid_extensions.get(type_doc, []):
        raise ValidationError(f"Le fichier {value.name} ne correspond pas au type {dict(Document.TYPE_DOCUMENT_CHOICES).get(type_doc, type_doc)}.")

### 🚀 Suppression automatique des anciens fichiers avant mise à jour
@receiver(pre_save, sender=Document)
def supprimer_fichier_ancien(sender, instance, **kwargs):
    """
    Supprime l'ancien fichier si un nouveau fichier est uploadé pour éviter l'accumulation de fichiers inutiles.
    """
    if instance.pk:
        ancien_document = Document.objects.get(pk=instance.pk)
        if ancien_document.fichier and ancien_document.fichier != instance.fichier:
            ancien_fichier_path = os.path.join(settings.MEDIA_ROOT, ancien_document.fichier.name)
            if os.path.exists(ancien_fichier_path):
                os.remove(ancien_fichier_path)


### 🚀 Suppression automatique du fichier après suppression d'un Document
@receiver(post_delete, sender=Document)
def supprimer_fichier_apres_suppression(sender, instance, **kwargs):
    """
    Supprime le fichier du stockage lorsque l'objet `Document` est supprimé.
    Évite les erreurs si le fichier a déjà été supprimé.
    """
    if instance.fichier:
        fichier_path = os.path.join(settings.MEDIA_ROOT, instance.fichier.name)
        try:
            if os.path.exists(fichier_path):
                os.remove(fichier_path)
        except Exception as e:
            print(f"Erreur lors de la suppression du fichier {fichier_path}: {e}")
from django.db import models
from django.core.exceptions import ValidationError
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.db.models import F
from .base import BaseModel
from .formations import Formation

class Evenement(BaseModel):
    """
    Modèle représentant un événement lié à une formation.
    """

    # Constantes pour les types d'événements
    INFO_PRESENTIEL = 'info_collective_presentiel'
    INFO_DISTANCIEL = 'info_collective_distanciel'
    JOB_DATING = 'job_dating'
    EVENEMENT_EMPLOI = 'evenement_emploi'
    FORUM = 'forum'
    JPO = 'jpo'
    AUTRE = 'autre'

    TYPE_EVENEMENT_CHOICES = [
        (INFO_PRESENTIEL, 'Information collective présentiel'),
        (INFO_DISTANCIEL, 'Information collective distanciel'),
        (JOB_DATING, 'Job dating'),
        (EVENEMENT_EMPLOI, 'Événement emploi'),
        (FORUM, 'Forum'),
        (JPO, 'Journée Portes Ouvertes (JPO)'),
        (AUTRE, 'Autre'),
    ]

    formation = models.ForeignKey(Formation, on_delete=models.CASCADE, null=True, blank=True,  related_name="evenements",verbose_name="Formation associée")
    type_evenement = models.CharField(max_length=100, choices=TYPE_EVENEMENT_CHOICES, verbose_name="Type d'événement",db_index=True)
    details = models.TextField(null=True,  blank=True, verbose_name="Détails de l'événement")
    event_date = models.DateField(null=True, blank=True, verbose_name="Date de l'événement")
    description_autre = models.CharField(max_length=255,  null=True,  blank=True,  verbose_name="Description pour 'Autre' événement")

    def clean(self):
        """
        Validation personnalisée :
        - Si l'événement est de type "Autre", la description doit être remplie.
        """
        if self.type_evenement == self.AUTRE and not self.description_autre:
            raise ValidationError({
                'description_autre': "Veuillez fournir une description pour l'événement de type 'Autre'."
            })

    def save(self, *args, **kwargs):
        """
        Personnalisation de la sauvegarde :
        - Vérifie les règles de validation (`full_clean()`).
        """
        self.full_clean()  # Exécute la validation avant la sauvegarde.
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Événement"
        verbose_name_plural = "Événements"
        ordering = ['-event_date']
        indexes = [
            models.Index(fields=['event_date']),  # Optimisation des recherches par date.
            models.Index(fields=['type_evenement']),  # Ajout d'un index sur le type d'événement.
        ]

    def __str__(self):
        """
        Retourne une représentation lisible de l'événement.
        Exemple : "Job dating - 2025-03-10"
        """
        type_event = self.get_type_evenement_display() if self.type_evenement else "Type inconnu"
        return f"{type_event} - {self.event_date.strftime('%d/%m/%Y')}" if self.event_date else f"{type_event} - Date inconnue"



# 🚀 Signaux pour mettre à jour `nombre_evenements` dans `Formation`
@receiver(post_save, sender=Evenement)
def update_nombre_evenements(sender, instance, **kwargs):
    """Met à jour le nombre d'événements dans la formation associée."""
    if instance.formation:
        # Recalcule le nombre total d'événements à chaque modification
        count = Evenement.objects.filter(formation=instance.formation).count()
        Formation.objects.filter(id=instance.formation.id).update(nombre_evenements=count)
        # Rafraîchir la formation
        if hasattr(instance, 'formation'):
            instance.formation.refresh_from_db()

@receiver(post_delete, sender=Evenement)
def update_nombre_evenements_after_delete(sender, instance, **kwargs):
    """Met à jour le nombre d'événements après suppression."""
    if hasattr(instance, 'formation') and instance.formation:
        # Recalcule le nombre après suppression
        count = Evenement.objects.filter(formation=instance.formation).count()
        Formation.objects.filter(id=instance.formation.id).update(nombre_evenements=count)import datetime
from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils import timezone
from jsonschema import ValidationError

from .partenaires import Partenaire

from .centres import Centre
from .types_offre import TypeOffre
from .base import BaseModel
from .statut import Statut, get_default_color

User = get_user_model()  # Récupère le modèle User


class FormationManager(models.Manager):
    """
    Manager personnalisé pour optimiser les requêtes sur les formations.
    Ajoute des méthodes pour filtrer les formations selon leur état.
    """
        
    def formations_actives(self):
        """
        Retourne uniquement les formations actives :
        - La date de début est passée (<= aujourd’hui)
        - La date de fin est future ou aujourd’hui (>= aujourd’hui)
        """
        today = timezone.now().date()
        return self.filter(start_date__lte=today, end_date__gte=today)

    def formations_a_venir(self):
        """Retourne uniquement les formations qui commencent dans le futur."""
        return self.filter(start_date__gt=timezone.now().date())

    def formations_terminees(self):
        """Retourne uniquement les formations terminées (date de fin dépassée)."""
        return self.filter(end_date__lt=timezone.now().date())

    def formations_a_recruter(self):
        """Retourne les formations qui ont encore des places disponibles."""
        return self.annotate(
            total_places=models.F('prevus_crif') + models.F('prevus_mp'),
            total_inscrits=models.F('inscrits_crif') + models.F('inscrits_mp')
        ).filter(total_places__gt=models.F('total_inscrits'))

    def formations_toutes(self):
        """Retourne **toutes** les formations, sans filtre."""
        return self.all()

    def trier_par(self, champ_tri):
        """Trie les formations selon un champ donné, si autorisé."""
        champs_autorises = [
            "centre", "-centre",
            "statut", "-statut",
            "type_offre", "-type_offre",
            "start_date", "-start_date",
            "end_date", "-end_date"
        ]
        return self.get_queryset().order_by(champ_tri) if champ_tri in champs_autorises else self.get_queryset()


class Formation(BaseModel):
    """
    Modèle représentant une formation.
    """

    # Informations générales
    nom = models.CharField(max_length=255, verbose_name="Nom de la formation")
    centre = models.ForeignKey(Centre, on_delete=models.CASCADE, related_name='formations', verbose_name="Centre de formation")
    type_offre = models.ForeignKey(TypeOffre, on_delete=models.CASCADE, related_name="formations", verbose_name="Type d'offre")
    statut = models.ForeignKey(Statut, on_delete=models.CASCADE, related_name="formations", verbose_name="Statut de la formation")

    # Dates et identifiants
    start_date = models.DateField(null=True, blank=True, verbose_name="Date de début")
    end_date = models.DateField(null=True, blank=True, verbose_name="Date de fin")
    num_kairos = models.CharField(max_length=50, null=True, blank=True, verbose_name="Numéro Kairos")
    num_offre = models.CharField(max_length=50, null=True, blank=True, verbose_name="Numéro de l'offre")
    num_produit = models.CharField(max_length=50, null=True, blank=True, verbose_name="Numéro du produit")

    # Gestion des places et inscriptions
    prevus_crif = models.PositiveIntegerField(default=0, verbose_name="Places prévues CRIF")
    prevus_mp = models.PositiveIntegerField(default=0, verbose_name="Places prévues MP")
    inscrits_crif = models.PositiveIntegerField(default=0, verbose_name="Inscrits CRIF")
    inscrits_mp = models.PositiveIntegerField(default=0, verbose_name="Inscrits MP")

    # Informations supplémentaires
    assistante = models.CharField(max_length=255, null=True, blank=True, verbose_name="Assistante")
    cap = models.PositiveIntegerField(null=True, blank=True, verbose_name="Capacité maximale")
    convocation_envoie = models.BooleanField(default=False, verbose_name="Convocation envoyée")
    entresformation = models.PositiveIntegerField(default=0, verbose_name="Entrées en formation")

    # Statistiques de recrutement
    nombre_candidats = models.PositiveIntegerField(default=0, verbose_name="Nombre de candidats")
    nombre_entretiens = models.PositiveIntegerField(default=0, verbose_name="Nombre d'entretiens")

    # Nombre d'événements liés
    nombre_evenements = models.PositiveIntegerField(default=0, verbose_name="Nombre d'événements")

    # Commentaires et logs
    dernier_commentaire = models.TextField(null=True, blank=True, verbose_name="Dernier commentaire")

    # Relation avec les partenaires
    partenaires = models.ManyToManyField(Partenaire, related_name="formations", verbose_name="Partenaires", blank=True)

    # Créateur de la formation
    utilisateur = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,related_name="formations_creees",verbose_name="Créé par" )

    # Manager personnalisé
    objects = FormationManager()

    def save(self, *args, **kwargs):
        is_new = self.pk is None
        old_instance = None

        if not is_new:
            try:
                old_instance = Formation.objects.get(pk=self.pk)
            except Formation.DoesNotExist:
                pass

        super().save(*args, **kwargs)  # Sauvegarde classique

        if old_instance:
            fields_to_track = [
                'nom', 'centre', 'type_offre', 'statut',
                'start_date', 'end_date', 'num_kairos',
                'num_offre', 'num_produit', 'prevus_crif',
                'prevus_mp', 'inscrits_crif', 'inscrits_mp',
                'assistante', 'cap', 'convocation_envoie',
                'entresformation', 'nombre_candidats', 'nombre_entretiens',
                'dernier_commentaire'
            ]

            for field in fields_to_track:
                old_value = getattr(old_instance, field)
                new_value = getattr(self, field)

                if old_value != new_value:
                    HistoriqueFormation.objects.create(
                        formation=self,
                        champ_modifie=field,
                        ancienne_valeur=str(old_value),
                        nouvelle_valeur=str(new_value),
                        modifie_par=self.utilisateur  # ou `kwargs.get('user')` selon ton besoin
                    )

    ### ✅ Méthode pour sérialiser les données avant enregistrement dans JSONField
    def to_serializable_dict(self):
        """
        Retourne un dictionnaire JSON-sérialisable des valeurs de la formation,
        en convertissant les dates en chaînes de caractères.
        """
        def convert_value(value):
            if isinstance(value, (datetime.date, datetime.datetime)):
                return value.strftime('%Y-%m-%d')  # ✅ Convertit les dates en format JSON
            elif isinstance(value, models.Model):
                return str(value)  # ✅ Convertit les objets Django en string
            return value 

        return {key: convert_value(getattr(self, key)) for key in [
            "nom", "centre", "type_offre", "statut", "start_date", "end_date", "num_kairos", "num_offre", "num_produit",
            "prevus_crif", "prevus_mp", "inscrits_crif", "inscrits_mp", "assistante", "cap", "convocation_envoie",
            "entresformation", "nombre_candidats", "nombre_entretiens", "nombre_evenements", "dernier_commentaire"
        ]}

    ### ✅ Méthodes calculées (remplaçant `@property`)

    def get_total_places(self):
        """Retourne le nombre total de places prévues (CRIF + MP)."""
        return self.prevus_crif + self.prevus_mp

    def get_total_inscrits(self):
        """Retourne le nombre total d'inscrits (CRIF + MP)."""
        return self.inscrits_crif + self.inscrits_mp

    def get_places_restantes_crif(self):
        """Retourne le nombre de places restantes pour CRIF."""
        return max(0, self.prevus_crif - self.inscrits_crif)

    def get_places_restantes_mp(self):
        """Retourne le nombre de places restantes pour MP."""
        return max(0, self.prevus_mp - self.inscrits_mp)

    def get_places_disponibles(self):
        """Retourne le nombre de places encore disponibles pour la formation."""
        return max(0, self.get_total_places() - self.get_total_inscrits())

    def get_a_recruter(self):
        """Retourne le nombre de places encore disponibles pour le recrutement."""
        return self.get_places_disponibles()

    def get_taux_saturation(self):
        """Calcule le taux de saturation de la formation en fonction des inscriptions."""
        total_places = self.get_total_places()
        return (self.get_total_inscrits() / total_places) * 100 if total_places > 0 else 0

    def is_a_recruter(self):
        """Renvoie `True` si la formation a encore des places disponibles, sinon `False`."""
        return self.get_a_recruter() > 0
    

### ✅ Méthodes d'ajout d'éléments associés

# ✅ Ajout d'un commentaire en utilisant la relation inverse
    def add_commentaire(self, utilisateur, contenu):
        """
        Ajoute un commentaire à la formation via la relation inverse.
        """
        commentaire = self.commentaires.create(
            utilisateur=utilisateur,
            contenu=contenu
        )
        self.dernier_commentaire = contenu  # Mettre à jour le dernier commentaire affiché
        self.save()
        return commentaire

    # ✅ Ajout d'un événement en utilisant la relation inverse
    def add_evenement(self, type_evenement, event_date, details=None, description_autre=None):
        """
        Ajoute un événement à la formation via la relation inverse.
        """
        from .evenements import Evenement  # ✅ Import local pour éviter la relation circulaire

        if type_evenement == Evenement.AUTRE and not description_autre:
            raise ValidationError("Veuillez fournir une description pour un événement de type 'Autre'.")

        evenement = Evenement.objects.create(
            formation=self,
            type_evenement=type_evenement,
            event_date=event_date,
            details=details,
            description_autre=description_autre if type_evenement == Evenement.AUTRE else None
        )

        self.nombre_evenements += 1  # ✅ Mise à jour du compteur d'événements
        self.save()
        return evenement



    ### ✅ Autres méthodes utiles

    def get_status_color(self):
        """
        Retourne la couleur associée au statut de la formation.
        Si le statut n’a pas de couleur définie, il prend une couleur par défaut.
        """
        return self.statut.couleur if self.statut.couleur else get_default_color(self.statut.nom)
    
    def get_absolute_url(self):
        """Retourne l'URL de détail de la formation."""
        return reverse('formation-detail', kwargs={'pk': self.pk})
    
    def get_commentaires(self):
        """Retourne tous les commentaires associés à cette formation, en incluant les utilisateurs."""
        return self.commentaires.select_related("utilisateur").all()  # ✅ Optimisation SQL


    def get_evenements(self):
        """Retourne tous les événements associés à cette formation."""
        return self.evenements.all()

    def get_documents(self):
        """Retourne tous les documents associés à cette formation."""
        return self.documents.all()

    def get_partenaires(self):
        """Retourne les partenaires associées."""
        return self.partenaires.all()

    def __str__(self):
        """Affiche une représentation textuelle de la formation."""
        return f"{self.nom} ({self.centre.nom if self.centre else 'Centre inconnu'})"

    class Meta:
        verbose_name = "Formation"
        verbose_name_plural = "Formations"
        ordering = ['-start_date', 'nom']
        indexes = [
            models.Index(fields=['start_date']),
            models.Index(fields=['end_date']),
            models.Index(fields=['nom']),
        ]

class HistoriqueFormation(models.Model):
    formation = models.ForeignKey('Formation', on_delete=models.CASCADE, related_name="historiques")
    utilisateur = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='historiques_utilisateur')
    action = models.CharField(max_length=100, default='modification')
    details = models.JSONField(default=dict, blank=True)
    date_modification = models.DateTimeField(default=timezone.now)
    champ_modifie = models.CharField(max_length=100, default="non_specifié" , verbose_name="Champ modifié")
    ancienne_valeur = models.TextField(null=True, blank=True)
    nouvelle_valeur = models.TextField(null=True, blank=True)
    modifie_par = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)
    commentaire = models.TextField(null=True, blank=True, verbose_name="Commentaire lié à la modification")

    class Meta:
        ordering = ['-date_modification']
        verbose_name = "Historique de modification de formation"
from django.db import models
from .base import BaseModel

class Partenaire(BaseModel):
    """
    Modèle représentant une partenaire.

    Ajout d'une relation avec `Formation` pour que les partenaires puissent être utilisées comme ressources.
    """

    nom = models.CharField(max_length=255, verbose_name="Nom du partenaire", unique=True )
    secteur_activite = models.CharField(max_length=255, verbose_name="Secteur d'activité",blank=True,null=True)
    contact_nom = models.CharField(max_length=255,verbose_name="Nom du contact",blank=True,null=True)
    contact_poste = models.CharField(max_length=255,verbose_name="Poste du contact",blank=True,null=True)
    contact_telephone = models.CharField(max_length=20, verbose_name="Téléphone du contact", blank=True, null=True)
    contact_email = models.EmailField(verbose_name="Email du contact", blank=True, null=True)
    description = models.TextField(verbose_name="Description de la relation", blank=True, null=True)

    # Manager par défaut (si PartenaireManager est supprimé)
    objects = models.Manager()

    def __str__(self):
        """Représentation lisible du partenaire."""
        return self.nom

    class Meta:
        verbose_name = "Partenaire"
        verbose_name_plural = "Partenaires"
        ordering = ['nom']
        indexes = [
            models.Index(fields=['nom']),  # Index pour optimiser la recherche par nom.
        ]
from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

from ..models.formations import Formation
from .company import Company

# ✅ Statuts possibles pour une prospection
PROSPECTION_STATUS_CHOICES = [
    ('a_faire', 'À faire'),
    ('en_cours', 'En cours'),
    ('a_relancer', 'À relancer'),
    ('acceptee', 'Acceptée'),
    ('refusee', 'Refusée'),
    ('annulee', 'Annulée'),
    ('Non renséigné', 'Non renséigné'),

]

# ✅ Objectifs de prospection
PROSPECTION_OBJECTIF_CHOICES = [
    ('prise_contact', 'Prise de contact'),
    ('rendez_vous', 'Obtenir un rendez-vous'),
    ('presentation_offre', 'Présentation d’une offre'),
    ('contrat', 'Signer un contrat'),
    ('partenariat', 'Établir un partenariat'),
    ('autre', 'Autre'),
]

# ✅ Motifs pour lesquels on fait la prospection
PROSPECTION_MOTIF_CHOICES = [
    ('POEI', 'POEI'),
    ('Apprentissage', 'Apprentissage'),
    ('VAE', 'VAE'),
    ('partenariat', 'Établir un partenariat'),
    ('autre', 'Autre'),
]

# ===============================
# 🔵 Modèle principal : Prospection
# ===============================
class Prospection(models.Model):
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE,
        related_name="prospections",
        verbose_name="Entreprise"
    )
    formation = models.ForeignKey(
        Formation, on_delete=models.CASCADE,
        null=True, blank=True,
        related_name="prospections",
        verbose_name="Formation en lien"
    )
    date_prospection = models.DateTimeField(
        default=timezone.now,
        verbose_name="Date de la prospection"
    )
    motif = models.CharField(
        max_length=30,
        choices=PROSPECTION_MOTIF_CHOICES,
        default='prise_contact',
        verbose_name="Motif de la prospection"
    )
    statut = models.CharField(
        max_length=20,
        choices=PROSPECTION_STATUS_CHOICES,
        default='a_faire',
        verbose_name="Statut de la prospection"
    )
    objectif = models.CharField(
        max_length=30,
        choices=PROSPECTION_OBJECTIF_CHOICES,
        default='prise_contact',
        verbose_name="Objectif de la prospection"
    )
    commentaire = models.TextField(
        blank=True, null=True,
        verbose_name="Commentaires de la prospection"
    )
    responsable = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_NULL,
        null=True, blank=True,
        verbose_name="Responsable de la prospection"
    )

    class Meta:
        verbose_name = "Suivi de la prospection"
        verbose_name_plural = "Suivis des prospections"
        ordering = ['-date_prospection']

    def __str__(self):
        return f"{self.company.name} - {self.formation.nom if self.formation else 'Sans formation'} - {self.get_statut_display()} - {self.get_objectif_display()}"

    # 🔁 Méthode save() personnalisée pour historiser les changements
    def save(self, *args, **kwargs):
        is_new = self.pk is None
        old_prospection = None

        # ⚠️ Si la prospection existe déjà, on récupère l'ancienne version pour détecter les changements
        if not is_new:
            try:
                old_prospection = Prospection.objects.get(pk=self.pk)
            except Prospection.DoesNotExist:
                pass

        # 💾 On sauvegarde d'abord la prospection
        super().save(*args, **kwargs)

        # 🕓 Ensuite, on vérifie s'il y a des changements à historiser
        if old_prospection:
            changement_statut = old_prospection.statut != self.statut
            changement_objectif = old_prospection.objectif != self.objectif
            changement_commentaire = old_prospection.commentaire != self.commentaire

            if changement_statut or changement_objectif or changement_commentaire:
                # 📚 Création d'un enregistrement d'historique
                HistoriqueProspection.objects.create(
                    prospection=self,
                    ancien_statut=old_prospection.statut,
                    nouveau_statut=self.statut,
                    modifie_par=self.responsable,
                    commentaire=self.commentaire or "",
                    resultat=(
                        f"Objectif modifié : {old_prospection.objectif} → {self.objectif}"
                        if changement_objectif else ""
                    ),
                    prochain_contact=timezone.now().date() + timezone.timedelta(days=7),  # ⏳ J+7 pour relancer
                )

# ===============================
# 🔵 Historique des changements
# ===============================
class HistoriqueProspection(models.Model):
    prospection = models.ForeignKey(
        Prospection, on_delete=models.CASCADE,
        related_name="historiques"
    )
    date_modification = models.DateTimeField(auto_now_add=True)
    ancien_statut = models.CharField(max_length=20, choices=PROSPECTION_STATUS_CHOICES)
    nouveau_statut = models.CharField(max_length=20, choices=PROSPECTION_STATUS_CHOICES)
    commentaire = models.TextField(null=True, blank=True)
    modifie_par = models.ForeignKey(
        get_user_model(), on_delete=models.SET_NULL,
        null=True
    )
    prochain_contact = models.DateField(
        null=True, blank=True,
        verbose_name="Date de relance"
    )
    resultat = models.TextField(
        null=True, blank=True,
        verbose_name="Résultat ou retour de la prospection"
    )
    moyen_contact = models.CharField(
        max_length=50,
        choices=[('email', 'Email'), ('telephone', 'Téléphone'), ('visite', 'Visite'), ('réseaux', 'Réseaux sociaux')],
        null=True, blank=True,
        verbose_name="Moyen de contact"
    )

    class Meta:
        ordering = ['-date_modification']
        verbose_name = "Historique de prospection"

    def __str__(self):
        return f"{self.date_modification} - {self.prospection.company.name} - {self.nouveau_statut}"
# models/rapports.py
from django.db import models
from django.utils import timezone
from .base import BaseModel

class Rapport(BaseModel):
    """
    Modèle représentant un rapport généré par le système.
    Les rapports peuvent être générés automatiquement ou manuellement.
    """
    TYPE_OCCUPATION = 'occupation'
    TYPE_CENTRE = 'centre'
    TYPE_STATUT = 'statut'
    TYPE_EVENEMENT = 'evenement'
    TYPE_RECRUTEMENT = 'recrutement'
    TYPE_PARTENAIRE = 'partenaire'
    TYPE_REPARTITION = 'repartition'
    TYPE_PERIODIQUE = 'periodique'
    TYPE_ANNUEL = 'annuel'
    TYPE_UTILISATEUR = 'utilisateur'
    
    TYPE_CHOICES = [
        (TYPE_OCCUPATION, 'Rapport d\'occupation des formations'),
        (TYPE_CENTRE, 'Rapport de performance par centre'),
        (TYPE_STATUT, 'Rapport de suivi des statuts'),
        (TYPE_EVENEMENT, 'Rapport d\'efficacité des événements'),
        (TYPE_RECRUTEMENT, 'Rapport de suivi du recrutement'),
        (TYPE_PARTENAIRE, 'Rapport d\'activité des partenaires'),
        (TYPE_REPARTITION, 'Rapport de répartition des partenaires'),
        (TYPE_PERIODIQUE, 'Rapport périodique'),
        (TYPE_ANNUEL, 'Rapport annuel consolidé'),
        (TYPE_UTILISATEUR, 'Rapport d\'activité utilisateurs'),
    ]
    
    PERIODE_QUOTIDIEN = 'quotidien'
    PERIODE_HEBDOMADAIRE = 'hebdomadaire'
    PERIODE_MENSUEL = 'mensuel'
    PERIODE_TRIMESTRIEL = 'trimestriel'
    PERIODE_ANNUEL = 'annuel'
    PERIODE_PERSONNALISE = 'personnalise'
    
    PERIODE_CHOICES = [
        (PERIODE_QUOTIDIEN, 'Quotidien'),
        (PERIODE_HEBDOMADAIRE, 'Hebdomadaire'),
        (PERIODE_MENSUEL, 'Mensuel'),
        (PERIODE_TRIMESTRIEL, 'Trimestriel'),
        (PERIODE_ANNUEL, 'Annuel'),
        (PERIODE_PERSONNALISE, 'Période personnalisée'),
    ]
    
    FORMAT_PDF = 'pdf'
    FORMAT_EXCEL = 'excel'
    FORMAT_CSV = 'csv'
    FORMAT_HTML = 'html'
    
    FORMAT_CHOICES = [
        (FORMAT_PDF, 'PDF'),
        (FORMAT_EXCEL, 'Excel'),
        (FORMAT_CSV, 'CSV'),
        (FORMAT_HTML, 'HTML'),
    ]
    
    nom = models.CharField(max_length=255, verbose_name="Nom du rapport")
    type_rapport = models.CharField(max_length=50, choices=TYPE_CHOICES, verbose_name="Type de rapport")
    periode = models.CharField(max_length=50, choices=PERIODE_CHOICES, verbose_name="Périodicité")
    date_debut = models.DateField(verbose_name="Date de début")
    date_fin = models.DateField(verbose_name="Date de fin")
    format = models.CharField(max_length=10, choices=FORMAT_CHOICES, default=FORMAT_HTML, verbose_name="Format")
    
    # Filtres optionnels
    centre = models.ForeignKey('Centre', null=True, blank=True, on_delete=models.SET_NULL, verbose_name="Centre")
    type_offre = models.ForeignKey('TypeOffre', null=True, blank=True, on_delete=models.SET_NULL, verbose_name="Type d'offre")
    statut = models.ForeignKey('Statut', null=True, blank=True, on_delete=models.SET_NULL, verbose_name="Statut")
    
    # Données du rapport
    donnees = models.JSONField(default=dict, verbose_name="Données du rapport")
    
    # Métadonnées
    date_generation = models.DateTimeField(default=timezone.now, verbose_name="Date de génération")
    utilisateur = models.ForeignKey('auth.User', null=True, blank=True, on_delete=models.SET_NULL, verbose_name="Généré par")
    temps_generation = models.FloatField(null=True, blank=True, verbose_name="Temps de génération (s)")
    
    class Meta:
        verbose_name = "Rapport"
        verbose_name_plural = "Rapports"
        ordering = ['-date_generation']
        
    def __str__(self):
        return f"{self.nom} - {self.get_type_rapport_display()} ({self.date_debut} à {self.date_fin})"
        # models/statut.py
from django.db import models
from django.core.exceptions import ValidationError
from .base import BaseModel

def get_default_color(statut_nom):
    """
    Retourne une couleur prédéfinie selon le type de statut.
    """
    COULEURS_PREDEFINIES = {
        'non_defini': "#FFEB3B",  # 🟡 Jaune (texte noir lisible)
        'recrutement_en_cours': "#4CAF50", # Vert
        'formation_en_cours': "#2196F3",  # Bleu
        'formation_a_annuler': "#FF9800", # Orange
        'formation_a_repousser': "#FFEB3B", # Jaune
        'formation_annulee': "#F44336",   # Rouge
        'pleine': "#9C27B0",             # Violet
        'quasi_pleine': "#3F51B5",       # Indigo
        'autre': "#795548",              # Marron
    }
    return COULEURS_PREDEFINIES.get(statut_nom, "#607D8B")  # Bleu-gris par défaut

class Statut(BaseModel):
    """
    Modèle représentant les statuts des formations.

    Ce modèle définit les différents états possibles d'une formation (ex: "Recrutement en cours", 
    "Formation en cours", "Formation annulée", etc.). Il permet également d'ajouter une couleur 
    pour une meilleure visibilité et un statut personnalisé si nécessaire.

    ✅ Utilisation principale :
    - Assigner un statut à une formation.
    - Permettre l'affichage du statut sous forme colorée sur l'interface utilisateur.
    - Offrir une flexibilité avec un statut "Autre" personnalisable.
    """

    # Constantes pour les choix de statut
    NON_DEFINI = 'non_defini'
    RECRUTEMENT_EN_COURS = 'recrutement_en_cours'
    FORMATION_EN_COURS = 'formation_en_cours'
    FORMATION_A_ANNULER = 'formation_a_annuler'
    FORMATION_A_REPOUSSER = 'formation_a_repousser'
    FORMATION_ANNULEE = 'formation_annulee'
    PLEINE = 'pleine'
    QUASI_PLEINE = 'quasi_pleine'
    AUTRE = 'autre'
    
    STATUT_CHOICES = [
        (NON_DEFINI, 'Non défini'),
        (RECRUTEMENT_EN_COURS, 'Recrutement en cours'),
        (FORMATION_EN_COURS, 'Formation en cours'),
        (FORMATION_A_ANNULER, 'Formation à annuler'),
        (FORMATION_A_REPOUSSER, 'Formation à repousser'),
        (FORMATION_ANNULEE, 'Formation annulée'),
        (PLEINE, 'Pleine'),
        (QUASI_PLEINE, 'Quasi-pleine'),
        (AUTRE, 'Autre'),
    ]
    
    nom = models.CharField(
        max_length=100, 
        choices=STATUT_CHOICES, 
        verbose_name="Nom du statut"
    )
    """
    Nom du statut, avec des choix prédéfinis.
    """

    couleur = models.CharField(
        max_length=7,  # Format #RRGGBB
        verbose_name="Couleur", 
        help_text="Couleur hexadécimale (ex: #FF5733)",
        blank=True  # Permet d'assigner une couleur par défaut si vide
    )
    """
    Code couleur associé au statut.
    Exemple : `#FF0000` pour rouge, `#00FF00` pour vert.
    Si ce champ est vide, une couleur prédéfinie selon le type de statut sera attribuée.
    """

    description_autre = models.CharField(
        max_length=255, 
        blank=True, 
        null=True, 
        verbose_name="Description personnalisée"
    )
    """
    Permet de renseigner une description si le statut sélectionné est "Autre".
    Obligatoire si le statut est `AUTRE`.
    """

    def clean(self):
        """
        Validation personnalisée :
        - Si le statut est 'Autre', alors `description_autre` doit être rempli.
        """
        if self.nom == self.AUTRE and not self.description_autre:
            raise ValidationError({
                'description_autre': "Le champ 'description_autre' doit être renseigné lorsque le statut est 'autre'."
            })

    def get_nom_display(self):
        """
        Retourne le nom du statut. Si le statut est 'Autre', affiche la description à la place.
        """
        if self.nom == self.AUTRE and self.description_autre:
            return self.description_autre  # ✅ Retourne la description si le statut est "Autre"
        return dict(self.STATUT_CHOICES).get(self.nom, self.nom)  # ✅ Sinon, retourne le nom normal

    def save(self, *args, **kwargs):
        """
        Sauvegarde avec validation :
        - Assigne une couleur prédéfinie si aucune couleur n'est spécifiée.
        - Appelle `clean()` avant l'enregistrement en base de données.
        """
        if not self.couleur:
            self.couleur = get_default_color(self.nom)
        
        self.full_clean()  # Applique les validations avant l'enregistrement
        super().save(*args, **kwargs)

    def __str__(self):
        """
        Représentation textuelle du modèle dans l'admin Django et les logs.
        """
        if self.nom == self.AUTRE and self.description_autre:
            return f"{self.description_autre} - {self.couleur}"
        return f"{self.get_nom_display()} "

    class Meta:
        verbose_name = "Statut"
        verbose_name_plural = "Statuts"
        ordering = ['nom']
        # models/types_offre.py
from django.db import models
from django.core.exceptions import ValidationError
from .base import BaseModel


class TypeOffre(BaseModel):
    """
    Modèle représentant les types d'offres de formation.

    Ce modèle définit les différents types d'offres disponibles dans l'application, 
    comme CRIF, Alternance, POEC, POEI, etc. Il permet également d'ajouter un type personnalisé 
    via l'option "Autre".

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
    
    nom = models.CharField(
        max_length=100, 
        choices=TYPE_OFFRE_CHOICES, 
        default=NON_DEFINI, 
        verbose_name="Type d'offre"
    )
    """
    Nom du type d'offre, avec une liste de choix prédéfinis.
    """

    autre = models.CharField(
        max_length=255, 
        blank=True,  # Suppression de null=True pour éviter les valeurs NULL sur un CharField
        verbose_name="Autre (personnalisé)"
    )
    """
    Champ permettant de spécifier un type personnalisé si "Autre" est sélectionné.
    """
    
    couleur = models.CharField(
    max_length=7,
    default='#6c757d',  # Gris Bootstrap par défaut
    verbose_name="Couleur associée (hexadécimal)"
)
    """
    Champ permettant d'ajouter une couleur aux types d'offres.
    """
    def clean(self):
        """
        Validation personnalisée :
        - Si le type d'offre est 'Autre', alors `autre` doit être rempli.
        """
        if self.nom == self.AUTRE and not self.autre:
            raise ValidationError({
                'autre': "Le champ 'autre' doit être renseigné lorsque le type d'offre est 'autre'."
            })

    def save(self, *args, **kwargs):
        self.full_clean()
        self.assign_default_color()  # 🎨 Assigne la couleur
        super().save(*args, **kwargs)


    def __str__(self):
        """
        Représentation textuelle du modèle dans l'admin Django et les logs.
        """
        return self.autre if self.nom == self.AUTRE and self.autre else self.get_nom_display()
    
    def is_personnalise(self):
        """
        Vérifie si le type d'offre est personnalisé (Autre).
        """
        return self.nom == self.AUTRE
    
    def assign_default_color(self):
        """Assigne une couleur par défaut selon le type d'offre"""
        couleurs = {
        self.CRIF: "#4e73df",         # Bleu
        self.ALTERNANCE: "#1cc88a",   # Vert
        self.POEC: "#f6c23e",         # Jaune
        self.POEI: "#e74a3b",         # Rouge
        self.TOSA: "#6f42c1",         # Violet
        self.AUTRE: "#20c997",        # Turquoise
        self.NON_DEFINI: "#6c757d",   # Gris
    }
    # On affecte seulement si aucune couleur personnalisée
        if not self.couleur or self.couleur == "#6c757d":
            self.couleur = couleurs.get(self.nom, "#6c757d")


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
        ]  # Empêche d'avoir plusieurs fois la même valeur personnalisée 'Autre'
    def text_color(self):
        """Retourne 'black' ou 'white' selon la couleur de fond"""
        if self.couleur.lower() in ['#ffff00', '#ffeb3b']:
            return 'black'
        return 'white'
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect

class CustomLoginRequiredMixin(LoginRequiredMixin):
    """Mixin personnalisé pour gérer les utilisateurs non connectés"""
    def handle_no_permission(self):
        # Ajouter un message d'erreur
        messages.error(self.request, "Vous devez être connecté pour accéder à cette page.")
        # Rediriger vers la page de connexion
        return redirect('login')  # Remplacez 'login' par le nom de votre URL de connexion

class BaseListView(CustomLoginRequiredMixin, ListView):
    """Vue de base pour les listes avec pagination"""
    paginate_by = 20
    template_name_suffix = '_list'


class BaseDetailView(CustomLoginRequiredMixin, DetailView):
    """Vue de base pour afficher un détail"""
    template_name_suffix = '_detail'


class BaseCreateView(CustomLoginRequiredMixin, CreateView):
    """Vue de base pour créer un objet"""

    def form_valid(self, form):
        """Ajoute un message de succès après la création"""
        response = super().form_valid(form)
        messages.success(self.request, f"{self.model._meta.verbose_name} créé avec succès.")
        return response


class BaseUpdateView(CustomLoginRequiredMixin, UpdateView):
    """Vue de base pour modifier un objet"""

    def form_valid(self, form):
        """Ajoute un message de succès après la modification"""
        response = super().form_valid(form)
        messages.success(self.request, f"{self.model._meta.verbose_name} mis à jour avec succès.")
        return response


class BaseDeleteView(CustomLoginRequiredMixin, DeleteView):
    """Vue de base pour supprimer un objet"""
    success_url = reverse_lazy('dashboard')

    def delete(self, request, *args, **kwargs):
        """Ajoute un message de succès après la suppression"""
        messages.success(request, f"{self.model._meta.verbose_name} supprimé avec succès.")
        return super().delete(request, *args, **kwargs)

        from django.urls import reverse_lazy
from django.db.models import Count, Sum, F, Q
from django.utils import timezone
from django.contrib.auth.mixins import PermissionRequiredMixin

from ..models import Centre, Formation
from .base_views import BaseListView, BaseDetailView, BaseCreateView, BaseUpdateView, BaseDeleteView


class CentreListView(BaseListView):
    """Vue listant tous les centres de formation avec des statistiques"""
    model = Centre
    context_object_name = 'centres'
    template_name = 'centres/centre_list.html'  # ✅ Défini explicitement le template
    
    def get_queryset(self):
        """
        Récupère la liste des centres de formation en annotant des statistiques :
        - Nombre total de formations liées à chaque centre.
        - Nombre de formations actives (date de fin >= aujourd'hui OU sans date de fin).
        - Nombre total d'inscrits (CRIF + MP).
        """
        queryset = super().get_queryset().annotate(
            nb_formations=Count('formations'),
            nb_formations_actives=Count(
                'formations',
                filter=Q(formations__end_date__gte=timezone.now()) | Q(formations__end_date__isnull=True)
            ),
            nb_inscrits=Sum(
                F('formations__inscrits_crif') + F('formations__inscrits_mp'),
                default=0
            )
        )
        
        # 🔍 Filtrage par nom du centre
        q = self.request.GET.get('q')
        if q:
            queryset = queryset.filter(nom__icontains=q)
            
        # 🔍 Filtrage par code postal
        cp = self.request.GET.get('code_postal')
        if cp:
            queryset = queryset.filter(code_postal__startswith=cp)
            
        return queryset
    
    def get_context_data(self, **kwargs):
        """
        Ajoute des statistiques générales et les filtres appliqués au contexte de la page.
        """
        context = super().get_context_data(**kwargs)
        
        # 📊 Statistiques globales
        context['total_centres'] = Centre.objects.count()
        context['total_formations'] = Formation.objects.count()
        
        # 🔍 Filtres actuellement appliqués
        context['filters'] = {
            'q': self.request.GET.get('q', ''),
            'code_postal': self.request.GET.get('code_postal', ''),
        }
        
        return context


class CentreDetailView(BaseDetailView):
    """Vue affichant les détails d'un centre de formation"""
    model = Centre
    context_object_name = 'centre'
    template_name = 'centres/centre_detail.html'  # Vérifie que ce fichier existe

    def get_context_data(self, **kwargs):
        """Ajoute au contexte les formations associées au centre"""
        context = super().get_context_data(**kwargs)
        
        # 📌 Récupération des formations associées au centre
        formations = self.object.formations.select_related('type_offre', 'statut').order_by('-start_date')

        # 🔍 Filtrage des formations par type d'offre
        type_offre = self.request.GET.get('type_offre')
        if type_offre:
            formations = formations.filter(type_offre_id=type_offre)

        # 🔍 Filtrage des formations par statut
        statut = self.request.GET.get('statut')
        if statut:
            formations = formations.filter(statut_id=statut)

        # 📊 Extraire les choix pour le template
        type_offres = formations.values_list('type_offre__id', 'type_offre__nom').distinct()
        statuts = formations.values_list('statut__id', 'statut__nom').distinct()

        # 📊 Ajouter au contexte
        context.update({
            'formations': formations,
            'type_offres': type_offres,
            'statuts': statuts
        })

        return context



class CentreCreateView(PermissionRequiredMixin, BaseCreateView):
    """Vue permettant de créer un nouveau centre de formation"""
    model = Centre
    permission_required = 'rap_app.add_centre'
    fields = ['nom', 'code_postal']
    success_url = reverse_lazy('centre-list')
    template_name = 'centres/centre_form.html'  # ✅ Vérification du chemin correct

    
    def get_context_data(self, **kwargs):
        """
        Ajoute un titre personnalisé au contexte.
        """
        context = super().get_context_data(**kwargs)
        context['titre'] = "Ajouter un centre de formation"
        return context


class CentreUpdateView(PermissionRequiredMixin, BaseUpdateView):
    """Vue permettant de modifier un centre de formation existant"""
    model = Centre
    permission_required = 'rap_app.change_centre'
    fields = ['nom', 'code_postal']
    template_name = 'centres/centre_form.html'  # ✅ Vérification du chemin correct

    
    def get_context_data(self, **kwargs):
        """
        Ajoute un titre dynamique au contexte en fonction du centre modifié.
        """
        context = super().get_context_data(**kwargs)
        context['titre'] = f"Modifier le centre : {self.object.nom}"
        return context


class CentreDeleteView(PermissionRequiredMixin, BaseDeleteView):
    """Vue permettant de supprimer un centre de formation"""
    model = Centre
    permission_required = 'rap_app.delete_centre'
    success_url = reverse_lazy('centre-list')
    template_name = 'centres/centre_confirm_delete.html'  # ✅ Ajout du bon chemin

from django.urls import reverse_lazy
from django.db.models import Q
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views import View
from django.shortcuts import get_list_or_404
from django.contrib.auth import get_user_model
from django.views.generic import ListView
import csv
from django.http import HttpResponse
from ..models.commentaires import User

from ..models import Commentaire, Formation
from .base_views import BaseListView, BaseDetailView, BaseCreateView, BaseUpdateView, BaseDeleteView

User = get_user_model()

class CommentaireListView(BaseListView):
    """Vue listant tous les commentaires avec options de filtrage"""
    model = Commentaire
    context_object_name = 'commentaires'
    template_name = 'commentaires/commentaire_list.html'
    paginate_by = 20  # ✅ Ajout de la pagination

    def get_queryset(self):
        """
        Récupère la liste des commentaires avec possibilité de filtrage par :
        - Formation associée
        - Utilisateur
        - Contenu (recherche textuelle)
        """
        queryset = super().get_queryset().select_related('formation', 'utilisateur')

        # 🔍 Filtrage dynamique
        formation_id = self.request.GET.get('formation')
        utilisateur_id = self.request.GET.get('utilisateur')
        search_query = self.request.GET.get('q')

        if formation_id:
            queryset = queryset.filter(formation_id=formation_id)

        if utilisateur_id:
            queryset = queryset.filter(utilisateur_id=utilisateur_id)

        if search_query:
            queryset = queryset.filter(contenu__icontains=search_query)

        print(f"DEBUG: {queryset.count()} commentaires trouvés")  # ✅ Debugging

        return queryset  # ✅ Ajout du return pour éviter une erreur 500

    def get_context_data(self, **kwargs):
        """Ajoute les options de filtre au contexte pour le template"""
        context = super().get_context_data(**kwargs)

        # Ajout des filtres et options de filtrage
        context['filters'] = {
            'formation': self.request.GET.get('formation', ''),
            'utilisateur': self.request.GET.get('utilisateur', ''),
            'q': self.request.GET.get('q', ''),
        }

        # Liste des formations et utilisateurs pour les filtres
        context['formations'] = Formation.objects.all()
        context['utilisateurs'] = User.objects.all()  # ✅ Ajout de la liste des utilisateurs

        return context



class CommentaireDetailView(BaseDetailView):
    """Vue affichant les détails d'un commentaire"""
    model = Commentaire
    context_object_name = 'commentaire'
    template_name = 'commentaires/commentaire_detail.html'


class CommentaireCreateView(BaseCreateView):
    """Vue permettant de créer un nouveau commentaire"""
    model = Commentaire
    fields = ['formation', 'contenu', 'saturation']
    template_name = 'commentaires/commentaire_form.html'
    
    def get_initial(self):
        """Pré-remplit le formulaire avec la formation si spécifiée dans l'URL"""
        initial = super().get_initial()
        formation_id = self.request.GET.get('formation')
        if formation_id:
            initial['formation'] = formation_id
        return initial
    
    def form_valid(self, form):
        """Associe automatiquement l'utilisateur connecté au commentaire"""
        form.instance.utilisateur = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        """Redirige vers la formation associée après création"""
        return reverse_lazy('formation-detail', kwargs={'pk': self.object.formation.pk})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titre'] = "Ajouter un commentaire"
        return context


class CommentaireUpdateView(PermissionRequiredMixin, BaseUpdateView):
    """Vue permettant de modifier un commentaire existant"""
    model = Commentaire
    permission_required = 'rap_app.change_commentaire'
    fields = ['contenu', 'saturation']
    template_name = 'commentaires/commentaire_form.html'
    
    def get_success_url(self):
        """Redirige vers la formation associée après modification"""
        return reverse_lazy('formation-detail', kwargs={'pk': self.object.formation.pk})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titre'] = f"Modifier le commentaire du {self.object.created_at.strftime('%d/%m/%Y')}"
        return context


class CommentaireDeleteView(PermissionRequiredMixin, BaseDeleteView):
    """Vue permettant de supprimer un commentaire"""
    model = Commentaire
    permission_required = 'rap_app.delete_commentaire'
    template_name = 'commentaires/commentaire_confirm_delete.html'
    
    def get_success_url(self):
        """Redirige vers la formation associée après suppression"""
        formation_id = self.object.formation.id
        return reverse_lazy('formation-detail', kwargs={'pk': formation_id})
    



class AllCommentairesView(ListView):
    model = Commentaire
    template_name = 'formations/commentaires_tous.html'
    context_object_name = 'commentaires'
    paginate_by = 20  # Pagination

    def get_queryset(self):
        """Récupère tous les commentaires avec les filtres appliqués."""
        queryset = Commentaire.objects.select_related('formation', 'utilisateur').order_by('-created_at')

        formation_id = self.request.GET.get('formation')
        utilisateur_id = self.request.GET.get('utilisateur')
        search_query = self.request.GET.get('q')
        order_by = self.request.GET.get('order_by', '-created_at')

        filters = Q()

        if formation_id:
            filters &= Q(formation_id=formation_id)

        if utilisateur_id:
            filters &= Q(utilisateur_id=utilisateur_id)

        if search_query:
            filters &= Q(contenu__icontains=search_query)

        if order_by:
            queryset = queryset.order_by(order_by)

        queryset = queryset.filter(filters)


        return queryset

    def get_context_data(self, **kwargs):
        """Ajoute la liste des formations et utilisateurs pour le filtrage."""
        context = super().get_context_data(**kwargs)
        context['formations'] = Formation.objects.all()
        context['utilisateurs'] = User.objects.all()
        return context

class ExportCommentairesView(View):
    """Vue permettant d'exporter les commentaires sélectionnés en CSV."""

    def post(self, request, *args, **kwargs):
        commentaire_ids = request.POST.getlist('commentaire_ids')  # Récupération des IDs sélectionnés
        
        if not commentaire_ids:
            return HttpResponse("Aucun commentaire sélectionné.", status=400)

        commentaires = get_list_or_404(Commentaire, id__in=commentaire_ids)

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="commentaires_export.csv"'

        writer = csv.writer(response)
        writer.writerow(["ID", "Utilisateur", "Date", "Formation", "Num Offre", "Commentaire"])

        for commentaire in commentaires:
            writer.writerow([
                commentaire.id,
                commentaire.utilisateur.username if commentaire.utilisateur else "Anonyme",
                commentaire.created_at.strftime("%d/%m/%Y %H:%M"),
                commentaire.formation.nom if commentaire.formation else "N/A",
                commentaire.formation.num_offre if commentaire.formation else "N/A",
                commentaire.contenu
            ])

        return response
        from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from ..forms.company_form import CompanyForm
from ..models.company import Company

# Liste des entreprises
class CompanyListView(ListView):
    model = Company
    template_name = 'company/company_list.html'
    context_object_name = 'companies'
    ordering = ['-created_at']

# Détail d'une entreprise
class CompanyDetailView(DetailView):
    model = Company
    template_name = 'company/company_detail.html'

# Création d'une entreprise
class CompanyCreateView(CreateView):
    model = Company
    form_class = CompanyForm
    template_name = 'company/company_form.html'
    success_url = reverse_lazy('company-list')

# Mise à jour d'une entreprise
class CompanyUpdateView(UpdateView):
    model = Company
    form_class = CompanyForm
    template_name = 'company/company_form.html'
    success_url = reverse_lazy('company-list')

# Suppression d'une entreprise
class CompanyDeleteView(DeleteView):
    model = Company
    template_name = 'company/company_confirm_delete.html'
    success_url = reverse_lazy('company-list')
from django.http import HttpRequest  # ✅ Import correct de HttpRequest
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.db.models import Count, Sum, Avg, F, Q, Case, When, IntegerField, Value
from django.utils import timezone
from datetime import timedelta
from django.db.models.functions import TruncMonth
from django.http import JsonResponse
from django.views import View
from django import template
from django.db.models import Count, Avg, F, Value, Sum, FloatField
from django.db.models.functions import Coalesce, TruncMonth
from django.db import models

from ..models.company import Company

from ..models.prospection import PROSPECTION_STATUS_CHOICES, Prospection

from ..models.formations import HistoriqueFormation

from ..views.base_views import BaseListView

from ..models.partenaires import Partenaire


from ..models import Formation, Centre, Commentaire, TypeOffre, Statut, Evenement, Recherche


from ..models import Formation, Statut

from ..models import Formation, Centre, Commentaire, TypeOffre, Statut, Evenement


class DashboardView(BaseListView):
    model = Formation  # Spécifiez le modèle à afficher
    template_name = 'dashboard.html'  # Spécifiez le template
    context_object_name = 'formations'  # Nom de la variable dans le template

    def get_context_data(self, **kwargs):
        # Appelez la méthode parente pour obtenir le contexte de base
        context = super().get_context_data(**kwargs)

        # ✅ Nombre total de formations par centre
        context['formations_par_centre'] = (
            Centre.objects.annotate(total_formations=Count('formations'))
            .order_by('-total_formations')
        )

        # ✅ Formations par type d'offre
        context['formations_par_type_offre'] = (
            TypeOffre.objects.annotate(total=Count('formations'))
            .order_by('-total')
        )

        # ✅ Formations par statut
        context['formations_par_statut'] = (
            Statut.objects.annotate(total=Count('formations'))
            .order_by('-total')
        )

        # ✅ Statistiques globales
        context['total_formations'] = Formation.objects.count()
        context['formations_actives'] = Formation.objects.formations_actives().count()
        context['formations_a_venir'] = Formation.objects.formations_a_venir().count()
        context['formations_terminees'] = Formation.objects.formations_terminees().count()
        context['formations_a_recruter'] = Formation.objects.formations_a_recruter().count()

        # ✅ Places prévues et disponibles
        context['total_places_prevues'] = Formation.objects.aggregate(
            total=Sum(F('prevus_crif') + F('prevus_mp'))
        )['total'] or 0

        context['total_places_prevues_crif'] = Formation.objects.aggregate(
            total=Sum('prevus_crif')
        )['total'] or 0

        context['total_places_prevues_mp'] = Formation.objects.aggregate(
            total=Sum('prevus_mp')
        )['total'] or 0

        context['total_places_restantes'] = Formation.objects.aggregate(
            total=Sum(F('prevus_crif') + F('prevus_mp') - F('inscrits_crif') - F('inscrits_mp'))
        )['total'] or 0

        context['total_places_restantes_crif'] = Formation.objects.aggregate(
            total=Sum(F('prevus_crif') - F('inscrits_crif'))
        )['total'] or 0

        context['total_places_restantes_mp'] = Formation.objects.aggregate(
            total=Sum(F('prevus_mp') - F('inscrits_mp'))
        )['total'] or 0

        # ✅ Recrutement et inscriptions
        context['total_candidats'] = Formation.objects.aggregate(total=Sum('nombre_candidats'))['total'] or 0
        context['total_entretiens'] = Formation.objects.aggregate(total=Sum('nombre_entretiens'))['total'] or 0
        context['total_inscrits'] = Formation.objects.aggregate(total=Sum(F('inscrits_crif') + F('inscrits_mp')))['total'] or 0
        context['total_inscrits_crif'] = Formation.objects.aggregate(total=Sum('inscrits_crif'))['total'] or 0
        context['total_inscrits_mp'] = Formation.objects.aggregate(total=Sum('inscrits_mp'))['total'] or 0

        # ✅ Calcul des taux moyens avec gestion d'erreur (évite division par zéro)
        try:
            context['taux_transformation_moyen'] = Formation.objects.aggregate(
                taux=Avg(100 * (F('inscrits_crif') + F('inscrits_mp')) / Coalesce(F('nombre_candidats'), Value(1)))
            )['taux'] or 0
        except ZeroDivisionError:
            context['taux_transformation_moyen'] = 0

        try:
            context['taux_saturation_moyen'] = Formation.objects.aggregate(
                taux=Avg(100 * (F('inscrits_crif') + F('inscrits_mp')) / Coalesce(F('prevus_crif') + F('prevus_mp'), Value(1)))
            )['taux'] or 0
        except ZeroDivisionError:
            context['taux_saturation_moyen'] = 0

        # ✅ Nombre de partenaires
        context['total_partenaires'] = Partenaire.objects.count()

        # ✅ Derniers commentaires des formations
        context['derniers_commentaires'] = (
            Commentaire.objects.select_related('formation', 'utilisateur')
            .order_by('-created_at')[:5]
        )

        # ✅ Candidats et Entretiens par Centre
        candidats_par_centre = (
            Centre.objects.annotate(
                total_candidats=Sum('formations__nombre_candidats'),
                total_entretiens=Sum('formations__nombre_entretiens')
            )
            .filter(Q(total_candidats__gt=0) | Q(total_entretiens__gt=0))
            .order_by('-total_candidats')
        )
        context['candidats_par_centre'] = candidats_par_centre

        # ✅ Places prévues et Inscrits par Centre
        places_par_centre = (
            Centre.objects.annotate(
                total_places_prevues=Sum(F('formations__prevus_crif') + F('formations__prevus_mp')),
                total_inscrits=Sum(F('formations__inscrits_crif') + F('formations__inscrits_mp')),
                places_prevues_crif=Sum('formations__prevus_crif'),
                places_prevues_mp=Sum('formations__prevus_mp'),
                inscrits_crif=Sum('formations__inscrits_crif'),
                inscrits_mp=Sum('formations__inscrits_mp')
            )
            .filter(total_places_prevues__gt=0)
            .order_by('-total_places_prevues')
        )
        context['places_par_centre'] = places_par_centre

        # ✅ Taux de transformation et saturation par Centre
        taux_par_centre = (
            Centre.objects.annotate(
                total_formations=Count('formations'),  # Ajout du total des formations
                total_candidats=Sum('formations__nombre_candidats'),
                total_entretiens=Sum('formations__nombre_entretiens'), 
                places_prevues_crif=Sum('formations__prevus_crif'),  # ✅ Ajout des places CRIF
                inscrits_crif=Sum('formations__inscrits_crif'),  # ✅ Ajout des inscrits CRIF
                places_prevues_mp=Sum('formations__prevus_mp'),  # ✅ Ajout des places MP
                inscrits_mp=Sum('formations__inscrits_mp'),  # ✅ Ajout des inscrits MP
                total_inscrits=Sum(F('formations__inscrits_crif') + F('formations__inscrits_mp')),
                total_places_prevues=Sum(F('formations__prevus_crif') + F('formations__prevus_mp')),
                taux_transformation=Case(
                    When(total_candidats__gt=0, 
                        then=100.0 * Sum(F('formations__inscrits_crif') + F('formations__inscrits_mp')) / Coalesce(Sum('formations__nombre_candidats'), Value(1))),
                    default=Value(0.0)
                ),
                taux_saturation=Case(
                    When(total_places_prevues__gt=0, 
                        then=100.0 * Sum(F('formations__inscrits_crif') + F('formations__inscrits_mp')) / Coalesce(Sum(F('formations__prevus_crif') + F('formations__prevus_mp')), Value(1))),
                    default=Value(0.0)
                )
            )
            .filter(Q(total_candidats__gt=0) | Q(total_places_prevues__gt=0))
            .order_by('-taux_saturation')
        )
        context['taux_par_centre'] = taux_par_centre

        # ✅ Prospections par statut (d'abord on stocke les valeurs)
        context['nb_prospections_en_cours'] = Prospection.objects.filter(statut='en_cours').count()
        context['nb_prospections_acceptees'] = Prospection.objects.filter(statut='acceptee').count()
        context['nb_prospections_a_faire'] = Prospection.objects.filter(statut='a_faire').count()
        context['nb_prospections_a_relancer'] = Prospection.objects.filter(statut='a_relancer').count()

        # ✅ Ensuite, les stats classiques pour les cartes du haut
        context['stats'] = [
        (context['total_formations'], "Formations", "primary", "fa-graduation-cap"),
        (context['total_candidats'], "Candidats", "secondary", "fa-users"),
        (context['total_entretiens'], "Entretiens", "warning", "fa-handshake"),
        (context['total_inscrits'], "Inscrits", "success", "fa-user-check"),
        (context['total_places_prevues'], "Places prévues", "info", "fa-calendar-alt"),
        (context['total_places_restantes'], "Places restantes", "danger", "fa-calendar-times"),
    ]

        total_prospections = Prospection.objects.count()
        prospections_acceptees = Prospection.objects.filter(statut='acceptee').count()

        context['taux_transformation_prospections'] = (
            (prospections_acceptees / total_prospections) * 100
            if total_prospections > 0 else 0
        )


        # ✅ Événements par type
        context['evenements_par_type'] = (
            Evenement.objects.values('type_evenement')
            .annotate(total=Count('id'))
            .order_by('-total')
        )

        # ✅ Récupération du nombre total d'événements par centre + détails par type
        evenements_par_centre = (
            Centre.objects.annotate(
                total_evenements=Count('formations__evenements', distinct=True)  # Utilisation du related_name
            )
        )

        details_evenements_par_centre = []
        for centre in evenements_par_centre:
            evenements = (
                Evenement.objects.filter(formation__centre=centre)
                .values('type_evenement')
                .annotate(total=Count('id'))
                .order_by('-total')
            )

            details_evenements_par_centre.append({
                'centre': centre,
                'total_evenements': centre.total_evenements,  # Total des événements pour ce centre
                'evenements': evenements
            })

        # ✅ Ajout au contexte
        context['evenements_par_centre'] = details_evenements_par_centre

        # Nombre total de prospections
        context['total_prospections'] = Prospection.objects.count()

        # Prospections par statut
        context['prospections_par_statut'] = (
            Prospection.objects.values('statut')
            .annotate(total=Count('id'))
            .order_by('-total')
        )

        # Prospections par objectif
        context['prospections_par_objectif'] = (
            Prospection.objects.values('objectif')
            .annotate(total=Count('id'))
            .order_by('-total')
        )

        # Nombre total d'entreprises
        context['total_entreprises'] = Company.objects.count()

        # Entreprises avec au moins une prospection
        context['entreprises_avec_prospections'] = (
            Company.objects.annotate(nb_prospections=Count('prospections'))
            .filter(nb_prospections__gt=0)
            .order_by('-nb_prospections')[:10]
        )

        context['prospections_par_statut'] = (
            Prospection.objects.values('statut')
            .annotate(total=Count('id'))
        )
        # Statuts existants avec leurs totaux
        statuts_db = {
            item['statut']: item['total']
            for item in Prospection.objects.values('statut').annotate(total=Count('id'))
        }

        # Ajoute tous les statuts possibles, même ceux absents
        prospections_par_statut_complet = []
        for key, label in PROSPECTION_STATUS_CHOICES:
            prospections_par_statut_complet.append({
                'statut': key,
                'label': label,
                'total': statuts_db.get(key, 0)
            })

        context['prospections_par_statut_complet'] = prospections_par_statut_complet



        return context  # ✅ Retourne correctement le contexte sans écrasement


class StatsAPIView(View):
    """API pour récupérer les statistiques du Dashboard"""

    def get(self, request, *args, **kwargs):
        action = request.GET.get('action')

        if action == 'formations_par_statut':
            return self.formations_par_statut()
        elif action == 'evolution_formations':
            return self.evolution_formations()
        elif action == 'formations_par_type':
            return self.formations_par_type()
        else:
            return JsonResponse({'error': 'Action non reconnue'}, status=400)

    def formations_par_statut(self):
        """Renvoie le nombre de formations par statut"""
        statuts = Statut.objects.annotate(
            nb_formations=Count('formations'),
            taux_moyen=Coalesce(
                Avg(
                    100.0 * (F('formations__inscrits_crif') + F('formations__inscrits_mp')) /
                    Coalesce(F('formations__prevus_crif') + F('formations__prevus_mp'), Value(1))
                ),
                Value(0.0),
                output_field=FloatField()
            )
        ).values('nom', 'nb_formations', 'taux_moyen', 'couleur')

        return JsonResponse({'statuts': list(statuts)})

    def evolution_formations(self):
        """Renvoie l'évolution du nombre de formations et d'inscrits par période"""
        date_limite = timezone.now().date() - timedelta(days=365)
        periode = self.request.GET.get('periode', 'mois')
        
        # Récupérer l'historique des formations
        query = HistoriqueFormation.objects.filter(created_at__gte=date_limite)
        
        # Définir comment obtenir la période selon le choix
        result = {}
        for historique in query:
            created_at = historique.created_at
            
            if periode == 'semaine':
                # Obtenir année et semaine
                year, week_num, _ = created_at.isocalendar()
                key = f"{year}-{week_num:02d}"
                label = f"Sem {week_num}, {year}"
            elif periode == 'annee':
                # Obtenir année
                year = created_at.year
                key = str(year)
                label = str(year)
            else:  # mois par défaut
                # Obtenir année et mois
                year = created_at.year
                month = created_at.month
                key = f"{year}-{month:02d}"
                label = f"{month:02d}/{year}"
            
            if key not in result:
                result[key] = {
                    'periode_evolution': key,
                    'label': label,
                    'nb_formations': 0,
                    'nb_inscrits': 0,
                    'total_candidats': 0,
                    'total_entretiens': 0,
                    'taux_saturation': 0,
                    'taux_transformation': 0,
                    'count': 0  # Pour calculer des moyennes
                }
            
            # Incrémenter les compteurs
            result[key]['nb_formations'] += 1
            
            # Traiter les champs qui peuvent être None
            if historique.inscrits_total is not None:
                result[key]['nb_inscrits'] += historique.inscrits_total
            
            if historique.formation is not None:
                # Candidats et entretiens de la formation
                candidats = getattr(historique.formation, 'nombre_candidats', 0) or 0
                entretiens = getattr(historique.formation, 'nombre_entretiens', 0) or 0
                result[key]['total_candidats'] += candidats
                result[key]['total_entretiens'] += entretiens
            
            if historique.saturation is not None:
                result[key]['taux_saturation'] += historique.saturation
                result[key]['count'] += 1
            
            # Transformation: calculer le rapport inscrits/candidats
            if candidats > 0 and historique.inscrits_total is not None:
                transformation = (historique.inscrits_total / candidats) * 100
                result[key]['taux_transformation'] += transformation
                # Ne pas incrémenter count à nouveau, nous utiliserons le même compte pour les deux moyennes
        
        # Calculer les moyennes
        evolution_list = []
        for key, data in result.items():
            if data['count'] > 0:
                data['taux_saturation'] = round(data['taux_saturation'] / data['count'], 1)
                data['taux_transformation'] = round(data['taux_transformation'] / data['count'], 1)
            del data['count']
            evolution_list.append(data)
        
        # Trier par période
        evolution_list.sort(key=lambda x: x['periode_evolution'])
        
        print(f"Données d'évolution réelles: {len(evolution_list)} périodes trouvées pour {periode}")
        return JsonResponse({'evolution': evolution_list})


        from django.urls import reverse_lazy
from django.db.models import Q
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import  get_object_or_404
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect


from ..models import Document, Formation
from .base_views import BaseListView, BaseDetailView, BaseCreateView, BaseUpdateView, BaseDeleteView


class DocumentListView(BaseListView):
    """Vue listant tous les documents avec options de filtrage"""
    model = Document
    context_object_name = 'documents'
    template_name = 'documents/document_list.html'
    
    def get_queryset(self):
        """
        Récupère la liste des documents avec possibilité de filtrage par:
        - Formation associée
        - Type de document
        - Nom de fichier (recherche textuelle)
        """
        queryset = super().get_queryset().select_related('formation')
        
        # Filtrage par formation
        formation_id = self.request.GET.get('formation')
        if formation_id:
            queryset = queryset.filter(formation_id=formation_id)
            
        # Filtrage par type de document
        type_doc = self.request.GET.get('type_document')
        if type_doc:
            queryset = queryset.filter(type_document=type_doc)
            
        # Recherche textuelle
        q = self.request.GET.get('q')
        if q:
            queryset = queryset.filter(
                Q(nom_fichier__icontains=q) | 
                Q(source__icontains=q)
            )
            
        return queryset
    
    def get_context_data(self, **kwargs):
        """Ajout des filtres actuels et des options de filtre au contexte"""
        context = super().get_context_data(**kwargs)
        
        # Filtres actuellement appliqués
        context['filters'] = {
            'formation': self.request.GET.get('formation', ''),
            'type_document': self.request.GET.get('type_document', ''),
            'q': self.request.GET.get('q', ''),
        }
        
        # Liste des formations pour le filtrage
        context['formations'] = Formation.objects.all()
        
        # Types de documents pour le filtrage
        context['types_document'] = Document.TYPE_DOCUMENT_CHOICES
        
        return context
class DocumentDownloadView(BaseDetailView):
    """Vue pour télécharger un document"""
    def get(self, request, pk):
        document = get_object_or_404(Document, pk=pk)
        response = HttpResponse(document.fichier, content_type='application/octet-stream')
        response['Content-Disposition'] = f'attachment; filename="{document.nom_fichier}"'
        return response
class DocumentDetailView(BaseDetailView):
    """Vue affichant les détails d'un document"""
    model = Document
    context_object_name = 'document'
    template_name = 'documents/document_detail.html'


class DocumentCreateView(PermissionRequiredMixin, BaseCreateView):
    """Vue permettant de créer un nouveau document"""
    model = Document
    permission_required = 'rap_app.add_document'
    fields = ['formation', 'nom_fichier', 'fichier', 'source', 'type_document']
    template_name = 'documents/document_form.html'
    
    def get_initial(self):
        """Pré-remplit le formulaire avec la formation si spécifiée dans l'URL"""
        initial = super().get_initial()
        formation_id = self.request.GET.get('formation')
        if formation_id:
            initial['formation'] = formation_id
        return initial
    
    def get_success_url(self):
        """Redirige vers la formation associée après création"""
        return reverse_lazy('formation-detail', kwargs={'pk': self.object.formation.pk})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titre'] = "Ajouter un document"
        # Ajout de la liste des types de documents
        context['types_document'] = Document.TYPE_DOCUMENT_CHOICES
        return context

class DocumentUpdateView(PermissionRequiredMixin, BaseUpdateView):
    """Vue permettant de modifier un document existant"""
    model = Document
    permission_required = 'rap_app.change_document'
    fields = ['nom_fichier', 'fichier', 'source', 'type_document']
    template_name = 'documents/document_form.html'
    
    def get_success_url(self):
        """Redirige vers la formation associée après modification"""
        return reverse_lazy('formation-detail', kwargs={'pk': self.object.formation.pk})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titre'] = f"Modifier le document : {self.object.nom_fichier}"
        # Ajout de la liste des types de documents
        context['types_document'] = Document.TYPE_DOCUMENT_CHOICES
        return context


class DocumentDeleteView(PermissionRequiredMixin, BaseDeleteView):
    """Vue permettant de supprimer un document"""
    model = Document
    permission_required = 'rap_app.delete_document'
    template_name = 'documents/document_confirm_delete.html'
    
    def get_success_url(self):
        """Redirige vers la formation associée après suppression"""
        formation_id = self.object.formation.id
        return reverse_lazy('formation-detail', kwargs={'pk': formation_id})
    

from django.urls import reverse_lazy
from django.db.models import Q
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from django.utils import timezone

from ..models import Evenement, Formation
from .base_views import BaseListView, BaseDetailView, BaseCreateView, BaseUpdateView, BaseDeleteView


class EvenementListView(BaseListView):
    """Vue listant tous les événements avec options de filtrage"""
    model = Evenement
    context_object_name = 'evenements'
    template_name = 'evenements/evenement_list.html'
    
    def get_queryset(self):
        """
        Récupère la liste des événements avec possibilité de filtrage par:
        - Formation associée
        - Type d'événement
        - Date (à venir, passés)
        """
        queryset = super().get_queryset().select_related('formation', 'formation__centre')
        
        # Filtrage par formation
        formation_id = self.request.GET.get('formation')
        if formation_id:
            queryset = queryset.filter(formation_id=formation_id)
            
        # Filtrage par type d'événement
        type_evt = self.request.GET.get('type')
        if type_evt:
            queryset = queryset.filter(type_evenement=type_evt)
            
        # Filtrage par période (à venir/passés)
        periode = self.request.GET.get('periode')
        if periode == 'future':
            queryset = queryset.filter(event_date__gte=timezone.now().date())
        elif periode == 'past':
            queryset = queryset.filter(event_date__lt=timezone.now().date())
            
        # Recherche textuelle
        q = self.request.GET.get('q')
        if q:
            queryset = queryset.filter(
                Q(details__icontains=q) | 
                Q(description_autre__icontains=q) |
                Q(formation__nom__icontains=q)
            )
            
        return queryset
    
    def get_context_data(self, **kwargs):
        """Ajout des filtres actuels et des options de filtre au contexte"""
        context = super().get_context_data(**kwargs)
        
        # Filtres actuellement appliqués
        context['filters'] = {
            'formation': self.request.GET.get('formation', ''),
            'type': self.request.GET.get('type', ''),
            'periode': self.request.GET.get('periode', ''),
            'q': self.request.GET.get('q', ''),
        }
        
        # Liste des formations pour le filtrage
        context['formations'] = Formation.objects.all()
        
        # Types d'événements pour le filtrage
        context['types_evenement'] = Evenement.TYPE_EVENEMENT_CHOICES
        
        # Date actuelle pour affichage
        context['now'] = timezone.now().date()
        
        return context


class EvenementDetailView(BaseDetailView):
    """Vue affichant les détails d'un événement"""
    model = Evenement
    context_object_name = 'evenement'
    template_name = 'evenements/evenement_detail.html'


class EvenementCreateView(PermissionRequiredMixin, BaseCreateView):
    """Vue permettant de créer un nouvel événement"""
    model = Evenement
    permission_required = 'rap_app.add_evenement'
    fields = ['formation', 'type_evenement', 'details', 'event_date', 'description_autre']
    template_name = 'evenements/evenement_form.html'
    
    def get_initial(self):
        """Pré-remplit le formulaire avec la formation si spécifiée dans l'URL"""
        initial = super().get_initial()
        formation_id = self.request.GET.get('formation')
        if formation_id:
            initial['formation'] = formation_id
        return initial
    
    def get_success_url(self):
        """Redirige vers la formation associée après création"""
        if self.object.formation:
            return reverse_lazy('formation-detail', kwargs={'pk': self.object.formation.pk})
        return reverse_lazy('evenement-list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titre'] = "Ajouter un événement"
        # Ajout de la liste des types d'événements
        context['types_evenement'] = Evenement.TYPE_EVENEMENT_CHOICES
        return context


class EvenementUpdateView(PermissionRequiredMixin, BaseUpdateView):
    """Vue permettant de modifier un événement existant"""
    model = Evenement
    permission_required = 'rap_app.change_evenement'
    fields = ['formation', 'type_evenement', 'details', 'event_date', 'description_autre']
    template_name = 'evenements/evenement_form.html'
    
    def get_success_url(self):
        """Redirige vers la formation associée après modification"""
        if self.object.formation:
            return reverse_lazy('formation-detail', kwargs={'pk': self.object.formation.pk})
        return reverse_lazy('evenement-list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titre'] = f"Modifier l'événement du {self.object.event_date.strftime('%d/%m/%Y') if self.object.event_date else ''}"
        # Ajout de la liste des types d'événements
        context['types_evenement'] = Evenement.TYPE_EVENEMENT_CHOICES
        return context


class EvenementDeleteView(PermissionRequiredMixin, BaseDeleteView):
    """Vue permettant de supprimer un événement"""
    model = Evenement
    permission_required = 'rap_app.delete_evenement'
    template_name = 'evenements/evenement_confirm_delete.html'
    
    def get_success_url(self):
        """Redirige vers la formation associée après suppression"""
        if hasattr(self, 'formation_id') and self.formation_id:
            return reverse_lazy('formation-detail', kwargs={'pk': self.formation_id})
        return reverse_lazy('evenement-list')
    
    def delete(self, request, *args, **kwargs):
        """Stocke l'ID de la formation avant suppression pour la redirection"""
        self.object = self.get_object()
        self.formation_id = self.object.formation.id if self.object.formation else None
        return super().delete(request, *args, **kwargs)
        import csv
from django.contrib.auth import get_user_model
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.db.models import Q, F, ExpressionWrapper, IntegerField, FloatField
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.utils import timezone
from django.db import transaction
from django.shortcuts import get_object_or_404, redirect
from datetime import datetime, date  # ✅ Ajoute cette ligne en haut du fichier
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
from django.views import View
from django.views.decorators.http import require_POST
from datetime import datetime

from django.contrib import messages
from django.http import HttpResponseBadRequest

from ..models.company import Company

from ..models.formations import HistoriqueFormation

from ..models.partenaires import Partenaire
from ..models import Formation


from ..models.centres import Centre
from ..models.statut import Statut
from ..models.types_offre import TypeOffre

from ..models.commentaires import Commentaire, User
from ..models import Formation
from .base_views import BaseListView, BaseDetailView, BaseCreateView, BaseUpdateView, BaseDeleteView

User = get_user_model()


class FormationListView(BaseListView):
    """Vue listant toutes les formations avec options de filtrage et indicateurs dynamiques."""
    model = Formation
    context_object_name = 'formations'
    template_name = 'formations/formation_list.html'
    paginate_by = 10  # ✅ Ajout de la pagination

    def get_queryset(self):
        """Récupère la liste des formations avec options de filtrage et recherche par mots-clés."""
        today = timezone.now().date()

        queryset = Formation.objects.select_related('centre', 'type_offre', 'statut').annotate(
            total_places=ExpressionWrapper(
                F('prevus_crif') + F('prevus_mp'), output_field=IntegerField()
            ),
            total_inscrits=ExpressionWrapper(
                F('inscrits_crif') + F('inscrits_mp'), output_field=IntegerField()
            ),
            places_restantes_crif=ExpressionWrapper(
                F('prevus_crif') - F('inscrits_crif'), output_field=IntegerField()
            ),
            places_restantes_mp=ExpressionWrapper(
                F('prevus_mp') - F('inscrits_mp'), output_field=IntegerField()
            ),
            taux_saturation=ExpressionWrapper(
                100.0 * (F('inscrits_crif') + F('inscrits_mp')) / 
                (F('prevus_crif') + F('prevus_mp')), output_field=FloatField()
            ),
            taux_transformation=ExpressionWrapper(
                100.0 * (F('inscrits_crif') + F('inscrits_mp')) / 
                (F('nombre_candidats') + 0.0001), output_field=FloatField()
            ),
        )

        # 🔍 Recherche et filtres
        mot_cle = self.request.GET.get('q', '').strip()
        if mot_cle:
            queryset = queryset.filter(
                Q(nom__icontains=mot_cle) |
                Q(num_offre__icontains=mot_cle) |
                Q(centre__nom__icontains=mot_cle) |
                Q(type_offre__nom__icontains=mot_cle) |
                Q(statut__nom__icontains=mot_cle)
            )

        centre_id = self.request.GET.get('centre', '').strip()
        type_offre_id = self.request.GET.get('type_offre', '').strip()
        statut_id = self.request.GET.get('statut', '').strip()
        periode = self.request.GET.get('periode', '').strip()

        if centre_id:
            queryset = queryset.filter(centre_id=centre_id)
        if type_offre_id:
            queryset = queryset.filter(type_offre_id=type_offre_id)
        if statut_id:
            queryset = queryset.filter(statut_id=statut_id)
        if periode:
            if periode == 'active':
                queryset = queryset.filter(start_date__lte=today, end_date__gte=today)
            elif periode == 'a_venir':
                queryset = queryset.filter(start_date__gt=today)
            elif periode == 'terminee':
                queryset = queryset.filter(end_date__lt=today)
            elif periode == 'a_recruter':
                queryset = queryset.filter(total_places__gt=F('total_inscrits'))

        return queryset
    
    

    def get_context_data(self, **kwargs):
        """Ajoute les statistiques, les centres, types d'offres et statuts au contexte pour le template."""
        context = super().get_context_data(**kwargs)

        context['stats'] = [
            (Formation.objects.count(), "Total formations", "primary", "fa-graduation-cap"),
            (Formation.objects.formations_actives().count(), "Formations Actives", "success", "fa-check-circle"),
            (Formation.objects.formations_a_venir().count(), "Formations À venir", "info", "fa-clock"),
            (Formation.objects.formations_terminees().count(), "Formations Terminées", "secondary", "fa-times-circle"),
            (Formation.objects.formations_a_recruter().count(), "Formations À recruter", "danger", "fa-users"),

        ]

        context['centres'] = Centre.objects.all()
        context['types_offre'] = TypeOffre.objects.all()
        context['statuts'] = Statut.objects.all()

        context['filters'] = {
            'centre': self.request.GET.get('centre', ''),
            'type_offre': self.request.GET.get('type_offre', ''),
            'statut': self.request.GET.get('statut', ''),
            'periode': self.request.GET.get('periode', ''),
            'q': self.request.GET.get('q', ''),
        }

        return context
        
def post(self, request, *args, **kwargs):
    formation = self.get_object()
    action = request.POST.get("action")

    if action == "add_company":
        return self.add_company(request, formation)
    elif action == "add_prospection":
        return self.add_prospection(request, formation)

    return super().post(request, *args, **kwargs)

def add_company(self, request, formation):
    from ..forms.company_form import CompanyForm
    form = CompanyForm(request.POST)
    if form.is_valid():
        company = form.save(commit=False)
        company.created_by = request.user
        company.save()
        messages.success(request, "✅ Entreprise ajoutée avec succès.")
    else:
        messages.error(request, "❌ Erreur lors de l'ajout de l'entreprise.")
    return redirect(request.path)

def add_prospection(self, request, formation):
    from ..forms.ProspectionForm import ProspectionForm
    form = ProspectionForm(request.POST)
    if form.is_valid():
        prospection = form.save(commit=False)
        prospection.formation = formation
        prospection.responsable = request.user
        prospection.save()
        messages.success(request, "✅ Prospection ajoutée avec succès.")
    else:
        messages.error(request, "❌ Erreur lors de l'ajout de la prospection.")
    return redirect(request.path)





class ModifierInscritsView(View):
    """Vue pour modifier les inscrits CRIF, MP, nombre de candidats, entretiens et prévus CRIF/MP via AJAX."""

    def post(self, request, formation_id, *args, **kwargs):  
        try:
            data = json.loads(request.body)
            field = data.get("field")
            value = data.get("value")

            # ✅ Ajout des nouveaux champs autorisés
            if field not in ["inscrits_crif", "inscrits_mp", "nombre_candidats", "nombre_entretiens", "prevus_crif", "prevus_mp"]:
                return JsonResponse({"success": False, "error": "Champ invalide"}, status=400)

            formation = Formation.objects.get(pk=formation_id)

            # ✅ Vérifier la permission de modification
            if not request.user.has_perm("rap_app.change_formation"):
                return JsonResponse({"success": False, "error": "Permission refusée"}, status=403)

            # ✅ Mettre à jour la valeur du champ
            setattr(formation, field, int(value))
            formation.save()

            return JsonResponse({"success": True, "message": "Mise à jour réussie", "new_value": value})

        except Formation.DoesNotExist:
            return JsonResponse({"success": False, "error": "Formation non trouvée"}, status=404)
        except json.JSONDecodeError:
            return JsonResponse({"success": False, "error": "Format JSON invalide"}, status=400)
        except Exception as e:
            return JsonResponse({"success": False, "error": str(e)}, status=500)

class FormationDetailView(BaseDetailView):
    """Vue affichant les détails d'une formation"""
    model = Formation
    context_object_name = 'formation'
    template_name = 'formations/formation_detail.html'

    def get_context_data(self, **kwargs):
        """Ajoute les commentaires, evenements et autres données au contexte"""
        context = super().get_context_data(**kwargs)
        formation = self.object

    # Récupération du dernier commentaire avec toutes ses infos
        dernier_commentaire = formation.get_commentaires().order_by('-created_at').first()

    # ✅ Partenaires associées
        context['partenaires'] = formation.partenaires.all()

        # ✅ Partenaires disponibles (celles qui ne sont pas encore associées)
        context['partenaires_disponibles'] = Partenaire.objects.exclude(id__in=formation.partenaires.values_list('id', flat=True))


        context['dernier_commentaire'] = dernier_commentaire  # ✅ Ajout du dernier commentaire complet
        context['commentaires'] = formation.get_commentaires().order_by('-created_at')
        context['derniers_commentaires'] = ( Commentaire.objects.select_related('formation', 'utilisateur').order_by('-created_at')[:5])
        context['evenements'] = formation.get_evenements().order_by('-event_date')
        context['documents'] = formation.documents.all().order_by('-created_at')
        context['partenaires'] = formation.get_partenaires()
        context['historique'] = formation.historiques.order_by('-date_modification')[:10]

        # ✅ Ajout des valeurs calculées pour affichage
        context['places_restantes_crif'] = formation.get_places_restantes_crif()
        context['places_restantes_mp'] = formation.get_places_restantes_mp()
        context['taux_saturation'] = formation.get_taux_saturation()

    # Récupérer toutes les prospections liées à cette formation
        context['prospections'] = formation.prospections.select_related('company', 'responsable')

        # Afficher les entreprises (distinctes) liées par prospection
        context['entreprises'] = Company.objects.filter(prospections__formation=formation).distinct()

        # Formulaires vides pour création rapide
        from ..forms.company_form import CompanyForm
        from ..forms.ProspectionForm import ProspectionForm
        context['company_form'] = CompanyForm()
        context['prospection_form'] = ProspectionForm(initial={'formation': formation})

        return context    
    def post(self, request, *args, **kwargs):
            """
            Gère l'ajout de commentaires, événements, documents et partenaires via POST.
            L'action est déterminée par le champ `action` du formulaire.
            """
            formation = self.get_object()
            action = request.POST.get('action')

            if action == 'add_commentaire':
                return self.add_commentaire(request, formation)

            elif action == 'add_evenement':
                return self.add_evenement(request, formation)

            elif action == 'add_document':
                return self.add_document(request, formation)

            elif action == 'add_partenaire':
                return self.add_partenaire(request, formation)

            return HttpResponseBadRequest("Action non valide.")

    def add_commentaire(self, request, formation):
        """Ajoute un commentaire à la formation"""
        contenu = request.POST.get('contenu', '').strip()

        if not contenu:
            return HttpResponseBadRequest("Le commentaire ne peut pas être vide.")

        formation.add_commentaire(request.user, contenu)
        messages.success(request, "Commentaire ajouté avec succès.")
        return redirect(self.request.path)
        

    def add_evenement(self, request, formation):
        """Ajoute un événement à la formation"""
        type_evenement = request.POST.get('type_evenement', '').strip()
        date = request.POST.get('date')
        details = request.POST.get('details', '').strip()
        description_autre = request.POST.get('description_autre', '').strip()

        if not type_evenement or not date:
            return HttpResponseBadRequest("Le type et la date de l'événement sont obligatoires.")

    # ✅ On appelle la méthode avec les bons arguments (4 au total)
        formation.add_evenement(type_evenement, date, details, description_autre)
        messages.success(request, "Événement ajouté avec succès.")
        return redirect(self.request.path)

    def add_document(self, request, formation):
        """Ajoute un document à la formation."""
        nom = request.POST.get('nom', '').strip()
        fichier = request.FILES.get('fichier')

        if not nom or not fichier:
            return HttpResponseBadRequest("Le nom et le fichier sont obligatoires.")

        # ✅ Ajout du document directement avec `.create()`
        formation.documents.create(
            utilisateur=request.user, 
            nom_fichier=nom, 
            fichier=fichier
        )

        messages.success(request, "Document ajouté avec succès.")
        return redirect(self.request.path)

class FormationCreateView(PermissionRequiredMixin, BaseCreateView):
    """Vue permettant de créer une nouvelle formation"""
    model = Formation
    permission_required = 'rap_app.add_formation'
    template_name = 'formations/formation_form.html'
    fields = [
        'nom', 'centre', 'type_offre', 'statut', 'start_date', 'end_date',
        'num_kairos', 'num_offre', 'num_produit', 'prevus_crif', 'prevus_mp',
        'inscrits_crif', 'inscrits_mp', 'assistante', 'cap', 'convocation_envoie',
        'entresformation', 'nombre_candidats', 'nombre_entretiens'
    ]

    def form_valid(self, form):
        """Associe l'utilisateur connecté à la formation et crée un historique"""
        with transaction.atomic():
            form.instance.utilisateur = self.request.user
            response = super().form_valid(form)

            # 📌 Création d'un historique
            HistoriqueFormation.objects.create(
                formation=self.object,
                utilisateur=self.request.user,
                action='création',
                details={'nom': self.object.nom}
            )

            return response

    def get_success_url(self):
        return reverse_lazy('formation-detail', kwargs={'pk': self.object.pk})


class FormationUpdateView(PermissionRequiredMixin, BaseUpdateView):
    """Vue permettant de modifier une formation existante"""
    model = Formation
    permission_required = 'rap_app.change_formation'
    template_name = 'formations/formation_form.html'
    fields = FormationCreateView.fields  # ✅ Réutilisation des champs

    def form_valid(self, form):
        """Détecte les modifications et met à jour l'historique"""
        def serialize(value):
            if isinstance(value, (datetime, date)):
                return value.isoformat()
            elif hasattr(value, '__str__'):
                return str(value)
            return value

        with transaction.atomic():
            old_obj = Formation.objects.get(pk=self.object.pk)
            response = super().form_valid(form)

            # ✅ Comparaison des champs modifiés
            changes = {}
            for field in self.fields:
                old_value = getattr(old_obj, field)
                new_value = getattr(self.object, field)

                # ✅ Sérialise les valeurs avant comparaison
                if serialize(old_value) != serialize(new_value):
                    changes[field] = {
                        'ancien': serialize(old_value),
                        'nouveau': serialize(new_value)
                    }

            # 📌 Enregistre l'historique si des changements ont été détectés
            if changes:
                HistoriqueFormation.objects.create(
                    formation=self.object,
                    utilisateur=self.request.user,
                    action='modification',
                    details=changes
                )

            return response


    def get_success_url(self):
        return reverse_lazy('formation-detail', kwargs={'pk': self.object.pk})


class FormationDeleteView(PermissionRequiredMixin, BaseDeleteView):
    """Vue permettant de supprimer une formation"""
    model = Formation
    permission_required = 'rap_app.delete_formation'
    success_url = reverse_lazy('formation-list')
    template_name = 'formations/formation_confirm_delete.html'


class FormationAddCommentView(BaseCreateView):
    """Vue permettant d'ajouter un commentaire à une formation"""
    model = Commentaire
    fields = ['contenu']
    template_name = 'formations/formation_add_comment.html'

    def dispatch(self, request, *args, **kwargs):
        """Vérifie que la formation existe avant d'ajouter un commentaire"""
        self.formation = get_object_or_404(Formation, pk=self.kwargs['pk'])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        """Associe le commentaire à la formation et à l'utilisateur"""
        form.instance.formation = self.formation
        form.instance.utilisateur = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('formation-detail', kwargs={'pk': self.formation.pk})

class ExportFormationsExcelView(View):
    def get(self, request, *args, **kwargs):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="formations_export.csv"'

        writer = csv.writer(response)
        writer.writerow([
            "Nom", "Centre", "num_offre", "Type d'offre", "Statut", "N° Kairos", 
            "Dates", "Assistante", "Candidats", "Entretiens",
            "Prévus CRIF", "Prévus MP", "Inscrits CRIF", "Inscrits MP",
            "Places restantes CRIF", "Places restantes MP",
            "Transformation", "Saturation"
        ])

        formations = Formation.objects.all()
        for formation in formations:
            writer.writerow([
                formation.nom, 
                formation.centre.nom if formation.centre else "-",
                formation.num_offre if formation.num_offre else "-",
                formation.type_offre.nom if formation.type_offre else "-",
                formation.statut.nom if formation.statut else "-",
                formation.num_kairos if formation.num_kairos else "-",
                f"{formation.start_date} - {formation.end_date}",
                formation.assistante if formation.assistante else "-",
                formation.nombre_candidats,
                formation.nombre_entretiens,
                formation.prevus_crif,
                formation.prevus_mp,
                formation.inscrits_crif,
                formation.inscrits_mp,
                formation.get_places_restantes_crif(),  # ✅ Appel correct
                formation.get_places_restantes_mp(),  # ✅ Appel correct
                formation.get_taux_saturation(),  # ✅ Ajout du taux de saturation
                formation.get_taux_saturation()  # ✅ Transformation (ajuster si différent)
            ])

        return response
    



from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.utils.timezone import datetime

from ..models.formations import Formation
from ..models import HistoriqueFormation

class HistoriqueFormationListView(ListView):
    model = HistoriqueFormation
    template_name = 'historiqueformation/historiqueformation_list.html'
    context_object_name = 'historiques'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        formation_id = self.request.GET.get("formation")
        date = self.request.GET.get("date")

        if formation_id:
            queryset = queryset.filter(formation__id=formation_id)
        if date:
            try:
                parsed_date = datetime.strptime(date, "%Y-%m-%d")
                queryset = queryset.filter(date_modification__date=parsed_date)
            except ValueError:
                pass  # Ignore mauvaise date

        return queryset.select_related("formation", "modifie_par")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['formations'] = Formation.objects.all().order_by("nom")
        return context

class HistoriqueFormationDetailView( DetailView):
    model = HistoriqueFormation
    template_name = 'historiqueformation/historiqueformation_detail.html'
    context_object_name = 'historique'

class HistoriqueFormationDeleteView(DeleteView):
    model = HistoriqueFormation
    template_name = "historiqueformation/historiqueformation_confirm_delete.html"
    success_url = reverse_lazy("historique-formation-list")

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "✅ Entrée historique supprimée avec succès.")
        return super().delete(request, *args, **kwargs)
from django.urls import reverse_lazy
from django.db.models import Count, Q
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect

from ..models.partenaires import Partenaire

from ..models import  Formation
from .base_views import BaseListView, BaseDetailView, BaseCreateView, BaseUpdateView, BaseDeleteView


class PartenaireListView(BaseListView):
    """Vue listant toutes les partenaires avec des statistiques"""
    model = Partenaire
    context_object_name = 'partenaires'
    template_name = 'partenaires/partenaire_list.html'
    
    def get_queryset(self):
        """
        Récupère la liste des partenaires en annotant des statistiques :
        - Nombre de formations associées à chaque partenaire
        """
        queryset = super().get_queryset().annotate(
            nb_formations=Count('formations')
        )
        
        # Filtrage par nom de l'partenaire
        q = self.request.GET.get('q')
        if q:
            queryset = queryset.filter(nom__icontains=q)
            
        # Filtrage par secteur d'activité
        secteur = self.request.GET.get('secteur')
        if secteur:
            queryset = queryset.filter(secteur_activite__icontains=secteur)
            
        return queryset
    
    def get_context_data(self, **kwargs):
        """
        Ajoute des statistiques générales et les filtres appliqués au contexte de la page.
        """
        context = super().get_context_data(**kwargs)
        context['total_partenaires_avec_formations'] = Partenaire.objects.filter(formations__isnull=False).distinct().count()

        
        # Statistiques globales
        context['total_partenaires'] = Partenaire.objects.count()
        context['total_formations'] = Formation.objects.count()
        
        # Secteurs d'activité uniques pour le filtre
        secteurs = Partenaire.objects.exclude(secteur_activite__isnull=True).exclude(secteur_activite='').values_list('secteur_activite', flat=True).distinct()
        context['secteurs'] = secteurs
        
        # Filtres actuellement appliqués
        context['filters'] = {
            'q': self.request.GET.get('q', ''),
            'secteur': self.request.GET.get('secteur', ''),
        }
        
        return context


class PartenaireDetailView(BaseDetailView):
    """Vue affichant les détails d'une partenaire"""
    model = Partenaire
    context_object_name = 'partenaire'
    template_name = 'partenaires/partenaire_detail.html'

    def get_context_data(self, **kwargs):
        """Ajoute au contexte les formations associées à l'partenaire"""
        context = super().get_context_data(**kwargs)
        
        # Récupération des formations associées à l'partenaire
        formations = self.object.formations.select_related('type_offre', 'statut', 'centre').order_by('-start_date')

        # Filtrage des formations par type d'offre
        type_offre = self.request.GET.get('type_offre')
        if type_offre:
            formations = formations.filter(type_offre_id=type_offre)

        # Filtrage des formations par statut
        statut = self.request.GET.get('statut')
        if statut:
            formations = formations.filter(statut_id=statut)

        context['formations'] = formations
        
        return context


class PartenaireCreateView(PermissionRequiredMixin, BaseCreateView):
    """Vue permettant de créer une nouvelle partenaire"""
    model = Partenaire
    permission_required = 'rap_app.add_partenaire'
    fields = ['nom', 'secteur_activite', 'contact_nom', 'contact_poste', 
              'contact_telephone', 'contact_email', 'description']
    success_url = reverse_lazy('partenaire-list')
    template_name = 'partenaires/partenaire_form.html'

    def form_valid(self, form):
        partenaire = form.save()
        messages.success(self.request, "✅ Partenaire ajouté avec succès.")
        return redirect('partenaire-list')  # 🔹 Rediriger après succès
    
    def get_context_data(self, **kwargs):
        """
        Ajoute un titre personnalisé au contexte.
        """
        context = super().get_context_data(**kwargs)
        context['titre'] = "Ajouter un partenaire"
        return context
    
class PartenaireCreateViewFormation(PermissionRequiredMixin, BaseCreateView):
    """Vue permettant de créer une partenaire et de l'associer à une formation"""
    model = Partenaire
    permission_required = 'rap_app.add_partenaire'
    fields = ['nom', 'secteur_activite', 'contact_nom', 'contact_poste', 
              'contact_telephone', 'contact_email', 'description']
    template_name = 'partenaires/partenaire_formation_form.html'

    def form_valid(self, form):
        print("✅ form_valid exécuté")  # Vérifie si cette ligne s'affiche dans la console
        formation_id = self.kwargs.get('formation_id')

        if not formation_id:
            print("❌ Aucun ID de formation fourni !")
            messages.error(self.request, "❌ Erreur : Aucun ID de formation fourni.")
            return HttpResponseRedirect(reverse_lazy('formation-list'))  

        formation = get_object_or_404(Formation, pk=formation_id)
        print(f"📌 Formation trouvée : {formation.nom} (ID: {formation.id})")

        self.object = form.save()
        print(f"✅ Partenaire créé : {self.object.nom}")

        formation.partenaires.add(self.object)
        formation.save()
        print("✅ Partenaire ajouté à la formation avec succès !")

        messages.success(self.request, "Le partenaire a été créé et associé à la formation avec succès.")
        return HttpResponseRedirect(reverse_lazy('formation-detail', kwargs={'pk': formation_id}))

    def get_context_data(self, **kwargs):
        """Ajoute un titre dynamique au contexte"""
        context = super().get_context_data(**kwargs)
        formation_id = self.kwargs.get('formation_id')
        formation = get_object_or_404(Formation, pk=formation_id)
        context['titre'] = f"Ajouter un partenaire à la formation : {formation.nom} - { formation.num_offre}"
        return context


class PartenaireUpdateView(PermissionRequiredMixin, BaseUpdateView):
    """Vue permettant de modifier une partenaire existante"""
    model = Partenaire
    permission_required = 'rap_app.change_partenaire'
    fields = ['nom', 'secteur_activite', 'contact_nom', 'contact_poste', 
              'contact_telephone', 'contact_email', 'description']
    template_name = 'partenaires/partenaire_form.html'
    
    def get_success_url(self):
        """Redirige vers le détail du partenaire après modification"""
        return reverse_lazy('partenaire-detail', kwargs={'pk': self.object.pk})
    
    def get_context_data(self, **kwargs):
        """
        Ajoute un titre dynamique au contexte en fonction du partenaire modifié.
        """
        context = super().get_context_data(**kwargs)
        context['titre'] = f"Modifier le partenaire : {self.object.nom}"
        return context

class PartenaireDeleteView(PermissionRequiredMixin, BaseDeleteView):
    """Vue permettant de supprimer une partenaire"""
    model = Partenaire
    permission_required = 'rap_app.delete_partenaire'
    success_url = reverse_lazy('partenaire-list')
    template_name = 'partenaires/partenaire_confirm_delete.html'
    from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from ..forms.ProspectionForm import ProspectionForm
from ..models.prospection import HistoriqueProspection, Prospection


def ProspectionHomeView(request):
    return render(request, 'prospection/prospection_home.html')  # ✅ Indiquer que le template est dans prospection/

class ProspectionListView( ListView):
    """Affiche la liste des prospections"""
    model = Prospection
    template_name = 'prospection/prospection_list.html'
    context_object_name = 'prospections'
    ordering = ['-date_prospection']
    paginate_by = 10  # Pagination


    def get_queryset(self):
        queryset = super().get_queryset()
        statut = self.request.GET.get('statut')
        formation = self.request.GET.get('formation')
        entreprise = self.request.GET.get('entreprise')

        if statut:
            queryset = queryset.filter(statut=statut)
        if formation:
            queryset = queryset.filter(formation_id=formation)
        if entreprise:
            queryset = queryset.filter(company_id=entreprise)

        return queryset

class ProspectionDetailView( DetailView):
    """Affiche le détail d'une prospection"""
    model = Prospection
    template_name = 'prospection/prospection_detail.html'
    context_object_name = 'prospection'

class ProspectionCreateView (CreateView):
    """Vue pour créer une prospection"""
    model = Prospection
    form_class = ProspectionForm
    template_name = 'prospection/prospection_form.html'
    success_url = reverse_lazy('prospection-list')

    def form_valid(self, form):
        messages.success(self.request, "✅ Prospection ajoutée avec succès.")
        return super().form_valid(form)
    
    def get_initial(self):
        initial = super().get_initial()
        formation_id = self.request.GET.get('formation')
        if formation_id:
            initial['formation'] = formation_id
        return initial


class ProspectionUpdateView( UpdateView):
    """Permet de modifier une prospection"""
    model = Prospection
    form_class = ProspectionForm
    template_name = 'prospection/prospection_form.html'
    success_url = reverse_lazy('prospection-list')

    def form_valid(self, form):
        messages.success(self.request, "✅ Prospection mise à jour avec succès.")
        return super().form_valid(form)

class ProspectionDeleteView(DeleteView):
    """Permet de supprimer une prospection"""
    model = Prospection
    template_name = 'prospection/prospection_confirm_delete.html'
    success_url = reverse_lazy('prospection-list')

    def delete(self, request, *args, **kwargs):
        messages.success(request, "✅ Prospection supprimée avec succès.")
        return super().delete(request, *args, **kwargs)

class HistoriqueProspectionListView(ListView):
    model = HistoriqueProspection
    template_name = 'prospection/historiqueprospection_list.html'
    context_object_name = 'historiques'
    paginate_by = 20

    def get_queryset(self):
        queryset = super().get_queryset()
        prospection_id = self.request.GET.get("prospection")

        if prospection_id:
            queryset = queryset.filter(prospection_id=prospection_id)

        return queryset.select_related('prospection', 'modifie_par')


class HistoriqueProspectionDetailView(DetailView):
    model = HistoriqueProspection
    template_name = 'prospection/historiqueprospection_detail.html'
    context_object_name = 'historique'
    # models/rapports.py
from django.db import models
from django.utils import timezone
from .base import BaseModel

class Rapport(BaseModel):
    """
    Modèle représentant un rapport généré par le système.
    Les rapports peuvent être générés automatiquement ou manuellement.
    """
    TYPE_OCCUPATION = 'occupation'
    TYPE_CENTRE = 'centre'
    TYPE_STATUT = 'statut'
    TYPE_EVENEMENT = 'evenement'
    TYPE_RECRUTEMENT = 'recrutement'
    TYPE_PARTENAIRE = 'partenaire'
    TYPE_REPARTITION = 'repartition'
    TYPE_PERIODIQUE = 'periodique'
    TYPE_ANNUEL = 'annuel'
    TYPE_UTILISATEUR = 'utilisateur'
    
    TYPE_CHOICES = [
        (TYPE_OCCUPATION, 'Rapport d\'occupation des formations'),
        (TYPE_CENTRE, 'Rapport de performance par centre'),
        (TYPE_STATUT, 'Rapport de suivi des statuts'),
        (TYPE_EVENEMENT, 'Rapport d\'efficacité des événements'),
        (TYPE_RECRUTEMENT, 'Rapport de suivi du recrutement'),
        (TYPE_PARTENAIRE, 'Rapport d\'activité des partenaires'),
        (TYPE_REPARTITION, 'Rapport de répartition des partenaires'),
        (TYPE_PERIODIQUE, 'Rapport périodique'),
        (TYPE_ANNUEL, 'Rapport annuel consolidé'),
        (TYPE_UTILISATEUR, 'Rapport d\'activité utilisateurs'),
    ]
    
    PERIODE_QUOTIDIEN = 'quotidien'
    PERIODE_HEBDOMADAIRE = 'hebdomadaire'
    PERIODE_MENSUEL = 'mensuel'
    PERIODE_TRIMESTRIEL = 'trimestriel'
    PERIODE_ANNUEL = 'annuel'
    PERIODE_PERSONNALISE = 'personnalise'
    
    PERIODE_CHOICES = [
        (PERIODE_QUOTIDIEN, 'Quotidien'),
        (PERIODE_HEBDOMADAIRE, 'Hebdomadaire'),
        (PERIODE_MENSUEL, 'Mensuel'),
        (PERIODE_TRIMESTRIEL, 'Trimestriel'),
        (PERIODE_ANNUEL, 'Annuel'),
        (PERIODE_PERSONNALISE, 'Période personnalisée'),
    ]
    
    FORMAT_PDF = 'pdf'
    FORMAT_EXCEL = 'excel'
    FORMAT_CSV = 'csv'
    FORMAT_HTML = 'html'
    
    FORMAT_CHOICES = [
        (FORMAT_PDF, 'PDF'),
        (FORMAT_EXCEL, 'Excel'),
        (FORMAT_CSV, 'CSV'),
        (FORMAT_HTML, 'HTML'),
    ]
    
    nom = models.CharField(max_length=255, verbose_name="Nom du rapport")
    type_rapport = models.CharField(max_length=50, choices=TYPE_CHOICES, verbose_name="Type de rapport")
    periode = models.CharField(max_length=50, choices=PERIODE_CHOICES, verbose_name="Périodicité")
    date_debut = models.DateField(verbose_name="Date de début")
    date_fin = models.DateField(verbose_name="Date de fin")
    format = models.CharField(max_length=10, choices=FORMAT_CHOICES, default=FORMAT_HTML, verbose_name="Format")
    
    # Filtres optionnels
    centre = models.ForeignKey('Centre', null=True, blank=True, on_delete=models.SET_NULL, verbose_name="Centre")
    type_offre = models.ForeignKey('TypeOffre', null=True, blank=True, on_delete=models.SET_NULL, verbose_name="Type d'offre")
    statut = models.ForeignKey('Statut', null=True, blank=True, on_delete=models.SET_NULL, verbose_name="Statut")
    
    # Données du rapport
    donnees = models.JSONField(default=dict, verbose_name="Données du rapport")
    
    # Métadonnées
    date_generation = models.DateTimeField(default=timezone.now, verbose_name="Date de génération")
    utilisateur = models.ForeignKey('auth.User', null=True, blank=True, on_delete=models.SET_NULL, verbose_name="Généré par")
    temps_generation = models.FloatField(null=True, blank=True, verbose_name="Temps de génération (s)")
    
    class Meta:
        verbose_name = "Rapport"
        verbose_name_plural = "Rapports"
        ordering = ['-date_generation']
        
    def __str__(self):
        return f"{self.nom} - {self.get_type_rapport_display()} ({self.date_debut} à {self.date_fin})"
        from django.urls import reverse_lazy
from django.db.models import Count
from django.contrib.auth.mixins import PermissionRequiredMixin
import random

from ..models import Statut, Formation
from .base_views import BaseListView, BaseDetailView, BaseCreateView, BaseUpdateView, BaseDeleteView


def generate_random_color():
    """
    Génère une couleur hexadécimale aléatoire si l'utilisateur ne la définit pas.
    Exemple de sortie : "#A3B2C1"
    """
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))


class StatutListView(BaseListView):
    """Liste des statuts de formation"""
    model = Statut
    context_object_name = 'statuts'
    template_name = 'statuts/statut_list.html'  # ✅ Ajout du chemin du template
    
    def get_queryset(self):
        """
        Récupère les statuts de formation avec un comptage des formations associées.
        """
        queryset = super().get_queryset().annotate(
            nb_formations=Count('formations')
        )
        
        # 🔍 Recherche par nom
        q = self.request.GET.get('q')
        if q:
            queryset = queryset.filter(nom__icontains=q)
            
        return queryset.order_by('nom')
    
    def get_context_data(self, **kwargs):
        """
        Ajoute les filtres appliqués au contexte pour les afficher dans le template.
        """
        context = super().get_context_data(**kwargs)
        context['filters'] = {
            'q': self.request.GET.get('q', ''),
        }
        return context
    def get_nom_display(self):
        """
        Retourne le nom du statut. Si le statut est 'Autre', affiche la description à la place.
        """
        if self.nom == self.AUTRE and self.description_autre:
            return self.description_autre
        return dict(self.STATUT_CHOICES).get(self.nom, self.nom)  # Retourne le nom du statut normal


class StatutDetailView(BaseDetailView):
    """Détail d'un statut de formation"""
    model = Statut
    context_object_name = 'statut'
    template_name = 'statuts/statut_detail.html'  # ✅ Ajout du chemin du template
    
    def get_context_data(self, **kwargs):
        """
        Ajoute les formations associées au statut dans le contexte.
        """
        context = super().get_context_data(**kwargs)
        context['formations'] = Formation.objects.filter(
            statut=self.object
        ).select_related('centre', 'type_offre').order_by('-start_date')
        return context


class StatutCreateView(PermissionRequiredMixin, BaseCreateView):
    """Création d'un statut de formation"""
    model = Statut
    permission_required = 'rap_app.add_statut'
    fields = ['nom', 'couleur', 'description_autre']
    success_url = reverse_lazy('statut-list')
    template_name = 'statuts/statut_form.html'  # ✅ Ajout du chemin du template
    
    def form_valid(self, form):
        """
        Vérifie si une couleur est fournie, sinon assigne une couleur aléatoire.
        """
        statut = form.save(commit=False)
        if not statut.couleur:
            statut.couleur = generate_random_color()
        statut.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        """
        Ajoute un titre dynamique au contexte du template.
        """
        context = super().get_context_data(**kwargs)
        context['titre'] = "Ajouter un statut de formation"
        return context


class StatutUpdateView(PermissionRequiredMixin, BaseUpdateView):
    """Mise à jour d'un statut de formation"""
    model = Statut
    permission_required = 'rap_app.change_statut'
    fields = ['nom', 'couleur', 'description_autre']
    template_name = 'statuts/statut_form.html'  # ✅ Même template que pour la création
    
    def form_valid(self, form):
        """
        Vérifie que la couleur est définie, sinon génère une couleur automatique.
        """
        statut = form.save(commit=False)
        if not statut.couleur:
            statut.couleur = generate_random_color()
        statut.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        """
        Ajoute un titre dynamique au contexte.
        """
        context = super().get_context_data(**kwargs)
        context['titre'] = f"Modifier le statut : {self.object.get_nom_display()}"
        return context


class StatutDeleteView(PermissionRequiredMixin, BaseDeleteView):
    """Suppression d'un statut de formation"""
    model = Statut
    permission_required = 'rap_app.delete_statut'
    success_url = reverse_lazy('statut-list')
    template_name = 'statuts/statut_confirm_delete.html'  # ✅ Ajout du chemin du template
from django.urls import reverse_lazy
from django.db.models import Count, Q
from django.contrib.auth.mixins import PermissionRequiredMixin

from ..models import TypeOffre, Formation
from .base_views import BaseListView, BaseDetailView, BaseCreateView, BaseUpdateView, BaseDeleteView


class TypeOffreListView(BaseListView):
    """Liste des types d'offres de formation"""
    model = TypeOffre
    context_object_name = 'types_offre'
    template_name = "types_offres/typeoffre_list.html"
    
    def get_queryset(self):
        queryset = super().get_queryset().annotate(
            nb_formations=Count('formations')
        )
        
        # Recherche par nom
        q = self.request.GET.get('q')
        if q:
            queryset = queryset.filter(Q(nom__icontains=q) | Q(autre__icontains=q))
        
        return queryset.order_by('nom')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Filtres appliqués
        context['filters'] = {
            'q': self.request.GET.get('q', ''),
        }
        
        return context


class TypeOffreDetailView(BaseDetailView):
    """Détail d'un type d'offre de formation"""
    model = TypeOffre
    context_object_name = 'type_offre'
    template_name = "types_offres/typeoffre_detail.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Récupérer les formations associées
        context['formations'] = Formation.objects.filter(
            type_offre=self.object
        ).select_related('centre', 'statut').order_by('-start_date')
        
        return context


class TypeOffreCreateView(PermissionRequiredMixin, BaseCreateView):
    """Création d'un type d'offre de formation"""
    model = TypeOffre
    permission_required = 'rap_app.add_typeoffre'
    fields = ['nom', 'autre']
    success_url = reverse_lazy('type-offre-list')
    template_name = "types_offres/typeoffre_form.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titre'] = "Ajouter un type d'offre de formation"
        return context


class TypeOffreUpdateView(PermissionRequiredMixin, BaseUpdateView):
    """Mise à jour d'un type d'offre de formation"""
    model = TypeOffre
    permission_required = 'rap_app.change_typeoffre'
    fields = ['nom', 'autre']
    template_name = "types_offres/typeoffre_form.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titre'] = f"Modifier le type d'offre : {self.object.__str__()}"
        return context


class TypeOffreDeleteView(PermissionRequiredMixin, BaseDeleteView):
    """Suppression d'un type d'offre de formation"""
    model = TypeOffre
    permission_required = 'rap_app.delete_typeoffre'
    success_url = reverse_lazy('type-offre-list')
    template_name = "types_offres/typeoffre_confirm_delete.html"
    import time
from django.db.models import Count, Sum, F, Q
import logging

from ..models.rapports import Rapport
from ..models import Formation

logger = logging.getLogger(__name__)

class GenerateurRapport:
    """Service de génération des différents types de rapports."""

    def generer_rapport(type_rapport, date_debut, date_fin, **kwargs):
        debut_generation = time.time()
        logger.info(f"📊 Génération du rapport {type_rapport} ({date_debut} → {date_fin})")

        rapport = Rapport(
            nom=f"Rapport {dict(Rapport.TYPE_CHOICES).get(type_rapport, 'Inconnu')} du {date_debut} au {date_fin}",
            type_rapport=type_rapport,
            date_debut=date_debut,
            date_fin=date_fin,
            **{k: v for k, v in kwargs.items() if k in ['centre', 'type_offre', 'statut', 'format', 'utilisateur', 'periode']}
        )

        try:
            generateur = getattr(GenerateurRapport, f"_generer_{type_rapport}", None)
            if not generateur:
                logger.error(f"❌ Aucun générateur trouvé pour {type_rapport}")
                return None

            rapport.donnees = generateur(date_debut, date_fin, **kwargs)

            rapport.temps_generation = time.time() - debut_generation
            rapport.save()
            logger.info(f"✅ Rapport {rapport.nom} généré et sauvegardé en {rapport.temps_generation:.2f}s")

        except Exception as e:
            logger.error(f"❌ Erreur lors de la génération du rapport {type_rapport} : {str(e)}")
            return None

        return rapport
    
    @staticmethod
    def _generer_occupation(date_debut, date_fin, **kwargs):
        """Génère un rapport d'occupation des formations."""
        formations = Formation.objects.filter(
            Q(start_date__gte=date_debut, start_date__lte=date_fin) | 
            Q(end_date__gte=date_debut, end_date__lte=date_fin) |
            Q(start_date__isnull=True, end_date__gte=date_debut)
        )
        
        if 'centre' in kwargs and kwargs['centre']:
            formations = formations.filter(centre=kwargs['centre'])
        if 'type_offre' in kwargs and kwargs['type_offre']:
            formations = formations.filter(type_offre=kwargs['type_offre'])
        if 'statut' in kwargs and kwargs['statut']:
            formations = formations.filter(statut=kwargs['statut'])

        formations = formations.annotate(
            places_totales=F('prevus_crif') + F('prevus_mp'),
            inscrits_totaux=F('inscrits_crif') + F('inscrits_mp'),
            taux_remplissage=100 * (F('inscrits_crif') + F('inscrits_mp')) / (F('prevus_crif') + F('prevus_mp'))
        )

        stats = formations.aggregate(
            total_formations=Count('id'),
            total_places=Sum(F('prevus_crif') + F('prevus_mp')),
            total_inscrits=Sum(F('inscrits_crif') + F('inscrits_mp')),
        )

        stats['taux_moyen'] = (stats['total_inscrits'] / stats['total_places']) * 100 if stats['total_places'] else 0

        formations_data = [{
            'id': f.id,
            'nom': f.nom,
            'centre': f.centre.nom,
            'type_offre': f.type_offre.get_nom_display(),
            'statut': f.statut.get_nom_display(),
            'places_totales': f.places_totales,
            'inscrits_totaux': f.inscrits_totaux,
            'taux_remplissage': round(f.taux_remplissage, 2)
        } for f in formations]

        return {
            'statistiques': stats,
            'formations': formations_data
        }



================================================
File: rap_app/models/partenaires.py
================================================
from django.db import models
from .base import BaseModel

class Partenaire(BaseModel):
    """
    Modèle représentant une partenaire.

    Ajout d'une relation avec `Formation` pour que les partenaires puissent être utilisées comme ressources.
    """

    nom = models.CharField(max_length=255, verbose_name="Nom du partenaire", unique=True )
    secteur_activite = models.CharField(max_length=255, verbose_name="Secteur d'activité",blank=True,null=True)
    contact_nom = models.CharField(max_length=255,verbose_name="Nom du contact",blank=True,null=True)
    contact_poste = models.CharField(max_length=255,verbose_name="Poste du contact",blank=True,null=True)
    contact_telephone = models.CharField(max_length=20, verbose_name="Téléphone du contact", blank=True, null=True)
    contact_email = models.EmailField(verbose_name="Email du contact", blank=True, null=True)
    description = models.TextField(verbose_name="Description de la relation", blank=True, null=True)

    # Manager par défaut (si PartenaireManager est supprimé)
    objects = models.Manager()

    def __str__(self):
        """Représentation lisible du partenaire."""
        return self.nom

    class Meta:
        verbose_name = "Partenaire"
        verbose_name_plural = "Partenaires"
        ordering = ['nom']
        indexes = [
            models.Index(fields=['nom']),  # Index pour optimiser la recherche par nom.
        ]



================================================
File: rap_app/models/prospection.py
================================================
from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

from ..models.formations import Formation
from .company import Company

# ✅ Statuts possibles pour une prospection
PROSPECTION_STATUS_CHOICES = [
    ('a_faire', 'À faire'),
    ('en_cours', 'En cours'),
    ('a_relancer', 'À relancer'),
    ('acceptee', 'Acceptée'),
    ('refusee', 'Refusée'),
    ('annulee', 'Annulée'),
    ('Non renséigné', 'Non renséigné'),

]

# ✅ Objectifs de prospection
PROSPECTION_OBJECTIF_CHOICES = [
    ('prise_contact', 'Prise de contact'),
    ('rendez_vous', 'Obtenir un rendez-vous'),
    ('presentation_offre', 'Présentation d’une offre'),
    ('contrat', 'Signer un contrat'),
    ('partenariat', 'Établir un partenariat'),
    ('autre', 'Autre'),
]

# ✅ Motifs pour lesquels on fait la prospection
PROSPECTION_MOTIF_CHOICES = [
    ('POEI', 'POEI'),
    ('Apprentissage', 'Apprentissage'),
    ('VAE', 'VAE'),
    ('partenariat', 'Établir un partenariat'),
    ('autre', 'Autre'),
]

# ===============================
# 🔵 Modèle principal : Prospection
# ===============================
class Prospection(models.Model):
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE,
        related_name="prospections",
        verbose_name="Entreprise"
    )
    formation = models.ForeignKey(
        Formation, on_delete=models.CASCADE,
        null=True, blank=True,
        related_name="prospections",
        verbose_name="Formation en lien"
    )
    date_prospection = models.DateTimeField(
        default=timezone.now,
        verbose_name="Date de la prospection"
    )
    motif = models.CharField(
        max_length=30,
        choices=PROSPECTION_MOTIF_CHOICES,
        default='prise_contact',
        verbose_name="Motif de la prospection"
    )
    statut = models.CharField(
        max_length=20,
        choices=PROSPECTION_STATUS_CHOICES,
        default='a_faire',
        verbose_name="Statut de la prospection"
    )
    objectif = models.CharField(
        max_length=30,
        choices=PROSPECTION_OBJECTIF_CHOICES,
        default='prise_contact',
        verbose_name="Objectif de la prospection"
    )
    commentaire = models.TextField(
        blank=True, null=True,
        verbose_name="Commentaires de la prospection"
    )
    responsable = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_NULL,
        null=True, blank=True,
        verbose_name="Responsable de la prospection"
    )

    class Meta:
        verbose_name = "Suivi de la prospection"
        verbose_name_plural = "Suivis des prospections"
        ordering = ['-date_prospection']

    def __str__(self):
        return f"{self.company.name} - {self.formation.nom if self.formation else 'Sans formation'} - {self.get_statut_display()} - {self.get_objectif_display()}"

    # 🔁 Méthode save() personnalisée pour historiser les changements
    def save(self, *args, **kwargs):
        is_new = self.pk is None
        old_prospection = None

        # ⚠️ Si la prospection existe déjà, on récupère l'ancienne version pour détecter les changements
        if not is_new:
            try:
                old_prospection = Prospection.objects.get(pk=self.pk)
            except Prospection.DoesNotExist:
                pass

        # 💾 On sauvegarde d'abord la prospection
        super().save(*args, **kwargs)

        # 🕓 Ensuite, on vérifie s'il y a des changements à historiser
        if old_prospection:
            changement_statut = old_prospection.statut != self.statut
            changement_objectif = old_prospection.objectif != self.objectif
            changement_commentaire = old_prospection.commentaire != self.commentaire

            if changement_statut or changement_objectif or changement_commentaire:
                # 📚 Création d'un enregistrement d'historique
                HistoriqueProspection.objects.create(
                    prospection=self,
                    ancien_statut=old_prospection.statut,
                    nouveau_statut=self.statut,
                    modifie_par=self.responsable,
                    commentaire=self.commentaire or "",
                    resultat=(
                        f"Objectif modifié : {old_prospection.objectif} → {self.objectif}"
                        if changement_objectif else ""
                    ),
                    prochain_contact=timezone.now().date() + timezone.timedelta(days=7),  # ⏳ J+7 pour relancer
                )

# ===============================
# 🔵 Historique des changements
# ===============================
class HistoriqueProspection(models.Model):
    prospection = models.ForeignKey(
        Prospection, on_delete=models.CASCADE,
        related_name="historiques"
    )
    date_modification = models.DateTimeField(auto_now_add=True)
    ancien_statut = models.CharField(max_length=20, choices=PROSPECTION_STATUS_CHOICES)
    nouveau_statut = models.CharField(max_length=20, choices=PROSPECTION_STATUS_CHOICES)
    commentaire = models.TextField(null=True, blank=True)
    modifie_par = models.ForeignKey(
        get_user_model(), on_delete=models.SET_NULL,
        null=True
    )
    prochain_contact = models.DateField(
        null=True, blank=True,
        verbose_name="Date de relance"
    )
    resultat = models.TextField(
        null=True, blank=True,
        verbose_name="Résultat ou retour de la prospection"
    )
    moyen_contact = models.CharField(
        max_length=50,
        choices=[('email', 'Email'), ('telephone', 'Téléphone'), ('visite', 'Visite'), ('réseaux', 'Réseaux sociaux')],
        null=True, blank=True,
        verbose_name="Moyen de contact"
    )

    class Meta:
        ordering = ['-date_modification']
        verbose_name = "Historique de prospection"

    def __str__(self):
        return f"{self.date_modification} - {self.prospection.company.name} - {self.nouveau_statut}"



================================================
File: rap_app/models/rapports.py
================================================
# models/rapports.py
from django.db import models
from django.utils import timezone
from .base import BaseModel

class Rapport(BaseModel):
    """
    Modèle représentant un rapport généré par le système.
    Les rapports peuvent être générés automatiquement ou manuellement.
    """
    TYPE_OCCUPATION = 'occupation'
    TYPE_CENTRE = 'centre'
    TYPE_STATUT = 'statut'
    TYPE_EVENEMENT = 'evenement'
    TYPE_RECRUTEMENT = 'recrutement'
    TYPE_PARTENAIRE = 'partenaire'
    TYPE_REPARTITION = 'repartition'
    TYPE_PERIODIQUE = 'periodique'
    TYPE_ANNUEL = 'annuel'
    TYPE_UTILISATEUR = 'utilisateur'
    
    TYPE_CHOICES = [
        (TYPE_OCCUPATION, 'Rapport d\'occupation des formations'),
        (TYPE_CENTRE, 'Rapport de performance par centre'),
        (TYPE_STATUT, 'Rapport de suivi des statuts'),
        (TYPE_EVENEMENT, 'Rapport d\'efficacité des événements'),
        (TYPE_RECRUTEMENT, 'Rapport de suivi du recrutement'),
        (TYPE_PARTENAIRE, 'Rapport d\'activité des partenaires'),
        (TYPE_REPARTITION, 'Rapport de répartition des partenaires'),
        (TYPE_PERIODIQUE, 'Rapport périodique'),
        (TYPE_ANNUEL, 'Rapport annuel consolidé'),
        (TYPE_UTILISATEUR, 'Rapport d\'activité utilisateurs'),
    ]
    
    PERIODE_QUOTIDIEN = 'quotidien'
    PERIODE_HEBDOMADAIRE = 'hebdomadaire'
    PERIODE_MENSUEL = 'mensuel'
    PERIODE_TRIMESTRIEL = 'trimestriel'
    PERIODE_ANNUEL = 'annuel'
    PERIODE_PERSONNALISE = 'personnalise'
    
    PERIODE_CHOICES = [
        (PERIODE_QUOTIDIEN, 'Quotidien'),
        (PERIODE_HEBDOMADAIRE, 'Hebdomadaire'),
        (PERIODE_MENSUEL, 'Mensuel'),
        (PERIODE_TRIMESTRIEL, 'Trimestriel'),
        (PERIODE_ANNUEL, 'Annuel'),
        (PERIODE_PERSONNALISE, 'Période personnalisée'),
    ]
    
    FORMAT_PDF = 'pdf'
    FORMAT_EXCEL = 'excel'
    FORMAT_CSV = 'csv'
    FORMAT_HTML = 'html'
    
    FORMAT_CHOICES = [
        (FORMAT_PDF, 'PDF'),
        (FORMAT_EXCEL, 'Excel'),
        (FORMAT_CSV, 'CSV'),
        (FORMAT_HTML, 'HTML'),
    ]
    
    nom = models.CharField(max_length=255, verbose_name="Nom du rapport")
    type_rapport = models.CharField(max_length=50, choices=TYPE_CHOICES, verbose_name="Type de rapport")
    periode = models.CharField(max_length=50, choices=PERIODE_CHOICES, verbose_name="Périodicité")
    date_debut = models.DateField(verbose_name="Date de début")
    date_fin = models.DateField(verbose_name="Date de fin")
    format = models.CharField(max_length=10, choices=FORMAT_CHOICES, default=FORMAT_HTML, verbose_name="Format")
    
    # Filtres optionnels
    centre = models.ForeignKey('Centre', null=True, blank=True, on_delete=models.SET_NULL, verbose_name="Centre")
    type_offre = models.ForeignKey('TypeOffre', null=True, blank=True, on_delete=models.SET_NULL, verbose_name="Type d'offre")
    statut = models.ForeignKey('Statut', null=True, blank=True, on_delete=models.SET_NULL, verbose_name="Statut")
    
    # Données du rapport
    donnees = models.JSONField(default=dict, verbose_name="Données du rapport")
    
    # Métadonnées
    date_generation = models.DateTimeField(default=timezone.now, verbose_name="Date de génération")
    utilisateur = models.ForeignKey('auth.User', null=True, blank=True, on_delete=models.SET_NULL, verbose_name="Généré par")
    temps_generation = models.FloatField(null=True, blank=True, verbose_name="Temps de génération (s)")
    
    class Meta:
        verbose_name = "Rapport"
        verbose_name_plural = "Rapports"
        ordering = ['-date_generation']
        
    def __str__(self):
        return f"{self.nom} - {self.get_type_rapport_display()} ({self.date_debut} à {self.date_fin})"


================================================
File: rap_app/models/recherches.py
================================================
# models/recherches.py
from django.db import models

from .types_offre import TypeOffre
from .base import BaseModel
from .centres import Centre
from .statut import Statut


class Recherche(BaseModel):
    """
    Modèle de suivi des recherches effectuées par les utilisateurs.

    Ce modèle stocke les termes de recherche, les filtres appliqués et d'autres 
    métadonnées comme l'adresse IP, le User-Agent et le nombre de résultats obtenus.
    
    Hérite de `BaseModel`, qui ajoute automatiquement :
    - `created_at` : Date et heure de création de la recherche.
    - `updated_at` : Date et heure de la dernière modification.
    """



    terme_recherche = models.CharField(
        max_length=255, 
        verbose_name="Terme de recherche",
        null=True,
        blank=True
    )
    """
    Chaîne de texte recherchée par l'utilisateur.
    Peut être vide si l'utilisateur a uniquement utilisé des filtres.
    """

    # Filtres appliqués par l'utilisateur
    filtre_centre = models.ForeignKey(
        Centre,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="recherches",
        verbose_name="Centre filtré"
    )
    """
    Filtre sur un centre de formation spécifique.
    """

    filtre_type_offre = models.ForeignKey(
        TypeOffre,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="recherches",
        verbose_name="Type d'offre filtré"
    )
    """
    Filtre sur un type d'offre spécifique.
    """

    filtre_statut = models.ForeignKey(
        Statut,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="recherches",
        verbose_name="Statut filtré"
    )
    """
    Filtre sur un statut spécifique de formation.
    """

    # Dates utilisées comme filtres
    date_debut = models.DateField(null=True, blank=True, verbose_name="Date de début filtrée")
    """
    Date minimale pour filtrer les résultats (ex: formations commençant après cette date).
    """

    date_fin = models.DateField(null=True, blank=True, verbose_name="Date de fin filtrée")
    """
    Date maximale pour filtrer les résultats (ex: formations se terminant avant cette date).
    """

    # Informations sur les résultats de la recherche
    nombre_resultats = models.PositiveIntegerField(default=0, verbose_name="Nombre de résultats obtenus")
    """
    Nombre total de résultats obtenus après exécution de la recherche.
    """

    temps_execution = models.FloatField(null=True, blank=True, verbose_name="Temps d'exécution (ms)")
    """
    Temps d'exécution de la requête en millisecondes (utile pour optimiser les performances).
    """





    @property
    def a_trouve_resultats(self):
        """
        Indique si la recherche a retourné des résultats.

        Retourne `True` si au moins un résultat a été trouvé, sinon `False`.
        """
        return self.nombre_resultats > 0

    def __str__(self):
        """
        Représentation textuelle de la recherche pour l'affichage dans l'admin.
        """
        terme = self.terme_recherche or "Sans terme"
        utilisateur = self.utilisateur or "Anonyme"
        return f"Recherche '{terme}' par {utilisateur} ({self.nombre_resultats} résultats)"

    class Meta:
        verbose_name = "Recherche"
        verbose_name_plural = "Recherches"
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['terme_recherche']),
            models.Index(fields=['created_at']),
            models.Index(fields=['nombre_resultats']),
        ]
    """
    - Trie les recherches par date de création (les plus récentes en premier).
    - Ajoute des index pour optimiser les recherches sur `terme_recherche`, `created_at` et `nombre_resultats`.
    """



================================================
File: rap_app/models/statut.py
================================================
# models/statut.py
from django.db import models
from django.core.exceptions import ValidationError
from .base import BaseModel

def get_default_color(statut_nom):
    """
    Retourne une couleur prédéfinie selon le type de statut.
    """
    COULEURS_PREDEFINIES = {
        'non_defini': "#FFEB3B",  # 🟡 Jaune (texte noir lisible)
        'recrutement_en_cours': "#4CAF50", # Vert
        'formation_en_cours': "#2196F3",  # Bleu
        'formation_a_annuler': "#FF9800",