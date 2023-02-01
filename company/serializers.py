from .models import Company
from rest_framework import serializers

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = ['idCompany','name_contact','nit','description','settings_admin','settings_user','phone_contact','cell_phone_contact','email_contact','date_create','date_update','user_create','user_update']