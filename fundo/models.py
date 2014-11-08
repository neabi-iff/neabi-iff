# -*- coding: utf-8 -*-
from django.db import models
import hashlib


class Fundo(models.Model):
    titulo = models.CharField("título", max_length=255)
    biblioteca = models.CharField(max_length=255)
    descricao = models.TextField("Descrição")

    class Meta:
        verbose_name = "Fundo"
        verbose_name_plural = "Fundos"

    def __unicode__(self):
        return "%s" % self.titulo


# class Documento(models.Model):
#     codigo_referencia = models.CharField(verbose_name='Código de Referência', max_length=255)
#     titulo = models.CharField(verbose_name='Título', max_length=255)
#     data = models.DateField(verbose_name='Data do Documento')
#     dimensao_suporte = models.CharField(verbose_name='Dimensão e Suporte', max_length=255)
#     nivel_descricao = models.CharField(verbose_name='Nível de Descrição', max_length=255)
#     autor = models.CharField(verbose_name='Nome(s) do(s) Produtore(s)', max_length=255)
#     ambito_conteudo = models.TextField(verbose_name='Ámbito e Conteúdo')
#     condicao_acesso = models.CharField(verbose_name='Condição de Acesso', max_length=255)
#     nota_conservacao = models.CharField(verbose_name='Notas de Conservação', max_length=255)
#     nota_gerais = models.CharField(verbose_name='Notas Gerais', max_length=255)
#     slug = models.SlugField(blank=True)

#     class Meta:
#         verbose_name = "Documento"
#         verbose_name_plural = "Documentos"

#     def __unicode__(self):
#         return "%s - %s" % (self.codigo_referencia, self.titulo)

#     def save(self, *args, **kwargs):
#         if not self.slug:
#             self.slug = hashlib.md5(str(self.codigo_referencia)+str(self.id)).hexdigest()
#         return super(Documento, self).save(*args, **kwargs)


# class Serie(models.Model):
#     titulo = models.CharField(max_length=255)
#     descricao = models.TextField(verbose_name='Descrição')

#     class Meta:
#         verbose_name = "Serie"
#         verbose_name_plural = "Series"

#     def __unicode__(self):
#         pass
