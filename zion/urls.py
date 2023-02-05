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
from product.views import ProductViewSet
from subcategory.views import SubCategoryViewSet
from company.views import CompanyViewSet
from location.views import LocationViewSet
from person.views import PersonViewSet
from user.views import UserViewSet
from supplier.views import SupplierViewSet
from lot.views import LotViewSet
from purchase.views import PurchaseViewSet


router = routers.DefaultRouter()

router.register(r'subcategories', SubCategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'companies', CompanyViewSet)
router.register(r'locations', LocationViewSet)
router.register(r'persons', PersonViewSet)
router.register(r'users', UserViewSet)
router.register(r'suppliers', SupplierViewSet)
router.register(r'lots', LotViewSet)
router.register(r'purchases', PurchaseViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(('category.urls','category'))),
    path('api_generate_token/',views.obtain_auth_token),
    path('login/',Login.as_view(),name='login'),
    path('logout/',Logout.as_view(),name='logout'),
    path('',include('myapp.urls')),
    path('',include('category.urls')),
    path('',include('subcategory.urls')),
    path('',include('purchase.urls')),
    path('',include('lot.urls')),
    path('accounts/',include('django.contrib.auth.urls')),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
]
