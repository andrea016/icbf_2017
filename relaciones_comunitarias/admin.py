from django.contrib import admin
from relaciones_comunitarias.models import Relaciones

@admin.register(Relaciones)
class Relaciones(admin.ModelAdmin):
    pass
