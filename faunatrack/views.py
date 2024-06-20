
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.http import HttpResponse, HttpRequest
from faunatrack.models import Projet, Observation
from django.urls import reverse_lazy
from faunatrack.forms import ProjetForm, ObsForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from faunatrack.models import Scientifique

# Vue sous forme de fonction 
# Permet de renvoyer ce que l'on veut.
# Généralement une HTTPResponse (texte)
# Un template avec un contexte (render)
# On peut également rediriger vers une autre url (redirect)
def hello_world(request):
    return HttpResponse('Hello world!')


def home_page(request: HttpRequest):
    couleur = 'bleu'
    if request.user.is_authenticated:
        return render(request, 'base.html', {
            "couleur_du_ciel": couleur
        })
    return redirect('login')



class AuthMixin(LoginRequiredMixin, UserPassesTestMixin):

    # lorsque j'ai un UserPassesTestMixin, je dois définir cette fonction avec ce nom
    def test_func(self):
        try:
            Scientifique.objects.get(user=self.request.user)
            return True
        except Scientifique.DoesNotExist:
            return False
        
    # def test_func3(self):
    #     scientifique = Scientifique.objects.filter(user=self.request.user).first()
    #     if not scientifique:
    #         return False
    #     return True

class ProjetList(AuthMixin, ListView):
    model = Projet
    # queryset = Projet.objects.filter(titre__icontains="premier")
    template_name = "projet_list.html"

    # def get():
    #     o = Output1.objects.all()
    #     with open(o.path) as f:
    #         to_memory(f)
    #     return render(request, 'template.html', {
    #         'data': to_memory
    #     })

class ProjetCreate(AuthMixin, CreateView):
    model = Projet 
    template_name = "projet_create.html"
    form_class = ProjetForm
    success_url = reverse_lazy('projet_list') # return redirect('projet_list')
    permission_required = "add_projet" # add/delete/change/list + "_" + nom_du_model_lowercase 

class ProjetUpdate(AuthMixin, UpdateView):
    model = Projet
    template_name = "projet_update.html"
    form_class = ProjetForm
    success_url = reverse_lazy('projet_list')

class ProjetDelete(AuthMixin, DeleteView):
    model = Projet
    template_name = "projet_delete.html"
    success_url = reverse_lazy('projet_list')

class ProjetDetail(AuthMixin, DetailView):
    pass

class ObsList(AuthMixin, ListView):
    model = Observation
    template_name = "obs_list.html"

class ObsCreate(AuthMixin, CreateView):
    model = Observation 
    template_name = "obs_create.html"
    form_class = ObsForm
    success_url = reverse_lazy('obs_list') 

class ObsUpdate(AuthMixin,UpdateView):
    model = Observation 
    template_name = "obs_update.html"
    form_class = ObsForm
    success_url = reverse_lazy('obs_list') 

class ObsDelete(AuthMixin, DeleteView):
    model = Observation 
    template_name = "obs_delete.html"
    success_url = reverse_lazy('obs_list') 