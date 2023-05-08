from django.db import models
from django.contrib.auth import get_user_model
from ref_dom_btp.models import Domaine, Travaux
User = get_user_model()

# Create your models here.

class Appreciation(models.Model):
    note = models.IntegerField()
    message = models.CharField(max_length=255)
    employeur = models.ForeignKey(User, on_delete=models.CASCADE)
    id_reservation = models.ForeignKey('Reservation', on_delete=models.CASCADE, related_name="appreciation_reserver")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    



class Offre(models.Model):
    date_debut = models.DateField()
    date_fin = models.DateField()
    description = models.TextField(blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    lieux = models.CharField(max_length=100)
    statut = models.BooleanField(default=True)
    id_reservation = models.ForeignKey('Reservation', on_delete=models.CASCADE, null=True, related_name="offre_reserver")
    id_domaine = models.ForeignKey(Domaine, on_delete=models.CASCADE, related_name="domaine_offre")
    id_travaux = models.ForeignKey(Travaux, on_delete=models.CASCADE, related_name="offre_travaux")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Commentaire(models.Model):
    content = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, related_name="commentaire_user")
    id_offre = models.ForeignKey(Offre, on_delete=models.CASCADE, null=False, related_name="commentaire_doffre")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Reservation(models.Model):
    montant = models.FloatField()
    code = models.CharField(max_length=60, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, related_name="user_reserve")
    worker = models.ForeignKey(User, on_delete=models.CASCADE, null=False, related_name="ouvrier_reserver")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id_offre = models.ForeignKey(Offre, on_delete=models.CASCADE, related_name="reservation_doffre")
    id_appreciation = models.ForeignKey(Appreciation, on_delete=models.CASCADE, null=True, related_name="reservation_apprecier")
