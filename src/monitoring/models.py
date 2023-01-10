from django.db import models

from  patient.models import Docteur, DossierMedical, Patient

class Lit(models.Model):
    numero= models.PositiveIntegerField(null=False)
    statut=models.BooleanField(default=False)

class Salle(models.Model):
    numero= models.PositiveIntegerField(null=False)
    lits = models.ManyToManyField(Lit)
    statut=models.BooleanField(default=False)

class Service(models.Model):
    nom= models.CharField(max_length=50,null=False)
    salles = models.ManyToManyField(Salle)

class Ordonnance(models.Model):
    contenu= models.TextField(null=True)
    docteur = models.ForeignKey(Docteur, on_delete=models.CASCADE)
    dossier_medical = models.ForeignKey(DossierMedical, on_delete=models.CASCADE)

class DossierMedical(models.Model):
    numero=models.CharField(unique=True,null=False)
    creation=models.DateField(auto_now=True)
    miseAjour=models.DateField(auto_now_add=True)
    ordonnances = models.OneToManyField(Ordonnance, related_name='dossier_medical')
    service = models.ForeignKey(Service, on_delete=models.CASCADE)


class RendezVous(models.Model):
    date=models.DateField(null=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    docteur = models.ForeignKey(Docteur, on_delete=models.CASCADE)
