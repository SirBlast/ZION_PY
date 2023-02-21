from django.urls import path
from .views import PurchaseList
urlpatterns =[    
    path('purchases/',PurchaseList.as_view(),name="purchase")
]