const url_api = 'http://localhost:9098/api/'; // URL base de tu API
const lo_path = 'reserva/';

function agregarReserva() {
    var data = {
        idHabitacion: document.getElementById('idHabitacion').value,
        fechaInicio: document.getElementById('startDate').value,
        fechaFin: document.getElementById('endDate').value,
        precioReserva: document.getElementById('numPrecio').value,
        estado: document.getElementById('cbEstado').value,
        idUsuario: document.getElementById('cbUsuario').value,
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
            alert('Reserva agregada correctamente');
        },
        error: function(xhr, status, error) {
            console.error('Error:', error);
            console.log('Detalles del error:', xhr.responseText);
            alert('Error al registrar la reserva. Por favor ingrese nuevamente: ');
        }
    });
}

function buscar() {
    var idReserva = document.getElementById('idReserva  ').value;
    $.ajax({
        type: "GET",
        url: url_api + lo_path + idReserva,
        dataType: "json",
        success: function(response) {
            if (!response.OK) {
                alert(response.msg);
                return;
            }
            document.getElementById('startDate').value = response.data.fechaInicio;
            document.getElementById('endDate').value = response.data.fechaFin;
            document.getElementById('numPrecio').value = response.data.precioReserva;
            document.getElementById('cbEstado').value = response.data.estado;
            document.getElementById('cbUsuario').value = response.data.idUsuario;
        },
        error: function(xhr, status, error) {
            console.error('Error:', error);
            console.log('Detalles del error:', xhr.responseText);
            alert('Error al buscar la habitación: ' + xhr.responseText);
        }
    });
}

function actualizar() {
    var idReserva = document.getElementById('idHabitacion').value;
    var data = {
        idHabitacion: document.getElementById('idHabitacion').value,
        fechaInicio: document.getElementById('startDate').value,
        fechaFin: document.getElementById('endDate').value,
        precioReserva: document.getElementById('numPrecio').value,
        estado: document.getElementById('cbEstado').value,
        idUsuario: document.getElementById('cbUsuario').value,
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

function leer() {
    var rut = document.getElementById('txRut').value;
    var pathUrl = url_api + lo_path + rut;

    $.ajax({
        type: "GET",
        async: false,
        url: pathUrl,
        cache: false,
        dataType: "json",
        beforeSend: function() {
            console.log('... cargando...');
        },
        error: function(data) {
            console.log('Tenemos problemas Houston ' + JSON.stringify(data));
            // Reset fields on error
            document.getElementById('txDv').value = "";
            document.getElementById('txNombre').value = "";
            document.getElementById('txPApellido').value = "";
            document.getElementById('txSApellido').value = "";
            document.getElementById('txEmail').value = "";
            document.getElementById('cbComuna').value = "";
            document.getElementById('cbGenero').value = "";
            document.getElementById('txFechaNacimiento').value = "";
            document.getElementById('cbPais').value = "";
            document.getElementById('txEstado').value = "";
            habilitaLeer();
        },
        success: function(data) {
            const json = data;
            if (!json) {
                console.log('No se recibió respuesta');
                return;
            }
        
            document.getElementById('txRut').value = json.rut;
            document.getElementById('txDv').value = json.dv;
            document.getElementById('txNombre').value = json.nombre;
            document.getElementById('txPApellido').value = json.papellido;
            document.getElementById('txSApellido').value = json.sapellido;
            document.getElementById('txEmail').value = json.email;
            document.getElementById('cbComuna').value = json.comuna;
            document.getElementById('cbGenero').value = json.genero;
            document.getElementById('txFechaNacimiento').value = json.fechaNacimiento;
            document.getElementById('cbPais').value = json.pais;
            // Asegúrate de manejar el valor null de fechaNacimiento si es necesario
            document.getElementById('txEstado').value = ""; // Ajusta según corresponda
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
    today.setHours(0, 0, 0, 0);
    if (startDate > today) {
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