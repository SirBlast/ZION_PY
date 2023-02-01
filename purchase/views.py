from django.shortcuts import render, redirect
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import PurchaseSerializer
from .models import Purchase



class PurchaseViewSet(viewsets.ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    permission_class = [permissions.IsAuthenticated]