from .models import SubCategory
from rest_framework import serializers

class SubCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SubCategory
        fields = ['idSubCategory','idCategory','name']