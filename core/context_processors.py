from .models import Social, Fundo


def social(request):
    return {'social': Social.objects.first()}


def destaque_acervo(request):
    try:
        destaque_acervo = Fundo.objects.get(destaque=True)
        if destaque_acervo.patrocinador_set.all():
            patrocinadores = destaque_acervo.patrocinador_set.all()
        else:
            patrocinadores = None
    except:
        destaque_acervo = None
        patrocinadores = None
    return {'destaque_acervo': destaque_acervo,
            'patrocinadores': patrocinadores}
