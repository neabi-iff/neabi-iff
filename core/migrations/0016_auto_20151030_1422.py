# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import core.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_auto_20150929_1823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documento',
            name='arquivo',
            field=models.FileField(max_length=1024, upload_to=core.models.pasta_fundo_uploads, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='documento',
            name='autor',
            field=models.CharField(max_length=1024, verbose_name=b'Nome(s) do(s) Produtor(es)', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='documento',
            name='condicao_acesso',
            field=models.CharField(max_length=1024, verbose_name=b'Condi\xc3\xa7\xc3\xa3o de Acesso', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='documento',
            name='dimensao_suporte',
            field=models.CharField(max_length=1024, verbose_name=b'Dimens\xc3\xa3o e Suporte', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='documento',
            name='nivel_descricao',
            field=models.CharField(max_length=1024, verbose_name=b'N\xc3\xadvel de Descri\xc3\xa7\xc3\xa3o', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='documento',
            name='nota_conservacao',
            field=models.CharField(max_length=1024, verbose_name=b'Notas de Conserva\xc3\xa7\xc3\xa3o', blank=True),
            preserve_default=True,
        ),
    ]
