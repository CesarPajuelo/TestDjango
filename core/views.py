from django.shortcuts import redirect, render
from .models import Trabajo
from .forms import TrabajoForm, CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages


# Create your views here.


def main(request):
    return render(request, 'core/main.html')

def mecanicos(request):
    return render(request, 'core/mecanicos.html')

def trabajos(request):
    trabajos = Trabajo.objects.all()
    context = {
        'trabajos' : trabajos
    }
    return render(request, 'core/trabajos.html',context)

def quienessomos(request):
    return render(request, 'core/quienessomos.html')


def agregar_servicio(request):

    data = {
        'form' : TrabajoForm()
    }

    if request.method == 'POST':
        formulario = TrabajoForm(data=request.POST, files= request.FILES)
        if formulario.is_valid():
           formulario.save()
           data["mensaje"] = "Enviado Correctamente"
        else:
            data["form"] = formulario
        

    return render(request, 'core/agregar.html',data)


def registro(request):

    data = {


        'form':  CustomUserCreationForm()
       
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te has registrado Correctamente")

            return redirect(to="main")
        data["form"] = formulario


    return render(request, 'registration/registro.html',data)






