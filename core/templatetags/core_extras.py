from django import template

register = template.Library()

@register.simple_tag
def get_url_fundo_com_projeto(slug_projeto):
    return "/neabi/projeto/%s/acervo/" %slug_projeto


@register.simple_tag
def get_url_fundo_sem_projeto(slug):
    return "/neabi/acervos/%s/" %slug


@register.simple_tag
def get_url_serie_com_projeto(slug_projeto, slug_acervo, slug):
    return "/neabi/projeto/%s/acervo/%s/serie/%s/" %(slug_projeto, slug_acervo, slug)


@register.simple_tag
def get_url_serie_sem_projeto(slug_acervo, slug):
    return "/neabi/acervos/%s/serie/%s/" %(slug_acervo, slug)

@register.simple_tag
def get_url_documento_com_projeto(slug_projeto, slug_acervo, slug_serie, slug):
    return "/neabi/projeto/%s/acervo/%s/serie/%s/documento/%s/" %(slug_projeto, slug_acervo, slug_serie, slug)


@register.simple_tag
def get_url_documento_sem_projeto(slug_acervo, slug_serie, slug):
    return "/neabi/acervos/%s/serie/%s/documento/%s/" %(slug_acervo, slug_serie, slug)