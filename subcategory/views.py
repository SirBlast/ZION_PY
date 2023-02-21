from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import SubCategory
from myapp.forms import SubCategoryForm


@login_required
def subcategories(request):
    subcategories_all = SubCategory.objects.all()
    context={'subcategories_all':subcategories_all}
    return render(request,'subcategories.html',context)

def addSubCategory(request):
    if request.method == "POST":
        form = SubCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/subcategories')
    else:
        form = SubCategoryForm()
    context ={'form':form}
    return render(request, 'addSubCategory.html',context)

def deleteSubCategory(request,idSubCategory):
    subcategory = SubCategory.objects.get(idSubCategory = int(idSubCategory))
    subcategory.delete()
    return redirect ('/subcategories')

def editSubCategory(request,idSubCategory):
    subcategory = SubCategory.objects.get(idSubCategory = int(idSubCategory))
    if request.method == "POST":
        form = SubCategoryForm(request.POST, instance=subcategory)
        if form.is_valid():
            form.save()
            return redirect("/subcategories")
    else:
        form = SubCategoryForm(instance=subcategory)
    context = {"form":form}
    return render(request,"editSubCategory.html",context)