from django.db import models

class Reservation(models.Model):
    
    idReservation = models.AutoField(primary_key=True)
    numeroVol = models.CharField(max_length=30, help_text="Propiétaire boutique")
    