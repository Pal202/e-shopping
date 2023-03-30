from django.shortcuts import render
from .models import *
# Create your views here.
def store(request):
    products = Product.objects.all()
    content={'products':products}
    return render(request,'store.html',content)

def cart(request):
    content={}
    return render(request,'cart.html',content)

def checkout(request):
    content={}
    return render(request,'checkout.html',content)
    