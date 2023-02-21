from django.db import models
from sale.models import Sale
from product.models import Product
from lot.models import Lot
#PurchaseSale Model
class PurchaseSale(models.Model):
    idPurchaseSale=models.AutoField(primary_key=True,unique=True)
    idSale=models.ForeignKey(Sale, on_delete=models.CASCADE)
    idProduct = models.ForeignKey(Product, on_delete=models.CASCADE)
    idLot = models.ForeignKey(Lot, on_delete=models.CASCADE)
    amount = models.IntegerField()
    value = models.FloatField()
    del_date = models.DateField(auto_now=True, auto_now_add=False,null=True)
    
    def __str__(self):
        return self.idPurchaseSale