from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.
class Competence(models.Model):
    competence = models.CharField(max_length=60)


class Etablissement(models.Model):
    label = models.CharField(max_length=60)


class Diplome(models.Model):
    label = models.CharField(max_length=60)


class Domaine_Etude(models.Model):
    label = models.CharField(max_length=60)


class Formation(models.Model):
    date_debut = models.DateField()
    date_fin = models.DateField()
    description = models.TextField(blank=True)
    id_etablissement = models.ForeignKey(Etablissement, on_delete=models.CASCADE, related_name="centre_formation")
    id_diplome = models.ForeignKey(Diplome, on_delete=models.CASCADE, related_name="diplome_formation")
    id_domaine_etude = models.ForeignKey(Domaine_Etude, on_delete=models.CASCADE, related_name="domaine_detude")
    worker = models.ForeignKey(User, on_delete=models.CASCADE, related_name='worker_certify')


class Experience(models.Model):
    poste = models.CharField(max_length=60)
    nom_entreprise = models.CharField(max_length=60, null=True)
    lieu = models.CharField(max_length=100)
    date_debut = models.DateField()
    date_fin = models.DateField()
    description = models.TextField(blank=True)
    worker = models.ForeignKey(User, on_delete=models.CASCADE, related_name='worker_experience')


class Competence_Ouvrier(models.Model):
    worker = models.ForeignKey(User, on_delete=models.CASCADE, related_name='worker_competence')
    id_competence = models.ForeignKey(Competence, on_delete=models.CASCADE, related_name='competence_worker')
    date = models.DateTimeField(auto_now_add=True)
    niveau = models.IntegerField()
