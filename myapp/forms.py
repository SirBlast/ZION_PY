from django.forms import ModelForm
from category.models import Category
from subcategory.models import SubCategory
from product.models import Product
from purchase.models import Purchase
from lot.models import Lot

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
        fields =['name','Category']                
        
class PurchaseForm(ModelForm):
    class Meta:
        model= Purchase
        fields =['idUser','idProduct','idSupplier','idLot','amount','cost','note'] 
        
class LotForm(ModelForm):
    class Meta:
        model= Lot
        fields =[]                
        