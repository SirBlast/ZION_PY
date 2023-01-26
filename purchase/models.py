from django.db import models
from user.models import User
from product.models import Product
from supplier.models import Supplier
from lot.models import Lot

#Purchase Model
class Purchase(models.Model):
    idPurchase = models.AutoField(primary_key=True,unique=True)
    idUser= models.ForeignKey(User, on_delete=models.CASCADE)
    idProduct = models.ForeignKey(Product, on_delete=models.CASCADE)
    idSupplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    idLot= models.ForeignKey(Lot, on_delete=models.CASCADE)
    amount = models.IntegerField()
    cost = models.FloatField()
    note = models.CharField(max_length=50)
    del_date = models.DateField(auto_now=False, auto_now_add=True,null=True)
    
    def __str__(self):
        return self.idPurchase