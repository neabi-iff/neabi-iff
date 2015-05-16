# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import fundo.models


class Migration(migrations.Migration):

    dependencies = [
        ('fundo', '0006_fundo_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fundo',
            name='imagem',
            field=models.ImageField(upload_to=fundo.models.pasta_fundo_uploads_images, blank=True),
            preserve_default=True,
        ),
    ]
