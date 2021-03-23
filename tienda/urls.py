from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('products', views.ProductViewSet)

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('api/v1/', include(router.urls)),
    path('search/', views.search, name="search"),
    path('search/asyn/', views.search_asynchronous, name="search_asyn"),
]