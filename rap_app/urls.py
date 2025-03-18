from django.urls import path

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
    path('rapports/<int:pk>/', RapportDetailView.as_view(), name='rapport-detail'),
    path('rapports/nouveau/', RapportCreationView.as_view(), name='rapport-create'),
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
   
    # Paramètres
    path('parametres/', parametres, name='parametres'),


]