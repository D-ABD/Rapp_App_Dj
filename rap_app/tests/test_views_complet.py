
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from datetime import date, timedelta
import json
from django.contrib.auth.models import Permission

from rap_app.models import (Centre, Statut, TypeOffre, Formation, Partenaire, Company, 
                            Prospection, Rapport, Commentaire, Document, HistoriqueFormation)

User = get_user_model()

class ViewTests(TestCase):
    def setUp(self):
        self.client = Client()
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

    def test_home_view(self):
        self.client.logout()
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)



    def test_formation_list_view(self):
        response = self.client.get(reverse("formation-list"))
        self.assertEqual(response.status_code, 200)

    def test_create_centre_view(self):
        response = self.client.post(reverse("centre-create"), {
            "nom": "Nouveau Centre",
            "code_postal": "12345",
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Centre.objects.filter(nom="Nouveau Centre").exists())

    def test_create_centre_invalid(self):
        response = self.client.post(reverse("centre-create"), {
            "nom": "",
            "code_postal": "12345"
        })
        self.assertEqual(response.status_code, 200)
        self.assertFormError(response, "form", "nom", "This field is required.")

    def test_access_without_login(self):
        self.client.logout()
        response = self.client.get(reverse("centre-list"))
        self.assertRedirects(response, reverse("login"))

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
            data=json.dumps(data),
            content_type="application/json",
            HTTP_X_REQUESTED_WITH="XMLHttpRequest"
        )
        self.assertEqual(response.status_code, 200)
        self.formation.refresh_from_db()
        self.assertEqual(self.formation.nombre_candidats, 25)

    def test_update_staut_field_ajax(self):
        nouveau_statut = Statut.objects.create(nom="formation_en_cours", couleur="#000000")
        url = reverse("update_formation_field", args=[self.formation.pk])
        data = {
            "field": "statut",
            "value": nouveau_statut.pk
        }
        response = self.client.post(
            url,
            data=json.dumps(data),
            content_type="application/json",
            HTTP_X_REQUESTED_WITH="XMLHttpRequest"
        )
        self.assertEqual(response.status_code, 200)
        self.formation.refresh_from_db()
        self.assertEqual(self.formation.statut, nouveau_statut)



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


from django.test import TestCase
from django.urls import reverse
from datetime import date
from rap_app.models.prepacomp import Semaine, PrepaCompGlobal
from rap_app.models.centres import Centre
from django.contrib.auth.models import User

class PrepaViewsTestCase(TestCase):
    def setUp(self):
        # Utilisateur test
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')

        # Données de test
        self.centre = Centre.objects.create(nom="Test Centre", objectif_annuel_prepa=100, objectif_hebdomadaire_prepa=10)
        self.semaine = Semaine.objects.create(
            centre=self.centre,
            annee=2024,
            mois=3,
            numero_semaine=13,
            date_debut_semaine=date(2024, 3, 25),
            date_fin_semaine=date(2024, 3, 31),
            nombre_adhesions=5,
            nombre_presents_ic=10,
        )
        self.bilan = PrepaCompGlobal.objects.create(
            centre=self.centre,
            annee=2024,
            total_candidats=50,
            total_prescriptions=40,
            adhesions=20,
            total_presents=25,
            total_places_ouvertes=30,
        )

    def test_prepa_home_view(self):
        response = self.client.get(reverse('prepa_home'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('annee_courante', response.context)

    def test_semaine_list_view(self):
        response = self.client.get(reverse('prepa_semaine_list'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('semaines', response.context)

    def test_semaine_detail_view(self):
        response = self.client.get(reverse('prepa_semaine_detail', args=[self.semaine.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['semaine'], self.semaine)

    def test_semaine_create_view_get(self):
        response = self.client.get(reverse('prepa_semaine_create'))
        self.assertEqual(response.status_code, 200)

    def test_semaine_update_view_get(self):
        response = self.client.get(reverse('prepa_semaine_update', args=[self.semaine.pk]))
        self.assertEqual(response.status_code, 200)

    def test_semaine_delete_view_post(self):
        response = self.client.post(reverse('prepa_semaine_delete', args=[self.semaine.pk]))
        self.assertRedirects(response, reverse('prepa_semaine_list'))
        self.assertFalse(Semaine.objects.filter(pk=self.semaine.pk).exists())

    def test_bilan_list_view(self):
        response = self.client.get(reverse('prepa_global_list'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('bilans', response.context)

    def test_bilan_detail_view(self):
        response = self.client.get(reverse('prepa_global_detail', args=[self.bilan.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['bilan'], self.bilan)

    def test_bilan_create_view_get(self):
        response = self.client.get(reverse('prepa_global_create'))
        self.assertEqual(response.status_code, 200)

    def test_objectifs_view_get(self):
        response = self.client.get(reverse('prepa_objectifs'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('centres', response.context)

    def test_objectifs_view_post(self):
        response = self.client.post(reverse('prepa_objectifs'), {
            f'objectif_annuel_{self.centre.pk}': '120',
            f'objectif_hebdo_{self.centre.pk}': '15'
        }, follow=True)
        self.assertRedirects(response, reverse('prepa_objectifs'))
        self.centre.refresh_from_db()
        self.assertEqual(self.centre.objectif_annuel_prepa, 120)
        self.assertEqual(self.centre.objectif_hebdomadaire_prepa, 15)

from django.test import TestCase
from ..models.vae_jury import SuiviJury, Centre
from datetime import date

class SuiviJuryModelTest(TestCase):
    def setUp(self):
        self.centre = Centre.objects.create(nom="Centre Jury", code_postal="75000")

    def test_creation_et_calcul_pourcentage(self):
        suivi = SuiviJury.objects.create(
            centre=self.centre,
            annee=2024,
            mois=3,
            objectif_jury=10,
            jurys_realises=7
        )
        self.assertEqual(suivi.pourcentage_atteinte, 70.0)
        self.assertEqual(suivi.ecart(), -3)

    def test_objectif_auto_centre_si_non_renseigné(self):
        self.centre.objectif_mensuel_jury = 12
        self.centre.save()
        suivi = SuiviJury.objects.create(
            centre=self.centre,
            annee=2024,
            mois=4,
            objectif_jury=0,
            jurys_realises=6
        )
        self.assertEqual(suivi.get_objectif_auto(), 12)
        self.assertEqual(suivi.get_pourcentage_atteinte(), 50.0)

    def test_str_affichage(self):
        suivi = SuiviJury.objects.create(
            centre=self.centre,
            annee=2024,
            mois=3,
            objectif_jury=5,
            jurys_realises=5
        )
        self.assertIn("Mars 2024", str(suivi))

    def test_pourcentage_zero_si_objectif_zero(self):
        suivi = SuiviJury.objects.create(
            centre=self.centre,
            annee=2024,
            mois=2,
            objectif_jury=0,
            jurys_realises=10
        )
        self.assertEqual(suivi.pourcentage_atteinte, 0)

from django.test import TestCase
from ..models.vae_jury import VAE, Centre, HistoriqueStatutVAE
from datetime import date

class VAEModelTest(TestCase):
    def setUp(self):
        self.centre = Centre.objects.create(nom="Centre VAE", code_postal="34000")

    def test_creation_vae_et_statut_par_defaut(self):
        vae = VAE.objects.create(
            centre=self.centre,
            date_creation=date(2024, 3, 30),
            statut='dossier'
        )
        self.assertEqual(vae.statut, 'dossier')
        self.assertTrue("dossier" in vae.__str__().lower())
        self.assertIsNotNone(vae.reference)
        self.assertEqual(vae.annee_creation, 2024)
        self.assertEqual(vae.mois_creation, 3)

    def test_save_auto_reference(self):
        vae = VAE.objects.create(
            centre=self.centre,
            date_creation=date.today(),
            statut='accompagnement'
        )
        self.assertTrue(vae.reference.startswith("VAE-"))
        self.assertEqual(vae.statut, 'accompagnement')

    def test_get_count_by_statut(self):
        VAE.objects.create(centre=self.centre, date_creation=date(2024, 3, 1), statut='dossier')
        VAE.objects.create(centre=self.centre, date_creation=date(2024, 3, 15), statut='jury')
        VAE.objects.create(centre=self.centre, date_creation=date(2024, 3, 20), statut='abandonnee')

        stats = VAE.get_count_by_statut(centre=self.centre, annee=2024, mois=3)
        self.assertEqual(stats['total'], 3)
        self.assertEqual(stats['dossier'], 1)
        self.assertEqual(stats['jury'], 1)
        self.assertEqual(stats['abandonnee'], 1)
        self.assertEqual(stats['en_cours'], 2)  # exclude 'terminee' and 'abandonnee'

    def test_historique_creation_on_save(self):
        vae = VAE.objects.create(
            centre=self.centre,
            date_creation=date.today(),
            statut='info'
        )
        historique = HistoriqueStatutVAE.objects.filter(vae=vae)
        self.assertEqual(historique.count(), 1)
        self.assertEqual(historique.first().statut, 'info')

    def test_historique_ajoute_si_statut_change(self):
        vae = VAE.objects.create(centre=self.centre, date_creation=date.today(), statut='info')
        vae.statut = 'accompagnement'
        vae.save()

        # 🔁 Recharge l'historique depuis la base
        historiques = HistoriqueStatutVAE.objects.filter(vae=vae).order_by('date_saisie')

        self.assertEqual(historiques.count(), 2)
        self.assertEqual(historiques.last().statut, 'accompagnement')
