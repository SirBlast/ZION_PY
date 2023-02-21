from django.db import models
from category.models import Category
from subcategory.models import SubCategory
       
#Product Model
class Product(models.Model):
    idProduct= models.AutoField(primary_key=True, unique=True)
    idCategory = models.ForeignKey(Category, on_delete=models.CASCADE)
    idSubCategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    product_name= models.CharField(max_length=50)
    price_unit_cop = models.FloatField()
    placement = models.CharField(max_length=50)
    del_date = models.DateField(auto_now=False, auto_now_add=True,null=True)
    
    def __str__(self):
        return self.product_name