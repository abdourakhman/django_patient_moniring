from django.db import models
from django.contrib.auth.models import User

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='user_patient')
    age = models.PositiveIntegerField(null=True)
    sexe = models.CharField(max_length=1, choices=[('M', 'Masculin'), ('F', 'Féminin')], null=True)
    groupe_sanguin = models.CharField(max_length=10, null=True)
    profile = models.ImageField(upload_to='profile_pic/PatientProfilePic/', null=True, blank=True)
    telephone = models.CharField(max_length=20, null=False)
    secretaire = models.ForeignKey("Secretaire", on_delete=models.SET_NULL, null=True, related_name='patients')
    rendez_vous = models.ManyToManyField("RendezVous", related_name='patients_rendez_vous')
    dossier = models.OneToOneField("DossierMedical", on_delete=models.CASCADE, null=True, related_name='dossier_patient')

class Docteur(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='user_docteur')
    age = models.PositiveIntegerField(null=True)
    sexe = models.CharField(max_length=1, choices=[('M', 'Masculin'), ('F', 'Féminin')], null=True)
    telephone = models.CharField(max_length=20, null=False)
    adresse = models.CharField(max_length=40)
    profile = models.ImageField(upload_to='profile_pic/DocteurProfilePic/', null=True, blank=True)
    specialite = models.CharField(max_length=50)
    service = models.ForeignKey("Service", on_delete=models.CASCADE)
    rendez_vous = models.ManyToManyField("RendezVous", related_name='docteurs_rendez_vous')
    ordonnances = models.ManyToManyField("Ordonnance", related_name='docteurs_ordonnances')
    patients = models.ManyToManyField(Patient, related_name='docteurs')

class Secretaire(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_secretaire')
    age = models.PositiveIntegerField(null=True)
    sexe = models.CharField(max_length=1, choices=[('M', 'Masculin'), ('F', 'Féminin')], null=True)
    telephone = models.CharField(max_length=20, null=False)
    adresse = models.CharField(max_length=40)
    profile = models.ImageField(upload_to='profile_pic/SecretaireProfilePic/', null=True, blank=True)

class Service(models.Model):
    nom = models.CharField(max_length=50, null=False)
    salles = models.ManyToManyField("Salle", related_name='salles_services')
    patients = models.ManyToManyField(Patient, related_name='patients_services')

class Salle(models.Model):
    numero = models.PositiveIntegerField(unique=True,null=False)
    lits = models.ManyToManyField("Lit", related_name='lits_salles')
    statut = models.BooleanField(default=False)

class Lit(models.Model):
    numero = models.PositiveIntegerField(unique=True,null=False)
    statut = models.BooleanField(default=False)

class Ordonnance(models.Model):
    contenu = models.TextField(null=True)
    docteurs = models.ManyToManyField(Docteur, related_name='docteurs_ordonnances')
    dossier_medical = models.ForeignKey("DossierMedical", on_delete=models.CASCADE, related_name='ordonnances')

class DossierMedical(models.Model):
    numero = models.CharField(max_length=50, unique=True, null=False)
    creation = models.DateField(auto_now=True)
    miseAjour = models.DateField(auto_now_add=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='dossiers')
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE, related_name='dossier_patient')

class RendezVous(models.Model):
    date = models.DateField(null=True)
    docteurs = models.ManyToManyField(Docteur, related_name='docteurs_rendez_vous')
    patients = models.ManyToManyField(Patient, related_name='patients_rendez_vous')
