# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import core.models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20150515_1842'),
    ]

    operations = [
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo_referencia', models.CharField(max_length=255, verbose_name=b'C\xc3\xb3digo de Refer\xc3\xaancia')),
                ('nota_conservacao', models.CharField(max_length=255, verbose_name=b'Notas de Conserva\xc3\xa7\xc3\xa3o')),
                ('titulo', models.CharField(unique=True, max_length=255, verbose_name=b'T\xc3\xadtulo')),
                ('data', models.DateField(verbose_name=b'Data do Documento')),
                ('dimensao_suporte', models.CharField(max_length=255, verbose_name=b'Dimens\xc3\xa3o e Suporte')),
                ('nivel_descricao', models.CharField(max_length=255, verbose_name=b'N\xc3\xadvel de Descri\xc3\xa7\xc3\xa3o')),
                ('autor', models.CharField(max_length=255, verbose_name=b'Nome(s) do(s) Autor(es)')),
                ('ambito_conteudo', tinymce.models.HTMLField(verbose_name=b'\xc3\x81mbito e Conte\xc3\xbado')),
                ('condicao_acesso', models.CharField(max_length=255, verbose_name=b'Condi\xc3\xa7\xc3\xa3o de Acesso')),
                ('nota_gerais', models.CharField(max_length=255, verbose_name=b'Notas Gerais')),
                ('slug', models.SlugField(max_length=255, editable=False, blank=True)),
                ('numero_id', models.CharField(max_length=255, editable=False, blank=True)),
                ('criado_em', models.DateField(auto_now_add=True)),
                ('arquivo', models.FileField(upload_to=core.models.pasta_fundo_uploads, blank=True)),
            ],
            options={
                'verbose_name': 'Documento',
                'verbose_name_plural': 'Documentos',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Fundo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(unique=True, max_length=255)),
                ('biblioteca', models.CharField(max_length=255)),
                ('descricao', tinymce.models.HTMLField(verbose_name=b'Descri\xc3\xa7\xc3\xa3o')),
                ('imagem', models.ImageField(upload_to=core.models.pasta_fundo_uploads_images, blank=True)),
                ('slug', models.SlugField(max_length=255, editable=False, blank=True)),
                ('numero_id', models.CharField(max_length=255, editable=False, blank=True)),
                ('criado_em', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Fundo',
                'verbose_name_plural': 'Fundos',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Serie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(unique=True, max_length=255)),
                ('descricao', tinymce.models.HTMLField(verbose_name=b'Descri\xc3\xa7\xc3\xa3o')),
                ('slug', models.SlugField(max_length=255, editable=False, blank=True)),
                ('numero_id', models.CharField(max_length=255, editable=False, blank=True)),
                ('criado_em', models.DateField(auto_now_add=True)),
                ('fundo', models.ForeignKey(to='core.Fundo')),
            ],
            options={
                'verbose_name': 'S\xe9rie',
                'verbose_name_plural': 'S\xe9ries',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='documento',
            name='serie',
            field=models.ForeignKey(verbose_name=b'S\xc3\xa9rie', to='core.Serie'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publicacoes',
            name='arquivo',
            field=models.FileField(upload_to=b'uploads/neabi/publicacoes/', blank=True),
            preserve_default=True,
        ),
    ]
