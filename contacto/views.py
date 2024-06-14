from django.shortcuts import render, redirect
from .forms import FormularioContacto
from django.http import HttpResponseRedirect
from django.core.mail import send_mail, EmailMessage

# Create your views here.

#forma 1 de mandar mail
"""""
def contacto(request):
    formulario=FormularioContacto()
    if request.method=="POST":
        formulario=FormularioContacto(data=request.POST)
        if formulario.is_valid():
           # nombre=request.POST.get('nombre')
            #email=request.POST.get('email')
            #contenido=request.POST.get('contenido')
            infForm=formulario.cleaned_data
            send_mail(infForm['nombre'],infForm['contenido'],
                      infForm.get('email',''),["felipeaguilarc.93@gmail.com"],)
            return redirect('/contacto/?valido')
    return render(request,"contacto/contacto.html",{'miFormulario':formulario})"""

#forma 2 de mandar mail
def contacto(request):
    formulario=FormularioContacto()
    if request.method=="POST":
        formulario=FormularioContacto(data=request.POST)
        if formulario.is_valid():
            nombre=request.POST.get('nombre')
            email=request.POST.get('email')
            contenido=request.POST.get('contenido')
            correo=EmailMessage("Mensaje desde app Django","La persona {}, con correo {}, ha enviado esto {}".format(nombre,email,contenido),"",["felipeaguilarc.93@gmail.com"])
            try:
                correo.send()
                return redirect('/contacto/?valido')
            except:
                return redirect('/contacto/?novalido')
    return render(request,"contacto/contacto.html",{'miFormulario':formulario})

