from django.db import models

# Create your models here.
class Domaine(models.Model):
    
    nom_domaine = models.CharField(max_length=100)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f"Nom du domaine : {self.nom_domaine}"



class Travaux(models.Model):
    
    nom_travaux = models.CharField(max_length=100)
    
    id_domaine = models.ForeignKey(Domaine, on_delete=models.CASCADE)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f"Nom du travaux : {self.nom_travaux}"

class Metier(models.Model):
    nom_metier = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f"Status : {self.nom_metier}"