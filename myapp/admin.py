from django.contrib import admin
from .models import Company
from .models import Location
from .models import Person
from .models import Product
from .models import Purchase
from .models import PurchaseSale
from .models import Sale
from .models import User

from .models import SubCategory
from .models import Lot
from .models import Supplier


admin.site.register(Company)
admin.site.register(Location)
admin.site.register(Person)
admin.site.register(Product)
admin.site.register(Purchase)
admin.site.register(PurchaseSale)
admin.site.register(Sale)
admin.site.register(User)


admin.site.register(Lot)
admin.site.register(Supplier)


# Register your models here.
