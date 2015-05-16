# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20150515_1724'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publicacoes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=255)),
                ('descricao', tinymce.models.HTMLField(verbose_name=b'Descri\xc3\xa7\xc3\xa3o')),
                ('arquivo', models.FileField(upload_to=b'uploads/neabi/publicacoes/')),
            ],
            options={
                'verbose_name': 'Plubica\xe7\xe3o',
                'verbose_name_plural': 'Publica\xe7\xf5es',
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='Acervo',
        ),
        migrations.AlterField(
            model_name='contato',
            name='descricao',
            field=tinymce.models.HTMLField(verbose_name=b'Descri\xc3\xa7\xc3\xa3o', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contato',
            name='email',
            field=models.EmailField(max_length=75, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contato',
            name='facebook',
            field=models.URLField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contato',
            name='google_plus',
            field=models.URLField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contato',
            name='telefone',
            field=models.CharField(max_length=255, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contato',
            name='twitter',
            field=models.URLField(blank=True),
            preserve_default=True,
        ),
    ]
