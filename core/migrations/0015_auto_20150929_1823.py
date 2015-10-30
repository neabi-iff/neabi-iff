# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import core.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20150604_2202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documento',
            name='arquivo',
            field=models.FileField(upload_to=core.models.pasta_fundo_uploads, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='documento',
            name='data',
            field=models.DateField(verbose_name=b'Data do Documento'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='documento',
            name='titulo',
            field=models.CharField(max_length=255, verbose_name=b'T\xc3\xadtulo'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='patrocinador',
            name='imagem',
            field=models.ImageField(upload_to=b'uploads/neabi/patrocinadores/'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publicacoes',
            name='arquivo',
            field=models.FileField(upload_to=b'uploads/neabi/publicacoes/'),
            preserve_default=True,
        ),
    ]
