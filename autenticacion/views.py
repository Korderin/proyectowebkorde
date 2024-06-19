from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

# Create your views here.

class VRegistro(View):
    
    def get(self, request):
        form=UserCreationForm()
        return render(request, 'autenticacion/autenticacion.html',{'form':form})

    def post(self, request):
        form=UserCreationForm(request.POST)
        if form.is_valid():
            usuario=form.save()
            login(request, usuario)

            return redirect('Home')
        else:
            for msg in form.error_messages:
                messages.error(request,form.error_messages[msg])
                return render(request, 'autenticacion/autenticacion.html',{'form':form})


def cerrar_sesion(request):
    logout(request)

    return redirect('Home')

def logear(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nusuario = form.cleaned_data.get('username')
            passusuario = form.cleaned_data.get('password')
            usuario = authenticate(username=nusuario, password=passusuario)
            if usuario is not None:
                login(request, usuario)
                return redirect('Home')  
            else:
                messages.error(request, 'Usuario o contraseña no válidos')
        else:
            messages.error(request, 'Usuario o contraseña no válidos')
    else:
        form = AuthenticationForm()
    
    return render(request, 'login/login.html', {'form': form})