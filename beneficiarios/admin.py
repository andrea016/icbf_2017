from django.contrib import admin
from beneficiarios.models import *

@admin.register(Beneficiario)
class Beneficiario(admin.ModelAdmin):
    pass
