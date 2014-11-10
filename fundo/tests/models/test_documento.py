# -*- coding: utf-8 -*-
from django.test import TestCase
from model_mommy import mommy
from fundo.models import Documento
from fundo.mommy_recipes import serie, fundo


class TestModelDocumento(TestCase):

    def setUp(self):
        self.documento = mommy.make_recipe('fundo.documento',
                                           codigo_referencia="ABN001",
                                           titulo=u'Pensão',
                                           serie=serie.make(nome="Liberdade"),
                                           fundo=fundo.make(nome="Fundo liberdade")
                                           )

    def test_verifica_se_o_documento_foi_criado(self):
        all_documento_in_database = Documento.objects.all()
        self.assertEquals(len(all_documento_in_database), 1)
        self.assertEquals(self.documento.codigo_referencia, u"ABN001")
        self.assertEquals(self.documento.titulo, u"Pensão")
        self.assertEquals(unicode(self.documento.serie), "Liberdade")
        self.assertEquals(unicode(self.documento.fundo), "Fundo liberdade")

    def test_representacao_unicode_do_objeto(self):
        self.assertEqual(unicode(self.documento), u"Pensão (ABN001)")

    def test_verbose_name_da_classe(self):
        verbose_name = Documento._meta.verbose_name
        self.assertEqual(verbose_name, 'Documento')

    def test_verbose_name_plural_da_classe(self):
        verbose_name_plural = Documento._meta.verbose_name_plural
        self.assertEqual(verbose_name_plural, 'Documentos')

    def test_verbose_name_do_campo_codigo_referencia(self):
        codigo_referencia = Documento._meta.get_field('codigo_referencia')
        self.assertEqual(codigo_referencia.verbose_name, 'Código de Referência')

    def test_verbose_name_do_campo_nota_conservacao(self):
        nota_conservacao = Documento._meta.get_field('nota_conservacao')
        self.assertEqual(nota_conservacao.verbose_name, 'Notas de Conservação')

    def test_verbose_name_do_campo_titulo(self):
        titulo = Documento._meta.get_field('titulo')
        self.assertEqual(titulo.verbose_name, 'Título')

    def test_verbose_name_do_campo_data(self):
        data = Documento._meta.get_field('data')
        self.assertEqual(data.verbose_name, 'Data do Documento')

    def test_verbose_name_do_campo_dimensao_suporte(self):
        dimensao_suporte = Documento._meta.get_field('dimensao_suporte')
        self.assertEqual(dimensao_suporte.verbose_name, 'Dimensão e Suporte')

    def test_verbose_name_do_campo_nivel_descricao(self):
        nivel_descricao = Documento._meta.get_field('nivel_descricao')
        self.assertEqual(nivel_descricao.verbose_name, 'Nível de Descrição')

    def test_verbose_name_do_campo_autor(self):
        autor = Documento._meta.get_field('autor')
        self.assertEqual(autor.verbose_name, 'Nome(s) do(s) Autor(es)')

    def test_verbose_name_do_campo_ambito_conteudo(self):
        ambito_conteudo = Documento._meta.get_field('ambito_conteudo')
        self.assertEqual(ambito_conteudo.verbose_name, 'Ámbito e Conteúdo')

    def test_verbose_name_do_campo_condicao_acesso(self):
        condicao_acesso = Documento._meta.get_field('condicao_acesso')
        self.assertEqual(condicao_acesso.verbose_name, 'Condição de Acesso')

    def test_verbose_name_do_campo_nota_gerais(self):
        nota_gerais = Documento._meta.get_field('nota_gerais')
        self.assertEqual(nota_gerais.verbose_name, 'Notas Gerais')

    def test_verbose_name_do_campo_serie(self):
        serie = Documento._meta.get_field('serie')
        self.assertEqual(serie.verbose_name, 'Série')

    def test_save_deve_gerar_slug(self):
        import hashlib
        slug = hashlib.md5('ABN001').hexdigest()
        self.assertEqual(self.documento.slug, slug)