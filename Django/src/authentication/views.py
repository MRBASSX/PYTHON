from django.http import HttpResponse
from django.shortcuts import render

from .models import product


# Create your views here.

def Home(request):
    Data = product.objects.all()
    return render(request, 'authentication/index.html', {"key": Data})
# return HttpResponse("Hi am your new page")
