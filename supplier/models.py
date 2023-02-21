from django.db import models

#Supplier Model
class Supplier(models.Model):
    idSupplier= models.AutoField(primary_key=True,unique=True)
    name_company=models.CharField(max_length=50)
    name_contact= models.CharField(max_length=50)
    phone_contact=models.CharField(max_length=50)
    whatsapp_contact= models.CharField(max_length=50)
    address= models.CharField(max_length=50)
    del_date =models.DateField(auto_now=False, auto_now_add=True,null=True)
    
    def __str__(self):
        return self.name_company
