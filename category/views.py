from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Category
from myapp.forms import CategoryForm


@login_required
def categories(request):
    categories_all = Category.objects.all()
    context={'categories_all':categories_all}
    return render(request,'categories.html',context)

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

def deleteCategory(request,idCategory):
    category = Category.objects.get(idCategory = int(idCategory))
    category.delete()
    return redirect ('/categories')

def editCategory(request,idCategory):
    category = Category.objects.get(idCategory = int(idCategory))
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect("/categories")
    else:
        form = CategoryForm(instance=category)
    context = {"form":form}
    return render(request,"editCategory.html",context)