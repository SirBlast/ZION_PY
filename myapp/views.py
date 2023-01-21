from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Product,Category
from .forms import ProductForm,CategoryForm
# Create your views here.
def hello(request):
    return HttpResponse("Hello world")

def about(request):
    return HttpResponse("About")

def home(request):
    return render(request,'home.html')
@login_required
def products(request):
    products_all = Product.objects.all()
    context={'products_all':products_all}
    return render(request,'products.html',context)

@login_required
def categories(request):
    categories_all = Category.objects.all()
    context={'categories_all':categories_all}
    return render(request,'categories.html',context)

def addProduct(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/products')
    else:
        form = ProductForm()
    context ={'form':form}
    return render(request, 'addProduct.html',context)

def deleteProduct(request,idProduct):
    product = Product.objects.get(idProduct = int(idProduct))
    product.delete()
    return redirect ('/products')

def editProduct(request,idProduct):
    product = Product.objects.get(idProduct = int(idProduct))
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect("/products")
    else:
        form = ProductForm(instance=product)
    context = {"form":form}
    return render(request,"editProduct.html",context)
    
def addCategory(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/categories')
    else:
        form = CategoryForm()
    context ={'form':form}
    return render(request, 'addCategory.html',context)
    

def exit(request):
    logout(request)
    return redirect('/')