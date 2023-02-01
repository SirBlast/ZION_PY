from django.shortcuts import render
from .models import Supplier
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import SupplierSerializer



class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_class = [permissions.IsAuthenticated]
