from django.shortcuts import render
from .models import Person
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import PersonSerializer



class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_class = [permissions.IsAuthenticated]
