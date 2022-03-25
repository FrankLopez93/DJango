from django.shortcuts import render
from django.http import HttpResponse
from gestionPedidos.models import Articulos

# Create your views here.

def busqueda_productos(request):
    return render(request, 'busqueda_productos.html')

def buscar(request):
    if request.GET['prd']:
        #[prd] es el name del input del formulario html
        #mensaje = 'Articulo buscado: %r' %request.GET['prd']
        producto = request.GET['prd']
        if len(producto) > 20:
            mensaje = 'Texto de busqueda demasiado largo'
        else:
            articulo = Articulos.objects.filter(nombre__icontains=producto)
            return render(request, 'resultados_busqueda.html', {'articulos': articulo, 'query': producto})
    else:
        mensaje = 'No has introducido nada'
  
    return HttpResponse(mensaje)

def contacto(request):
    if request.method == 'POST':
        return render(request, 'gracias.html')

    return render(request, 'contacto.html')