from django.contrib import admin
from django.urls import path
from faunatrack.views import home_page, ProjetList, ProjetDelete, ProjetCreate,ProjetUpdate

urlpatterns = [
    path("", home_page, name="home"),
    path("projet/", ProjetList.as_view(), name="projet_list"),
    path("projet/add/", ProjetCreate.as_view(), name="projet_create"),
    path("projet/<int:pk>/edit/", ProjetUpdate.as_view(), name="projet_update"),
    path("projet/<int:pk>/delete/", ProjetDelete.as_view(), name="projet_delete")
]

# Ne pas oublier le / à la fin ! 
# On ajoute des URL parameters quand on a besoin d'accéder à un objet particulier (typiquement édition/suppression)