# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('fundo', '0003_documento_criado_em'),
    ]

    operations = [
        migrations.AddField(
            model_name='fundo',
            name='criado_em',
            field=models.DateField(default=datetime.datetime(2015, 5, 10, 14, 37, 11, 709495, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fundo',
            name='numero',
            field=models.CharField(max_length=255, editable=False, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='documento',
            name='slug',
            field=models.SlugField(max_length=255, blank=True),
            preserve_default=True,
        ),
    ]
