from django.contrib import admin
from operarios.models import *

@admin.register(Operario)
class Operario(admin.ModelAdmin):
    pass
