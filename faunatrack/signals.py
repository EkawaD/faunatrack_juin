from django.db.models.signals import post_save, pre_save, post_delete, pre_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from faunatrack.models import Scientifique


@receiver(post_save, sender=User)
def add_scientifique_when_user_created(sender, instance, created, **kwargs):
    if created:
        Scientifique.objects.create(user=instance, universite="")

# QUERYSET DJANGO -> method qui s'applique sur les tables/modeles
# 
# Scientifique.objects.all() -> Toute ma table [Scientifique1, Scientifique2]
# Scientifique.objects.filter(user="bastien") -> [ScientifiqueBastien]
# Scientifique.objects.all().filter(user="bastien") -> [ScientifiqueBastien]
# Scientifique.objects.filter(user="bastien").first()
# Scientifique.objects.filter(user="bastien").last()
# Observation.objects.filter(quantite!=1) # ERROR
# Observation.objects.filter(quantite=1)
# Observation.objects.exclude(quantite=1)
# Observation.objects.filter(espece__nom="Ours")
# Projet.objects.all().order_by("-date")
# Projet.objects.filter(date__gte=datetime.now())
# Scientifique.objects.create() # Crée un objet en database
# Scientifique.objects.update()
# Scientifique.objects.delete()
# especes_id = Projet.objects.filter(date__gte=datetime.now(), observations__in=[Obs1, Obs2]).values("espece")
# Observation.objects.filter(espece__in=especes_id)

