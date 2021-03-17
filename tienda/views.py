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
    products = Product.objects.filter(name__icontains=text) 
    return render(request, 'tienda/search.html', {'products':products})
