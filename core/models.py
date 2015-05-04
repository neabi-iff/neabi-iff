from django.db import models


class Contato(models.Model):
    descricao = models.TextField()
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    facebook = models.URLField()

    class Meta:
        verbose_name = 'Contato'
        verbose_name_plural = 'Contatos'

    def __unicode__(self):
        return '%s' % (self.descricao)

    # def save(self, *args, **kwargs):
    #     if Contato.objects.count() == 0:
    #         return super(Contato, self).save(*args, **kwargs)


class Acervo(models.Model):
    nome = models.CharField(max_length=1024)
    imagem = models.ImageField()
    link = models.URLField()

    class Meta:
        verbose_name = 'Acervo'
        verbose_name_plural = 'Acervos'

    def __unicode__(self):
        return '%s' % (self.nome)


class SobreNeabi(models.Model):
    sobre = models.TextField()

    class Meta:
        verbose_name = 'Sobre o Neabi'
        verbose_name_plural = 'Sobre o Neabi'

    def __unicode__(self):
        return '%s' % (self.sobre)
