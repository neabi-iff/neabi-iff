# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models
import core.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20150527_1827'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projeto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=1024)),
                ('descricao', tinymce.models.HTMLField(verbose_name=b'Descri\xc3\xa7\xc3\xa3o')),
                ('slug', models.SlugField(max_length=255, editable=False, blank=True)),
            ],
            options={
                'verbose_name': 'Projeto',
                'verbose_name_plural': 'Projetos',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='fundo',
            name='projeto',
            field=models.OneToOneField(null=True, blank=True, to='core.Projeto'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='documento',
            name='ambito_conteudo',
            field=tinymce.models.HTMLField(verbose_name=b'\xc3\x81mbito e Conte\xc3\xbado', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='documento',
            name='ano',
            field=models.CharField(max_length=4, verbose_name=b'Ano do Documento', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='documento',
            name='arquivo',
            field=models.FileField(upload_to=core.models.pasta_fundo_uploads),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='documento',
            name='autor',
            field=models.CharField(max_length=255, verbose_name=b'Nome(s) do(s) Produtor(es)', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='documento',
            name='codigo_referencia',
            field=models.CharField(max_length=255, verbose_name=b'C\xc3\xb3digo de Refer\xc3\xaancia', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='documento',
            name='condicao_acesso',
            field=models.CharField(max_length=255, verbose_name=b'Condi\xc3\xa7\xc3\xa3o de Acesso', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='documento',
            name='data',
            field=models.DateField(verbose_name=b'Data do Documento', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='documento',
            name='dimensao_suporte',
            field=models.CharField(max_length=255, verbose_name=b'Dimens\xc3\xa3o e Suporte', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='documento',
            name='nivel_descricao',
            field=models.CharField(max_length=255, verbose_name=b'N\xc3\xadvel de Descri\xc3\xa7\xc3\xa3o', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='documento',
            name='nota_conservacao',
            field=models.CharField(max_length=255, verbose_name=b'Notas de Conserva\xc3\xa7\xc3\xa3o', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='documento',
            name='nota_gerais',
            field=tinymce.models.HTMLField(verbose_name=b'Notas Gerais', blank=True),
            preserve_default=True,
        ),
    ]
