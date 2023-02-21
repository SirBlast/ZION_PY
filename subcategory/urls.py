from django.urls import path
from . import views
urlpatterns =[    
    path('subcategories/',views.subcategories),
    path('addSubCategory/',views.addSubCategory),
    path('deleteSubCategory/<int:idSubCategory>/',views.deleteSubCategory, name='deletesubcategory'),
    path('editSubCategory/<int:idSubCategory>/',views.editSubCategory, name='editsubcategory'),
]