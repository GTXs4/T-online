from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from .models import Product
from django.shortcuts import render, redirect

# Create your views here.
class Home(ListView):
    model = Product
    paginate_by = 12

def search(request):
    """
    Obtenemos mediante get el producto que 
    se esta buscando
    """
    text = request.GET.get('text', '') # Obtenemos el texto mediante GET
    text = text.upper() # Ponemos el texto en mayusculas
    products = Product.objects.filter(name__contains=text)
    if not products:
        # Si no encontro el producto con mayuscula, prueba con minusculas
        text = text.lower()
        products = Product.objects.filter(name__contains=text)
    if not products:
        # Si no encontro el producto con minusculas, prueba capitalizar
        text = text.capitalize()
        products = Product.objects.filter(name__contains=text)
    if not products:
        # Si no encontro el producto con capitalizar, prueba title
        text = text.title()
        products = Product.objects.filter(name__contains=text)  
    return render(request, 'tienda/search.html', {'products':products})
