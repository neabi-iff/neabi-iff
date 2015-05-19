# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_fundo_destaque'),
    ]

    operations = [
        migrations.AddField(
            model_name='patrocinador',
            name='acervo',
            field=models.ForeignKey(default=1, to='core.Fundo'),
            preserve_default=False,
        ),
    ]
