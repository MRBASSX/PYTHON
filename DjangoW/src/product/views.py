from django.http import HttpResponse
from .models import Product
from django.shortcuts import render


# Create your views here.

def Home(request):
    ourproducts = Product.objects.all()

    return HttpResponse(ourproducts)


def About(request):
    ourproducts = Product.objects.all()
    return render(request, 'product/index.html', {"key": ourproducts})
