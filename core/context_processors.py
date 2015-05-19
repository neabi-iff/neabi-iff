from .models import Social, Patrocinador, Fundo

def social(request):
    return {'social': Social.objects.first()}

def destaque_acervo(request):
    try:
        destaque_acervo = Fundo.objects.get(destaque=True)
        patrocinadores = destaque_acervo.patrocinador_set.all()
    except:
        destaque_acervo = None
        patrocinadores = None
    return {'destaque_acervo': destaque_acervo, 'patrocinadores': patrocinadores}