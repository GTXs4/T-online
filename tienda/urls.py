from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('search/', views.search, name="search"),
    path('search/asyn/', views.search_asynchronous, name="search_asyn"),
]