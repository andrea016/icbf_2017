#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from operarios.models import Operario

tipo_ben = (('NI', 'Niño o Niña') , ('MG', 'Madre Gestante'),('ML','Madre Lactante'))
g_etnico = (( 'AF', 'Afrocolombiano'),( 'IN', 'Indígena'), ('RG','Rrom/Gitano'), ('RA','Raizal del Archipiélago de San Andrés'), ('PA','Palenquero'), ('NO','No se Autoreconze'))
list_sexo = ( ('M', 'Masculino') , ('F', 'Femenino'))
respuesta = ( ('S', 'SI') , ('N', 'NO'))
dias = (('1', '1 Dia') , ('2', '2 Dias'), ('3', '3 Dias'),('4', '4 Dias'), ('5', '5 Dias'), ('6', '6 Dias'), ('7', '7 Dias'))
horas = (('1', '1 Hora') , ('2', '2 Horas'), ('3', '3 Horas'),('4', '4 Horas'), ('5', '5 Horas'), ('6', '6 Horas'), ('7', '7 Horas'),('8', '8 Horas'),('8-12', '8 a 12 Horas'),('12', 'Mas de 12 Horas'))
estado_eps = (('A', 'Afiliado'),('D', 'Desafiliado'))
condicion_especial = (('VC', 'Victima Conflicto'),('CD', 'Con Discapacidad'),('VD', 'Victima Desastres'), ('OC', 'Otra Condicion'),('NA', 'Ninguna de las Anteriores'))
poblacion_prioritaria = (('S', 'Sisben'),('U', 'Unidos'),('N', 'Ninguno'))
beneficio_familias_accion = (( 'N', 'Nutrición'),( 'E', 'Educación'))
beneficio_programa =  (( 'D', 'Departamental'),( 'M', 'Municipal'),( 'O', 'ONG'),( 'X', 'Otro'))
estado_madre = (( 'G', 'Gestacion'),( 'L', 'Lactando'), ('N','Ninguna'))
apoyo_vecinos = (( 'T', 'Tienen Alguna Dificultad'),( 'F', 'Festejos Comunitarios'), ('C','Civicas o Comunitarias'),('D','Deportivas o Lúdicas'),('N','No se Apoya'))
comparte_vecinos = (( 'F', 'Fiestas Familiares'),( 'E', 'Emergencias Naturales'), ('D','Deportivas o Lúdicas'),('C','Civicas o Comunitarias'))
comparte_situaciones = (( 'F', 'Familiares'),( 'V', 'Vecinos'), ('A','Amigos'),('N','No los Comparten'))
solucion_conflictos = (( 'DA', 'Dialogando'),( 'SI', 'Se Ignoran'), ('DS','Discutiendo'),('UM','Utilizando Mecanismos Institucionales de Conciliación'),('OT','Otro'))
talentos = (( 'AR', 'Arte'),( 'ES', 'Escribir'), ('MU','Música'),( 'CS' ,'Coser'), ('CO','Cocinar'), ('PI','Pintar'), ('OR','Oralidad'), ('SE','Sembrar'), ('CE','Cerámica'),('CA','Carpinteria'),('PE','Pescar'),('OT','Otro'))
difusion_comunitaria = (( 'P', 'Perifoneo'),( 'C', 'Carteleras'), ('V','Voz a Voz'), ('E','Emisoras Comunitarias'), ('R','Redes Sociales'), ('O','Otro'))
z_ubicacion = ( ('C', 'Cabecera') , ('R', 'Resto'))
sanitario = (('EX', 'Exclusivo para el núcleo familiar'), ('CO', 'Compartido con otros núcleos'))
diagnos = (('DA', 'Desnutrición Aguda') , ('DG', 'Desnutrición Global'),('RA','Riesgo de Desnutrición Aguda'),('RG','Riesgo Desnutrición Global'),('OB','Obesidad'),('SO','Sobrepeso'),('RC','Retraso en el Crecimiento'),('RR','Riesgo de Retraso en el Crecimiento'), ('EU','Eutrófico (normal)'))
exam = (('CH','Cuadro Hemático'),('TH','THS'),('T3','T3'),('T4','Hormonas Tiroideas'),('PL','Perfil Lipídico'),('PS','Proteinas en Sangre'),('ES','Electrolitos en Sangre'),('HC','Hormona del Crecimiento'),('CP','Coprológico'),('GC','Glicemia'),('BS','Basal'))
program = (('CR','Centro de Recuperación Nutricional'),('RA','Recuperación Nutricional Ambulatoria'),('PL','Programas Liderados (Municipio/Distrito)'),('RN','Recuperación Nutricional Comunitaria'),('NI','Ninguno'),('OT','Otro'))
organizacion_barrio = (('DL','Deportivas o lúdicas'),('CO','Comunitarias'),('OS','Organizaciones sin ánimo de lucro'),('CI','Cívicas'),('AP','Asociaciones de padres de familia'),('RE','Religiosas'))
leche = (('MA','Leche materna complementada con alimentación familiar '),('VA','Leche de vaca y alimentación familiar'),('LF','Leche de formula'),('AF','Alimentación familiar'),('FA','Leche de formula y alimentación familiar'),('OF',' Leche de otro mamífero y alimentación familiar'),('OT','Otra'))
regimen = (('C','Contributivo'),('S','Subsidiado'),('E','Especial'))
tip_parto = (('N','Natural'),('A','Asistido'))
serv_parto = (('H','Hospitalario'),('N','No Hospitalario'))
carnet_desactualizado = (('DC','Desconocimiento de los cuidadores'),('DA','Dificultad de acceso a los servicios de salud'),('PC','Por decisión del cuidador'),('MC','Por motivos culturales'))
inasistencia_controles = (('PD','Por desconocimiento'),('SN','Se realizó la remisión pero no se ha asignado la cita'),('NO','No existe la oferta del servicio en el centro de salud'),('NA','No se encuentra afiliado al SGSSS'),('AN','La cita fue asignada pero no asistió'),('MN','Por que el médico no lo considera necesario'),('MG','El médico general no ha realizado la remisión al servicio'),('NS','Se niega el servicio'))
tipo_servicio_negado =('CE','Cita de consulta externa',('AU','Atención de urgencias'),
                    ('MF','Medicamentos formulados'),('VA','Vacunación'),('CC','Control de crecimiento y desarrollo'),
                    ('CF','Consulta oftalmológica'),('CO','Consulta odontológica'),('CX','Consulta con especialista'),
                    ('CI','Cirugía'),('OT','Otro'))
motivo_negacion = ('ND',' No hay citas disponibles',('NC','Por no tener el carnet de afiliación'),
                  ('NA','No le permitieron el acceso al hospital o centro de salud'),('OD','Porque se encuentra afiliado en otro departamento'),
                  ('LA','La actividad'),('IT','Intervención'),('PM','Procedimiento o medicamento'),('NS','No se encuentra cubierta por el POS'))


################ OCUPACIONES ##################

class Ocupaciones(models.Model):
    ocupacion = models.CharField(max_length=40, blank=False)
    def __str__(self):
        return self.ocupacion
    class Meta:
        verbose_name_plural = 'Crear Ocupacion'

################ ESTADO LABORAL ##################

class Estado_Laboral(models.Model):
    estado_laboral = models.CharField(max_length=40, blank=False)
    def __str__(self):
        return self.estado_laboral
    class Meta:
        verbose_name_plural = 'Crear Estados Laborales'

################ TIPO DOCUMENTO ##################

class Tipo_Documento(models.Model):
    tipo = models.CharField(max_length=30, blank=False)
    def __str__(self):
        return self.tipo
    class Meta:
        verbose_name_plural = 'Crear Tipos de Documento'

################ EPS ##################

class EPS(models.Model):
    nombre = models.CharField(max_length=100, blank=False)
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = 'Crear EPS'


class No_EPS(models.Model):
    causa_no_eps = models.CharField(max_length=50, blank=False)
    def __str__(self):
        return self.causa_no_eps
    class Meta:
        verbose_name_plural = 'Crear Causas que llevan a no tener EPS'


################ METAS PROYECTADAS A LAS CABEZA DE HOGAR ##################

class Metas_Cabeza(models.Model):
    metas = models.CharField(max_length=40, blank=False)
    def __str__(self):
        return self.metas
    class Meta:
        verbose_name_plural = 'Crear Metas Proyectadas a Cabezas de Hogar'


################ ORGANIZACIONES CIVILES  ##################

class Organizaciones_Civiles(models.Model):
    organizacion = models.CharField(max_length=40, blank=False)
    def __str__(self):
        return self.organizacion
    class Meta:
        verbose_name_plural = 'Crear Organizaciones Civiles'


############ PARENTEZCO ################

class Parentezco(models.Model):
    parentezco = models.CharField(max_length=40, blank=False)
    def __str__(self):
        return self.parentezco
    class Meta:
        verbose_name_plural = 'Crear Parentezco'

######### NIVEL DE ESCOLARIDAD ##############

class Nivel_Escolaridad(models.Model):
    nivel_escolaridad = models.CharField(max_length=40, blank=False)
    def __str__(self):
        return self.nivel_escolaridad
    class Meta:
        verbose_name_plural = 'Crear Nivel de Escolaridad'

################ LOCALIZACION ##################

class Paises(models.Model):
    pais = models.CharField(max_length=70, blank=False)
    def __str__(self):
        return self.pais
    class Meta:
        verbose_name_plural = 'Crear Pais'

class Departamentos(models.Model):
    pais = models.ForeignKey(Paises)
    departamento = models.CharField(max_length=70, blank=False)
    def __str__(self):
        return self.departamento
    class Meta:
        verbose_name_plural = 'Crear Departamento'

class Ciudades(models.Model):
    departamento = models.ForeignKey(Departamentos)
    ciudad = models.CharField(max_length=70, blank=False)
    def __str__(self):
        return self.ciudad
    class Meta:
        verbose_name_plural = 'Crear Ciudades o Municipios'

class Logs(models.Model):
    usuario = models.ForeignKey(Operario)
    accion = models.CharField( max_length=40,  null=False ,blank=False)
    modelo = models.CharField( max_length=40,  null=False ,blank=False)
    detalle = models.CharField( max_length=40,  null=False ,blank=False)
    referencia = models.CharField( max_length=40,  null=False ,blank=False)
    fecha = models.DateField(default=datetime.now, blank=True)
    hora  = models.TimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.modelo
