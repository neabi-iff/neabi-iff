# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_patrocinador'),
    ]

    operations = [
        migrations.AddField(
            model_name='fundo',
            name='destaque',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
