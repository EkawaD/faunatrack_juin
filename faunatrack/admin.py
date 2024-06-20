from django.contrib import admin
from faunatrack.models import Espece, Observation, Scientifique, Projet
from import_export.resources import ModelResource
from import_export.admin import ImportExportModelAdmin
# from django.core.management import call_command

class EspeceRessource(ModelResource):
    class Meta:
        model = Espece


# admin.py permet d'enregistrer nos modèles dans l'interface admin
# On utilise un décorateur mais on peut aussi faire
# admin.site.register(Espece, EspeceAdmin)
@admin.register(Espece)
class EspeceAdmin(ImportExportModelAdmin):
   # list_display = ("nom",) # On peut utilise un tuple, mais ne pas oublier la virgule quand une seule valeur
    list_display = ["__str__", "status"]
    resource_class = EspeceRessource
    

@admin.register(Observation)
class ObservationAdmin(admin.ModelAdmin):
    list_display = ["__str__", "date", "quantite"]
    list_filter = ["espece"]
    search_field = ["espece__nom"]
    ordering = ["-date"]

    actions = ["to_danger_status"]

    def to_danger_status(self, request, queryset):
        for observation in queryset:
            espece = observation.espece
            espece.status = Espece.StatusChoice.DANGER
            espece.save()

@admin.register(Scientifique)
class ScientifiqueAdmin(admin.ModelAdmin):
    list_display = ["__str__", "universite"]

@admin.register(Projet)
class ProjetAdmin(admin.ModelAdmin):
    list_display = ["__str__", "titre"]
    filter_horizontal = ['observations', ]
    exclude = ["slug"]


# python manage.py createsuperuser