# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fundo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='documento',
            name='fundo',
            field=models.ForeignKey(to='fundo.Fundo'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='documento',
            name='serie',
            field=models.ForeignKey(verbose_name=b'S\xc3\xa9rie', to='fundo.Serie'),
            preserve_default=False,
        ),
    ]
