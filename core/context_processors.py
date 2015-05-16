from .models import Social

def social(request):
    return {'social': Social.objects.first()}