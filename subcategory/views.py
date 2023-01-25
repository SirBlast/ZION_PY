from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import SubCategory


@login_required
def subcategories(request):
    subcategories_all = SubCategory.objects.all()
    context={'subcategories_all':subcategories_all}
    return render(request,'subcategories.html',context)