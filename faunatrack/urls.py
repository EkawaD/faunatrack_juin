from django.contrib import admin
from django.urls import path
from faunatrack.views import home_page, ProjetList

urlpatterns = [
    path("", home_page, name="home"),
    path("projet/", ProjetList.as_view(), name="projet_list")
]

