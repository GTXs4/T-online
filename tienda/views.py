from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from .models import Product
from .serializers import ProductSerializer
from rest_framework import viewsets, filters
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend

from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.http import JsonResponse

# Create your views here.
class Home(ListView):
    model = Product
    paginate_by = 12

class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # Paginacion
    pagination_class = PageNumberPagination
    pagination_class.page_size = 12

    # Filtros
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    # Campos para la busqueda
    search_fields = ['name']
    # Campos para la ordenacion
    ordering_fields = ['name', 'price', 'category']
    # Campos para los filtros
    filterset_fields = {
        'price': ['lte', 'gte'],
        'category': ['exact']
    }

def search(request):
    """
    Obtenemos mediante get el producto que 
    se esta buscando
    """
    text = request.GET.get('text', '') # Obtenemos el texto mediante GET
    page_num = int(request.GET.get('page', 1))
    products = Product.objects.filter(name__icontains=text)
    product_paginator = Paginator(products, 12)
    page = product_paginator.get_page(page_num)
    context = {
        'text' : text,
        'page' : page
        }
    return render(request, 'tienda/search.html', context)

def search_asynchronous(request):
    text = request.GET.get('text', '')
    products = Product.objects.filter(name__icontains=text)
    product_paginator = Paginator(products, 12)
    page = product_paginator.get_page(1)

    # Crea una lista de diccionarios con los productos
    page_products = []
    for product in page.object_list:
        page_products.append({
            'name' : product.name, 
            'price' : product.price, 
            'url' : product.url_image.url[1:] if product.url_image else None
            })
    # Asigna las pagina previa y la siguiente
    try:
        next_page = page.next_page_number()
    except:
        next_page = None
    try:
        previous_page = page.previous_page_number()
    except:
        previous_page = None 
    
    json_response = {
        'text' : text,
        'next_page' : next_page,
        'previous_page' : previous_page, 
        'page_products' : page_products        
        }
    return JsonResponse(json_response, safe=False)
