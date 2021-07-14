from django.shortcuts import render
from .models import Trabajo


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









