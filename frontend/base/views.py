from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, 'inicio.html')

def inicioSesion(request):
    return render(request, 'core/login.html')

def registro(request):
    return render(request, 'core/registro.html')

def contraseñaOlvidada(request):
    return render(request, 'core/contraOlvidada.html')

def about(request):
    return render(request, 'about.html')
