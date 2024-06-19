from django.contrib import admin
from django.urls import path
from faunatrack.views import hello_world

urlpatterns = [
    path("hello_world/", hello_world, name="home")
]
