from django.db import models

#Company Model
class Company(models.Model):
    idCompany= models.AutoField(primary_key=True,unique=True)
    name_contact = models.CharField(max_length=50)
    nit = models.CharField(max_length=50)
    description = models.CharField(max_length=50,null=True)
    settings_admin=models.TextField()
    settings_user=models.TextField()
    phone_contact=models.CharField(max_length=50)
    cell_phone_contact=models.CharField(max_length=50)
    email_contact=models.EmailField(max_length=254)
    del_date = models.DateField(auto_now=True, auto_now_add=False,null=True)
    date_create = models.DateTimeField(auto_now=False, auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True, auto_now_add=False)
    user_create = models.CharField(max_length=50)
    user_update = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name_contact