from .models import User
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['idUser','idPerson','user_name','password','date_last_log','role','del_date']