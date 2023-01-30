from django.urls import path
from . import views
urlpatterns =[    
    path('lots/',views.lots),
    path('addLot/',views.addLot),
    path('deleteLot/<int:idLot>/',views.deleteLot, name='deleteLot'),
    
]