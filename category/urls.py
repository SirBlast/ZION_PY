from django.urls import path
from . import views
urlpatterns =[    
    path('categories/',views.categories),
    path('addCategory/',views.addCategory),
    path('deleteCategory/<int:idCategory>/',views.deleteCategory, name='deletecategory'),
    path('editCategory/<int:idCategory>/',views.editCategory, name='editcategory'),
]