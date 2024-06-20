from django import forms
from faunatrack.models import Projet, Observation
from faunatrack.validators import validate_latitude

class ProjetForm(forms.ModelForm):
    class Meta:
        model = Projet
        #fields = '__all__' # Tout les champs de mon model sont dans mon formulaire
        fields = ["titre", "description", "observations"]

class ObsForm(forms.ModelForm):
    class Meta:
        model = Observation
        fields = '__all__'

    def clean_latitude(self):
        latitude = self.cleaned_data.get('latitude')
        validate_latitude(latitude)
        return latitude
    
    def clean_longitude(self):
        latitude = self.cleaned_data.get('longitude')
        if latitude > 150:
            raise forms.ValidationError("Vous êtes un grand malade !!")
        return latitude