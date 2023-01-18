from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
# Create your views here.
def hello(request):
    return HttpResponse("Hello world")

def about(request):
    return HttpResponse("About")

def home(request):
    return render(request,'home.html')
@login_required
def products(request):
    return render(request,'products.html')

def exit(request):
    logout(request)
    return redirect('/')