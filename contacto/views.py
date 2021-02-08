from django.shortcuts import render, redirect
from .forms import FormularioContacto
from django.core.mail import EmailMessage
from django.core.mail import send_mail
# Create your views here.

def contacto(request):
    formulario_contacto=FormularioContacto()

    if request.method=="POST":
        formulario_contacto=FormularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            contenido=request.POST.get("contenido")

            email=EmailMessage("Mensaje desde CRO","Nombre: {} \n\n Email: {} \n\n {}".format(nombre,email,contenido),"",["naxitho100@gmail.com"],reply_to=[email])

            try:
                email.send()
                return redirect("/contacto/?valido")
            except:

                return redirect("/contacto/?no_valido")

    return render(request,"contacto/contacto.html", {"formulario":formulario_contacto})