from django.db import models
from account.models import Employeur, Worker
from ref_dom_btp.models import Domaine, Travaux

# Create your models here.

class Appreciation(models.Model):
    note = models.IntegerField()
    message = models.TextField()
    employeur = models.ForeignKey(Employeur, on_delete=models.CASCADE, default="", related_name="appreciation_employeur")
    id_reservation = models.ForeignKey('Reservation', on_delete=models.CASCADE, related_name="appreciation_reserver")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    



class Offre(models.Model):
    jour = models.DateField()
    heure = models.TimeField(default="01:00:00")
    description = models.TextField(blank=True)
    employeur = models.ForeignKey(Employeur, on_delete=models.CASCADE, default="", related_name="employeur_offres")
    lieu = models.CharField(max_length=100)
    statut = models.BooleanField(default=True)
    
    id_domaine = models.ForeignKey(Domaine, on_delete=models.CASCADE, related_name="domaine_offre")
    id_travaux = models.ForeignKey(Travaux, on_delete=models.CASCADE, related_name="offre_travaux")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f"{self.id_travaux} publier par : {self.employeur}"


class Commentaire(models.Model):
    content = models.TextField()
    date = models.DateTimeField(auto_now=True)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE, default="", related_name="workers_commentaire")
    id_offre = models.ForeignKey(Offre, on_delete=models.CASCADE, null=False, related_name="commentaire_doffre")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f"Commentaire de: {self.worker}"

class Reservation(models.Model):
    montant = models.FloatField()
    code = models.CharField(max_length=60, null=True)
    employeur = models.ForeignKey(Employeur, on_delete=models.CASCADE, default="", related_name="employeur_reserve")
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE, null=False, related_name="ouvrier_reserver")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id_offre = models.ForeignKey(Offre, on_delete=models.CASCADE, related_name="reservation_doffre")