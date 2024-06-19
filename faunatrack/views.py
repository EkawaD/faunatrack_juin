from typing import Any
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.http import HttpResponse, HttpRequest
from faunatrack.models import Projet

# Class based view
# Class HelloWorld:
# Create your views here.

def hello_world(request):
    return HttpResponse('Hello world!')

def home_page(request: HttpRequest):
    couleur = 'bleu'
    if request.user.is_authenticated:
        return render(request, 'base.html', {
            "couleur_du_ciel": couleur
        })
    return redirect('login')

class ProjetList(ListView):
    model = Projet
    queryset = Projet.objects.filter(titre__icontains="premier")
    template_name = "projet_list.html"


