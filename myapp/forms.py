from django.forms import ModelForm
from category.models import Category
from subcategory.models import SubCategory
from product.models import Product

class ProductForm(ModelForm):
    class Meta:
       model= Product
       fields =['product_name','price_unit_cop','idCategory','idSubCategory','description','placement']
     
class CategoryForm(ModelForm):
    class Meta:
        model= Category 
        fields =['name']
        
class SubCategoryForm(ModelForm):
    class Meta:
        model= SubCategory 
        fields =['name','idCategory']                
        