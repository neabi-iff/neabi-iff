# -*- coding: utf-8 -*-
from django.db import models
import hashlib
from datetime import datetime
from tinymce.models import HTMLField
import watson


def get_proximo_numero_id(self, model):
    ano_corrente = datetime.today().year
    try:
        ultimo_numero_id_ano = model.objects.filter(criado_em__year=ano_corrente).latest('id')
        proximo_numero_id = int(ultimo_numero_id_ano.id) + 1 # 20011-000001
    except model.DoesNotExist:
        proximo_numero_id = 1
    numero_id = "%s-%05d" % (ano_corrente, proximo_numero_id)

    return numero_id


def pasta_fundo_uploads(instance, filename):
    return 'uploads/neabi/fundo_{0}/serie_{1}/doc_{2}/{3}'.format(instance.serie.fundo,\
     instance.serie, instance, filename)


def pasta_fundo_uploads_images(instance, filename):
    return 'uploads/neabi/fundo_{0}/images/{1}'.format(instance,\
        filename)


from django.core.exceptions import ValidationError

def validar_maximo_uma_instancia(obj):
    model = obj.__class__
    if (model.objects.count() > 0 and
            obj.id != model.objects.get().id):
        raise ValidationError("Só pode criar uma instância de %s." % model.__name__)


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

    def clean(self):
        validar_maximo_uma_instancia(self)


class Neabi(models.Model):
    sobre = HTMLField("Sobre o Neabi")

    class Meta:
        verbose_name = 'Sobre o Neabi'
        verbose_name_plural = 'Sobre o Neabi'

    def __unicode__(self):
        return '%d' % (self.id)

    def clean(self):
        validar_maximo_uma_instancia(self)


class Publicacoes(models.Model):
    titulo = models.CharField(max_length=255)
    descricao = HTMLField("Descrição")
    arquivo = models.FileField(upload_to='uploads/neabi/publicacoes/', blank=True)

    class Meta:
        verbose_name = 'Plubicação'
        verbose_name_plural = 'Publicações'

    def __unicode__(self):
        return '%s' % (self.titulo)


class Fundo(models.Model):
    destaque = models.BooleanField(default=False)
    nome = models.CharField(max_length=255, unique=True)
    biblioteca = models.CharField(max_length=255)
    descricao = HTMLField("Descrição")
    imagem = models.ImageField(upload_to=pasta_fundo_uploads_images, blank=True)
    slug = models.SlugField(blank=True, max_length=255, editable=False)
    criado_em = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "Fundo"
        verbose_name_plural = "Fundos"

    def __unicode__(self):
        return u"%s" %(self.nome)

    def save(self, *args, **kwargs):
        return super(Fundo, self).save(*args, **kwargs)


class Serie(models.Model):
    nome = models.CharField(max_length=255, unique=True)
    descricao = HTMLField("Descrição")
    fundo = models.ForeignKey("Fundo")
    slug = models.SlugField(blank=True, max_length=255, editable=False)
    criado_em = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = u"Série"
        verbose_name_plural = u"Séries"

    def __unicode__(self):
        return u"%s" %(self.nome)


class Documento(models.Model):
    codigo_referencia = models.CharField('Código de Referência', max_length=255)
    nota_conservacao = models.CharField('Notas de Conservação', max_length=255)
    titulo = models.CharField('Título', max_length=255, unique=True)
    data = models.DateField('Data do Documento')
    ano = models.CharField('Ano do Documento', max_length=4)
    dimensao_suporte = models.CharField('Dimensão e Suporte', max_length=255)
    nivel_descricao = models.CharField('Nível de Descrição', max_length=255)
    autor = models.CharField('Nome(s) do(s) Autor(es)', max_length=255)
    ambito_conteudo = HTMLField('Ámbito e Conteúdo')
    condicao_acesso = models.CharField('Condição de Acesso', max_length=255)
    nota_gerais = models.CharField('Notas Gerais', max_length=255)
    serie = models.ForeignKey("Serie", verbose_name='Série')
    slug = models.SlugField(blank=True, max_length=255 , editable= False)
    criado_em = models.DateField(auto_now_add=True)
    arquivo = models.FileField(upload_to=pasta_fundo_uploads, blank=True)

    class Meta:
        verbose_name = "Documento"
        verbose_name_plural = "Documentos"

    def __unicode__(self):
        return u"%s" % (self.titulo)


class Social(models.Model):
    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    google_plus = models.URLField(blank=True)

    class Meta:
        verbose_name = "Social"
        verbose_name_plural = "Sociais"

    def __unicode__(self):
        return u"%d" % (self.id)

    def clean(self):
        validar_maximo_uma_instancia(self)


class Patrocinador(models.Model):
    nome = models.CharField(max_length=500)
    link = models.URLField(blank=True)
    imagem = models.ImageField(upload_to="uploads/neabi/patrocinadores/", blank=True)
    acervo = models.ForeignKey('Fundo')

    class Meta:
        verbose_name = "Patrocinador"
        verbose_name_plural = "Patrocinadores"

    def __unicode__(self):
        return u"%s" % (self.nome)


# SIGNALS
from django.db.models import signals
from django.template.defaultfilters import slugify

def create_slug(signal, instance, sender, **kwargs):
    """Este signal gera um slug automaticamente."""
    try:
        titulo = instance.titulo
    except:
        titulo = instance.nome
    slug = slugify(titulo)
    instance.slug = slug

signals.pre_save.connect(create_slug, sender=Documento)
signals.pre_save.connect(create_slug, sender=Fundo)
signals.pre_save.connect(create_slug, sender=Serie)



watson.register(Fundo)
watson.register(Serie)
watson.register(Documento)
