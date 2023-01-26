from django.db import models
from location.models import Location
#Person Model
class Person(models.Model):
    idPerson = models.AutoField(primary_key=True,unique=True)
    idLocation = models.ForeignKey(Location,on_delete=models.CASCADE)
    first_name= models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    idNumber = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    telephone = models.CharField(max_length=50)
    email_contact = models.EmailField(max_length=254)
    date_of_birth = models.DateField()
    del_date = models.DateField(auto_now=False, auto_now_add=True,null=True)
    date_create = models.DateField(auto_now=True, auto_now_add=False)
    date_update = models.DateField(auto_now=False, auto_now_add=True)
    user_create = models.CharField(max_length=50)
    user_update = models.CharField(max_length=50)
    
    def __str__(self):
        return self.idNumber   
