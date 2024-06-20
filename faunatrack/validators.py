from django.forms import ValidationError

def validate_latitude(value):
    if value < -90 or value > 90:
        raise ValidationError("La latitude doit être comprise entre -90 et 90 degré")
    
def validate_longitude(value):
    if value < -180 or value > 180:
        raise ValidationError("La longitude doit être comprise entre -180 et 180 degré")
    

# 3 types de validation
# - côté client (templates/) géré automatiquement par Django
# - côté formulaires (forms.py) A valider dans ma class ModelForm
# - côté base de donnée (models.py) A valider dans ma class Model