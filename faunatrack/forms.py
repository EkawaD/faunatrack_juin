from django import forms
from faunatrack.models import Projet, Observation

class ProjetForm(forms.ModelForm):
    class Meta:
        model = Projet
        #fields = '__all__' # Tout les champs de mon model sont dans mon formulaire
        fields = ["titre", "description", "observations"]

class ObsForm(forms.ModelForm):
    class Meta:
        model = Observation
        fields = '__all__'
