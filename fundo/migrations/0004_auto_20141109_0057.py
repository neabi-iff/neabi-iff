# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fundo', '0003_serie_nome'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='serie',
            options={'verbose_name': 'S\xe9rie', 'verbose_name_plural': 'S\xe9ries'},
        ),
        migrations.RemoveField(
            model_name='fundo',
            name='titulo',
        ),
        migrations.AddField(
            model_name='fundo',
            name='nome',
            field=models.CharField(max_length=255, verbose_name=b'Nome do Fundo'),
            preserve_default=False,
        ),
    ]
