from django.shortcuts import render

# Create your views here.

def index(request):
    context= {} 
    return render(request, 'core/index.html', context)

def main(request):
    context= {} 
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







