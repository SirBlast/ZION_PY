from .models import Product
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['idProduct','idCategory','idSubCategory','description','product_name','price_unit_cop','placement']