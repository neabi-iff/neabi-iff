# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_documento_ano'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documento',
            name='ano',
            field=models.CharField(max_length=4, verbose_name=b'Ano do Documento'),
            preserve_default=True,
        ),
    ]
