# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Neabi',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sobre', tinymce.models.HTMLField(verbose_name=b'Sobre o Neabi')),
            ],
            options={
                'verbose_name': 'Sobre o Neabi',
                'verbose_name_plural': 'Sobre o Neabi',
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='SobreNeabi',
        ),
    ]
