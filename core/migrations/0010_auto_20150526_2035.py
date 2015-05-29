# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_patrocinador_acervo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='documento',
            name='numero_id',
        ),
        migrations.RemoveField(
            model_name='fundo',
            name='numero_id',
        ),
        migrations.RemoveField(
            model_name='serie',
            name='numero_id',
        ),
    ]
