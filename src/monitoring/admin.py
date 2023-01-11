from django.contrib import admin
from monitoring.models import Patient,Secretaire,Docteur,Salle,Service,Lit,Ordonnance,DossierMedical,RendezVous
# Register your models here.

personnelMedical=[Patient,Secretaire,Docteur,Salle,Service,Lit,Ordonnance,DossierMedical,RendezVous]

class AdminLit(admin.ModelAdmin):
    list_display = ('numero','salle','statut')

class AdminSalle(admin.ModelAdmin):
    list_display=('nom','statut')

admin.site.register(Lit,AdminLit)
admin.site.register(Salle,AdminSalle)