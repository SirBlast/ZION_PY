from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Category


@login_required
def categories(request):
    categories_all = Category.objects.all()
    context={'categories_all':categories_all}
    return render(request,'categories.html',context)