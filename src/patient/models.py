from django.db import models
from django.contrib.auth.models import User

from monitoring.models import Service, RendezVous, Ordonnance, DossierMedical
    
class Secretaire(User):
    pass


class Docteur(User):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    rendez_vous = models.OneToManyField(RendezVous, related_name='docteur')
    ordonnances = models.ManyToManyField(Ordonnance)


class Patient(User):
    profile_pic= models.ImageField(upload_to='profile_pic/PatientProfilePic/',null=True,blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=False)
    symptoms = models.CharField(max_length=100,null=False)
    assignedDoctorId = models.PositiveIntegerField(null=True)
    admitDate=models.DateField(auto_now=True)
    status=models.BooleanField(default=False)
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