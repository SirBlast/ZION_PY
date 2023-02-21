from django.db import models
from purchase.models import Purchase
from user.models import User

#Sale Model
class Sale(models.Model):
    idSale= models.AutoField(primary_key=True,unique=True)
    idPurchase = models.ForeignKey(Purchase, on_delete=models.CASCADE)
    idUser = models.ForeignKey(User, on_delete=models.CASCADE)
   # idPurchaseSale = models.ForeignKey(PurchaseSale, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True, auto_now_add=False)
    payment_method= models.CharField(max_length=50)
    note= models.CharField(max_length=50)
    total = models.FloatField()
    del_date = models.DateField(auto_now=True, auto_now_add=False,null=True)
    
    def __str__(self):
        return self.idSale
