from .models import Person
from rest_framework import serializers

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['idPerson','idLocation','first_name','last_name','idNumber','address','telephone','email_contact','date_of_birth','del_date','date_create','date_update','user_create','user_update']