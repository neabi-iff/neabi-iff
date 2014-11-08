# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fundo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=255, verbose_name=b't\xc3\xadtulo')),
                ('biblioteca', models.CharField(max_length=255)),
                ('descricao', models.TextField(verbose_name=b'Descri\xc3\xa7\xc3\xa3o')),
            ],
            options={
                'verbose_name': 'Fundo',
                'verbose_name_plural': 'Fundos',
            },
            bases=(models.Model,),
        ),
    ]
