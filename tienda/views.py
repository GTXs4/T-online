from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from .models import Product
from django.shortcuts import render

# Create your views here.
class Home(ListView):
    model = Product
    paginate_by = 3
