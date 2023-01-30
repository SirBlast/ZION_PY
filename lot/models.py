from django.db import models


#Lot Model
class Lot(models.Model):
    idLot=models.AutoField(primary_key=True,unique=True)
    del_date = models.DateField(auto_now=False, auto_now_add=True,null=True)
    
    def __str__(self):
        return str(self.idLot)
    