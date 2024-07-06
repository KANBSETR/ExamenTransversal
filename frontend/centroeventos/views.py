from django.shortcuts import render

# Create your views here.
def eventos(request):
    return render(request, 'evento.html')

def evento_modificar(request):
    return render(request, 'modificarEvento.html')