from django.shortcuts import render

# Create your views here.
def servicios(request):
    return render(request, 'servicioad.html')


def modificar_servicio(request):
    return render(request, 'modificarServicio.html')