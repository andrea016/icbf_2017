# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-10 21:52
from __future__ import unicode_literals

import beneficiarios.models
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Beneficiario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(blank=True, default=datetime.datetime.now)),
                ('tipo_beneficiario', models.CharField(choices=[(b'NI', b'Ni\xc3\xb1o o Ni\xc3\xb1a'), (b'MG', b'Madre Gestante'), (b'ML', b'Madre Lactante')], max_length=2)),
                ('primer_nombre', models.TextField()),
                ('segundo_nombre', models.TextField(blank=True)),
                ('primer_apellido', models.TextField()),
                ('segundo_apellido', models.TextField(blank=True)),
                ('numero_documento', models.CharField(blank=True, max_length=15)),
                ('fecha_expedicion', models.CharField(blank=True, max_length=10)),
                ('lugar_expedicion', models.CharField(blank=True, max_length=5)),
                ('fecha_nacimiento', models.CharField(blank=True, max_length=10)),
                ('edad', models.DecimalField(blank=True, decimal_places=0, max_digits=1, null=True)),
                ('genero', models.CharField(blank=True, choices=[(b'M', b'Masculino'), (b'F', b'Femenino')], max_length=1)),
                ('foto', models.ImageField(blank=True, upload_to=beneficiarios.models.beneficiario_directory_path)),
                ('grupo_etnico', models.CharField(blank=True, choices=[(b'AF', b'Afrocolombiano'), (b'IN', b'Ind\xc3\xadgena'), (b'RG', b'Rrom/Gitano'), (b'RA', b'Raizal del Archipi\xc3\xa9lago de San Andr\xc3\xa9s'), (b'PA', b'Palenquero'), (b'NO', b'No se Autoreconze')], max_length=2)),
                ('grupo_perteneciente', models.TextField(blank=True)),
                ('a15', models.CharField(blank=True, choices=[(b'S', b'SI'), (b'N', b'NO')], max_length=2)),
                ('a16', models.CharField(blank=True, choices=[(b'S', b'SI'), (b'N', b'NO')], max_length=2)),
                ('direccion_acudiente', models.TextField(blank=True)),
                ('telefono_acudiente', models.CharField(blank=True, max_length=15, null=True)),
                ('a18', models.CharField(blank=True, choices=[(b'S', b'SI'), (b'N', b'NO')], max_length=2)),
                ('a19', models.CharField(blank=True, choices=[(b'S', b'SI'), (b'N', b'NO')], max_length=2)),
                ('modulo_b', models.CharField(blank=True, max_length=15)),
                ('modulo_c', models.CharField(blank=True, max_length=15)),
                ('modulo_d', models.CharField(blank=True, max_length=15)),
                ('modulo_e', models.CharField(blank=True, max_length=15)),
                ('modulo_f', models.CharField(blank=True, max_length=15)),
                ('modulo_g', models.CharField(blank=True, max_length=15)),
            ],
            options={
                'verbose_name_plural': 'Crear Beneficiario',
            },
        ),
    ]