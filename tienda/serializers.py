from .models import Product
from rest_framework import serializers
from django.contrib.humanize.templatetags.humanize import intcomma

class ProductSerializer(serializers.ModelSerializer):

    url_image = serializers.ImageField(use_url=False)
    price = serializers.SerializerMethodField('get_price_formatted')

    class Meta:
        model = Product
        fields = '__all__'

    def get_price_formatted(self, product):
        return intcomma(product.price)