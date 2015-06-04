# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20150528_2355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documento',
            name='codigo_referencia',
            field=models.CharField(max_length=255, verbose_name=b'C\xc3\xb3digo de Refer\xc3\xaancia *', blank=True),
            preserve_default=True,
        ),
    ]
