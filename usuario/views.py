from django.shortcuts import render

# Create your views here.

def inicio(request):
    return render(request, 'usuario/inicio.html', {})

def lista(request):
    return render(request, 'usuario/lista.persona.html', {})

