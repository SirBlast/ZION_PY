from django.shortcuts import render
from rest_framework import permissions
from rest_framework import viewsets
from .models import Location
from .serializers import LocationSerializer

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_class = [permissions.IsAuthenticated]