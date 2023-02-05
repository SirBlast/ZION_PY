from django.urls import path
from .views import CompanyList
urlpatterns =[  
        path ('companies/',CompanyList.as_view(), name ='company_list'),          
]