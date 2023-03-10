# Generated by Django 3.0.5 on 2023-01-11 19:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Docteur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prenom', models.CharField(max_length=40)),
                ('nom', models.CharField(max_length=40)),
                ('age', models.PositiveIntegerField(null=True)),
                ('sexe', models.CharField(choices=[('M', 'Masculin'), ('F', 'Féminin')], max_length=1, null=True)),
                ('telephone', models.CharField(max_length=20)),
                ('adresse', models.CharField(max_length=40)),
                ('specialite', models.CharField(max_length=50)),
                ('profile', models.ImageField(blank=True, null=True, upload_to='profile_pic/DocteurProfilePic/')),
            ],
        ),
        migrations.CreateModel(
            name='DossierMedical',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=50, unique=True)),
                ('creation', models.DateField(auto_now=True)),
                ('miseAjour', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prenom', models.CharField(max_length=40)),
                ('nom', models.CharField(max_length=40)),
                ('naissance', models.DateField(null=True)),
                ('sexe', models.CharField(choices=[('M', 'Masculin'), ('F', 'Féminin')], max_length=1, null=True)),
                ('telephone', models.CharField(max_length=20)),
                ('symptoms', models.CharField(max_length=100, null=True)),
                ('groupe_sanguin', models.CharField(max_length=10, null=True)),
                ('admission', models.DateField(auto_now_add=True)),
                ('profile', models.ImageField(blank=True, null=True, upload_to='profile_pic/PatientProfilePic/')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Secretaire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prenom', models.CharField(max_length=40)),
                ('nom', models.CharField(max_length=40)),
                ('age', models.PositiveIntegerField(null=True)),
                ('sexe', models.CharField(choices=[('M', 'Masculin'), ('F', 'Féminin')], max_length=1, null=True)),
                ('telephone', models.CharField(max_length=20)),
                ('adresse', models.CharField(max_length=40)),
                ('profile', models.ImageField(blank=True, null=True, upload_to='profile_pic/SecretaireProfilePic/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_secretaire', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Salle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=10, unique=True)),
                ('statut', models.BooleanField(default=True)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='salles', to='monitoring.Service')),
            ],
        ),
        migrations.CreateModel(
            name='RendezVous',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('docteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rendez_vous_docteur', to='monitoring.Docteur')),
                ('patients', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='rendez_vous_patient', to='monitoring.Patient')),
            ],
        ),
        migrations.AddField(
            model_name='patient',
            name='secretaire',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='patients', to='monitoring.Secretaire'),
        ),
        migrations.AddField(
            model_name='patient',
            name='services',
            field=models.ManyToManyField(related_name='patients', to='monitoring.Service'),
        ),
        migrations.AddField(
            model_name='patient',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_patient', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Ordonnance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenu', models.TextField()),
                ('date', models.DateField(auto_now=True)),
                ('docteur', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='docteurs', to='monitoring.Docteur')),
                ('dossier_medical', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ordonnances', to='monitoring.DossierMedical')),
            ],
        ),
        migrations.CreateModel(
            name='Lit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.PositiveIntegerField(unique=True)),
                ('statut', models.BooleanField(default=True)),
                ('salle', models.ForeignKey(default=0, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='lits', to='monitoring.Salle')),
            ],
        ),
        migrations.AddField(
            model_name='dossiermedical',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patients', to='monitoring.Patient'),
        ),
        migrations.AddField(
            model_name='dossiermedical',
            name='service',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dossiers', to='monitoring.Service'),
        ),
        migrations.AddField(
            model_name='docteur',
            name='service',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.SET_DEFAULT, to='monitoring.Service'),
        ),
        migrations.AddField(
            model_name='docteur',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_docteur', to=settings.AUTH_USER_MODEL),
        ),
    ]
