from django.urls import path
from .views import SubCategoryList

urlpatterns =[  
    path ('subcategories/',SubCategoryList.as_view(), name ='subcategory_list'),   
]