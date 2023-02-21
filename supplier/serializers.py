from .models import Supplier
from rest_framework import serializers

class SupplierSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Supplier
        fields = ['idSupplier','name_company','name_contact','phone_contact','whatsapp_contact','address','del_date']