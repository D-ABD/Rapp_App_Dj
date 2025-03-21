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
