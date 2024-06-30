from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, 'inicio.html')

def about(request):
    return render(request, 'about.html')

def inicioSesion(request):
    return render(request, 'login.html')

def registro(request):
    return render(request, 'registro.html')

def contraseñaOlvidada(request):
    return render(request, 'contraOlvidada.html')

def usuarios(request):
    return render(request, 'listadoUsuarios.html')

def modalActualizarUsuarios(request):
    return render(request, 'modalActualizarUsuarios.html')