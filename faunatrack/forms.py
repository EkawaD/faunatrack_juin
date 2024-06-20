from django import forms
from faunatrack.models import Projet, Observation
from faunatrack.validators import validate_latitude

# Lorsque l'on a une vue Create ou Update, on doit définir une class Form qui hérite de ModelForm
class ProjetForm(forms.ModelForm):
    class Meta:
        model = Projet # On précise le model...
        fields = ["titre", "description", "observations"] # .. et les champs que l'on veut

class ObsForm(forms.ModelForm):
    class Meta:
        model = Observation
        fields = '__all__' # Tout les champs de mon model sont dans mon formulaire


    def clean_latitude(self):
        ''' 
        Pour valider les données d'un formulaire, on surcharge les méthodes
        clean_xxxx pour valider le champ xxx 
        On doit toujours retourner la valeur attendue.
        '''
        latitude = self.cleaned_data.get('latitude')
        validate_latitude(latitude)
        return latitude
    
    def clean_longitude(self):
        ''' Exemple ou on ajoute une validation sur le formulaire UNIQUEMENT (pas dans le model)'''
        latitude = self.cleaned_data.get('longitude')
        if latitude > 150:
            raise forms.ValidationError("Vous êtes un grand malade !!")
        return latitude