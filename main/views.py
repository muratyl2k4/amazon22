from django.shortcuts import render
from .muhasebe import mailparse
from .models import Data
def home(request):
    return render(request , 'index.html') 


def kargotakip(request):
    return render(request , 'kargotakip.html') 


def muhasebe(request):
    mailparse(user = request.user)
    d = Data.objects.filter(KULLANICI = request.user)
    data = {
        "info" : d
    }
    return render(request , 'muhasebe.html' , data) 


def pl(request):
    return render(request , 'pl.html') 