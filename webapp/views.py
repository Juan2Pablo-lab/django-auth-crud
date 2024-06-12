from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.

def bienvenido(request):
    return render(request, 'bienvenido.html')

def Registro(request):
    if request.method == 'POST':
        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(username=request.POST["username"], password=request.POST["password1"])
                user.save()
                login(request, user)
                return redirect('index')
            except IntegrityError:
                return render(request, 'registro.html', {'formUsuario': UserCreationForm, 'error': 'Error, el usuario ya existe.'})
        return render(request, 'registro.html', {'formUsuario': UserCreationForm, 'error': 'Error, las contraseñas no son iguales .'})
    return render(request, 'registro.html', {'formUsuario': UserCreationForm})

def iniciarSesion(request):
    if request.method == 'POST':
        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
        if user is None:
            return render(request, 'iniciar_sesion.html', {'formUsuario': AuthenticationForm, 'error': 'Error, el usuario o la contraseña no son validos.'})
        else:
            login(request, user)
            return redirect('index')
    return render(request, 'iniciar_sesion.html', {'formUsuario': AuthenticationForm})

def cerrarSesion(request):
    logout(request)
    return redirect('index')





