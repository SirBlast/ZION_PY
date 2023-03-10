from .models import Purchase
from rest_framework import serializers

class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = ['idPurchase','idUser','idProduct','idSupplier','idLot','amount','cost','note','del_date']