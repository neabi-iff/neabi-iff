# -*- coding: utf-8 -*-
from django.db import models
from tinymce.models import HTMLField


class Contato(models.Model):
    descricao = HTMLField("Descrição", blank=True)
    email = models.EmailField(blank=True)
    telefone = models.CharField(max_length=255, blank=True)
    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    google_plus = models.URLField(blank=True)

    class Meta:
        verbose_name = 'Contato'
        verbose_name_plural = 'Contatos'

    def __unicode__(self):
        return '%s' % (self.id)

class Neabi(models.Model):
    sobre = HTMLField("Sobre o Neabi")

    class Meta:
        verbose_name = 'Sobre o Neabi'
        verbose_name_plural = 'Sobre o Neabi'

    def __unicode__(self):
        return '%d' % (self.id)

class Publicacoes(models.Model):
    titulo = models.CharField(max_length=255)
    descricao = HTMLField("Descrição")
    arquivo = models.FileField(upload_to='uploads/neabi/publicacoes/', blank=True)

    class Meta:
        verbose_name = 'Plubicação'
        verbose_name_plural = 'Publicações'

    def __unicode__(self):
        return '%s' % (self.titulo)
