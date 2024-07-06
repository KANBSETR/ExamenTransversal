function validacionDatosAgregar(data, habitacionesExistentes) {
    // Validar que el número de habitación sea 100 o mayor y no mayor a 999
    if (data.numeroHabitacion < 100) {
        Swal.fire({
            title: 'Error',
            text: 'El número de habitación debe ser 100 o mayor.',
            icon: 'error',
            confirmButtonText: 'Aceptar'
        });
        return false;
    } else if (data.numeroHabitacion > 999) {
        Swal.fire({
            title: 'Error',
            text: 'El número de habitación no puede ser mayor a 999.',
            icon: 'error',
            confirmButtonText: 'Aceptar'
        });
        return false;
    }

    // Validar que el número de habitación no exista ya
    if (numeroHabitacionExiste(data.numeroHabitacion, habitacionesExistentes)) {
        Swal.fire({
            title: 'Error',
            text: 'Error, no puede asignar el mismo número a otra habitación existente.',
            icon: 'error',
            confirmButtonText: 'Aceptar'
        });
        return false;
    }

    return true;
}

function numeroHabitacionExiste(numeroHabitacion, habitacionesExistentes) {
    return habitacionesExistentes.includes(numeroHabitacion);
}

document.getElementById('numeroHabitacion').addEventListener('input', function() {
    if (parseInt(this.value, 10) < 100) {
      this.value = 100;
    }
  });