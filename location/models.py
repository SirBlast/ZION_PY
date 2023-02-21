from django.db import models
from company.models import Company
#Location Model
class Location (models.Model):
    idLocation = models.AutoField(primary_key=True,unique=True)
    idCompany = models.ForeignKey(Company, on_delete=models.CASCADE)
    name_contact = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    settings_admin = models.TextField()
    settings_user = models.TextField()
    phone_contact = models.CharField(max_length=50)
    cell_phone = models.CharField(max_length=50)
    email_contact = models.EmailField(max_length=254)
    del_date = models.DateField(auto_now=True, auto_now_add=False,null=True)
    date_create = models.DateTimeField(auto_now=False, auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True, auto_now_add=False)
    user_create = models.CharField(max_length=50)
    user_update = models.CharField(max_length=50)

    def __str__(self):
        return self.name_contact