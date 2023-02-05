from .models import Lot
from rest_framework import serializers

class LotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lot
        fields = ['idLot','del_date']