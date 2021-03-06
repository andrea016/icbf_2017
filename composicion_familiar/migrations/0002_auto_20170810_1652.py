# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-10 21:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('composicion_familiar', '0001_initial'),
        ('beneficiarios', '0002_auto_20170810_1652'),
        ('parametrizacion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='familiar',
            name='estado_laboral',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='parametrizacion.Estado_Laboral'),
        ),
        migrations.AddField(
            model_name='familiar',
            name='nivel_escolaridad',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='parametrizacion.Nivel_Escolaridad'),
        ),
        migrations.AddField(
            model_name='familiar',
            name='nombre_eps',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='parametrizacion.EPS'),
        ),
        migrations.AddField(
            model_name='familiar',
            name='ocupacion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='parametrizacion.Ocupaciones'),
        ),
        migrations.AddField(
            model_name='familiar',
            name='parentezco',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parametrizacion.Parentezco'),
        ),
        migrations.AddField(
            model_name='familiar',
            name='tipo_documento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='parametrizacion.Tipo_Documento'),
        ),
        migrations.AddField(
            model_name='cabeza_nucleo',
            name='beneficiario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='beneficiarios.Beneficiario'),
        ),
    ]
