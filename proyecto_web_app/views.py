from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.

def bienvenida(request):

    return render(request,"proyecto_web_app/bienvenida.html")

def bienvenida2(request):

    return render(request,"proyecto_web_app/bienvenida2.html")

def home(request):

    return render(request,"proyecto_web_app/home.html")


