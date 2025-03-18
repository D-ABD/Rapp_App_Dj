Directory structure:
└── d-abd-rapp_app_dj.git/
    ├── README.md
    ├── __init__.py
    ├── db.sqlite3
    ├── fichier
    ├── formation.js
    ├── manage.py
    ├── requirements.txt
    ├── un
    ├── vide
    ├── .!63787!db.sqlite3
    ├── .!63801!db.sqlite3
    ├── rap_app/
    │   ├── __init__.py
    │   ├── apps.py
    │   ├── urls.py
    │   ├── .DS_Store
    │   ├── __pycache__/
    │   ├── admin/
    │   │   ├── __init__.py
    │   │   ├── centres_admin.py
    │   │   ├── commentaires_admin.py
    │   │   ├── documents_admin.py
    │   │   ├── evenements_admin.py
    │   │   ├── formations_admin.py
    │   │   ├── partenaires_admin.py
    │   │   ├── recherches_admin.py
    │   │   ├── statuts_admin.py
    │   │   ├── types_offre_admin.py
    │   │   ├── utilisateurs_admin.py
    │   │   └── __pycache__/
    │   ├── forms/
    │   │   └── __init__.py
    │   ├── migrations/
    │   │   ├── 0001_initial.py
    │   │   ├── 0002_alter_partenaire_nom.py
    │   │   ├── 0003_alter_rapport_options_remove_rapport_created_at_and_more.py
    │   │   ├── 0004_alter_rapport_options_and_more.py
    │   │   ├── 0005_alter_rapport_options_remove_rapport_centre_and_more.py
    │   │   ├── 0006_delete_rapport.py
    │   │   ├── __init__.py
    │   │   └── __pycache__/
    │   ├── models/
    │   │   ├── __init__.py
    │   │   ├── base.py
    │   │   ├── centres.py
    │   │   ├── commentaires.py
    │   │   ├── documents.py
    │   │   ├── evenements.py
    │   │   ├── formations.py
    │   │   ├── historique_formations.py
    │   │   ├── models.md
    │   │   ├── partenaires.py
    │   │   ├── recherches.py
    │   │   ├── statut.py
    │   │   ├── types_offre.py
    │   │   └── __pycache__/
    │   ├── static/
    │   │   ├── __init__.py
    │   │   ├── images/
    │   │   └── js/
    │   │       └── formation.js
    │   ├── templates/
    │   │   ├── base.html
    │   │   ├── dashboard.html
    │   │   ├── home.html
    │   │   ├── centres/
    │   │   │   ├── centre_confirm_delete.html
    │   │   │   ├── centre_detail.html
    │   │   │   ├── centre_form.html
    │   │   │   └── centre_list.html
    │   │   ├── commentaires/
    │   │   │   ├── commentaire_confirm.html
    │   │   │   ├── commentaire_detail.html
    │   │   │   ├── commentaire_form.html
    │   │   │   └── commentaire_list.html
    │   │   ├── composants/
    │   │   │   ├── bouton_retour.html
    │   │   │   ├── commentaires_bouton.html
    │   │   │   ├── footer.html
    │   │   │   ├── navbar.html
    │   │   │   └── sidebar.html
    │   │   ├── dashboard_composants/
    │   │   │   ├── comments_list.html
    │   │   │   ├── events_by_type_and_center.html
    │   │   │   ├── evolution_chart.html
    │   │   │   ├── formations_by_type_and_statut.html
    │   │   │   ├── performance_table.html
    │   │   │   └── stats_cards.html
    │   │   ├── documents/
    │   │   │   ├── document_confirm_delete.html
    │   │   │   ├── document_detail.html
    │   │   │   ├── document_form.html
    │   │   │   └── document_list.html
    │   │   ├── evenements/
    │   │   │   ├── evenement_confirm_delete.html
    │   │   │   ├── evenement_detail.html
    │   │   │   ├── evenement_form.html
    │   │   │   └── evenement_list.html
    │   │   ├── formations/
    │   │   │   ├── commentaires_tous.html
    │   │   │   ├── formation_add_comment.html
    │   │   │   ├── formation_confirm_delete.html
    │   │   │   ├── formation_detail copy.html
    │   │   │   ├── formation_detail.html
    │   │   │   ├── formation_form.html
    │   │   │   ├── formation_list.html
    │   │   │   ├── formation_update_partenaire.html
    │   │   │   └── includes/
    │   │   │       ├── commentaires_formation.html
    │   │   │       ├── create_new_formations.html
    │   │   │       ├── documents_formation.html
    │   │   │       ├── evenements_formation.html
    │   │   │       ├── filters_and_search_formations.html
    │   │   │       ├── formations_table.html
    │   │   │       ├── pagination.html
    │   │   │       ├── partenaires_formation.html
    │   │   │       ├── saturation_formation.html
    │   │   │       └── stats_formations.html
    │   │   ├── parametres/
    │   │   │   └── parametres.html
    │   │   ├── partenaires/
    │   │   │   ├── partenaire_confirm_delete.html
    │   │   │   ├── partenaire_detail.html
    │   │   │   ├── partenaire_form.html
    │   │   │   ├── partenaire_formation_form.html
    │   │   │   └── partenaire_list.html
    │   │   ├── statuts/
    │   │   │   ├── statut_confirm_delete.html
    │   │   │   ├── statut_detail.html
    │   │   │   ├── statut_form.html
    │   │   │   └── statut_list.html
    │   │   ├── types_offres/
    │   │   │   ├── typeoffre_confirm_delete.html
    │   │   │   ├── typeoffre_detail.html
    │   │   │   ├── typeoffre_form.html
    │   │   │   └── typeoffre_list.html
    │   │   └── users/
    │   │       ├── login.html
    │   │       ├── password_reset.html
    │   │       ├── password_reset_complete.html
    │   │       ├── password_reset_confirm.html
    │   │       ├── password_reset_done.html
    │   │       ├── profile.html
    │   │       ├── register.html
    │   │       └── user_list.html
    │   ├── templatetags/
    │   │   ├── __init__.py
    │   │   ├── custom_filters.py
    │   │   ├── form_filters.py
    │   │   └── __pycache__/
    │   ├── tests/
    │   │   ├── __init__.py
    │   │   ├── test_models.py
    │   │   ├── test_views.py
    │   │   └── tv.md
    │   └── views/
    │       ├── __init__.py
    │       ├── base_views.py
    │       ├── centres_views.py
    │       ├── commentaires_views.py
    │       ├── dashboard_views.py
    │       ├── documents_views.py
    │       ├── evenements_views.py
    │       ├── formations_views.py
    │       ├── home_views.py
    │       ├── parametres_views.py
    │       ├── partenaires_views.py
    │       ├── recherches_views.py
    │       ├── statuts_views.py
    │       ├── types_offre_views.py
    │       ├── users_views.py
    │       ├── views.md
    │       └── __pycache__/
    ├── rap_app_project/
    │   ├── __init__.py
    │   ├── asgi.py
    │   ├── settings.py
    │   ├── urls.py
    │   ├── wsgi.py
    │   └── __pycache__/
    └── staticfiles/
        ├── __init__.py
        ├── admin/
        │   ├── css/
        │   │   ├── autocomplete.css
        │   │   ├── base.css
        │   │   ├── changelists.css
        │   │   ├── dark_mode.css
        │   │   ├── dashboard.css
        │   │   ├── forms.css
        │   │   ├── login.css
        │   │   ├── nav_sidebar.css
        │   │   ├── responsive.css
        │   │   ├── responsive_rtl.css
        │   │   ├── rtl.css
        │   │   ├── widgets.css
        │   │   └── vendor/
        │   │       └── select2/
        │   │           ├── LICENSE-SELECT2.md
        │   │           └── select2.css
        │   ├── img/
        │   │   ├── LICENSE
        │   │   ├── README.txt
        │   │   └── gis/
        │   └── js/
        │       ├── actions.js
        │       ├── autocomplete.js
        │       ├── calendar.js
        │       ├── cancel.js
        │       ├── change_form.js
        │       ├── collapse.js
        │       ├── core.js
        │       ├── filters.js
        │       ├── inlines.js
        │       ├── jquery.init.js
        │       ├── nav_sidebar.js
        │       ├── popup_response.js
        │       ├── prepopulate.js
        │       ├── prepopulate_init.js
        │       ├── SelectBox.js
        │       ├── SelectFilter2.js
        │       ├── theme.js
        │       ├── urlify.js
        │       ├── admin/
        │       │   ├── DateTimeShortcuts.js
        │       │   └── RelatedObjectLookups.js
        │       └── vendor/
        │           ├── jquery/
        │           │   ├── jquery.js
        │           │   └── LICENSE.txt
        │           ├── select2/
        │           │   ├── LICENSE.md
        │           │   ├── select2.full.js
        │           │   └── i18n/
        │           │       ├── af.js
        │           │       ├── ar.js
        │           │       ├── az.js
        │           │       ├── bg.js
        │           │       ├── bn.js
        │           │       ├── bs.js
        │           │       ├── ca.js
        │           │       ├── cs.js
        │           │       ├── da.js
        │           │       ├── de.js
        │           │       ├── dsb.js
        │           │       ├── el.js
        │           │       ├── en.js
        │           │       ├── es.js
        │           │       ├── et.js
        │           │       ├── eu.js
        │           │       ├── fa.js
        │           │       ├── fi.js
        │           │       ├── fr.js
        │           │       ├── gl.js
        │           │       ├── he.js
        │           │       ├── hi.js
        │           │       ├── hr.js
        │           │       ├── hsb.js
        │           │       ├── hu.js
        │           │       ├── hy.js
        │           │       ├── id.js
        │           │       ├── is.js
        │           │       ├── it.js
        │           │       ├── ja.js
        │           │       ├── ka.js
        │           │       ├── km.js
        │           │       ├── ko.js
        │           │       ├── lt.js
        │           │       ├── lv.js
        │           │       ├── mk.js
        │           │       ├── ms.js
        │           │       ├── nb.js
        │           │       ├── ne.js
        │           │       ├── nl.js
        │           │       ├── pl.js
        │           │       ├── ps.js
        │           │       ├── pt-BR.js
        │           │       ├── pt.js
        │           │       ├── ro.js
        │           │       ├── ru.js
        │           │       ├── sk.js
        │           │       ├── sl.js
        │           │       ├── sq.js
        │           │       ├── sr-Cyrl.js
        │           │       ├── sr.js
        │           │       ├── sv.js
        │           │       ├── th.js
        │           │       ├── tk.js
        │           │       ├── tr.js
        │           │       ├── uk.js
        │           │       ├── vi.js
        │           │       ├── zh-CN.js
        │           │       └── zh-TW.js
        │           └── xregexp/
        │               ├── LICENSE.txt
        │               └── xregexp.js
        └── js/
            ├── formation.js
            └── formations.js


Files Content:

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
   
    # Paramètres
    path('parametres/', parametres, name='parametres'),


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
File: rap_app/forms/__init__.py
================================================



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
from .historique_formations import HistoriqueFormation
from .recherches import Recherche

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



================================================
File: rap_app/models/historique_formations.py
================================================
import datetime
from django.db import models
from django.utils.timezone import now
from django.contrib.auth import get_user_model
from .base import BaseModel
from .formations import Formation

User = get_user_model()

class HistoriqueFormation(BaseModel):
    formation = models.ForeignKey(
        Formation, on_delete=models.CASCADE, null=True, blank=True, 
        related_name="historique_formations", verbose_name="Formation concernée"
    )
    utilisateur = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True, 
        related_name="historique_utilisateurs", verbose_name="Utilisateur ayant modifié"
    )

    action = models.CharField(max_length=255, verbose_name="Action effectuée")

    ancien_statut = models.CharField(max_length=100, null=True, blank=True, verbose_name="Statut avant modification")
    nouveau_statut = models.CharField(max_length=100, null=True, blank=True, verbose_name="Statut après modification")

    details = models.JSONField(null=True, blank=True, verbose_name="Détails des modifications")

    inscrits_total = models.PositiveIntegerField(null=True, blank=True, verbose_name="Total inscrits")
    inscrits_crif = models.PositiveIntegerField(null=True, blank=True, verbose_name="Inscrits CRIF")
    inscrits_mp = models.PositiveIntegerField(null=True, blank=True, verbose_name="Inscrits MP")
    total_places = models.PositiveIntegerField(null=True, blank=True, verbose_name="Total places")
    saturation = models.FloatField(null=True, blank=True, verbose_name="Niveau de saturation (%)")
    taux_remplissage = models.FloatField(null=True, blank=True, verbose_name="Taux de remplissage (%)")

    semaine = models.PositiveIntegerField(null=True, blank=True, verbose_name="Numéro de la semaine")
    mois = models.PositiveIntegerField(null=True, blank=True, verbose_name="Mois")
    annee = models.PositiveIntegerField(null=True, blank=True, verbose_name="Année")

    def save(self, *args, **kwargs):
        """
        Personnalisation de la sauvegarde :
        - Récupère les valeurs dynamiques de la formation
        - Convertit les données avant enregistrement pour éviter les erreurs JSON
        """
        if self.formation:
            # 🔥 Calcul dynamique des valeurs issues de `Formation`
            self.total_places = (self.formation.prevus_crif or 0) + (self.formation.prevus_mp or 0)
            self.inscrits_total = (self.formation.inscrits_crif or 0) + (self.formation.inscrits_mp or 0)
            self.inscrits_crif = self.formation.inscrits_crif
            self.inscrits_mp = self.formation.inscrits_mp
            self.saturation = (self.inscrits_total / self.total_places) * 100 if self.total_places > 0 else 0
            self.taux_remplissage = (self.inscrits_total / self.total_places) * 100 if self.total_places > 0 else 0

            # ✅ Stocke les valeurs temporelles si elles ne sont pas encore définies
            if not self.semaine:
                self.semaine = self.created_at.isocalendar()[1]
            if not self.mois:
                self.mois = self.created_at.month
            if not self.annee:
                self.annee = self.created_at.year

            # ✅ Convertit toutes les données en format JSON-safe
            self.details = self._serialize_details(self.formation.to_serializable_dict())

        super().save(*args, **kwargs)

    def _serialize_details(self, details):
        """
        Convertit les objets non sérialisables (ex: dates) en chaînes de caractères JSON-compatibles.
        """
        def convert_value(value):
            if isinstance(value, (datetime.date, datetime.datetime)):
                return value.strftime('%Y-%m-%d %H:%M:%S')  # ✅ Format JSON-compatible
            return value  # Garde les autres valeurs inchangées

        return {key: convert_value(value) for key, value in details.items()}

    class Meta:
        verbose_name = "Historique de formation"
        verbose_name_plural = "Historiques des formations"
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['created_at']),
            models.Index(fields=['action']),
            models.Index(fields=['formation']),
        ]

    def __str__(self):
        return f"{self.formation.nom if self.formation else 'Formation inconnue'} - {self.created_at.strftime('%Y-%m-%d')}"


================================================
File: rap_app/models/models.md
================================================
Directory structure:
└── d-abd-rapp_app_dj.git/
    ├── README.md
    ├── __init__.py
    ├── db.sqlite3
    ├── manage.py
    ├── requirements.txt
    ├── .!63787!db.sqlite3
    ├── .!63801!db.sqlite3
    ├── formations/
    │   └── documents/
    ├── rap_app/
    │   ├── __init__.py
    │   ├── apps.py
    │   ├── urls.py
    │   ├── .DS_Store
    │   ├── __pycache__/
    │   ├── admin/
    │   │   ├── __init__.py
    │   │   ├── centres_admin.py
    │   │   ├── commentaires_admin.py
    │   │   ├── documents_admin.py
    │   │   ├── evenements_admin.py
    │   │   ├── formations_admin.py
    │   │   ├── parametres_admin.py
    │   │   ├── partenaires_admin.py
    │   │   ├── recherches_admin.py
    │   │   ├── statuts_admin.py
    │   │   ├── types_offre_admin.py
    │   │   ├── utilisateurs_admin.py
    │   │   └── __pycache__/
    │   ├── forms/
    │   │   └── __init__.py
    │   ├── migrations/
    │   │   ├── 0001_initial.py
    │   │   ├── 0002_alter_partenaire_nom.py
    │   │   ├── 0003_alter_rapport_options_remove_rapport_created_at_and_more.py
    │   │   ├── 0004_alter_rapport_options_and_more.py
    │   │   ├── 0005_alter_rapport_options_remove_rapport_centre_and_more.py
    │   │   ├── 0006_delete_rapport.py
    │   │   ├── __init__.py
    │   │   └── __pycache__/
    │   ├── models/
    │   │   ├── __init__.py
    │   │   ├── base.py
    │   │   ├── centres.py
    │   │   ├── commentaires.py
    │   │   ├── documents.py
    │   │   ├── evenements.py
    │   │   ├── formations.py
    │   │   ├── historique_formations.py
    │   │   ├── models.md
    │   │   ├── parametres.py
    │   │   ├── partenaires.py
    │   │   ├── recherches.py
    │   │   ├── statut.py
    │   │   ├── types_offre.py
    │   │   └── __pycache__/
    │   ├── static/
    │   │   └── __init__.py
    │   ├── templates/
    │   │   ├── base.html
    │   │   ├── home.html
    │   │   ├── centres/
    │   │   │   ├── centre_confirm_delete.html
    │   │   │   ├── centre_detail.html
    │   │   │   ├── centre_form.html
    │   │   │   └── centre_list.html
    │   │   ├── commentaires/
    │   │   │   ├── commentaire_confirm.html
    │   │   │   ├── commentaire_detail.html
    │   │   │   ├── commentaire_form.html
    │   │   │   └── commentaire_list.html
    │   │   ├── composants/
    │   │   │   ├── bouton_retour.html
    │   │   │   ├── footer.html
    │   │   │   ├── navbar.html
    │   │   │   └── sidebar.html
    │   │   ├── documents/
    │   │   │   ├── document_confirm_delete.html
    │   │   │   ├── document_detail.html
    │   │   │   ├── document_form.html
    │   │   │   └── document_list.html
    │   │   ├── evenements/
    │   │   │   ├── evenement_confirm_delete.html
    │   │   │   ├── evenement_detail.html
    │   │   │   ├── evenement_form.html
    │   │   │   └── evenement_list.html
    │   │   ├── formations/
    │   │   │   ├── formation_add_comment.html
    │   │   │   ├── formation_confirm_delete.html
    │   │   │   ├── formation_detail.html
    │   │   │   ├── formation_form.html
    │   │   │   ├── formation_list.html
    │   │   │   └── formation_update_partenaire.html
    │   │   ├── includes/
    │   │   │   └── pagination.html
    │   │   ├── partenaires/
    │   │   │   ├── partenaire_confirm_delete.html
    │   │   │   ├── partenaire_detail.html
    │   │   │   ├── partenaire_form.html
    │   │   │   ├── partenaire_formation_form.html
    │   │   │   └── partenaire_list.html
    │   │   ├── rapports/
    │   │   │   ├── rapport_detail.html
    │   │   │   ├── rapport_form.html
    │   │   │   └── rapports.html
    │   │   ├── statuts/
    │   │   │   ├── statut_confirm_delete.html
    │   │   │   ├── statut_detail.html
    │   │   │   ├── statut_form.html
    │   │   │   └── statut_list.html
    │   │   └── types_offres/
    │   │       ├── typeoffre_confirm_delete.html
    │   │       ├── typeoffre_detail.html
    │   │       ├── typeoffre_form.html
    │   │       └── typeoffre_list.html
    │   ├── templatetags/
    │   │   ├── __init__.py
    │   │   ├── custom_filters.py
    │   │   └── __pycache__/
    │   ├── tests/
    │   │   ├── __init__.py
    │   │   ├── test_models.py
    │   │   ├── test_views.py
    │   │   └── tv.md
    │   └── views/
    │       ├── __init__.py
    │       ├── base_views.py
    │       ├── centres_views.py
    │       ├── commentaires_views.py
    │       ├── dashboard_views.py
    │       ├── documents_views.py
    │       ├── evenements_views.py
    │       ├── formations_views.py
    │       ├── home_views.py
    │       ├── parametres_views.py
    │       ├── partenaires_views.py
    │       ├── recherches_views.py
    │       ├── statuts_views.py
    │       ├── types_offre_views.py
    │       ├── views.md
    │       └── __pycache__/
    └── rap_app_project/
        ├── __init__.py
        ├── asgi.py
        ├── settings.py
        ├── urls.py
        ├── wsgi.py
        └── __pycache__/


Files Content:

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

from .views import (
    home_views, centres_views, statuts_views, types_offre_views,
    commentaires_views, documents_views, partenaires_views, evenements_views, formations_views
)  # Import des vues

urlpatterns = [
    # Page d'accueil
    path('', home_views.home, name='home'),

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
    path('formations/<int:pk>/', formations_views.FormationDetailView.as_view(), name='formation-detail'),
    path('formations/ajouter/', formations_views.FormationCreateView.as_view(), name='formation-create'),
    path('formations/<int:pk>/modifier/', formations_views.FormationUpdateView.as_view(), name='formation-update'),
    path('formations/<int:pk>/supprimer/', formations_views.FormationDeleteView.as_view(), name='formation-delete'),
    path('formations/<int:pk>/commentaire/', formations_views.FormationAddCommentView.as_view(), name='formation-add-comment'),
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
from .parametres_admin import ParametreAdmin
from .recherches_admin import RechercheAdmin
from .partenaires_admin import PartenaireAdmin  # Nouveau
from .evenements_admin import EvenementAdmin    # Nouveau
from .documents_admin import DocumentAdmin      # Nouveau




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
        if obj.fichier and obj.fichier.size:
            return f"{obj.fichier.size / 1024:.2f} Ko"
        return "-"
    
    taille_fichier.short_description = "Taille du fichier"

    
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
File: rap_app/admin/parametres_admin.py
================================================
from django.contrib import admin
from ..models import Parametre


@admin.register(Parametre)
class ParametreAdmin(admin.ModelAdmin):
    list_display = ('cle', 'valeur_preview', 'description_preview', 'updated_at')
    search_fields = ('cle', 'valeur', 'description')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Paramètre', {
            'fields': ('cle', 'valeur', 'description')
        }),
        ('Métadonnées', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def valeur_preview(self, obj):
        # Tronquer la valeur si elle est trop longue
        preview = obj.valeur[:50] + ('...' if len(obj.valeur) > 50 else '')
        return preview
    valeur_preview.short_description = 'Valeur'

    def description_preview(self, obj):
        if obj.description:
            # Tronquer la description si elle est trop longue
            preview = obj.description[:50] + ('...' if len(obj.description) > 50 else '')
            return preview
        return "-"
    description_preview.short_description = 'Description'


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
File: rap_app/forms/__init__.py
================================================



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
from .historique_formations import HistoriqueFormation
from .parametres import Parametre
from .recherches import Recherche

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
    'Parametre',
    'Recherche',
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
        Exemple d'usage : affichage dans une liste ou recherche avancée.
        """
        return f"{self.nom} ({self.code_postal})" if self.code_postal else self.nom

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


@receiver(post_save, sender=Commentaire)
def update_formation_saturation(sender, instance, **kwargs):
    """
    Met à jour la `saturation` de la formation avec la dernière valeur de saturation du commentaire.
    Met également à jour le `dernier_commentaire` pour un affichage rapide.
    """
    if instance.formation:
        # Mise à jour directe via update() pour court-circuiter les méthodes save()
        updates = {}
        
        if instance.saturation is not None:
            updates['saturation'] = instance.saturation
        
        # Récupérer le dernier commentaire
        dernier_commentaire = Commentaire.objects.filter(formation=instance.formation).order_by('-created_at').first()
        updates['dernier_commentaire'] = dernier_commentaire.contenu if dernier_commentaire else None
        
        # Appliquer toutes les mises à jour en une seule opération
        if updates:
            Formation.objects.filter(id=instance.formation.id).update(**updates)

@receiver(post_delete, sender=Commentaire)
def handle_commentaire_delete(sender, instance, **kwargs):
    """
    Met à jour la formation après la suppression d'un commentaire :
    - Met à jour le `dernier_commentaire` avec le commentaire précédent s'il en reste un.
    """
    if instance.formation:
        # Récupérer directement le dernier commentaire à partir du modèle
        dernier_commentaire = Commentaire.objects.filter(formation=instance.formation).order_by('-created_at').first()
        Formation.objects.filter(id=instance.formation.id).update(
            dernier_commentaire=dernier_commentaire.contenu if dernier_commentaire else None
        )


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
from pyexpat.errors import messages
from xml.dom.minidom import Document
from django.db import models
from django.http import HttpResponseBadRequest
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils import timezone
from jsonschema import ValidationError

from .partenaires import Partenaire

from .centres import Centre
from .types_offre import TypeOffre
from .base import BaseModel
from .statut import Statut

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



================================================
File: rap_app/models/historique_formations.py
================================================
import datetime
from django.db import models
from django.utils.timezone import now
from django.contrib.auth import get_user_model
from .base import BaseModel
from .formations import Formation

User = get_user_model()

class HistoriqueFormation(BaseModel):
    formation = models.ForeignKey(
        Formation, on_delete=models.CASCADE, null=True, blank=True, 
        related_name="historique_formations", verbose_name="Formation concernée"
    )
    utilisateur = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True, 
        related_name="historique_utilisateurs", verbose_name="Utilisateur ayant modifié"
    )

    action = models.CharField(max_length=255, verbose_name="Action effectuée")

    ancien_statut = models.CharField(max_length=100, null=True, blank=True, verbose_name="Statut avant modification")
    nouveau_statut = models.CharField(max_length=100, null=True, blank=True, verbose_name="Statut après modification")

    details = models.JSONField(null=True, blank=True, verbose_name="Détails des modifications")

    inscrits_total = models.PositiveIntegerField(null=True, blank=True, verbose_name="Total inscrits")
    inscrits_crif = models.PositiveIntegerField(null=True, blank=True, verbose_name="Inscrits CRIF")
    inscrits_mp = models.PositiveIntegerField(null=True, blank=True, verbose_name="Inscrits MP")
    total_places = models.PositiveIntegerField(null=True, blank=True, verbose_name="Total places")
    saturation = models.FloatField(null=True, blank=True, verbose_name="Niveau de saturation (%)")
    taux_remplissage = models.FloatField(null=True, blank=True, verbose_name="Taux de remplissage (%)")

    semaine = models.PositiveIntegerField(null=True, blank=True, verbose_name="Numéro de la semaine")
    mois = models.PositiveIntegerField(null=True, blank=True, verbose_name="Mois")
    annee = models.PositiveIntegerField(null=True, blank=True, verbose_name="Année")

    def save(self, *args, **kwargs):
        """
        Personnalisation de la sauvegarde :
        - Récupère les valeurs dynamiques de la formation
        - Convertit les données avant enregistrement pour éviter les erreurs JSON
        """
        if self.formation:
            # 🔥 Calcul dynamique des valeurs issues de `Formation`
            self.total_places = (self.formation.prevus_crif or 0) + (self.formation.prevus_mp or 0)
            self.inscrits_total = (self.formation.inscrits_crif or 0) + (self.formation.inscrits_mp or 0)
            self.inscrits_crif = self.formation.inscrits_crif
            self.inscrits_mp = self.formation.inscrits_mp
            self.saturation = (self.inscrits_total / self.total_places) * 100 if self.total_places > 0 else 0
            self.taux_remplissage = (self.inscrits_total / self.total_places) * 100 if self.total_places > 0 else 0

            # ✅ Stocke les valeurs temporelles si elles ne sont pas encore définies
            if not self.semaine:
                self.semaine = self.created_at.isocalendar()[1]
            if not self.mois:
                self.mois = self.created_at.month
            if not self.annee:
                self.annee = self.created_at.year

            # ✅ Convertit toutes les données en format JSON-safe
            self.details = self._serialize_details(self.formation.to_serializable_dict())

        super().save(*args, **kwargs)

    def _serialize_details(self, details):
        """
        Convertit les objets non sérialisables (ex: dates) en chaînes de caractères JSON-compatibles.
        """
        def convert_value(value):
            if isinstance(value, (datetime.date, datetime.datetime)):
                return value.strftime('%Y-%m-%d %H:%M:%S')  # ✅ Format JSON-compatible
            return value  # Garde les autres valeurs inchangées

        return {key: convert_value(value) for key, value in details.items()}

    class Meta:
        verbose_name = "Historique de formation"
        verbose_name_plural = "Historiques des formations"
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['created_at']),
            models.Index(fields=['action']),
            models.Index(fields=['formation']),
        ]

    def __str__(self):
        return f"{self.formation.nom if self.formation else 'Formation inconnue'} - {self.created_at.strftime('%Y-%m-%d')}"



================================================
File: rap_app/models/models.md
================================================
from django.db import models


class BaseModel(models.Model):
    """Modèle de base avec champs communs"""
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Dernière mise à jour")

    class Meta:
        abstract = True

----------------------------------------------------------------------
----------------------------------------------------------------------
from django.db import models
from django.core.validators import RegexValidator
from django.urls import reverse
from .base import BaseModel


class Centre(BaseModel):
    """Centre de formation"""
    nom = models.CharField(max_length=255, verbose_name="Nom du centre")
    code_postal = models.CharField(
        max_length=10, 
        null=True, 
        blank=True, 
        verbose_name="Code postal",
        validators=[RegexValidator(regex=r'^\d{5}$', message="Le code postal doit contenir 5 chiffres")]
    )

    def __str__(self):
        return self.nom

    def get_absolute_url(self):
        return reverse('centre-detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Centre"
        verbose_name_plural = "Centres"
        ordering = ['nom']
        indexes = [models.Index(fields=['nom'])]

----------------------------------------------------------------------
----------------------------------------------------------------------
from django.db import models
from .base import BaseModel
from .formations import Formation
from .utilisateurs import Utilisateur


class Commentaire(BaseModel):
    """Commentaires sur les formations"""
    formation = models.ForeignKey(
        Formation, 
        on_delete=models.CASCADE, 
        related_name="commentaires", 
        verbose_name="Formation"
    )
    auteur = models.CharField(max_length=255, verbose_name="Auteur du commentaire", blank=True)
    contenu = models.TextField(verbose_name="Contenu du commentaire")
    utilisateur = models.ForeignKey(
        Utilisateur, 
        on_delete=models.CASCADE, 
        related_name="commentaires", 
        verbose_name="Utilisateur associé"
    )

    def __str__(self):
        return f"Commentaire de {self.utilisateur} pour la formation {self.formation.nom}"
    
    class Meta:
        verbose_name = "Commentaire"
        verbose_name_plural = "Commentaires"
        ordering = ['-created_at']

----------------------------------------------------------------------
----------------------------------------------------------------------
from django.db import models
from .base import BaseModel
from .formations import Formation


class Document(BaseModel):
    """Documents liés aux formations"""
    formation = models.ForeignKey(
        Formation, 
        on_delete=models.CASCADE, 
        related_name="documents", 
        verbose_name="Formation associée"
    )
    nom_fichier = models.CharField(max_length=255, verbose_name="Nom du fichier")
    fichier = models.FileField(upload_to='formations/documents/', verbose_name="Fichier")
    source = models.TextField(null=True, blank=True, verbose_name="Source du document")

    def __str__(self):
        return self.nom_fichier

    class Meta:
        verbose_name = "Document"
        verbose_name_plural = "Documents"
        ordering = ['-created_at']

----------------------------------------------------------------------
----------------------------------------------------------------------
from django.db import models
from django.core.exceptions import ValidationError
from .base import BaseModel
from .formations import Formation
from .ressources import Ressource


class Evenement(BaseModel):
    """Événements liés aux formations"""
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
        (JPO, 'JPO'),
        (AUTRE, 'Autre'),
    ]

    formation = models.ForeignKey(
        Formation, 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True, 
        related_name="evenements"
    )
    type_evenement = models.CharField(max_length=100, choices=TYPE_EVENEMENT_CHOICES, verbose_name="Type d'événement")
    details = models.TextField(null=True, blank=True, verbose_name="Détails de l'événement")
    event_date = models.DateField(verbose_name="Date de l'événement")
    description_autre = models.CharField(
        max_length=255, 
        null=True, 
        blank=True, 
        verbose_name="Description de l'autre événement"
    )

    def clean(self):
        """Validation personnalisée pour les événements de type 'autre'"""
        if self.type_evenement == self.AUTRE and not self.description_autre:
            raise ValidationError({
                'description_autre': "Veuillez fournir une description pour l'événement 'Autre'."
            })

    def save(self, *args, **kwargs):
        self.full_clean()
        is_new = self.pk is None
        super().save(*args, **kwargs)
        
        # Mettre à jour le nombre d'événements dans Ressource si c'est un nouvel événement
        if is_new and self.formation:
            ressource, created = Ressource.objects.get_or_create(formation=self.formation)
            ressource.nombre_evenements = Evenement.objects.filter(formation=self.formation).count()
            ressource.save(update_fields=['nombre_evenements', 'updated_at'])

    class Meta:
        verbose_name = "Événement"
        verbose_name_plural = "Événements"
        ordering = ['-event_date']
        indexes = [models.Index(fields=['event_date'])]

    def __str__(self):
        return f"{self.get_type_evenement_display()} - {self.event_date}"

----------------------------------------------------------------------
----------------------------------------------------------------------
from django.db import models
from django.core.exceptions import ValidationError
from django.urls import reverse
from django.utils import timezone

from .centres import Centre
from .types_offre import TypeOffre
from .base import BaseModel
from .statut import Statut


class FormationManager(models.Manager):
    """Manager personnalisé pour le modèle Formation"""
    def formations_actives(self):
        """Récupère les formations actives (non terminées)"""
        return self.filter(
            models.Q(end_date__gt=timezone.now()) | 
            models.Q(end_date__isnull=True)
        )
    
    def formations_a_venir(self):
        """Récupère les formations à venir"""
        return self.filter(start_date__gt=timezone.now())
    
    def formations_terminees(self):
        """Récupère les formations terminées"""
        return self.filter(end_date__lt=timezone.now())


class Formation(BaseModel):
    """Modèle principal des formations"""
    nom = models.CharField(max_length=255, verbose_name="Nom de la formation")
    centre = models.ForeignKey(
        Centre, 
        on_delete=models.CASCADE, 
        related_name='formations', 
        verbose_name="Centre de formation"
    )
    type_offre = models.ForeignKey(
        TypeOffre, 
        on_delete=models.CASCADE, 
        related_name="formations", 
        verbose_name="Type d'offre"
    )
    statut = models.ForeignKey(
        Statut, 
        on_delete=models.CASCADE, 
        related_name="formations", 
        verbose_name="Statut de la formation"
    )
    start_date = models.DateField(null=True, blank=True, verbose_name="Date de début")
    end_date = models.DateField(null=True, blank=True, verbose_name="Date de fin")
    num_kairos = models.CharField(max_length=50, null=True, blank=True, verbose_name="Numéro Kairos")
    num_offre = models.CharField(max_length=50, null=True, blank=True, verbose_name="Numéro de l'offre")
    num_produit = models.CharField(max_length=50, null=True, blank=True, verbose_name="Numéro du produit")
    prevus_crif = models.PositiveIntegerField(verbose_name="Prévus CRIF", default=0)
    prevus_mp = models.PositiveIntegerField(verbose_name="Prévus MP", default=0)
    inscrits_crif = models.PositiveIntegerField(default=0, verbose_name="Inscrits CRIF")
    inscrits_mp = models.PositiveIntegerField(default=0, verbose_name="Inscrits MP")
    assistante = models.CharField(max_length=255, null=True, blank=True, verbose_name="Assistante responsable")
    cap = models.PositiveIntegerField(null=True, blank=True, verbose_name="Capacité maximum")
    convocation_envoie = models.BooleanField(default=False, verbose_name="Convocation envoyée")
    entresformation = models.PositiveIntegerField(default=0, verbose_name="Entrées en formation")
    
    # Utilisation du manager personnalisé
    objects = FormationManager()
    
    @property
    def total_places(self):
        """Calcule le nombre total de places"""
        return self.prevus_crif + self.prevus_mp
    
    @property
    def inscrits_total(self):
        """Calcule le nombre total d'inscrits"""
        return self.inscrits_crif + self.inscrits_mp
    
    @property
    def a_recruter(self):
        """Calcule le nombre de personnes à recruter"""
        return max(0, self.total_places - self.inscrits_total)
    
    @property
    def taux_remplissage(self):
        """Calcule le taux de remplissage"""
        if self.total_places > 0:
            return (self.inscrits_total / self.total_places) * 100
        return 0
    
    @property
    def est_active(self):
        """Vérifie si la formation est active"""
        return not self.end_date or self.end_date >= timezone.now().date()
    
    def clean(self):
        """Validation personnalisée pour les dates"""
        if self.start_date and self.end_date and self.start_date > self.end_date:
            raise ValidationError({
                'end_date': "La date de fin ne peut pas être antérieure à la date de début."
            })
    
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('formation-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = "Formation"
        verbose_name_plural = "Formations"
        ordering = ['-start_date', 'nom']
        indexes = [
            models.Index(fields=['start_date']),
            models.Index(fields=['end_date']),
            models.Index(fields=['nom']),
        ]

----------------------------------------------------------------------
----------------------------------------------------------------------
from django.db import models
from .base import BaseModel
from .formations import Formation
from .utilisateurs import Utilisateur


class HistoriqueFormation(BaseModel):
    """Historique des modifications de formations"""
    formation = models.ForeignKey(
        Formation, 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True, 
        related_name="historique_formations"
    )
    utilisateur = models.ForeignKey(
        Utilisateur, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name="historique_utilisateurs"
    )
    action = models.CharField(max_length=255)
    ancien_statut = models.CharField(max_length=100, null=True, blank=True)
    nouveau_statut = models.CharField(max_length=100, null=True, blank=True)
    details = models.JSONField(null=True, blank=True)
    
    # Champs pour le suivi statistique
    inscrits_total = models.PositiveIntegerField(null=True, blank=True, verbose_name="Nombre d'inscrits total")
    inscrits_crif = models.PositiveIntegerField(null=True, blank=True, verbose_name="Nombre d'inscrits CRIF")
    inscrits_mp = models.PositiveIntegerField(null=True, blank=True, verbose_name="Nombre d'inscrits MP")
    total_places = models.PositiveIntegerField(null=True, blank=True, verbose_name="Nombre total de places")
    
    # Période de l'évolution
    semaine = models.PositiveIntegerField(null=True, blank=True, verbose_name="Semaine")
    mois = models.PositiveIntegerField(null=True, blank=True, verbose_name="Mois")
    annee = models.PositiveIntegerField(null=True, blank=True, verbose_name="Année")
    
    @property
    def taux_remplissage(self):
        """Calcule le taux de remplissage"""
        if self.total_places and self.total_places > 0 and self.inscrits_total is not None:
            return (self.inscrits_total / self.total_places) * 100
        return 0
    
    class Meta:
        verbose_name = "Historique de la formation"
        verbose_name_plural = "Historiques des formations"
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['created_at']),
            models.Index(fields=['action']),
        ]

    def __str__(self):
        return f"{self.formation.nom if self.formation else 'Formation inconnue'} - {self.created_at.strftime('%Y-%m-%d')}"

----------------------------------------------------------------------
----------------------------------------------------------------------
from django.db import models
from .base import BaseModel


class Parametre(BaseModel):
    """Paramètres généraux de l'application"""
    cle = models.CharField(max_length=100, unique=True)
    valeur = models.TextField()
    description = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.cle

    class Meta:
        verbose_name = "Paramètre"
        verbose_name_plural = "Paramètres"
        ordering = ['cle']

----------------------------------------------------------------------
----------------------------------------------------------------------
from django.db import models
from django.core.exceptions import ValidationError
from .base import BaseModel
from .formations import Formation


class Rapport(BaseModel):
    """Rapports périodiques sur les formations"""
    HEBDOMADAIRE = 'Hebdomadaire'
    MENSUEL = 'Mensuel'
    ANNUEL = 'Annuel'
    
    PERIODE_CHOICES = [
        (HEBDOMADAIRE, 'Hebdomadaire'),
        (MENSUEL, 'Mensuel'),
        (ANNUEL, 'Annuel'),
    ]
    
    formation = models.ForeignKey(
        Formation, 
        on_delete=models.CASCADE, 
        related_name="rapports", 
        null=True, 
        blank=True
    )
    periode = models.CharField(max_length=50, choices=PERIODE_CHOICES, verbose_name="Période du rapport")
    date_debut = models.DateField(verbose_name="Date de début de la période")
    date_fin = models.DateField(verbose_name="Date de fin de la période")
    total_inscrits = models.PositiveIntegerField(verbose_name="Total des inscrits", default=0)
    inscrits_crif = models.PositiveIntegerField(verbose_name="Inscrits CRIF", default=0)
    inscrits_mp = models.PositiveIntegerField(verbose_name="Inscrits MP", default=0)
    total_places = models.PositiveIntegerField(verbose_name="Total des places", default=0)
    nombre_evenements = models.PositiveIntegerField(verbose_name="Nombre d'événements", default=0)
    nombre_candidats = models.PositiveIntegerField(verbose_name="Nombre de candidats", default=0)
    nombre_entretiens = models.PositiveIntegerField(verbose_name="Nombre d'entretiens", default=0)
    
    @property
    def taux_remplissage(self):
        """Calcule le taux de remplissage"""
        if self.total_places > 0:
            return (self.total_inscrits / self.total_places) * 100
        return 0
    
    @property
    def taux_transformation(self):
        """Calcule le taux de transformation"""
        if self.nombre_candidats > 0:
            return (self.total_inscrits / self.nombre_candidats) * 100
        return 0
    
    def clean(self):
        """Validation personnalisée pour les dates"""
        if self.date_debut > self.date_fin:
            raise ValidationError({
                'date_fin': "La date de fin ne peut pas être antérieure à la date de début."
            })
    
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Rapport de formation"
        verbose_name_plural = "Rapports de formation"
        ordering = ['-date_fin']
        indexes = [
            models.Index(fields=['date_debut']),
            models.Index(fields=['date_fin']),
            models.Index(fields=['periode']),
        ]

    def __str__(self):
        return f"Rapport {self.formation.nom if self.formation else 'Global'} - {self.periode} ({self.date_debut} à {self.date_fin})"

----------------------------------------------------------------------
----------------------------------------------------------------------
from django.db import models
from django.core.exceptions import ValidationError
from .base import BaseModel
from .formations import Formation


class Rapport(BaseModel):
    """Rapports périodiques sur les formations"""
    HEBDOMADAIRE = 'Hebdomadaire'
    MENSUEL = 'Mensuel'
    ANNUEL = 'Annuel'
    
    PERIODE_CHOICES = [
        (HEBDOMADAIRE, 'Hebdomadaire'),
        (MENSUEL, 'Mensuel'),
        (ANNUEL, 'Annuel'),
    ]
    
    formation = models.ForeignKey(
        Formation, 
        on_delete=models.CASCADE, 
        related_name="rapports", 
        null=True, 
        blank=True
    )
    periode = models.CharField(max_length=50, choices=PERIODE_CHOICES, verbose_name="Période du rapport")
    date_debut = models.DateField(verbose_name="Date de début de la période")
    date_fin = models.DateField(verbose_name="Date de fin de la période")
    total_inscrits = models.PositiveIntegerField(verbose_name="Total des inscrits", default=0)
    inscrits_crif = models.PositiveIntegerField(verbose_name="Inscrits CRIF", default=0)
    inscrits_mp = models.PositiveIntegerField(verbose_name="Inscrits MP", default=0)
    total_places = models.PositiveIntegerField(verbose_name="Total des places", default=0)
    nombre_evenements = models.PositiveIntegerField(verbose_name="Nombre d'événements", default=0)
    nombre_candidats = models.PositiveIntegerField(verbose_name="Nombre de candidats", default=0)
    nombre_entretiens = models.PositiveIntegerField(verbose_name="Nombre d'entretiens", default=0)
    
    @property
    def taux_remplissage(self):
        """Calcule le taux de remplissage"""
        if self.total_places > 0:
            return (self.total_inscrits / self.total_places) * 100
        return 0
    
    @property
    def taux_transformation(self):
        """Calcule le taux de transformation"""
        if self.nombre_candidats > 0:
            return (self.total_inscrits / self.nombre_candidats) * 100
        return 0
    
    def clean(self):
        """Validation personnalisée pour les dates"""
        if self.date_debut > self.date_fin:
            raise ValidationError({
                'date_fin': "La date de fin ne peut pas être antérieure à la date de début."
            })
    
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Rapport de formation"
        verbose_name_plural = "Rapports de formation"
        ordering = ['-date_fin']
        indexes = [
            models.Index(fields=['date_debut']),
            models.Index(fields=['date_fin']),
            models.Index(fields=['periode']),
        ]

    def __str__(self):
        return f"Rapport {self.formation.nom if self.formation else 'Global'} - {self.periode} ({self.date_debut} à {self.date_fin})"

----------------------------------------------------------------------
----------------------------------------------------------------------
from django.db import models

from .types_offre import TypeOffre
from .base import BaseModel
from .utilisateurs import Utilisateur
from .centres import Centre
from .statut import Statut


class Recherche(BaseModel):
    """Suivi des recherches effectuées par les utilisateurs"""
    utilisateur = models.ForeignKey(
        Utilisateur,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="recherches",
        verbose_name="Utilisateur"
    )
    terme_recherche = models.CharField(
        max_length=255, 
        verbose_name="Terme de recherche",
        null=True,
        blank=True
    )
    filtre_centre = models.ForeignKey(
        Centre,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="recherches",
        verbose_name="Centre filtré"
    )
    filtre_type_offre = models.ForeignKey(
        TypeOffre,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="recherches",
        verbose_name="Type d'offre filtré"
    )
    filtre_statut = models.ForeignKey(
        Statut,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="recherches",
        verbose_name="Statut filtré"
    )
    date_debut = models.DateField(null=True, blank=True, verbose_name="Date de début filtrée")
    date_fin = models.DateField(null=True, blank=True, verbose_name="Date de fin filtrée")
    nombre_resultats = models.PositiveIntegerField(default=0, verbose_name="Nombre de résultats obtenus")
    temps_execution = models.FloatField(null=True, blank=True, verbose_name="Temps d'exécution (ms)")
    adresse_ip = models.GenericIPAddressField(null=True, blank=True, verbose_name="Adresse IP")
    user_agent = models.TextField(null=True, blank=True, verbose_name="User Agent")
    
    @property
    def a_trouve_resultats(self):
        """Indique si la recherche a donné des résultats"""
        return self.nombre_resultats > 0
    
    def __str__(self):
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

----------------------------------------------------------------------
----------------------------------------------------------------------
from django.db import models
from .base import BaseModel
from .formations import Formation


class Ressource(BaseModel):
    """Ressources liées aux formations"""
    formation = models.OneToOneField(
        Formation, 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True, 
        related_name="ressource"
    )
    nombre_candidats = models.PositiveIntegerField(null=True, blank=True, verbose_name="Nombre de candidats")
    nombre_entretiens = models.PositiveIntegerField(null=True, blank=True, verbose_name="Nombre d'entretiens")
    nombre_evenements = models.PositiveIntegerField(default=0, verbose_name="Nombre d'événements")
    
    @property
    def nombre_inscrits(self):
        """Récupère le nombre d'inscrits de la formation associée"""
        return self.formation.inscrits_total if self.formation else 0
    
    @property
    def taux_transformation(self):
        """Calcule le taux de transformation"""
        if self.nombre_candidats and self.nombre_candidats > 0 and self.nombre_inscrits > 0:
            return (self.nombre_inscrits / self.nombre_candidats) * 100
        return 0
    
    def __str__(self):
        return f"Ressource pour {self.formation.nom if self.formation else 'Formation inconnue'}"

    class Meta:
        verbose_name = "Ressource"
        verbose_name_plural = "Ressources"

----------------------------------------------------------------------
----------------------------------------------------------------------
from django.db import models
from django.core.exceptions import ValidationError
from .base import BaseModel


class Statut(BaseModel):
    """Statut des formations"""
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
    
    nom = models.CharField(max_length=100, choices=STATUT_CHOICES, verbose_name="Nom du statut")
    couleur = models.CharField(max_length=20, verbose_name="Couleur", help_text="Format: #RRGGBB ou nom de couleur")
    description_autre = models.CharField(max_length=255, blank=True, null=True, verbose_name="Description personnalisée")
    
    def clean(self):
        """Validation personnalisée pour les statuts de type 'autre'"""
        if self.nom == self.AUTRE and not self.description_autre:
            raise ValidationError({
                'description_autre': "Le champ 'description_autre' doit être renseigné lorsque le statut est 'autre'."
            })

    def save(self, *args, **kwargs):
        self.full_clean()  # Appelle la méthode clean() avant la sauvegarde
        super().save(*args, **kwargs)

    def __str__(self):
        if self.nom == self.AUTRE and self.description_autre:
            return f"{self.description_autre} - {self.couleur}"
        return f"{self.get_nom_display()} - {self.couleur}"

    class Meta:
        verbose_name = "Statut"
        verbose_name_plural = "Statuts"
        ordering = ['nom']
----------------------------------------------------------------------
----------------------------------------------------------------------
from django.db import models
from django.core.exceptions import ValidationError
from .base import BaseModel


class TypeOffre(BaseModel):
    """Types d'offres de formation"""
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
    
    nom = models.CharField(max_length=100, choices=TYPE_OFFRE_CHOICES, default=NON_DEFINI, verbose_name="Type d'offre")
    autre = models.CharField(max_length=255, blank=True, null=True, verbose_name="Autre (personnalisé)")
    
    def clean(self):
        if self.nom == self.AUTRE and not self.autre:
            raise ValidationError({
                'autre': "Le champ 'autre' doit être renseigné lorsque le type d'offre est 'autre'."
            })

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        if self.nom == self.AUTRE and self.autre:
            return self.autre
        return self.get_nom_display()

    class Meta:
        verbose_name = "Type d'offre"
        verbose_name_plural = "Types d'offres"
        ordering = ['nom']

----------------------------------------------------------------------
----------------------------------------------------------------------
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
import uuid


class Utilisateur(AbstractUser):
    """Modèle utilisateur étendu basé sur AbstractUser de Django"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    role = models.CharField(max_length=50, blank=True, verbose_name="Rôle")
    
    # Redéfinition des relations many-to-many avec related_name personnalisé
    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name='utilisateur_set',
        related_query_name='utilisateur'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='utilisateur_set',
        related_query_name='utilisateur'
    )
    
    def __str__(self):
        return f"{self.get_full_name() or self.username}"
    
    class Meta:
        verbose_name = "Utilisateur"
        verbose_name_plural = "Utilisateurs"
----------------------------------------------------------------------
----------------------------------------------------------------------

Lancer les tests des models
python3 manage.py test rap_app.tests.test_models







les models ont des relations entre eux. une foration peut donc avoir des commentaires, des documents, des ressources associés et evenements. lorsqu'un evenement est cree, il est comptabilisé dans ressources. verifie la cohérence des models. de plus, le model formation calculte automatiquement le nombre de places totales, le nombre de places à recruter, le taux de remplissage...et bien entendu, une formation à un statut, un type d'offre, un centre. et l'utilisateurs peut utiliser des filtres pour afficher les partenaires


================================================
File: rap_app/models/parametres.py
================================================
# models/parametres.py
from django.db import models
from .base import BaseModel


class Parametre(BaseModel):
    """
    Modèle représentant les paramètres généraux de l'application.

    Ce modèle permet de stocker des configurations dynamiques sans modifier directement 
    le code ou la base de données. Il est utilisé pour gérer des réglages comme :
    - Modes d'affichage (ex: mode sombre, affichage des logs).
    - Paramètres métiers (ex: nombre maximum d'inscriptions par formation).
    - Clés API ou identifiants spécifiques.

    Hérite de `BaseModel`, qui ajoute automatiquement :
    - `created_at` : Date et heure de création du paramètre.
    - `updated_at` : Date et heure de la dernière modification.
    """

    cle = models.CharField(
        max_length=100, 
        unique=True, 
        verbose_name="Clé du paramètre"
    )
    """
    Identifiant unique du paramètre.
    Exemples : 
    - 'mode_sombre' pour activer/désactiver le mode dark.
    - 'nombre_max_inscriptions' pour définir une limite d'inscriptions.
    - 'url_webhook_teams' pour configurer les notifications vers Teams.
    """

    valeur = models.TextField(
        verbose_name="Valeur du paramètre"
    )
    """
    Stocke la valeur du paramètre sous forme de texte.
    - Peut contenir un nombre (ex: "50"), un booléen ("true" / "false") ou une URL.
    - Si le paramètre est complexe (ex: une liste JSON), la valeur peut contenir un JSON stringifié.
    """

    description = models.TextField(
        null=True, 
        blank=True, 
        verbose_name="Description du paramètre"
    )
    """
    Explication optionnelle du rôle du paramètre.
    Permet de documenter les clés stockées et de faciliter leur gestion.
    """

    def __str__(self):
        """Retourne la clé du paramètre pour une meilleure lisibilité en back-office."""
        return self.cle

    class Meta:
        verbose_name = "Paramètre"
        verbose_name_plural = "Paramètres"
        ordering = ['cle']
    """
    - Trie les paramètres par ordre alphabétique de leur clé.
    - Facilite l'affichage dans l'administration et dans les interfaces utilisateur.
    """



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
        'non_defini': "#A0A0A0",         # Gris
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


================================================
File: rap_app/models/types_offre.py
================================================
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
        """
        Sauvegarde avec validation :
        - Appelle `clean()` avant l'enregistrement en base de données.
        """
        self.full_clean()
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




================================================
File: rap_app/static/__init__.py
================================================



================================================
File: rap_app/templates/base.html
================================================
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}Mon Application{% endblock %}</title>
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <!-- FontAwesome pour les icônes -->
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css" rel="stylesheet">
    <!-- Custom CSS -->
    <style>
        body {
            background-color: #f8f9fa;
            display: flex;
            flex-direction: column;
            min-height: 100vh; /* Pour que le footer reste en bas de la page */
        }
        .sidebar {
            height: 100vh;
            position: fixed;
            top: 0;
            left: 0;
            z-index: 100;
            width: 250px; /* Largeur de la sidebar */
            background-color: #6c757d; /* Fond gris */
            display: none; /* Cachée par défaut */
            transition: transform 0.3s; /* Animation fluide */
        }
        .main-content {
            margin-left: 0; /* Pas de marge par défaut */
            margin-top: 60px; /* Hauteur de la navbar */
            padding: 20px;
            transition: margin-left 0.3s; /* Animation fluide */
            flex: 1; /* Pour que le contenu principal prenne tout l'espace disponible */
        }
        .navbar {
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            z-index: 101;
            height: 60px; /* Hauteur de la navbar */
        }
        .btn-custom {
            background-color: #007bff;
            color: white;
        }
        .btn-custom:hover {
            background-color: #0056b3;
        }
        footer {
            flex-shrink: 0; /* Pour que le footer ne rétrécisse pas */
        }
    </style>
</head>
<body>
    <!-- Navbar -->
    {% include "composants/navbar.html" %}

    <!-- Sidebar -->
    {% include "composants/sidebar.html" %}

    <!-- Main Content -->
    <main class="main-content">
        {% block content %}{% endblock %}
    </main>

    <!-- Footer -->
    {% include "composants/footer.html" %}

    <!-- Bootstrap JS -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>

    <!-- Script pour ouvrir/fermer la sidebar -->
    <script>
        function toggleSidebar() {
            const sidebar = document.getElementById('sidebar');
            const sidebarToggle = document.getElementById('sidebarToggle');
            const mainContent = document.querySelector('.main-content');

            if (sidebar.style.display === 'none' || sidebar.style.display === '') {
                sidebar.style.display = 'block'; // Ouvrir la sidebar
                mainContent.style.marginLeft = '250px'; // Décaler le contenu principal
                sidebarToggle.innerHTML = '<i class="fas fa-times"></i>'; // Changer l'icône en "fermer"
            } else {
                sidebar.style.display = 'none'; // Fermer la sidebar
                mainContent.style.marginLeft = '0'; // Réinitialiser le contenu principal
                sidebarToggle.innerHTML = '<i class="fas fa-bars"></i>'; // Changer l'icône en "ouvrir"
            }
        }
    </script>
</body>
</html>


================================================
File: rap_app/templates/home.html
================================================
{% extends "base.html" %}

{% block title %}Accueil{% endblock %}

{% block content %}
<div class="container">
    <h1>Bienvenue sur la page d'accueil !</h1>
    <p>Ceci est une page de démonstration.</p>
</div>
{% endblock %}


================================================
File: rap_app/templates/centres/centre_confirm_delete.html
================================================
{% extends "base.html" %}

{% block content %}
{% include "composants/bouton_retour.html" %}
<h2>Supprimer le centre : {{ centre.nom }}</h2>
<p>Êtes-vous sûr de vouloir supprimer ce centre ? Cette action est irréversible.</p>

<form method="post">
    {% csrf_token %}
    <button type="submit">Oui, supprimer</button>
    <a href="{% url 'centre-list' %}">Annuler</a>
</form>

{% endblock %}



================================================
File: rap_app/templates/centres/centre_detail.html
================================================
{% extends "base.html" %}

{% block content %}
{% include "composants/bouton_retour.html" %}

<h2>Détails du Centre : {{ centre.nom }}</h2>
<p>Code Postal : {{ centre.code_postal }}</p>

<h3>Formations associées</h3>
<form method="get">
    <label>Type d'offre :</label>
    <select name="type_offre">
        <option value="">-- Tous --</option>
        {% for type in type_offres %}
        <option value="{{ type.0 }}" {% if request.GET.type_offre == type.0|stringformat:"s" %}selected{% endif %}>
            {{ type.1 }}
        </option>
        {% endfor %}
    </select>

    <label>Statut :</label>
    <select name="statut">
        <option value="">-- Tous --</option>
        {% for statut in statuts %}
        <option value="{{ statut.0 }}" {% if request.GET.statut == statut.0|stringformat:"s" %}selected{% endif %}>
            {{ statut.1 }}
        </option>
        {% endfor %}
    </select>

    <button type="submit">Filtrer</button>
</form>

<table>
    <thead>
        <tr>
            <th>Nom</th>
            <th>Type</th>
            <th>Statut</th>
            <th>Début</th>
            <th>Fin</th>
            <th>Inscrits</th>
        </tr>
    </thead>
    <tbody>
        {% for formation in formations %}
        <tr>
            <td>{{ formation.nom }}</td>
            <td>{{ formation.type_offre.nom }}</td>
            <td style="color: {{ formation.statut.couleur }}">{{ formation.statut.nom }}</td>
            <td>{{ formation.start_date }}</td>
            <td>{{ formation.end_date }}</td>
            <td>{{ formation.inscrits_total }}</td>
        </tr>
        {% empty %}
        <tr><td colspan="6">Aucune formation associée.</td></tr>
        {% endfor %}
    </tbody>
</table>

<a href="{% url 'centre-update' centre.pk %}">Modifier</a> |
<a href="{% url 'centre-delete' centre.pk %}">Supprimer</a>

{% endblock %}



================================================
File: rap_app/templates/centres/centre_form.html
================================================

{% extends "base.html" %}

{% block content %}
{% include "composants/bouton_retour.html" %}

<h2>{{ titre }}</h2>

<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Enregistrer</button>
</form>

<a href="{% url 'centre-list' %}">Retour à la liste</a>
{% endblock %}



================================================
File: rap_app/templates/centres/centre_list.html
================================================
{% extends "base.html" %}

{% block content %}
{% include "composants/bouton_retour.html" %}

<h2>Liste des Centres</h2>

<form method="get">
    <input type="text" name="q" placeholder="Rechercher un centre" value="{{ filters.q }}">
    <input type="text" name="code_postal" placeholder="Filtrer par code postal" value="{{ filters.code_postal }}">
    <button type="submit">Filtrer</button>
</form>
<table>
    <thead>
        <tr>
            <th>Nom</th>
            <th>Code Postal</th>
            <th>Formations</th>
            <th>Inscrits</th>
            <th>Actions</th>
        </tr>
    </thead>
    <tbody>
        {% for centre in centres %}
        <tr>
            <td>{{ centre.nom }}</td>
            <td>{{ centre.code_postal }}</td>
            <td>{{ centre.nb_formations }}</td>
            <td>{{ centre.nb_inscrits }}</td>
            <td>
                <a href="{% url 'centre-detail' centre.pk %}">Voir</a> |
                <a href="{% url 'centre-update' centre.pk %}">Modifier</a> |
                <a href="{% url 'centre-delete' centre.pk %}">Supprimer</a>
            </td>
        </tr>
        {% empty %}
        <tr><td colspan="5">Aucun centre trouvé.</td></tr>
        {% endfor %}
    </tbody>
</table>

<a href="{% url 'centre-create' %}">Ajouter un centre</a>

{% endblock %}



================================================
File: rap_app/templates/commentaires/commentaire_confirm.html
================================================
{% extends 'base.html' %}
{% load static %}

{% block title %}Supprimer le Commentaire{% endblock %}

{% block content %}
<div class="container mt-4">
    <div class="card">
        <div class="card-header bg-danger text-white">
            <h5 class="mb-0">Confirmation de suppression</h5>
        </div>
        <div class="card-body">
            <h4 class="mb-4">Êtes-vous sûr de vouloir supprimer ce commentaire ?</h4>
            
            <div class="alert alert-warning">
                <p><strong>Attention :</strong> Cette action est irréversible.</p>
            </div>
            
            <div class="card mb-4">
                <div class="card-header bg-light">
                    <h6 class="mb-0">Détails du commentaire</h6>
                </div>
                <div class="card-body">
                    <dl class="row mb-0">
                        <dt class="col-sm-3">Formation</dt>
                        <dd class="col-sm-9">{{ commentaire.formation.nom }}</dd>
                        
                        <dt class="col-sm-3">Créé par</dt>
                        <dd class="col-sm-9">{{ commentaire.utilisateur.username|default:"Anonyme" }}</dd>
                        
                        <dt class="col-sm-3">Date</dt>
                        <dd class="col-sm-9">{{ commentaire.created_at|date:"d/m/Y H:i" }}</dd>
                        
                        <dt class="col-sm-3">Contenu</dt>
                        <dd class="col-sm-9">{{ commentaire.contenu|truncatewords:50 }}</dd>
                        
                        {% if commentaire.saturation %}
                        <dt class="col-sm-3">Saturation</dt>
                        <dd class="col-sm-9">{{ commentaire.saturation }}%</dd>
                        {% endif %}
                    </dl>
                </div>
            </div>
            
            <form method="post">
                {% csrf_token %}
                <div class="d-flex justify-content-end">
                    <a href="{% url 'commentaire-detail' commentaire.id %}" class="btn btn-outline-secondary me-2">
                        <i class="fas fa-times"></i> Annuler
                    </a>
                    <button type="submit" class="btn btn-danger">
                        <i class="fas fa-trash"></i> Confirmer la suppression
                    </button>
                </div>
            </form>
        </div>
    </div>
</div>
{% endblock %}


================================================
File: rap_app/templates/commentaires/commentaire_detail.html
================================================
{% extends 'base.html' %}
{% load static %}

{% block title %}Détail du Commentaire{% endblock %}

{% block content %}
<div class="container mt-4">
    <div class="d-flex justify-content-between align-items-center mb-4">
        <h1>Détail du Commentaire</h1>
        <div>
            <a href="{% url 'commentaire-list' %}" class="btn btn-outline-secondary">
                <i class="fas fa-arrow-left"></i> Retour à la liste
            </a>
        </div>
    </div>

    <div class="card mb-4">
        <div class="card-header bg-light">
            <div class="d-flex justify-content-between align-items-center">
                <h5 class="mb-0">Informations du commentaire</h5>
                <div class="btn-group">
                    <a href="{% url 'commentaire-update' commentaire.id %}" class="btn btn-warning">
                        <i class="fas fa-edit"></i> Modifier
                    </a>
                    <a href="{% url 'commentaire-delete' commentaire.id %}" class="btn btn-danger">
                        <i class="fas fa-trash"></i> Supprimer
                    </a>
                </div>
            </div>
        </div>
        <div class="card-body">
            <div class="row mb-3">
                <div class="col-md-4">
                    <h6>Formation associée</h6>
                    <p>
                        <a href="{% url 'formation-detail' commentaire.formation.id %}">
                            {{ commentaire.formation.nom }}
                        </a>
                    </p>
                </div>
                <div class="col-md-4">
                    <h6>Créé par</h6>
                    <p>{{ commentaire.utilisateur.username|default:"Anonyme" }}</p>
                </div>
                <div class="col-md-4">
                    <h6>Date de création</h6>
                    <p>{{ commentaire.created_at|date:"d/m/Y H:i" }}</p>
                </div>
            </div>

            <div class="row mb-3">
                <div class="col-md-12">
                    <h6>Contenu du commentaire</h6>
                    <div class="p-3 bg-light rounded">
                        {{ commentaire.contenu|linebreaks }}
                    </div>
                </div>
            </div>

            {% if commentaire.saturation %}
            <div class="row">
                <div class="col-md-6">
                    <h6>Niveau de saturation</h6>
                    <div class="progress" style="height: 30px;">
                        <div class="progress-bar 
                            {% if commentaire.saturation >= 80 %}bg-success
                            {% elif commentaire.saturation >= 50 %}bg-info
                            {% else %}bg-warning{% endif %}" 
                            role="progressbar" 
                            style="width: {{ commentaire.saturation }}%;" 
                            aria-valuenow="{{ commentaire.saturation }}" 
                            aria-valuemin="0" 
                            aria-valuemax="100">
                            {{ commentaire.saturation }}%
                        </div>
                    </div>
                </div>
            </div>
            {% endif %}
        </div>
    </div>

    <!-- Informations sur la dernière mise à jour -->
    <div class="card mt-4">
        <div class="card-header bg-light">
            <h5 class="mb-0">Historique</h5>
        </div>
        <div class="card-body">
            <div class="row">
                <div class="col-md-6">
                    <p><strong>Créé le :</strong> {{ commentaire.created_at|date:"d/m/Y H:i" }}</p>
                </div>
                <div class="col-md-6">
                    <p><strong>Dernière mise à jour :</strong> {{ commentaire.updated_at|date:"d/m/Y H:i" }}</p>
                </div>
            </div>
        </div>
    </div>
</div>
{% endblock %}


================================================
File: rap_app/templates/commentaires/commentaire_form.html
================================================
{% extends 'base.html' %}
{% load static %}

{% block title %}{{ titre }}{% endblock %}

{% block content %}
<div class="container mt-4">
    <div class="d-flex justify-content-between align-items-center mb-4">
        <h1>{{ titre }}</h1>
        <div>
            {% if commentaire.id %}
                <a href="{% url 'commentaire-detail' commentaire.id %}" class="btn btn-outline-secondary">
                    <i class="fas fa-arrow-left"></i> Retour au détail
                </a>
            {% else %}
                <a href="{% url 'commentaire-list' %}" class="btn btn-outline-secondary">
                    <i class="fas fa-arrow-left"></i> Retour à la liste
                </a>
            {% endif %}
        </div>
    </div>

    <div class="card">
        <div class="card-header bg-light">
            <h5 class="mb-0">Formulaire</h5>
        </div>
        <div class="card-body">
            <form method="post">
                {% csrf_token %}
                
                {% if form.non_field_errors %}
                <div class="alert alert-danger">
                    {% for error in form.non_field_errors %}
                        {{ error }}
                    {% endfor %}
                </div>
                {% endif %}

                <!-- Formation -->
                <div class="mb-3">
                    <label for="{{ form.formation.id_for_label }}" class="form-label">Formation</label>
                    {{ form.formation }}
                    {% if form.formation.errors %}
                    <div class="invalid-feedback d-block">
                        {% for error in form.formation.errors %}
                            {{ error }}
                        {% endfor %}
                    </div>
                    {% endif %}
                </div>

                <!-- Contenu -->
                <div class="mb-3">
                    <label for="{{ form.contenu.id_for_label }}" class="form-label">Contenu du commentaire</label>
                    {{ form.contenu }}
                    {% if form.contenu.errors %}
                    <div class="invalid-feedback d-block">
                        {% for error in form.contenu.errors %}
                            {{ error }}
                        {% endfor %}
                    </div>
                    {% endif %}
                    <small class="form-text text-muted">Décrivez votre commentaire concernant cette formation.</small>
                </div>

                <!-- Saturation -->
                <div class="mb-3">
                    <label for="{{ form.saturation.id_for_label }}" class="form-label">Niveau de saturation (%)</label>
                    {{ form.saturation }}
                    {% if form.saturation.errors %}
                    <div class="invalid-feedback d-block">
                        {% for error in form.saturation.errors %}
                            {{ error }}
                        {% endfor %}
                    </div>
                    {% endif %}
                    <small class="form-text text-muted">Indiquez le niveau de saturation actuel (0-100).</small>
                </div>

                <div class="d-flex justify-content-end mt-4">
                    <button type="submit" class="btn btn-primary">
                        <i class="fas fa-save"></i> Enregistrer
                    </button>
                </div>
            </form>
        </div>
    </div>
</div>
{% endblock %}

{% block extra_js %}
<script>
    // Ajouter les classes Bootstrap aux champs du formulaire
    document.addEventListener('DOMContentLoaded', function() {
        // Ajouter la classe form-select au champ formation
        var formationField = document.getElementById('{{ form.formation.id_for_label }}');
        if(formationField) {
            formationField.classList.add('form-select');
        }
        
        // Ajouter la classe form-control au champ contenu
        var contenuField = document.getElementById('{{ form.contenu.id_for_label }}');
        if(contenuField) {
            contenuField.classList.add('form-control');
            contenuField.rows = 5;
        }
        
        // Ajouter la classe form-control au champ saturation
        var saturationField = document.getElementById('{{ form.saturation.id_for_label }}');
        if(saturationField) {
            saturationField.classList.add('form-control');
            saturationField.type = 'number';
            saturationField.min = 0;
            saturationField.max = 100;
        }
    });
</script>
{% endblock %}


================================================
File: rap_app/templates/commentaires/commentaire_list.html
================================================
{% extends 'base.html' %}
{% load static %}

{% block title %}Liste des Commentaires{% endblock %}

{% block content %}
<div class="container mt-4">
    <div class="d-flex justify-content-between align-items-center mb-4">
        <h1>Liste des Commentaires</h1>
        <a href="{% url 'commentaire-create' %}" class="btn btn-primary">
            <i class="fas fa-plus"></i> Nouveau commentaire
        </a>
    </div>

    <!-- Filtres -->
    <div class="card mb-4">
        <div class="card-header bg-light">
            <h5 class="mb-0">Filtres</h5>
        </div>
        <div class="card-body">
            <form method="get" class="row g-3">
                <div class="col-md-4">
                    <label for="formation" class="form-label">Formation</label>
                    <select name="formation" id="formation" class="form-select">
                        <option value="">Toutes les formations</option>
                        {% for formation in formations %}
                            <option value="{{ formation.id }}" {% if filters.formation == formation.id|stringformat:"s" %}selected{% endif %}>
                                {{ formation.nom }} - {{ formation.num_offre|default:"-" }}
                            </option>
                        {% endfor %}
                    </select>
                </div>
                <div class="col-md-4">
                    <label for="utilisateur" class="form-label">Utilisateur</label>
                    <select name="utilisateur" id="utilisateur" class="form-select">
                        <option value="">Tous les utilisateurs</option>
                        <!-- Les utilisateurs seraient ajoutés dynamiquement -->
                    </select>
                </div>
                <div class="col-md-4">
                    <label for="q" class="form-label">Recherche</label>
                    <input type="text" class="form-control" id="q" name="q" value="{{ filters.q }}" placeholder="Rechercher dans le contenu...">
                </div>
                <div class="col-12 text-end">
                    <button type="submit" class="btn btn-primary">Filtrer</button>
                    <a href="{% url 'commentaire-list' %}" class="btn btn-outline-secondary">Réinitialiser</a>
                </div>
            </form>
        </div>
    </div>

    <!-- Liste des commentaires -->
    <div class="card">
        <div class="card-header bg-light">
            <div class="d-flex justify-content-between align-items-center">
                <h5 class="mb-0">Résultats ({{ commentaires|length }})</h5>
            </div>
        </div>
        <div class="card-body p-0">
            {% if commentaires %}
                <div class="table-responsive">
                    <table class="table table-hover table-striped mb-0">
                        <thead>
                            <tr>
                                <th>Formation</th>
                                <th>Utilisateur</th>
                                <th>Date</th>
                                <th>Contenu</th>
                                <th>Saturation</th>
                                <th>Actions</th>
                            </tr>
                        </thead>
                        <tbody>
                            {% for commentaire in commentaires %}
                                <tr>
                                    <td>
                                        <a href="{% url 'formation-detail' commentaire.formation.id %}">
                                            {{ commentaire.formation.nom }} - {{ commentaire.formation.num_offre|default:"-" }}
                                        </a>
                                    </td>
                                    <td>{{ commentaire.utilisateur.username|default:"Anonyme" }}</td>
                                    <td>{{ commentaire.created_at|date:"d/m/Y H:i" }}</td>
                                    <td>
                                        <div class="text-truncate" style="max-width: 300px;">
                                            {{ commentaire.contenu }}
                                        </div>
                                    </td>
                                    <td>
                                        {% if commentaire.saturation %}
                                            <div class="progress" style="height: 20px;">
                                                <div class="progress-bar 
                                                    {% if commentaire.saturation >= 80 %}bg-success
                                                    {% elif commentaire.saturation >= 50 %}bg-info
                                                    {% else %}bg-warning{% endif %}" 
                                                    role="progressbar" 
                                                    style="width: {{ commentaire.saturation }}%;" 
                                                    aria-valuenow="{{ commentaire.saturation }}" 
                                                    aria-valuemin="0" 
                                                    aria-valuemax="100">
                                                    {{ commentaire.saturation }}%
                                                </div>
                                            </div>
                                        {% else %}
                                            <span class="text-muted">Non défini</span>
                                        {% endif %}
                                    </td>
                                    <td>
                                        <div class="btn-group btn-group-sm">
                                            <a href="{% url 'commentaire-detail' commentaire.id %}" class="btn btn-info" title="Détails">
                                                <i class="fas fa-eye"></i>
                                            </a>
                                            <a href="{% url 'commentaire-update' commentaire.id %}" class="btn btn-warning" title="Modifier">
                                                <i class="fas fa-edit"></i>
                                            </a>
                                            <a href="{% url 'commentaire-delete' commentaire.id %}" class="btn btn-danger" title="Supprimer">
                                                <i class="fas fa-trash"></i>
                                            </a>
                                        </div>
                                    </td>
                                </tr>
                            {% endfor %}
                        </tbody>
                    </table>
                </div>
            {% else %}
                <div class="text-center py-4">
                    <p class="text-muted">Aucun commentaire trouvé.</p>
                </div>
            {% endif %}
        </div>
    </div>
</div>
{% endblock %}


================================================
File: rap_app/templates/composants/bouton_retour.html
================================================
<!-- templates/composants/bouton_retour.html -->
 <!-- Bouton retour qui renvoie à la page précédente   -->
<button onclick="window.history.back();" class="btn btn-custom mb-3">
    <i class="fas fa-arrow-left"></i> Retour
</button>


================================================
File: rap_app/templates/composants/footer.html
================================================
<!-- templates/composants/footer.html -->
<footer class="bg-dark text-white mt-4">
    <div class="container py-3"> <!-- Augmenté de py-1 à py-3 pour plus d'espace -->
        <!-- Copyright -->
        <div class="text-center pt-3 border-top border-light"> <!-- Changé border-secondary à border-light et augmenté pt-2 à pt-3 -->
            <p class="mb-0 text-white">&copy; 2025 - RAP-APP. Tous droits réservés.</p> <!-- Changé text-muted à text-white -->
        </div>
    </div>
</footer>


================================================
File: rap_app/templates/composants/navbar.html
================================================
<!-- templates/composants/navbar.html -->
<nav class="navbar navbar-expand-lg navbar-dark bg-primary">
    <div class="container-fluid">
        <!-- Bouton pour ouvrir/fermer la sidebar -->
        <button class="btn btn-sm btn-secondary me-3" id="sidebarToggle" onclick="toggleSidebar()">
            <i class="fas fa-bars"></i>
        </button>

        <!-- Logo ou nom de l'application -->
        <a class="navbar-brand" href="{% url 'home' %}">Mon Application</a>

        <!-- Bouton pour les écrans mobiles -->
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>

        <!-- Liens de navigation -->
        <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav me-auto">
                <li class="nav-item">
                    <a class="nav-link" href="{% url 'home' %}">Accueil</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="{% url 'centre-list' %}">Centres</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="{% url 'statut-list' %}">Statuts</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="{% url 'type-offre-list' %}">Types offres</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="{% url 'admin:index' %}">Admin</a>
                </li>

                <li class="nav-item">
                    <a class="nav-link" href="{% url 'commentaire-list' %}">Commentaires</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="{% url 'evenement-list' %}">Evenements</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="{% url 'partenaire-list' %}">Partenaires</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="{% url 'formation-list' %}">Formations</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="{% url 'document-list' %}">Documents</a>
                </li>
            </ul>

            <!-- Section utilisateur (optionnelle) -->
            <ul class="navbar-nav ms-auto">
                <li class="nav-item">
                    <a class="nav-link" href="#">Connexion</a>
                </li>
            </ul>
        </div>
    </div>
</nav>


================================================
File: rap_app/templates/composants/sidebar.html
================================================
<!-- templates/composants/sidebar.html -->
<div class="sidebar bg-secondary border-end" style="width: 250px; display: none;" id="sidebar">
    <div class="p-3">
        <!-- Titre du menu -->
        <h5 class="mb-3 text-white">Menu</h5>

        <!-- Liens du menu -->
        <ul class="nav flex-column">
            <li class="nav-item">
                <a class="nav-link text-white" href="{% url 'home' %}">
                    <i class="fas fa-home me-2"></i> Accueil
                </a>
            </li>
            <li class="nav-item">
                <a class="nav-link text-white" href="{% url 'centre-list' %}">
                    <i class="fas fa-building me-2"></i> Centres
                </a>
            </li>
            <li class="nav-item">
                <a class="nav-link text-white" href="#">
                    <i class="fas fa-cog me-2"></i> Paramètres
                </a>
            </li>
        </ul>
    </div>
</div>


================================================
File: rap_app/templates/documents/document_confirm_delete.html
================================================
{% extends 'base.html' %}
{% load static %}

{% block title %}Supprimer le Document{% endblock %}

{% block content %}
<div class="container mt-4">
    <div class="card">
        <div class="card-header bg-danger text-white">
            <h5 class="mb-0">Confirmation de suppression</h5>
        </div>
        <div class="card-body">
            <h4 class="mb-4">Êtes-vous sûr de vouloir supprimer ce document ?</h4>
            
            <div class="alert alert-warning">
                <p><strong>Attention :</strong> Cette action est irréversible. Le fichier sera également supprimé du serveur.</p>
            </div>
            
            <div class="card mb-4">
                <div class="card-header bg-light">
                    <h6 class="mb-0">Détails du document</h6>
                </div>
                <div class="card-body">
                    <div class="row">
                        <div class="col-md-6">
                            <dl class="row mb-0">
                                <dt class="col-sm-4">Nom</dt>
                                <dd class="col-sm-8">{{ document.nom_fichier }}</dd>
                                
                                <dt class="col-sm-4">Type</dt>
                                <dd class="col-sm-8">{{ document.get_type_document_display }}</dd>
                                
                                <dt class="col-sm-4">Formation</dt>
                                <dd class="col-sm-8">{{ document.formation.nom }}</dd>
                                
                                <dt class="col-sm-4">Taille</dt>
                                <dd class="col-sm-8">
                                    {% if document.taille_fichier %}
                                        {% if document.taille_fichier > 1024 %}
                                            {{ document.taille_fichier|divisibleby:"1024"|floatformat:2 }} Mo
                                        {% else %}
                                            {{ document.taille_fichier }} Ko
                                        {% endif %}
                                    {% else %}
                                        Non disponible
                                    {% endif %}
                                </dd>
                                
                                <dt class="col-sm-4">Date d'ajout</dt>
                                <dd class="col-sm-8">{{ document.created_at|date:"d/m/Y" }}</dd>
                            </dl>
                        </div>
                        <div class="col-md-6">
                            <div class="text-center border p-3">
                                {% if document.type_document == 'image' %}
                                    <img src="{{ document.fichier.url }}" alt="{{ document.nom_fichier }}" class="img-fluid" style="max-height: 150px;">
                                {% else %}
                                    <i class="fas {% if document.type_document == 'pdf' %}fa-file-pdf{% elif document.type_document == 'contrat' %}fa-file-contract{% else %}fa-file{% endif %} fa-5x text-secondary"></i>
                                {% endif %}
                                <div class="mt-3">
                                    <a href="{{ document.fichier.url }}" class="btn btn-sm btn-outline-secondary" target="_blank">
                                        <i class="fas fa-external-link-alt me-1"></i> Voir le fichier
                                    </a>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            
            <form method="post">
                {% csrf_token %}
                <div class="d-flex justify-content-end">
                    <a href="{% url 'document-detail' document.id %}" class="btn btn-outline-secondary me-2">
                        <i class="fas fa-times"></i> Annuler
                    </a>
                    <button type="submit" class="btn btn-danger">
                        <i class="fas fa-trash"></i> Confirmer la suppression
                    </button>
                </div>
            </form>
        </div>
    </div>
</div>
{% endblock %}


================================================
File: rap_app/templates/documents/document_detail.html
================================================
{% extends 'base.html' %}
{% load static %}

{% block title %}Détail du Document{% endblock %}

{% block content %}
<div class="container mt-4">
    <div class="d-flex justify-content-between align-items-center mb-4">
        <h1>Détail du Document</h1>
        <div>
            <a href="{% url 'document-list' %}" class="btn btn-outline-secondary">
                <i class="fas fa-arrow-left"></i> Retour à la liste
            </a>
            <a href="{{ document.fichier.url }}" target="_blank" class="btn btn-primary ms-2">
                <i class="fas fa-download"></i> Télécharger
            </a>
        </div>
    </div>

    <div class="row">
        <div class="col-md-7">
            <!-- Informations principales -->
            <div class="card mb-4">
                <div class="card-header bg-light">
                    <div class="d-flex justify-content-between align-items-center">
                        <h5 class="mb-0">Informations du document</h5>
                        <div class="btn-group">
                            <a href="{% url 'document-update' document.id %}" class="btn btn-warning">
                                <i class="fas fa-edit"></i> Modifier
                            </a>
                            <a href="{% url 'document-delete' document.id %}" class="btn btn-danger">
                                <i class="fas fa-trash"></i> Supprimer
                            </a>
                        </div>
                    </div>
                </div>
                <div class="card-body">
                    <div class="row mb-3">
                        <div class="col-md-6">
                            <h6>Nom du fichier</h6>
                            <p>{{ document.nom_fichier }}</p>
                        </div>
                        <div class="col-md-6">
                            <h6>Type de document</h6>
                            <p>{{ document.get_type_document_display }}</p>
                        </div>
                    </div>

                    <div class="row mb-3">
                        <div class="col-md-6">
                            <h6>Formation associée</h6>
                            <p>
                                <a href="{% url 'formation-detail' document.formation.id %}">
                                    {{ document.formation.nom }}
                                </a>
                            </p>
                        </div>
                        <div class="col-md-6">
                            <h6>Taille du fichier</h6>
                            <p>
                                {% if document.taille_fichier %}
                                    {% if document.taille_fichier > 1024 %}
                                        {{ document.taille_fichier|divisibleby:"1024"|floatformat:2 }} Mo
                                    {% else %}
                                        {{ document.taille_fichier }} Ko
                                    {% endif %}
                                {% else %}
                                    Non disponible
                                {% endif %}
                            </p>
                        </div>
                    </div>

                    {% if document.source %}
                    <div class="row mb-3">
                        <div class="col-md-12">
                            <h6>Source</h6>
                            <p>{{ document.source }}</p>
                        </div>
                    </div>
                    {% endif %}
                </div>
            </div>

            <!-- Informations sur la dernière mise à jour -->
            <div class="card mt-4">
                <div class="card-header bg-light">
                    <h5 class="mb-0">Historique</h5>
                </div>
                <div class="card-body">
                    <div class="row">
                        <div class="col-md-6">
                            <p><strong>Créé le :</strong> {{ document.created_at|date:"d/m/Y H:i" }}</p>
                        </div>
                        <div class="col-md-6">
                            <p><strong