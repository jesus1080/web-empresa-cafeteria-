from .models import Link

#funcion para extender el diccionario de contexto

def ctx_dict(request):
    ctx = {}
    links = Link.objects.all()
    for link in links:
        ctx[link.key] = link.url 
    return ctx