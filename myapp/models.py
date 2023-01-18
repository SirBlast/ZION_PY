from django.db import models
#Company Model
class Company(models.Model):
    idCompany= models.AutoField(primary_key=True)
    name_contact = models.CharField(max_length=50)
    nit = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    settings_admin=models.TextField()
    settings_user=models.TextField()
    phone_contact=models.CharField(max_length=50)
    cell_phone_contact=models.CharField(max_length=50)
    email_contact=models.EmailField(max_length=254)
    del_date = models.DateField(auto_now=False, auto_now_add=False)
    date_create = models.DateField(auto_now=True, auto_now_add=False)
    date_update = models.DateField(auto_now=False, auto_now_add=True)
    user_create = models.CharField(max_length=50)
    user_update = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name_contact
#Location Model
class Location (models.Model):
    idLocation = models.AutoField(primary_key=True)
    idCompany = models.ForeignKey(Company, on_delete=models.CASCADE)
    name_contact = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    settings_admin = models.TextField()
    settings_user = models.TextField()
    phone_contact = models.CharField(max_length=50)
    cell_phone = models.CharField(max_length=50)
    email_contact = models.EmailField(max_length=254)
    del_date = models.DateField(auto_now=False, auto_now_add=False)
    date_create = models.DateField(auto_now=True, auto_now_add=False)
    date_update = models.DateField(auto_now=False, auto_now_add=True)
    user_create = models.CharField(max_length=50)
    user_update = models.CharField(max_length=50)

    def __str__(self):
        return self.name_contact
#Person Model
class Person(models.Model):
    idPerson = models.AutoField(primary_key=True)
    idLocation = models.ForeignKey(Location,on_delete=models.CASCADE)
    first_name= models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    idNumber = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    telephone = models.CharField(max_length=50)
    email_contact = models.EmailField(max_length=254)
    date_of_birth = models.DateField()
    del_date = models.DateField(auto_now=False, auto_now_add=False)
    date_create = models.DateField(auto_now=True, auto_now_add=False)
    date_update = models.DateField(auto_now=False, auto_now_add=True)
    user_create = models.CharField(max_length=50)
    user_update = models.CharField(max_length=50)
        
#User Model
class User(models.Model):
    idUser = models.AutoField(primary_key=True)
    idPerson = models.ForeignKey(Person,on_delete=models.CASCADE)
    user_name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    date_last_log = models.DateField()
    role = models.CharField(max_length=50)
    del_date = models.DateField(auto_now=False, auto_now_add=False)

#Supplier Model
class Supplier(models.Model):
    idSupplier= models.AutoField(primary_key=True)
    name_company=models.CharField(max_length=50)
    name_contact= models.CharField(max_length=50)
    phone_contact=models.CharField(max_length=50)
    whatsapp_contact= models.CharField(max_length=50)
    address= models.CharField(max_length=50)
    del_date =models.DateField(auto_now=False, auto_now_add=False)


#Lot Model
class Lot(models.Model):
    idLot=models.AutoField(primary_key=True)
    del_date = models.DateField(auto_now=False, auto_now_add=False)
#Category Model
class Category(models.Model):
    idCategory=models.AutoField(primary_key=True)
    name =models.CharField(max_length=50)
    del_date= models.DateField(auto_now=False, auto_now_add=False)
#SubCategory Model
class SubCategory(models.Model):
    idSubCategory = models.AutoField(primary_key=True)
    idCategory = models.ForeignKey(Category, on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    del_date= models.DateField(auto_now=False, auto_now_add=False)    
#Product Model
class Product(models.Model):
    idProduct= models.AutoField(primary_key=True)
    idCategory = models.ForeignKey(Category, on_delete=models.CASCADE)
    idSubCategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)

#Purchase Model
class Purchase(models.Model):
    idPurchase = models.AutoField(primary_key=True)
    idUser= models.ForeignKey(User, on_delete=models.CASCADE)
    idProduct = models.ForeignKey(Product, on_delete=models.CASCADE)
    idSupplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    idLot= models.ForeignKey(Lot, on_delete=models.CASCADE)
    amount = models.IntegerField()
    cost = models.FloatField()
    note = models.CharField(max_length=50)
    del_date = models.DateField(auto_now=False, auto_now_add=False)
#Sale Model
class Sale(models.Model):
    idSale= models.AutoField(primary_key=True)
    idPurchase = models.ForeignKey(Purchase, on_delete=models.CASCADE)
    idUser = models.ForeignKey(User, on_delete=models.CASCADE)
    idPurchaseSale = models.ForeignKey(PurchaseSale, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True, auto_now_add=False)
    payment_method= models.CharField(max_length=50)
    note= models.CharField(max_length=50)
    total = models.FloatField()
    del_date=models.DateField(auto_now=False, auto_now_add=False)    
#PurchaseSale Model
class PurchaseSale(models.Model):
    idPurchaseSale=models.AutoField(primary_key=True)
    idSale=models.ForeignKey(Sale, on_delete=models.CASCADE)
    idProduct = models.ForeignKey(Product, on_delete=models.CASCADE)
    idLot = models.ForeignKey(Lot, on_delete=models.CASCADE)
    amount = models.IntegerField()
    value = models.FloatField()
    del_date= models.DateField(auto_now=False, auto_now_add=False)