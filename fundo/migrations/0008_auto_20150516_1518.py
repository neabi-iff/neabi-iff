# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
import tinymce.models
import fundo.models


class Migration(migrations.Migration):

    dependencies = [
        ('fundo', '0007_auto_20150514_1957'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='arquivo',
            name='documento',
        ),
        migrations.DeleteModel(
            name='Arquivo',
        ),
        migrations.AddField(
            model_name='documento',
            name='arquivo',
            field=models.FileField(default=datetime.datetime(2015, 5, 16, 15, 18, 50, 742933, tzinfo=utc), upload_to=fundo.models.pasta_fundo_uploads),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='documento',
            name='ambito_conteudo',
            field=tinymce.models.HTMLField(verbose_name=b'\xc3\x81mbito e Conte\xc3\xbado'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='fundo',
            name='descricao',
            field=tinymce.models.HTMLField(verbose_name=b'Descri\xc3\xa7\xc3\xa3o'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='serie',
            name='descricao',
            field=tinymce.models.HTMLField(verbose_name=b'Descri\xc3\xa7\xc3\xa3o'),
            preserve_default=True,
        ),
    ]
