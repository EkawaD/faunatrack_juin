from django.contrib import admin
from faunatrack.models import Espece, Observation, Scientifique, Projet

# Register your models here.
@admin.register(Espece)
class EspeceAdmin(admin.ModelAdmin):
   # list_display = ("nom",) # ça c'est juste => tuple (2 entrées) /!\ si 1 entrée ne pas oublier la virgule
    list_display = ["__str__", "status"]

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