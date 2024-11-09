from django.db import models

# Create your models here.
from django.db import models

class Projet(models.Model):
    nom = models.CharField(max_length=200)
    description = models.TextField()
    date_debut = models.DateField()
    date_fin = models.DateField(null=True, blank=True)
    statut = models.CharField(max_length=50, choices=[('En cours', 'En cours'), ('Terminé', 'Terminé'), ('En attente', 'En attente')])

    def __str__(self):
        return self.nom

class Tache(models.Model):
    projet = models.ForeignKey(Projet, on_delete=models.CASCADE, related_name='taches')
    titre = models.CharField(max_length=200)
    description = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)
    date_echeance = models.DateField(null=True, blank=True)
    statut = models.CharField(max_length=50, choices=[('À faire', 'À faire'), ('En cours', 'En cours'), ('Terminé', 'Terminé')])

    def __str__(self):
        return self.titre
    


class KPI(models.Model):
    projet = models.ForeignKey(Projet, on_delete=models.CASCADE, related_name="kpis")
    nom = models.CharField(max_length=200)
    valeur = models.FloatField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.nom} - {self.valeur} ({self.date})"
    
