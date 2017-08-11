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
from icbf.settings import URL
from salud.models import Salud
from parametrizacion.views import registrarLogs
from beneficiarios.models import Beneficiario
import json

################## FUNCION GUARDAR O ACTUALIZAR SALUD ######################

@transaction.atomic
@csrf_exempt
@login_required(login_url="login:login")
def guardarSalud(request):
    if request.method == 'POST':
        if request.POST['f_estado'] == "INCOMPLETO":
            s = Salud()
            s.beneficiario_id = request.POST['f_ben']
            #F1. El niño o niña se encuentra afiliado al Sistema General de seguridad social en salud
            s.f1 =  request.POST['f1']
            #F2. El niño o niña es beneficiario del régimen
            s.f2 =  request.POST['f2']
            #F3. Nombre de la Entidad Promotora de Salud a la que se encuentra afiliado
            s.f3_id =  request.POST['f3']
            #Semana de gestación en la que ocurrio el parto (Nacimiento)
            s.semana_nacimiento =  request.POST['f3_semana']
            s.tipo_parto =  request.POST['f3_parto']
            s.servicio_parto =  request.POST['f3_servicio']
            #F4. ¿El niño o niña cuenta con el carnet de vacunación actualizado?
            s.f4 =   request.POST['f4']
            #F5. El niño o niña cuenta con el siguiente esquema de vacunación (Marque con una X aquellas que han sido aplicadas)
            s.f5 =  request.POST['vacunas_aplicadas']
            #F6. En caso de no contar con el carnet de vacunación al día según la edad del niño o niña ¿Cuál ha sido el motivo?
            s.save()

            f = Beneficiario.objects.get(id=request.POST['f_ben'])
            f.modulo_f = "COMPLETADO"
            f.save()
            registrarLogs(request.user.id,'GUARDAR','Salud','Guardar Salud',f.primer_nombre+" "+f.segundo_nombre+" "+f.primer_apellido+" "+f.segundo_apellido)
        else:
            s = Salud.objects.get(beneficiario=request.POST['f_ben'])
            #F1. El niño o niña se encuentra afiliado al Sistema General de seguridad social en salud
            s.f1 =  request.POST['f1']
            #F2. El niño o niña es beneficiario del régimen
            s.f2 =  request.POST['f2']
            #F3. Nombre de la Entidad Promotora de Salud a la que se encuentra afiliado
            s.f3_id =  request.POST['f3']
            #Semana de gestación en la que ocurrio el parto (Nacimiento)
            s.semana_nacimiento =  request.POST['f3_semana']
            s.tipo_parto =  request.POST['f3_parto']
            s.servicio_parto =  request.POST['f3_servicio']
            #F4. ¿El niño o niña cuenta con el carnet de vacunación actualizado?
            s.f4 =   request.POST['f4']
            #F5. El niño o niña cuenta con el siguiente esquema de vacunación (Marque con una X aquellas que han sido aplicadas)
            s.f5 =  request.POST['vacunas_aplicadas']
            #F6. En caso de no contar con el carnet de vacunación al día según la edad del niño o niña ¿Cuál ha sido el motivo?
            s.save()

            f = Beneficiario.objects.get(id=request.POST['f_ben'])
            registrarLogs(request.user.id,'ACTUALIZAR','Salud','Actualizar Salud',f.primer_nombre+" "+f.segundo_nombre+" "+f.primer_apellido+" "+f.segundo_apellido)
        messages.success(request, 'Salud')
        return HttpResponseRedirect('/beneficiarios')
    else:
        return HttpResponseRedirect("/")
