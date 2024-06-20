from django import forms
from faunatrack.models import Projet 

class ProjetForm(forms.ModelForm):
    class Meta:
        model = Projet
        #fields = '__all__' # Tout les champs de mon model sont dans mon formulaire
        fields = ["titre", "description", "observations"]