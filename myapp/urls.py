from django.urls import path
from category.views import categories
from . import views
urlpatterns =[
    path('', views.home),
    path('products/',views.products),
    path('addProduct/',views.addProduct),
    path('deleteProduct/<int:idProduct>/',views.deleteProduct, name='delete'),
    path('editProduct/<int:idProduct>/',views.editProduct, name='edit'), 
    path('exit/',views.exit)
]