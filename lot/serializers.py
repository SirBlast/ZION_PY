from .models import Lot
from rest_framework import serializers

class LotSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Lot
        fields = ['idLot','del_date']