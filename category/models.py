from django.db import models

# Create your models here.
#Category Model
class Category(models.Model):
    idCategory = models.AutoField(primary_key=True,unique=True)
    name = models.CharField(max_length=50)
    del_date = models.DateField(auto_now=False, auto_now_add=True,null=True)
    
    def __str__(self):
        return self.name