#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from django.db import models
from django.contrib.auth.models import User
from parametrizacion.models import *
from beneficiarios.models import Beneficiario


class Salud(models.Model):
    beneficiario = models.ForeignKey(Beneficiario, null=False ,blank=False)
    f1 = models.CharField( max_length=2, choices = respuesta,blank=True)
    #F2. El niño o niña es beneficiario del régimen
    f2 =models.CharField( max_length=2,  null=False ,blank=True)
    #F3. Nombre de la Entidad Promotora de Salud a la que se encuentra afiliado
    f3 = models.ForeignKey(EPS, null=False ,blank=False)
    #Semana de gestación en la que ocurrio el parto (Nacimiento)
    semana_nacimiento = models.CharField( max_length=4,  null=False ,blank=True)
    tipo_parto = models.CharField( max_length=2,  null=False ,blank=True)
    servicio_parto =  models.CharField( max_length=2,  null=False ,blank=True)
    #F4. ¿El niño o niña cuenta con el carnet de vacunación actualizado?
    f4 =  models.CharField( max_length=2, choices = respuesta,blank=True)
    #F5. El niño o niña cuenta con el siguiente esquema de vacunación (Marque con una X aquellas que han sido aplicadas)
    f5 = models.TextField(null=False ,blank=True)

    def __str__(self):
        return str(self.beneficiario)
