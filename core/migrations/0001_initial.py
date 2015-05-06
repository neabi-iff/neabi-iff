# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Acervo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=1024)),
                ('imagem', models.ImageField(upload_to=b'')),
                ('link', models.URLField()),
            ],
            options={
                'verbose_name': 'Acervo',
                'verbose_name_plural': 'Acervos',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descricao', models.TextField()),
                ('email', models.EmailField(max_length=75)),
                ('telefone', models.CharField(max_length=20)),
                ('facebook', models.URLField()),
            ],
            options={
                'verbose_name': 'Contato',
                'verbose_name_plural': 'Contatos',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SobreNeabi',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sobre', models.TextField()),
            ],
            options={
                'verbose_name': 'Sobre o Neabi',
                'verbose_name_plural': 'Sobre o Neabi',
            },
            bases=(models.Model,),
        ),
    ]
