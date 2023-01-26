from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Purchase
@login_required
def purchases(request):
    purchases_all = Purchase.objects.all()
    context={'purchases_all':purchases_all}
    return render(request,'purchases.html',context)