from django.db import models
from django.contrib.auth.models import User

from monitoring.models import Service, RendezVous, Ordonnance, DossierMedical
    
class Secretaire(User):
    age= models.PositiveIntegerField(null=True)
    sexe = models.CharField(max_length=1, choices=[('M', 'Masculin'),('F', 'Féminin')], null=True)
    statut=models.BooleanField(default=False)
    telephone = models.CharField(max_length=20,null=False)
    adresse = models.CharField(max_length=40)
    profile= models.ImageField(upload_to='profile_pic/SecretaireProfilePic/',null=True,blank=True)
    statut=models.BooleanField(default=False)


class Docteur(User):
    age= models.PositiveIntegerField(null=True)
    sexe = models.CharField(max_length=1, choices=[('M', 'Masculin'),('F', 'Féminin')], null=True)
    statut=models.BooleanField(default=False)
    telephone = models.CharField(max_length=20,null=False)
    adresse = models.CharField(max_length=40)
    profile= models.ImageField(upload_to='profile_pic/DocteurProfilePic/',null=True,blank=True)
    specialite= models.CharField(max_length=50)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    rendez_vous = models.OneToManyField(RendezVous, related_name='docteur')
    ordonnances = models.OneToManyField(Ordonnance, related_name='docteur')



class Patient(User):
    age= models.PositiveIntegerField(null=True)
    sexe = models.CharField(max_length=1, choices=[('M', 'Masculin'),('F', 'Féminin')], null=True)
    groupe_sanguin=models.CharField(max_length=10, null=True)
    profile= models.ImageField(upload_to='profile_pic/PatientProfilePic/',null=True,blank=True)
    telephone = models.CharField(max_length=20,null=False)
    adresse = models.CharField(max_length=40)
    symptoms = models.CharField(max_length=100,null=False)
    admitDate=models.DateField(auto_now=True)
    statut=models.BooleanField(default=False)
    secretaire = models.ForeignKey(Secretaire, on_delete=models.CASCADE)
    docteurs = models.ManyToManyField(Docteur)
    services = models.ManyToManyField(Service)
    rendez_vous = models.OneToManyField(RendezVous, related_name='patient')
    dossier_medical = models.OneToOneField(DossierMedical, on_delete=models.CASCADE)

    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return self.user.first_name+" ("+self.symptoms+")"