from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class Scientifique(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # Que se passe t il pour le SCIENTIFIQUE si un USER est supprimé 
    universite = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username
    
class Espece(models.Model):

    class StatusChoice(models.TextChoices):
        DANGER = "danger"
        SAIN = "hors de danger"


    nom = models.CharField(max_length=255, unique=True)
    status = models.CharField(choices=StatusChoice.choices, default=StatusChoice.SAIN, max_length=255)

    def __str__(self):
        return self.nom
    
class Observation(models.Model):
    date = models.DateField(auto_now_add=True)
    quantite = models.IntegerField(default=1)
    notes = models.TextField(blank=True, null=True, default=None)
    photo = models.ImageField(upload_to="obs_photos/", blank=True, null=True)
    espece =  models.ForeignKey(Espece, related_name="observations", on_delete=models.PROTECT) # Que se passe t il pour le OBSERVATION si un ESPECE est supprimé 
    scientifique = models.ForeignKey(Scientifique, related_name="observations", on_delete=models.PROTECT) # Que se passe t il pour le OBSERVATION si un SCIENTIFIQUE est supprimé 

    def __str__(self):
        return f"{self.quantite} {self.espece} observé par {self.scientifique}"
    
class Projet(models.Model):
    titre = models.CharField(max_length=255)
    description = models.TextField(blank=True, default=None, null=True)
    observations = models.ManyToManyField(Observation, related_name="projets")
    slug = models.SlugField(blank=True) # = CharField avec validators (pas d'espace, pas de char spéciaux)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.titre)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.titre


# class ObservationPhotos:
#     observation = models.ForeignKey(Observation, related_name="photos")
#     filename = models.CharField()
#     photo = models.ImageField(upload_to="/obs_photos")

# from django.contrib.auth.models import AbstractUser

# class UserFaunatrack(AbstractUser):
#     universite = models.CharField(max_length=255)
# Seulement si l'utilisateur django est indissociable a jamais de l'user dans ma bdd 

