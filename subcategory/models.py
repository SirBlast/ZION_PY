from django.db import models
from category.models import Category


#SubCategory Model
class SubCategory(models.Model):
    idSubCategory = models.AutoField(primary_key=True,unique=True)
    idCategory = models.ForeignKey(Category, on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    del_date= models.DateField(auto_now=False, auto_now_add=True,null=True)
    
    def __str__(self):
        return self.name


