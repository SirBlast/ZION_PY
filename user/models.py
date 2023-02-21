from django.db import models
from person.models import Person
     
#User Model
class User(models.Model):
    idUser = models.AutoField(primary_key=True,unique=True)
    idPerson = models.ForeignKey(Person,on_delete=models.CASCADE)
    user_name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    date_last_log = models.DateField()
    role = models.CharField(max_length=50)
    del_date = models.DateField(auto_now=True, auto_now_add=False,null=True)
    
    def __str__(self):
        return self.user_name
