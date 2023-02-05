from django.urls import path
from .views import LotList
urlpatterns =[ 
        path('lots/',LotList.as_view(),name="lot")           
]