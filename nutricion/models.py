#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from django.db import models
from django.contrib.auth.models import User
from parametrizacion.models import *
from beneficiarios.models import Beneficiario

class Controles(models.Model):
    beneficiario  = models.ForeignKey(Beneficiario, null=False ,blank=False)
    numero_orden = models.CharField( max_length=20,  null=False ,blank=False)
    fecha_control = models.CharField( max_length=10,  null=False ,blank=False)
    edad_anios = models.CharField( max_length=2,  null=False ,blank=False)
    edad_meses = models.CharField( max_length=2,  null=False ,blank=False)
    peso_kilos = models.CharField( max_length= 2,  null=False ,blank=False)
    peso_gramos = models.CharField( max_length= 4,  null=False ,blank=False)
    talla = models.CharField( max_length=3,  null=False ,blank=False)
    interpretacion = models.TextField(null=False ,blank=True)
    peso_idealK = models.CharField( max_length = 2,  null=False ,blank=True)
    peso_idealG = models.CharField( max_length= 4,  null=False ,blank=True)
    talla_ideal = models.CharField( max_length=3,  null=False ,blank=True)
    estado = models.CharField( max_length=20,  null=False ,blank=True)
    color = models.CharField( max_length=10,  null=False ,blank=True)

class CantidadControles(models.Model):
    beneficiario  = models.ForeignKey(Beneficiario, null=False ,blank=False)
    edad =  models.CharField( max_length=20,  null=False ,blank=True)
    cantidad =  models.CharField( max_length=20,  null=False ,blank=True)
    fecha = models.CharField( max_length=10,  null=False ,blank=True)

class Examenes(models.Model):
    beneficiario  = models.ForeignKey(Beneficiario, null=False ,blank=False)
    toma = models.CharField(max_length=10,  null=False ,blank=True)
    diagnostico = models.CharField( max_length=2, choices = diagnos, blank=True)
    examenen = models.CharField( max_length=2, choices = exam, blank=True)
    programa = models.CharField( max_length=2, choices = program, blank=True)
    otro = models.CharField( max_length=30,  null=False ,blank=True)

class Nutricion(models.Model):
    beneficiario = models.ForeignKey(Beneficiario, null=False ,blank=False)
    peso_nacer = models.CharField( max_length=4,  null=False ,blank=True)
    talla_nacer = models.CharField( max_length=4,  null=False ,blank=True)
    #E3. ¿El niño o niña cuenta con el carnet actualizado de crecimiento y desarrollo
    e3 =  models.CharField( max_length=2, choices = respuesta,blank=True)
    #E4 Si el niño o niña cuenta con el carnet de crecimiento y desarrollo verifique, cuantos controles de crecimiento y desarrollo ha recibido en los últimos 6 meses
    e4 =  models.TextField(null=False ,blank=True)
    e4_f1 =  models.CharField( max_length=10,  null=False ,blank=True)
    e4_f2 =  models.CharField( max_length=10,  null=False ,blank=True)
    e4_f3 =  models.CharField( max_length=10,  null=False ,blank=True)
    #E5. Si el niño o niña es menor de seis meses ¿Está siendo alimentado con leche materna de forma exclusiva?
    e5 =  models.CharField( max_length=2, choices = respuesta,blank=True)
    #E6. Si la respuesta anterior es NO, ¿qué tipo de alimentación recibe el niño o niña menor de seis meses?
    e6 = models.CharField( max_length=2, choices = leche,blank=True)
    e6_otra = models.TextField(null=False ,blank=True)
    #E7. Si el niño o niña es mayor de 6 meses y menor de 2 años, está siendo alimentado con
    e7 = models.CharField( max_length=2, choices = leche,blank=True)
    e7_otra = models.TextField(null=False ,blank=True)
    #E8. Si el niño o niña presenta diagnóstico de desnutrición u obesidad, le han realizado los siguientes exámenes
    t1_d8 = models.TextField(null=False ,blank=True)
    id_t1_d8 = models.TextField(null=False ,blank=True)
    e1_d8 = models.TextField(null=False ,blank=True)
    id_e1_d8 = models.TextField(null=False ,blank=True)
    a1_d8 = models.TextField(null=False ,blank=True)
    id_a1_d8 = models.TextField(null=False ,blank=True)
    t2_d8 = models.TextField(null=False ,blank=True)
    id_t2_d8 = models.TextField(null=False ,blank=True)
    e2_d8 = models.TextField(null=False ,blank=True)
    id_e2_d8 = models.TextField(null=False ,blank=True)
    a2_d8 = models.TextField(null=False ,blank=True)
    id_a2_d8 = models.TextField(null=False ,blank=True)
    t3_d8 = models.TextField(null=False ,blank=True)
    id_t3_d8 = models.TextField(null=False ,blank=True)
    e3_d8 = models.TextField(null=False ,blank=True)
    id_e3_d8 = models.TextField(null=False ,blank=True)
    a3_d8 = models.TextField(null=False ,blank=True)
    id_a3_d8 = models.TextField(null=False ,blank=True)
    t4_d8 = models.TextField(null=False ,blank=True)
    id_t4_d8 = models.TextField(null=False ,blank=True)
    e4_d8 = models.TextField(null=False ,blank=True)
    id_e4_d8 = models.TextField(null=False ,blank=True)
    a4_d8 = models.TextField(null=False ,blank=True)
    id_a4_d8 = models.TextField(null=False ,blank=True)
    #E9. El niño o niña mayor de dos años ¿ha recibido en el último año antiparasitarios, por parte de algún servicio de salud?
    e9 = models.CharField( max_length=2, choices = respuesta,blank=True)
    #E10. En caso de haber recibido antiparasitarios, indique la última fecha en la que fue tomada por el niño o niña
    e10 = models.CharField( max_length=10,  null=False ,blank=True)
    #E11. El niño o niña tiene alguna dieta especial o restricción alimentaria o alergia alimentaria
    e11 = models.CharField( max_length=2, choices = respuesta,blank=True)
    e11_cual = models.TextField(null=False ,blank=True)

    def __str__(self):
        return str(self.nombres)
