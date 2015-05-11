# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('fundo', '0002_auto_20150510_1424'),
    ]

    operations = [
        migrations.AddField(
            model_name='documento',
            name='criado_em',
            field=models.DateField(default=datetime.datetime(2015, 5, 10, 14, 30, 50, 335973, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
