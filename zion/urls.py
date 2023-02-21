"""zion URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken import views

from category.views import Login,Logout
from product.views import Login,Logout
from subcategory.views import Login,Logout
from company.views import Login,Logout
from location.views import Login,Logout
from person.views import Login,Logout
from user.views import Login,Logout
from supplier.views import Login,Logout
from lot.views import Login,Logout
from purchase.views import login,Logout


router = routers.DefaultRouter()






urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(('category.urls','category'))),
    path('',include(('subcategory.urls','subcategory'))),
    path('',include(('company.urls','company'))),
    path('',include(('location.urls','location'))),
    path('',include(('product.urls','product'))),
    path('',include(('lot.urls','lot'))),
    path('',include(('person.urls','person'))),
    path('',include(('user.urls','user'))),
    path('',include(('supplier.urls','supplier'))),
    path('',include(('purchase.urls','purchase'))),
    
    path('api_generate_token/',views.obtain_auth_token),
    path('login/',Login.as_view(),name='login'),
    path('logout/',Logout.as_view(),name='logout'),
    path('',include('myapp.urls')),
    
   
    path('accounts/',include('django.contrib.auth.urls')),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
]
