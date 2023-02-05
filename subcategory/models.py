from django.db import models
from category.models import Category


#SubCategory Model
class SubCategory(models.Model):
    idSubCategory = models.AutoField(primary_key=True,unique=True)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    del_date = models.DateField(auto_now=True, auto_now_add=False,null=True)
    
    def __str__(self):
        return self.name


