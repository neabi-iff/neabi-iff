# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fundo', '0002_auto_20141110_0026'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pagina',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=255, verbose_name=b'T\xc3\xadtulo')),
                ('arquivo', models.ImageField(upload_to=b'paginas/')),
                ('documento', models.ForeignKey(to='fundo.Documento')),
            ],
            options={
                'verbose_name': 'Pagina',
                'verbose_name_plural': 'Paginas',
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='documento',
            options={'verbose_name': 'Documento', 'verbose_name_plural': 'Documentos'},
        ),
        migrations.AlterField(
            model_name='documento',
            name='autor',
            field=models.CharField(max_length=255, verbose_name=b'Nome(s) do(s) Autor(es)'),
            preserve_default=True,
        ),
    ]
