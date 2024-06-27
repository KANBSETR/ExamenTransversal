const url_api = 'http://localhost:9098/api/'; // URL base de tu API
const lo_path = 'habitacion/';

function agregarHabitacion() {
    var data = {
        numeroHabitacion: document.getElementById('numHabitacion').value,
        cantDormitorios: document.getElementById('cantDormitorio').value,
        cantBanos: document.getElementById('numBanos').value,
        cantCamas: document.getElementById('numCamas').value,
        tamanoCamas: document.getElementById('numTamano').value,
        cantPersonasDisp: document.getElementById('numCapacidad').value,
        precio: document.getElementById('numPrecio').value,
        estadoHabitacion: document.getElementById('txEstado').value,
        idServicioAdicional: document.getElementById('txServicio').value,
        descripcion: document.getElementById('taAdicional').value,
        idTipoHabitacion: document.getElementById('numTipo').value,
        idEmpleado: document.getElementById('numEmpleado').value,
        idHotel: document.getElementById('numHotel').value,
    };

    $.ajax({
        type: "POST",
        url: url_api + lo_path,
        data: JSON.stringify(data),
        contentType: "application/json",
        dataType: "json",
        success: function(response) {
            if (!response.OK) {
                alert('Habitación agregada correctamente');
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
