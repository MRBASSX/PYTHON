from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.


def Home(request):
    return render(request, 'authentication/index.html', {"key": "Mr Boss"})
# return HttpResponse("Hi am your new page")
