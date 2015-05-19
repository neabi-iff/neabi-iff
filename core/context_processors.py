from .models import Social, Patrocinador, Fundo

def social(request):
    return {'social': Social.objects.first()}

def patrocinadores(request):
    return {'patrocinadores': Patrocinador.objects.all()}

def destaque_acervo(request):
    try:
        destaque_acervo = Fundo.objects.get(destaque=True)
    except:
        destaque_acervo = None
    return {'destaque_acervo': destaque_acervo }