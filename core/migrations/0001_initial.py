# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo_referencia', models.CharField(max_length=255, verbose_name=b'C\xc3\xb3digo de Refer\xc3\xaancia')),
                ('titulo', models.CharField(max_length=255, verbose_name=b'T\xc3\xadtulo')),
                ('data', models.DateField(verbose_name=b'Data do Documento')),
                ('dimensao_suporte', models.CharField(max_length=255, verbose_name=b'Dimens\xc3\xa3o e Suporte')),
                ('nivel_descricao', models.CharField(max_length=255, verbose_name=b'N\xc3\xadvel de Descri\xc3\xa7\xc3\xa3o')),
                ('autor', models.CharField(max_length=255, verbose_name=b'Nome(s) do(s) Produtore(s)')),
                ('ambito_conteudo', models.TextField(verbose_name=b'\xc3\x81mbito e Conte\xc3\xbado')),
                ('condicao_acesso', models.CharField(max_length=255, verbose_name=b'Condi\xc3\xa7\xc3\xa3o de Acesso')),
                ('nota_conservacao', models.CharField(max_length=255, verbose_name=b'Notas de Conserva\xc3\xa7\xc3\xa3o')),
                ('nota_gerais', models.CharField(max_length=255, verbose_name=b'Notas Gerais')),
            ],
            options={
                'verbose_name': 'Documento',
                'verbose_name_plural': 'Documentos',
            },
            bases=(models.Model,),
        ),
    ]
