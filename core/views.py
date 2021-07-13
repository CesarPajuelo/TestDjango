from django.shortcuts import render
from .models import Vehiculo

# Create your views here.


def main(request):
    Vehiculos = Vehiculo.objects.all()   
    context= {
        'listaVehiculos':Vehiculos

    } 
    return render(request, 'core/main.html', context)


def mecanicos(request):
    context= {} 
    return render(request, 'core/mecanicos.html', context)

def trabajos(request):
    context= {} 
    return render(request, 'core/trabajos.html', context)

def quienessomos(request):
    context= {} 
    return render(request, 'core/quienessomos.html', context)











