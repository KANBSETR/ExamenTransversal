from django.shortcuts import render

# Create your views here.
def habitacion(request):
    return render(request, 'habitacion.html')
