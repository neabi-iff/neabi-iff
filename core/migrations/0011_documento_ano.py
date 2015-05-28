# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20150526_2035'),
    ]

    operations = [
        migrations.AddField(
            model_name='documento',
            name='ano',
            field=models.IntegerField(default=1, verbose_name=b'Ano do Documento'),
            preserve_default=False,
        ),
    ]
