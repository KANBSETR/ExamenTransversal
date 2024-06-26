const url_api = 'http://localhost:9098/api/'; // URL base de tu API
const lo_path = 'habitacion/';

function agregarHabitacion() {
    var data = {
        idHabitacion: document.getElementById('idHabitacion').value,
        numHabitacion: document.getElementById('numHabitacion').value,
        cantBanos: document.getElementById('numBanos').value,
        cantCamas: document.getElementById('numCamas').value,
        tamanoCamas: document.getElementById('cbTamano').value,
        capaMax: document.getElementById('numCapacidad').value,
        precio: document.getElementById('numPrecio').value,
        estado: document.getElementById('cbEstado').value,
        servicios: document.getElementById('cbServicios').value,
        tipoHabitacion: document.getElementById('cbTipoHab').value,
        empleado: document.getElementById('cbEmpleado').value,
        hotel: document.getElementById('cbHotel').value,
    };

    $.ajax({
        type: "POST",
        url: url_api + lo_path,
        data: JSON.stringify(data),
        contentType: "application/json",
        dataType: "json",
        success: function(response) {
            if (!response.OK) {
                alert(response.msg);
                return;
            }
            alert('Habitación agregada correctamente');
        },
        error: function(xhr, status, error) {
            console.error('Error:', error);
            console.log('Detalles del error:', xhr.responseText);
            alert('Error al agregar la habitación: ' + xhr.responseText);
        }
    });
}


function actualizar() {
    var idHabitacion = document.getElementById('idHabitacion').value;
    var data = {
        idHabitacion: document.getElementById('idHabitacion').value,
        numHabitacion: document.getElementById('numHabitacion').value,
        cantBanos: document.getElementById('numBanos').value,
        cantCamas: document.getElementById('numCamas').value,
        tamanoCamas: document.getElementById('cbTamano').value,
        capaMax: document.getElementById('numCapacidad').value,
        precio: document.getElementById('numPrecio').value,
        estado: document.getElementById('cbEstado').value,
        servicios: document.getElementById('cbServicios').value,
        tipoHabitacion: document.getElementById('cbTipoHab').value,
        empleado: document.getElementById('cbEmpleado').value,
        hotel: document.getElementById('cdHotel').value,
    };

    $.ajax({
        type: "PUT",
        url: url_api + lo_path + idHabitacion,
        data: JSON.stringify(data),
        contentType: "application/json",
        dataType: "json",
        success: function(response) {
            if (!response.OK) {
                alert(response.msg);
                return;
            }
            alert('Habitacion actualizada correctamente');
        },
        error: function(xhr, status, error) {
            console.error('Error:', error);
            console.log('Detalles del error:', xhr.responseText);
            alert('Error al actualizar la habitación: ' + xhr.responseText);
        }
    });
}

function eliminar() {
    var idHabitacion = document.getElementById('idHabitacion').value;
    $.ajax({
        type: "DELETE",
        url: url_api + lo_path + id_habitacion,
        dataType: "json",
        success: function(response) {
            if (!response.OK) {
                alert(response.msg);
                return;
            }
            alert('Habitacion eliminada correctamente');
        },
        error: function(xhr, status, error) {
            console.error('Error:', error);
            console.log('Detalles del error:', xhr.responseText);
            alert('Error al eliminar la habitacion: ' + xhr.responseText);
        }
    });
}














































document.addEventListener('DOMContentLoaded', function () {
    // Establecer la fecha mínima de inicio como la fecha actual
    var today = new Date().toISOString().split('T')[0];
    document.getElementById('startDate').setAttribute('min', today);
    document.getElementById('endDate').setAttribute('min', today);
});

document.getElementById('startDate').addEventListener('change', function () {
    const startDate = new Date(this.value);
    startDate.setDate(startDate.getDate() + 1);
    const minEndDate = startDate.toISOString().split('T')[0];
    document.getElementById('endDate').setAttribute('min', minEndDate);
});

function calculateTotal() {
    // Obtener los valores de las fechas y el precio por día
    const startDate = new Date(document.getElementById('startDate').value);
    const endDate = new Date(document.getElementById('endDate').value);
    const pricePerDay = 70000;

    // Validar que las fechas sean válidas
    if (isNaN(startDate) || isNaN(endDate)) {
        document.getElementById('mensaje').innerText = 'Por favor, ingrese fechas válidas.';
        document.getElementById('result').innerText = '';
        return;
    }

    // Validar que la fecha de inicio no sea anterior a la fecha actual
    const today = new Date();
    today.setHours(0, 0, 0, 0);  // Asegurarse de que no haya diferencias por la hora del día
    if (startDate < today) {
        document.getElementById('mensaje').innerText = 'La fecha de inicio no puede ser anterior a la fecha actual.';
        document.getElementById('result').innerText = '';
        return;
    }

    // Validar que la fecha de término no sea anterior a la fecha de inicio
    if (endDate <= startDate) {
        document.getElementById('mensaje').innerText = 'La fecha de término debe ser posterior a la fecha de inicio.';
        document.getElementById('result').innerText = '';
        return;
    }

    // Validar que el precio por día sea válido
    if (isNaN(pricePerDay) || pricePerDay <= 0) {
        document.getElementById('mensaje').innerText = 'Por favor, ingrese un precio por día válido.';
        document.getElementById('result').innerText = '';
        return;
    }

    const tiempo = endDate - startDate;

    // Calcular la diferencia en días
    const dias = tiempo / (1000 * 3600 * 24);

    // Calcular el total
    const totalPrecio = dias * pricePerDay;

    // Mostrar el resultado
    document.getElementById('result').innerText = `El costo total de la reserva es: $${totalPrecio.toFixed(2)}`;
    document.getElementById('mensaje').innerText = '';

    calculateTotal();
}