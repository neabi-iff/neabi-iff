# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import fundo.models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('fundo', '0005_auto_20150510_1449'),
    ]

    operations = [
        migrations.AddField(
            model_name='fundo',
            name='imagem',
            field=models.ImageField(default=datetime.datetime(2015, 5, 10, 21, 5, 54, 320702, tzinfo=utc), upload_to=fundo.models.pasta_fundo_uploads_images),
            preserve_default=False,
        ),
    ]
