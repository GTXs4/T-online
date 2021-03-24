from django.views.generic.base import TemplateView
from .models import Product, Category
from .serializers import ProductSerializer
from rest_framework import viewsets, filters
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import render

# Create your views here.
class Home(TemplateView):
    template_name = 'tienda/home.html'

    def get(self, request):
        return render(request, self.template_name, {'categories': Category.objects.all()})

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
