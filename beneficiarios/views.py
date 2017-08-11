#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.http import HttpResponseRedirect, HttpResponse,Http404
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.db import transaction
from django.contrib import auth,messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.contrib.auth.hashers import make_password
from django.views.decorators.csrf import csrf_exempt
from icbf.settings import URL, SERVIDOR, GRUPO1, GRUPO2, STATIC_URL,AWS_SECRET_ACCESS_KEY, AWS_STORAGE_BUCKET_NAME, AWS_ACCESS_KEY_ID
from parametrizacion.models import  *
from beneficiarios.models import Beneficiario
from relaciones_comunitarias.models import Relaciones
from nutricion.models import Nutricion
from salud.models import Salud
from caracteristicas_vivienda.models import *
from entidad_administradora_servicio.models import *
from composicion_familiar.models import *
from operarios.models import Operario
from parametrizacion.views import registrarLogs
from django.db.models import Q
import json, os, boto3, tinys3, time

################## LISTADO BENEFICIARIOS ######################

@login_required(login_url="login:login")
def beneficiarios(request):
    if User.objects.filter(pk=request.user.id, groups__name=GRUPO1).exists():
        beneficiarios = Beneficiario.objects.all()
        return render(request,'beneficiarios/listado_beneficiarios.html',{'beneficiarios': beneficiarios })

################## TEMPLATE CREAR BENEFICIRARIO  ######################

@login_required(login_url="login:login")
def crearBeneficiario(request):
    paises = Paises.objects.all()
    unidades_servicio = UDS.objects.all()
    tipos_documentos = Tipo_Documento.objects.all().exclude(tipo = "NIT").exclude(tipo="RUT")
    lugares_expedicion = Ciudades.objects.all()
    miembros = Parentezco.objects.all()
    return render(request,'beneficiarios/nuevo_beneficiario.html',{ 'paises': paises ,'unidades_servicio': unidades_servicio,
                'tipos_documentos': tipos_documentos,'lugares_expedicion': lugares_expedicion,
                'miembros':miembros })

################## FUNCION GUARDAR BENEFICIARIO ######################

@transaction.atomic
@csrf_exempt
@login_required(login_url="login:login")
def guardarBeneficiario(request):
    if request.method == 'POST':
        if  User.objects.filter(pk=request.user.id, groups__name=GRUPO1).exists():
            b = Beneficiario()
            b.uds_id = request.POST['uds']
            b.tipo_beneficiario = request.POST['tip_ben']
            b.primer_nombre = request.POST['1nombre']
            b.segundo_nombre = request.POST['2nombre']
            b.primer_apellido = request.POST['1apellido']
            b.segundo_apellido = request.POST['2apellido']

            if request.POST['bandera_foto'] == "CAMBIO":
                b.foto = request.FILES['archivo']
            else:
                b.foto = "media/beneficiarios/no_photo.png"

            b.tipo_documento_id = request.POST['tip_doc']
            b.numero_documento = request.POST['numdoc']
            b.fecha_expedicion = request.POST['fec_exp']
            b.lugar_expedicion = request.POST['lug_exp']
            b.fecha_nacimiento = request.POST['fec_nac']
            diferencia_fechas = datetime.strptime(time.strftime("%Y-%m-%d"), '%Y-%m-%d') - datetime.strptime(request.POST['fec_nac'], '%Y-%m-%d')
            edad_numerica = diferencia_fechas.days / 365.2425
            b.edad = str(round(edad_numerica,0))
            b.genero = request.POST['genero']
            b.pais_id = request.POST['pais_nac']
            b.departamento_id = request.POST['departamento_nac']
            b.ciudad_id = request.POST['ciudad_nac']
            b.grupo_etnico = request.POST['grupo_etnico']
            #A14. Si el núcleo familiar del beneficiario se reconoce como Afrocolombiano o Indígena indique a qué comunidad, resguardo o territorio colectivo pertenece
            b.grupo_perteneciente = request.POST['a14']
            #A15. ¿En la familia se habla la lengua nativa del grupo étnico al que pertenece?
            b.a15 = request.POST['a15']
            #A16. ¿El beneficiario habla la lengua nativa del grupo étnico al que pertenece?
            b.a16 = request.POST['a16']
            #A.17. Datos de contacto del Adulto responsable o acudiente
            b.direccion_acudiente = request.POST['direccion_acu']
            b.telefono_acudiente = request.POST['tel_acu']
            #A.18. Ha sido víctima del desplazamiento forzado u otro hecho victimizante?
            b.a18 = request.POST['a18']
            #¿Algún miembro del grupo familiar con el que convive el beneficiario ha sido víctima del Desplazamiento forzado u otro hecho victimizante?
            b.a19 = request.POST['a19']
            # Señale el tipo de relación del miembro del grupo familiar con el que convive, que ha sido víctima del Desplazamiento u otro hecho victimizante
            b.a20_id = request.POST['a20']
            b.modulo_b = "INCOMPLETO"
            b.modulo_c = "INCOMPLETO"
            b.modulo_d = "INCOMPLETO"
            b.modulo_e = "INCOMPLETO"
            b.modulo_f = "INCOMPLETO"
            b.modulo_g = "INCOMPLETO"
            b.save()
            registrarLogs(request.user.id,'GUARDAR','Beneficiarios','Guardar Beneficiario',b.primer_nombre+" "+b.segundo_nombre+" "+b.primer_apellido+" "+b.segundo_apellido)
            messages.success(request, 'Creado')
            return HttpResponseRedirect('/beneficiarios')
        else:
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect("/")


################## TEMPLATE EDITAR BENEFICIARIO ######################

@login_required(login_url="login:login")
def editarBeneficiario(request,id = None):
    url = URL
    paises = Paises.objects.all()
    unidades_servicio = UDS.objects.all()
    tipos_documentos = Tipo_Documento.objects.all().exclude(tipo = "NIT").exclude(tipo="RUT")
    lugares_expedicion = Ciudades.objects.all()
    miembros = Parentezco.objects.all()
    try:
        caracteristicas = CaracteristicasVivienda.objects.get(beneficiario = id)
    except:
        caracteristicas = ""
    try:
        cabeza_nucleo = Cabeza_Nucleo.objects.get(beneficiario = id)
    except:
        cabeza_nucleo = ""
    try:
        relaciones = Relaciones.objects.get(beneficiario = id)
    except:
        relaciones = ""
    try:
        nutricion = Nutricion.objects.get(beneficiario = id)
    except:
        nutricion = ""
    try:
        salud = Salud.objects.get(beneficiario = id)
    except:
        salud = ""
    try:
        factores_riesgo = Factores_Riesgo.objects.get(beneficiario = id)
    except:
        factores_riesgo= ""

    tipos_viviendas = Tipo_Vivienda.objects.all()
    tipos_tenencias = Tipo_Tenencia_Vivienda.objects.all()
    tipos_camas = Tipo_Cama.objects.all()
    servicios_domiciliarios = Servicios_Domiciliarios.objects.all()
    fuentes_agua = Fuente_Agua_Consumible.objects.all()
    periodo_agua  = Periodo_Agua.objects.all()
    usos_aguas = Uso_Agua.objects.all()
    tratamiento_basuras = Tratamiento_Basuras.objects.all()
    tipos_sanitarios = Tipo_Sanitario.objects.all()
    servicios_comunitarios = Servicios_Comunitarios.objects.all()
    nivel_escolaridad = Nivel_Escolaridad.objects.all()
    ocupaciones = Ocupaciones.objects.all()
    estados_laborales = Estado_Laboral.objects.all()
    listado_eps = EPS.objects.all()
    miembros_familia = Familiar.objects.filter(beneficiario = id)
    causas_no_eps = No_EPS.objects.all()
    metas_cabeza = Metas_Cabeza.objects.all()
    organizaciones_civiles = Organizaciones_Civiles.objects.all()

    print(salud)

    if  User.objects.filter(pk=request.user.id, groups__name=GRUPO1).exists():
        beneficiario = Beneficiario.objects.get(id = id)
        return render(request,'beneficiarios/editar_beneficiario.html',{'beneficiario': beneficiario,
                    'url': url ,'paises': paises,'unidades_servicio': unidades_servicio,
                    'tipos_documentos': tipos_documentos,'lugares_expedicion': lugares_expedicion,
                    'miembros':miembros,'caracteristicas': caracteristicas,'cabeza_nucleo': cabeza_nucleo,
                    'relaciones':relaciones, 'nutricion': nutricion, 'salud': salud, 'factores_riesgo': factores_riesgo,
                    'tipos_viviendas':tipos_viviendas,'tipos_tenencias': tipos_tenencias,
                    'tipos_camas': tipos_camas , 'servicios_domiciliarios': servicios_domiciliarios,
                    'fuentes_agua': fuentes_agua,'periodo_agua': periodo_agua, 'usos_aguas': usos_aguas,
                    'tratamiento_basuras': tratamiento_basuras, 'tipos_sanitarios':tipos_sanitarios,
                    'servicios_comunitarios': servicios_comunitarios, 'nivel_escolaridad': nivel_escolaridad,
                    'ocupaciones': ocupaciones, 'estados_laborales': estados_laborales, 'listado_eps': listado_eps,
                    'miembros_familia': miembros_familia, 'causas_no_eps': causas_no_eps, 'metas_cabeza': metas_cabeza,
                    'organizaciones_civiles' : organizaciones_civiles })
    else:
        return HttpResponseRedirect('/')

################## FUNCION ACTUALIZAR AGENTE ##############

@login_required(login_url="login:login")
def actualizarBeneficiario(request):
    if request.method == 'POST':
        b = Beneficiario.objects.get(id=request.POST['beneficiario_id'])
        diferencia_fechas = datetime.strptime(time.strftime("%Y-%m-%d"), '%Y-%m-%d') - datetime.strptime(request.POST['fec_nac'], '%Y-%m-%d')
        edad_numerica = diferencia_fechas.days / 365.2425
        b.edad = str(round(edad_numerica,0))
        b.grupo_etnico = request.POST['grupo_etnico']
        #A14. Si el núcleo familiar del beneficiario se reconoce como Afrocolombiano o Indígena indique a qué comunidad, resguardo o territorio colectivo pertenece
        b.grupo_perteneciente = request.POST['a14']
        #A15. ¿En la familia se habla la lengua nativa del grupo étnico al que pertenece?
        b.a15 = request.POST['a15']
        #A16. ¿El beneficiario habla la lengua nativa del grupo étnico al que pertenece?
        b.a16 = request.POST['a16']
        #A.17. Datos de contacto del Adulto responsable o acudiente
        b.direccion_acudiente = request.POST['direccion_acu']
        b.telefono_acudiente = request.POST['tel_acu']
        #A.18. Ha sido víctima del desplazamiento forzado u otro hecho victimizante?
        b.a18 = request.POST['a18']
        #¿Algún miembro del grupo familiar con el que convive el beneficiario ha sido víctima del Desplazamiento forzado u otro hecho victimizante?
        b.a19 = request.POST['a19']
        # Señale el tipo de relación del miembro del grupo familiar con el que convive, que ha sido víctima del Desplazamiento u otro hecho victimizante
        b.a20_id = request.POST['a20']

        """
        f_anterior = str(b.foto)
        if request.POST['bandera_foto'] == "CAMBIO":
            b.foto  = request.FILES['archivo']
            if  f_anterior != ("media/beneficiarios/no_photo.png"):
                try:
                    conn = tinys3.Connection(AWS_ACCESS_KEY_ID,AWS_SECRET_ACCESS_KEY)
                    conn.delete(f_anterior,AWS_STORAGE_BUCKET_NAME)
                except OSError as e:
                    print(e)
            if int(request.POST['beneficiario_id']) == request.user.id:
                request.session["foto"] = URL +"media/beneficiarios/" + str(request.POST['beneficiario_id']) +"/"+str(b.foto)
            messages.success(request, 'Actualizado')
        else:
            b.foto = f_anterior
            messages.success(request, 'Actualizado')

        """

        b.save()
        registrarLogs(request.user.id,'ACTUALIZAR','Beneficiarios','Actualizar Beneficiario',b.primer_nombre+" "+b.segundo_nombre+" "+b.primer_apellido+" "+b.segundo_apellido)

        return HttpResponseRedirect('/beneficiarios')
    else:
        return HttpResponseRedirect('/')


################## FUNCION ELIMINAR BENEFICIARIO ######################

@csrf_exempt
@transaction.atomic
@login_required(login_url="login:login")
def eliminarBeneficiario(request, id=None):
  if request.method == 'DELETE':
      if User.objects.filter(pk=request.user.id, groups__name=GRUPO1).exists():
           usu = User.objects.get(id=id)
           beneficiario = Beneficiario.objects.get(id = id)
           """
           conn = tinys3.Connection(AWS_ACCESS_KEY_ID,AWS_SECRET_ACCESS_KEY)
           conn.delete(str(beneficiario.foto),AWS_STORAGE_BUCKET_NAME)
           """
           beneficiario.delete()
           registrarLogs(request.user.id,'ELIMINAR','Beneficiarios','Eliminar Beneficiario',usu.first_name + " " + usu.last_name)
           usu.delete()
           messages.success(request, 'Borrado')
           return HttpResponse(status=200)
      else:
          return HttpResponseRedirect("/")
  else:
      return HttpResponseRedirect("/")
