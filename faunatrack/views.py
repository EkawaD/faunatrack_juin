
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse, HttpRequest
from faunatrack.models import Projet
from django.urls import reverse_lazy
from faunatrack.forms import ProjetForm

class ProjetCreate(CreateView):
    model = Projet 
    template_name = "projet_create.html"
    form_class = ProjetForm
    success_url = reverse_lazy('projet_list') # return redirect('projet_list')

class ProjetUpdate(UpdateView):
    model = Projet
    template_name = "projet_update.html"
    form_class = ProjetForm
    success_url = reverse_lazy('projet_list')

class ProjetDelete(DeleteView):
    model = Projet
    template_name = "projet_delete.html"
    success_url = reverse_lazy('projet_list')

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

