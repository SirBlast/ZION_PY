from django.urls import path
from .views import SupplierList
urlpatterns =[ 
        path('suppliers/',SupplierList.as_view(),name="supplier")           
]