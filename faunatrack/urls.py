from django.contrib import admin
from django.urls import path
from faunatrack.views import home_page,ObsCreate,ObsUpdate,ObsDelete , ObsList, ProjetList, ProjetDelete, ProjetCreate,ProjetUpdate

urlpatterns = [
    path("", home_page, name="home"),
    path("projet/", ProjetList.as_view(), name="projet_list"),
    path("projet/add/", ProjetCreate.as_view(), name="projet_create"),
    path("projet/<int:pk>/edit/", ProjetUpdate.as_view(), name="projet_update"),
    path("projet/<int:pk>/delete/", ProjetDelete.as_view(), name="projet_delete"),
    path("observation/", ObsList.as_view(), name="obs_list"),
    path("observation/add/", ObsCreate.as_view(), name="obs_create"),
    path("observation/<int:pk>/edit/", ObsUpdate.as_view(), name="obs_update"),
    path("observation/<int:pk>/delete/", ObsDelete.as_view(), name="obs_delete")
]

# Ne pas oublier le / à la fin ! 
# On ajoute des URL parameters quand on a besoin d'accéder à un objet particulier (typiquement édition/suppression)