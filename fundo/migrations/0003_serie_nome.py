# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fundo', '0002_auto_20141108_2351'),
    ]

    operations = [
        migrations.AddField(
            model_name='serie',
            name='nome',
            field=models.CharField(max_length=255),
            preserve_default=False,
        ),
    ]
