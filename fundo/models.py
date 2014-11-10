# -*- coding: utf-8 -*-
from django.db import models
#import hashlib


class Fundo(models.Model):
    nome = models.CharField("Nome do Fundo", max_length=255)
    biblioteca = models.CharField(max_length=255)
    descricao = models.TextField("Descrição")

    class Meta:
        verbose_name = "Fundo"
        verbose_name_plural = "Fundos"

    def __unicode__(self):
        return u"%s" % self.nome


class Serie(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField("Descrição")

    class Meta:
        verbose_name = u"Série"
        verbose_name_plural = u"Séries"

    def __unicode__(self):
        return u"%s" % self.nome


class Documento(models.Model):
    codigo_referencia = models.CharField('Código de Referência', max_length=255)
    nota_conservacao = models.CharField('Notas de Conservação', max_length=255)
    titulo = models.CharField('Título', max_length=255)
    data = models.DateField('Data do Documento')
    dimensao_suporte = models.CharField('Dimensão e Suporte', max_length=255)
    nivel_descricao = models.CharField('Nível de Descrição', max_length=255)
    autor = models.CharField('Nome(s) do(s) Autor(es)', max_length=255)
    ambito_conteudo = models.TextField('Ámbito e Conteúdo')
    condicao_acesso = models.CharField('Condição de Acesso', max_length=255)
    nota_gerais = models.CharField('Notas Gerais', max_length=255)
    slug = models.SlugField(blank=True)
    serie = models.ForeignKey("Serie", verbose_name='Série')
    fundo = models.ForeignKey("Fundo")

    class Meta:
        verbose_name = "Documento"
        verbose_name_plural = "Documentos"

    def __unicode__(self):
        return u"%s (%s)" % (self.titulo, self.codigo_referencia)

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
