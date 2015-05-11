# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fundo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='arquivo',
            options={'verbose_name': 'Arquivo', 'verbose_name_plural': 'Arquivos'},
        ),
        migrations.AddField(
            model_name='documento',
            name='numero',
            field=models.CharField(max_length=255, editable=False, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='serie',
            name='md5sum',
            field=models.SlugField(max_length=255, editable=False, blank=True),
            preserve_default=True,
        ),
    ]
