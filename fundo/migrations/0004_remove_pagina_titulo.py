# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fundo', '0003_auto_20141111_1942'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pagina',
            name='titulo',
        ),
    ]
