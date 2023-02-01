from .models import Location
from rest_framework import serializers

class LocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Location
        fields = ['idLocation','idCompany','name_contact','address','settings_admin','settings_user','phone_contact','cell_phone','email_contact','del_date','date_create','date_update','user_create','user_update']