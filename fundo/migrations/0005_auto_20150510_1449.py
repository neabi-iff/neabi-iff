# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('fundo', '0004_auto_20150510_1437'),
    ]

    operations = [
        migrations.RenameField(
            model_name='documento',
            old_name='numero',
            new_name='numero_id',
        ),
        migrations.RenameField(
            model_name='fundo',
            old_name='numero',
            new_name='numero_id',
        ),
        migrations.RemoveField(
            model_name='serie',
            name='md5sum',
        ),
        migrations.AddField(
            model_name='serie',
            name='criado_em',
            field=models.DateField(default=datetime.datetime(2015, 5, 10, 14, 49, 28, 569937, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='serie',
            name='numero_id',
            field=models.CharField(max_length=255, editable=False, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='documento',
            name='slug',
            field=models.SlugField(max_length=255, editable=False, blank=True),
            preserve_default=True,
        ),
    ]
