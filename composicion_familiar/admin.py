from django.contrib import admin
from composicion_familiar.models import Familiar, Cabeza_Nucleo

@admin.register(Familiar)
class FamiliarAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'parentezco', 'tipo_documento', 'numero_documento')

@admin.register(Cabeza_Nucleo)
class Cabeza_Nucleo(admin.ModelAdmin):
    pass
