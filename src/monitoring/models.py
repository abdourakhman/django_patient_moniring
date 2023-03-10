from django.db import models
from django.contrib.auth.models import User



departments=[('Cardiologist','Cardiologist'),
('Dermatologists','Dermatologists'),
('Emergency Medicine Specialists','Emergency Medicine Specialists'),
('Allergists/Immunologists','Allergists/Immunologists'),
('Anesthesiologists','Anesthesiologists'),
('Colon and Rectal Surgeons','Colon and Rectal Surgeons')
]

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='user_patient')
    prenom = models.CharField(max_length=40)
    nom = models.CharField(max_length=40)
    naissance = models.DateField(null=True)
    sexe = models.CharField(max_length=1, choices=[('M', 'Masculin'), ('F', 'Féminin')], null=True)
    telephone = models.CharField(max_length=20, null=False)
    symptoms = models.CharField(max_length=100,null=True)
    groupe_sanguin = models.CharField(max_length=10, null=True)
    secretaire = models.ForeignKey("Secretaire", on_delete=models.DO_NOTHING, null=True, related_name='patients')
    admission=models.DateField(auto_now_add=True)
    services = models.ManyToManyField("Service", related_name='patients')
    profile = models.ImageField(upload_to='profile_pic/PatientProfilePic/', null=True, blank=True)

    
    def __str__(self):
        return f"{self.prenom} {self.nom}"


class Docteur(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='user_docteur')
    prenom = models.CharField(max_length=40,null=False)
    nom = models.CharField(max_length=40,null=False)
    age = models.PositiveIntegerField(null=True)
    sexe = models.CharField(max_length=1, choices=[('M', 'Masculin'), ('F', 'Féminin')], null=True)
    telephone = models.CharField(max_length=20, null=False)
    adresse = models.CharField(max_length=40)
    specialite = models.CharField(max_length=50,choices=departments,default='Cardiologist')
    profile = models.ImageField(upload_to='profile_pic/DocteurProfilePic/', null=True, blank=True)
    service = models.ForeignKey("Service", on_delete=models.SET_DEFAULT,null=False,default=0)

    def __str__(self):
        return f" {self.user.email}/{self.prenom} {self.nom}"

class Secretaire(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_secretaire')
    prenom = models.CharField(max_length=40)
    nom = models.CharField(max_length=40)
    age = models.PositiveIntegerField(null=True)
    sexe = models.CharField(max_length=1, choices=[('M', 'Masculin'), ('F', 'Féminin')], null=True)
    telephone = models.CharField(max_length=20, null=False)
    adresse = models.CharField(max_length=40)
    profile = models.ImageField(upload_to='profile_pic/SecretaireProfilePic/', null=True, blank=True)

    def __str__(self):
        return f"{self.prenom} {self.nom}"


class Salle(models.Model):
    nom = models.CharField(max_length=10, unique=True)
    statut = models.BooleanField(default=True)
    service = models.ForeignKey("Service", on_delete=models.CASCADE, related_name='salles')
    def __str__(self):
        return f"Salle {self.nom}"


class Service(models.Model):
    nom = models.CharField(max_length=50,choices=departments,default='Cardiologist')
    def __str__(self):
        return f"{self.nom}"

class Lit(models.Model):
    numero = models.PositiveIntegerField(unique=True,null=False)
    salle = models.ForeignKey("Salle", on_delete=models.SET_DEFAULT,default=0,related_name='lits')
    statut = models.BooleanField(null=False,default=True)
    
    def __str__(self):
        return f"lit N°{self.numero}/{self.salle}"

class Ordonnance(models.Model):
    contenu = models.TextField(null=False)
    docteur = models.ForeignKey("Docteur", on_delete=models.CASCADE, related_name='docteurs', null=True)
    date = models.DateField(auto_now=True)
    dossier_medical = models.ForeignKey("DossierMedical", on_delete=models.CASCADE, related_name='ordonnances', null=True)

    def __str__(self):
        return f"ordonnace docteur {self.docteur}"

class DossierMedical(models.Model):
    numero = models.CharField(max_length=50, unique=True, null=False)
    creation = models.DateField(auto_now=True)
    miseAjour = models.DateField(auto_now_add=True)
    service = models.ForeignKey("Service", on_delete=models.CASCADE, related_name='dossiers', null=True)
    patient = models.ForeignKey("Patient", on_delete=models.CASCADE, related_name='patients')

    def __str__(self):
        return f"Dossier n°{self.numero}/ {self.service}"

class RendezVous(models.Model):
    date = models.DateField(null=False)
    docteur = models.ForeignKey("Docteur", on_delete=models.CASCADE,related_name='rendez_vous_docteur')
    patients = models.ForeignKey("Patient", on_delete=models.DO_NOTHING,related_name='rendez_vous_patient')

    def __str__(self):
        return f"{self.date}"

class Docteur_Patient:
    docteur = models.ForeignKey("Docteur", on_delete=models.CASCADE,related_name='docteur_patient')
    patient = models.ForeignKey("Patient", on_delete=models.CASCADE,related_name='docteur_patient')

class Patient_Service:
    patient = models.ForeignKey("Patient", on_delete=models.CASCADE,related_name='patient_service')
    docteur = models.ForeignKey("Docteur", on_delete=models.CASCADE,related_name='docteur_patient2')






