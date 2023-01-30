from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Purchase
from myapp.forms import PurchaseForm

@login_required
def purchases(request):
    purchases_all = Purchase.objects.all()
    context={'purchases_all':purchases_all}
    return render(request,'purchases.html',context)

def addPurchase(request):
    if request.method=="POST":
        form = PurchaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/purchases')
        
    else:
        form = PurchaseForm()
    context ={'form':form}
    return render(request, 'addPurchase.html',context)    