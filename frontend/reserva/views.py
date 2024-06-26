from django.shortcuts import render

# Create your views here.
def reserva(request):
    return render(request, 'reserva.html')

def completar_reserva(request):
    return render(request, 'completarReserva.html')

def pago(request):
    return render(request, 'pagoCompletado.html')