
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from datetime import date, timedelta
import json
from django.contrib.auth.models import Permission

from rap_app.models import (Centre, Statut, TypeOffre, Formation, Partenaire, Company, 
                            Prospection, Rapport, Commentaire, Document, HistoriqueFormation
)

User = get_user_model()

class ViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.client.login(username="testuser", password="testpass")
        self.centre = Centre.objects.create(nom="Test Centre", code_postal="75000")
        self.statut = Statut.objects.create(nom="formation_en_cours", couleur="#123456")
        self.type_offre = TypeOffre.objects.create(nom="poec", couleur="#654321")
        self.formation = Formation.objects.create(
            nom="Formation Test",
            centre=self.centre,
            type_offre=self.type_offre,
            statut=self.statut,
            start_date=date.today(),
            end_date=date.today() + timedelta(days=5),
            utilisateur=self.user
        )
        self.company = Company.objects.create(name="Company Test")
        self.prospection = Prospection.objects.create(formation=self.formation, company=self.company, statut="nouveau")
        self.partenaire = Partenaire.objects.create(nom="Partenaire A")
        self.rapport = Rapport.objects.create(formation=self.formation, date_debut=date.today(), date_fin=date.today())
    
    def test_dashboard_access(self):
        response = self.client.get(reverse("dashboard"))
        self.assertEqual(response.status_code, 200)

    def test_formation_list_view(self):
        response = self.client.get(reverse("formation-list"))
        self.assertEqual(response.status_code, 200)

    def test_centre_list_view(self):
        response = self.client.get(reverse("centre-list"))
        self.assertEqual(response.status_code, 200)

    def test_statut_list_view(self):
        response = self.client.get(reverse("statut-list"))
        self.assertEqual(response.status_code, 200)

    def test_type_offre_list_view(self):
        response = self.client.get(reverse("type-offre-list"))
        self.assertEqual(response.status_code, 200)

    def test_partenaire_list_view(self):
        response = self.client.get(reverse("partenaire-list"))
        self.assertEqual(response.status_code, 200)

    def test_company_list_view(self):
        response = self.client.get(reverse("company-list"))
        self.assertEqual(response.status_code, 200)

    def test_prospection_list_view(self):
        response = self.client.get(reverse("prospection-list"))
        self.assertEqual(response.status_code, 200)

    def test_rapport_list_view(self):
        response = self.client.get(reverse("rapport-list"))
        self.assertEqual(response.status_code, 200)

    def test_commentaire_list_view(self):
        response = self.client.get(reverse("commentaire-list"))
        self.assertEqual(response.status_code, 200)

    def test_document_list_view(self):
        response = self.client.get(reverse("document-list"))
        self.assertEqual(response.status_code, 200)

    def test_historique_formation_list_view(self):
        response = self.client.get(reverse("historique-formation-list"))
        self.assertEqual(response.status_code, 200)

    def test_user_list_view(self):
        response = self.client.get(reverse("user-list"))
        self.assertEqual(response.status_code, 200)

    def test_formation_detail_view(self):
        response = self.client.get(reverse("formation-detail", args=[self.formation.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.formation.nom)

    def test_create_centre_view(self):
        response = self.client.post(reverse("centre-create"), {
            "nom": "Nouveau Centre",
            "code_postal": "12345",
            # Ajoute ici tous les champs requis dans le formulaire
        })
        # Pour debug :
        print("Status Code:", response.status_code)
        print("HTML:", response.content.decode())

        self.assertEqual(response.status_code, 302)  # Redirection attendue après succès
        self.assertTrue(Centre.objects.filter(nom="Nouveau Centre").exists())

    def test_create_centre_invalid(self):
        response = self.client.post(reverse("centre-create"), {
            "nom": "",  # nom vide
            "code_postal": "12345"
        })
        self.assertEqual(response.status_code, 200)  # formulaire renvoyé avec erreurs
        self.assertFormError(response, "form", "nom", "This field is required.")

    def test_access_without_login(self):
        self.client.logout()
        response = self.client.get(reverse("centre-list"))
        self.assertRedirects(response, reverse("login"))  # sans `?next=`


    def test_update_centre(self):
        response = self.client.post(reverse("centre-update", args=[self.centre.pk]), {
            "nom": "Centre Modifié",
            "code_postal": "99999"
        })
        self.assertRedirects(response, reverse("centre-detail", args=[self.centre.pk]))
        self.centre.refresh_from_db()
        self.assertEqual(self.centre.nom, "Centre Modifié")

    def test_delete_centre(self):
        response = self.client.post(reverse("centre-delete", args=[self.centre.pk]))
        self.assertRedirects(response, reverse("centre-list"))
        self.assertFalse(Centre.objects.filter(pk=self.centre.pk).exists())

    def test_export_companies_csv(self):
        response = self.client.get(reverse("company-export"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response["Content-Type"], "text/csv")
        self.assertIn("Company Test", response.content.decode())


class ViewTestsComplementaires(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="testuser2", password="testpass")
        self.client.login(username="testuser2", password="testpass")

        self.centre = Centre.objects.create(nom="Centre Test", code_postal="75000")
        self.statut = Statut.objects.create(nom="formation_en_cours", couleur="#123456")
        self.type_offre = TypeOffre.objects.create(nom="poec", couleur="#654321")
        perm = Permission.objects.get(codename='delete_historiqueformation')
        
        self.user.user_permissions.add(perm)
        self.formation = Formation.objects.create(
            nom="Formation Complémentaire",
            centre=self.centre,
            type_offre=self.type_offre,
            statut=self.statut,
            start_date=date.today(),
            end_date=date.today() + timedelta(days=5),
            utilisateur=self.user
        )


    def test_update_formation_field_ajax(self):
        url = reverse("update_formation_field", args=[self.formation.pk])
        data = {
            "field": "nombre_candidats",
            "value": 25
        }

        response = self.client.post(
            url,
            data=json.dumps(data),  # On encode en JSON
            content_type="application/json",  # On précise que c'est du JSON
            HTTP_X_REQUESTED_WITH="XMLHttpRequest"  # Header AJAX
        )

        self.assertEqual(response.status_code, 200)
        self.formation.refresh_from_db()
        self.assertEqual(self.formation.nombre_candidats, 25)


    def test_historique_formation_detail_view(self):
        historique = HistoriqueFormation.objects.create(
            formation=self.formation,
            action="modification",
            champ_modifie="nom",
            ancienne_valeur="Ancien Nom",
            nouvelle_valeur="Nouveau Nom",
            modifie_par=self.user,
            commentaire="Test modif"
        )

        url = reverse("historique-formation-detail", args=[historique.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "modification")


    def test_historique_formation_delete_view(self):
        historique = HistoriqueFormation.objects.create(
            formation=self.formation,
            action="suppression",
            champ_modifie="statut",
            ancienne_valeur="ancien",
            nouvelle_valeur="nouveau",
            modifie_par=self.user
        )
        url = reverse("historique-formation-delete", args=[historique.pk])
        response = self.client.post(url)
        self.assertRedirects(response, reverse("historique-formation-list"))
        self.assertFalse(HistoriqueFormation.objects.filter(pk=historique.pk).exists())

from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date
from ..models.vae_jury import Centre, SuiviJury, VAE


class VaeJuryViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')

        self.centre = Centre.objects.create(nom="Test Centre", code_postal="75000", objectif_annuel_jury=100, objectif_mensuel_jury=10)
        self.suivi = SuiviJury.objects.create(centre=self.centre, annee=2024, mois=3, objectif_jury=10, jurys_realises=5)
        self.vae = VAE.objects.create(centre=self.centre, date_creation=date.today(), statut='dossier')

    def test_vae_jury_home_view(self):
        response = self.client.get(reverse('vae-jury-home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'vae_jury/vae_jury_home.html')

    def test_jury_list_view(self):
        response = self.client.get(reverse('jury-list'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('suivis', response.context)

    def test_vae_list_view(self):
        response = self.client.get(reverse('vae-list'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('vaes', response.context)

    def test_jury_detail_view(self):
        response = self.client.get(reverse('jury-detail', kwargs={'pk': self.suivi.pk}))
        self.assertEqual(response.status_code, 200)

    def test_vae_detail_view(self):
        response = self.client.get(reverse('vae-detail', kwargs={'pk': self.vae.pk}))
        self.assertEqual(response.status_code, 200)

    def test_jury_create_view(self):
        response = self.client.get(reverse('jury-create'))
        self.assertEqual(response.status_code, 200)

    def test_vae_create_view(self):
        response = self.client.get(reverse('vae-create'))
        self.assertEqual(response.status_code, 200)

    def test_jury_update_view(self):
        response = self.client.get(reverse('jury-update', kwargs={'pk': self.suivi.pk}))
        self.assertEqual(response.status_code, 200)

    def test_vae_update_view(self):
        response = self.client.get(reverse('vae-update', kwargs={'pk': self.vae.pk}))
        self.assertEqual(response.status_code, 200)

    def test_vae_jury_dashboard_view(self):
        response = self.client.get(reverse('vae-jury-dashboard'))
        self.assertEqual(response.status_code, 200)

    def test_api_jurys_data(self):
        response = self.client.get(reverse('api-jurys-data'))
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    def test_api_vae_data(self):
        response = self.client.get(reverse('api-vae-data'))
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), dict)
