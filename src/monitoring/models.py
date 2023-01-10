from django.db import models

from  patient.models import Docteur, DossierMedical, Patient

class Lit(models.Model):
    pass

class Salle(models.Model):
    lits = models.ManyToManyField(Lit)

class Service(models.Model):
    salles = models.ManyToManyField(Salle)

class Ordonnance(models.Model):
    docteur = models.ForeignKey(Docteur, on_delete=models.CASCADE)
    dossier_medical = models.ForeignKey(DossierMedical, on_delete=models.CASCADE)

class DossierMedical(models.Model):
    ordonnances = models.OneToManyField(Ordonnance, related_name='dossier_medical')
    service = models.ForeignKey(Service, on_delete=models.CASCADE)


class RendezVous(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    docteur = models.ForeignKey(Docteur, on_delete=models.CASCADE)
