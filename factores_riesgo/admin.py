from django.contrib import admin
from composicion_familiar.models import Familiar

@admin.register(Familiar)
class Factores_RiesgoAdmin(admin.ModelAdmin):
    #list_display = ('nombres', 'parentezco', 'tipo_documento', 'numero_documento')
    pass
