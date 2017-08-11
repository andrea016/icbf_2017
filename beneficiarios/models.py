#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from django.db import models
from django.contrib.auth.models import User
from parametrizacion.models import *
from entidad_administradora_servicio.models import *

def beneficiario_directory_path(instance,filename):
    return "media/beneficiarios/"'{0}/{1}'.format(instance.id ,filename)

class Beneficiario(models.Model):
    fecha  = models.DateField(default=datetime.now, blank=True)
    uds =  models.ForeignKey(UDS, null=False ,blank=False)
    tipo_beneficiario =  models.CharField( max_length=2, choices = tipo_ben)
    primer_nombre = models.TextField(null=False ,blank=False)
    segundo_nombre = models.TextField(null=False ,blank=True)
    primer_apellido = models.TextField(null=False ,blank=False)
    segundo_apellido = models.TextField(null=False ,blank=True)
    tipo_documento = models.ForeignKey(Tipo_Documento, null=False ,blank=True)
    numero_documento = models.CharField( max_length=15,  null=False ,blank=True)
    fecha_expedicion = models.CharField( max_length=10,  null=False ,blank=True)
    lugar_expedicion = models.CharField( max_length=5,  null=False ,blank=True)
    fecha_nacimiento = models.CharField( max_length=10,  null=False ,blank=True)
    edad =  models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    genero = models.CharField( max_length=1, choices = list_sexo,blank=True)
    foto =  models.ImageField(upload_to=beneficiario_directory_path, blank=True)
    pais = models.ForeignKey(Paises,null=True ,blank=True)
    departamento = models.ForeignKey(Departamentos,null=True ,blank=True)
    ciudad = models.ForeignKey(Ciudades,null=True ,blank=True)
    grupo_etnico =  models.CharField( max_length=2, choices = g_etnico,blank=True)
    #A14. Si el núcleo familiar del beneficiario se reconoce como Afrocolombiano o Indígena indique a qué comunidad, resguardo o territorio colectivo pertenece
    grupo_perteneciente = models.TextField(null=False ,blank=True)
    #A15. ¿En la familia se habla la lengua nativa del grupo étnico al que pertenece?
    a15 =  models.CharField( max_length=2, choices = respuesta,blank=True)
    #A16. ¿El beneficiario habla la lengua nativa del grupo étnico al que pertenece?
    a16 = models.CharField( max_length=2, choices = respuesta,blank=True)
    #A.17. Datos de contacto del Adulto responsable o acudiente
    direccion_acudiente = models.TextField(null=False ,blank=True)
    telefono_acudiente = models.CharField(max_length=15, null=True ,blank=True)
    #A.18. Ha sido víctima del desplazamiento forzado u otro hecho victimizante?
    a18 =  models.CharField( max_length=2, choices = respuesta,blank=True)
    #¿Algún miembro del grupo familiar con el que convive el beneficiario ha sido víctima del Desplazamiento forzado u otro hecho victimizante?
    a19 = models.CharField( max_length=2, choices = respuesta,blank=True)
    # Señale el tipo de relación del miembro del grupo familiar con el que convive, que ha sido víctima del Desplazamiento u otro hecho victimizante
    a20 = models.ForeignKey(Parentezco, null=True ,blank=True)
    #Banderas para saber que modulos estan completados
    modulo_b  =  models.CharField( max_length=15, null=False, blank=True)
    modulo_c = models.CharField( max_length=15, null=False, blank=True)
    modulo_d = models.CharField( max_length=15, null=False, blank=True)
    modulo_e = models.CharField( max_length=15, null=False, blank=True)
    modulo_f = models.CharField( max_length=15, null=False, blank=True)
    modulo_g = models.CharField( max_length=15, null=False, blank=True)

    def __str__(self):
        return str(self.primer_nombre)
    class Meta:
        verbose_name_plural = 'Crear Beneficiario'
