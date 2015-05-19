# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_social'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patrocinador',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=500)),
                ('link', models.URLField(blank=True)),
                ('imagem', models.ImageField(upload_to=b'uploads/neabi/patrocinadores/', blank=True)),
            ],
            options={
                'verbose_name': 'Patrocinador',
                'verbose_name_plural': 'Patrocinadores',
            },
            bases=(models.Model,),
        ),
    ]
