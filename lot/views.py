from django.shortcuts import render, redirect
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import LotSerializer
from .models import Lot



class LotViewSet(viewsets.ModelViewSet):
    queryset = Lot.objects.all()
    serializer_class = LotSerializer
    permission_class = [permissions.IsAuthenticated]
    