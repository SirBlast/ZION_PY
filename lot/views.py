from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Lot
from myapp.forms import LotForm

@login_required
def lots(request):
    lots_all = Lot.objects.all()
    context={'lots_all':lots_all}
    return render(request,'lots.html',context)

def addLot(request):
    if request.method=="POST":
        form = LotForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/lots')
        
    else:
        form = LotForm()
    context ={'form':form}
    return render(request, 'addLot.html',context)

def deleteLot(request,idLot):
    lot = Lot.objects.get(idLot = int(idLot))
    lot.delete()
    return redirect ('/lots')    