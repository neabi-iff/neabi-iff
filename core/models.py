# -*- coding: utf-8 -*-
from django.db import models


class Documento(models.Model):
    codigo_referencia = models.CharField(verbose_name='Código de Referência', max_length=255)
    titulo = models.CharField(verbose_name='Título', max_length=255)
    data = models.DateField(verbose_name='Data do Documento')
    dimensao_suporte = models.CharField(verbose_name='Dimensão e Suporte', max_length=255)
    nivel_descricao = models.CharField(verbose_name='Nível de Descrição', max_length=255)
    autor = models.CharField(verbose_name='Nome(s) do(s) Produtore(s)', max_length=255)
    ambito_conteudo = models.TextField(verbose_name='Ámbito e Conteúdo')
    condicao_acesso = models.CharField(verbose_name='Condição de Acesso', max_length=255)
    nota_conservacao = models.CharField(verbose_name='Notas de Conservação', max_length=255)
    nota_gerais = models.CharField(verbose_name='Notas Gerais', max_length=255)

    class Meta:
        verbose_name = "Documento"
        verbose_name_plural = "Documentos"

    def __unicode__(self):
        pass
