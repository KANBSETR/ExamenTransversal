const url_api = 'http://localhost:9098/api/'; // URL base de tu API
const lo_path = 'habitacion/';

function agregarHabitacion() {
    var data = {
        numeroHabitacion: document.getElementById('numeroHabitacion').value,
        cantDormitorios: document.getElementById('cantDormitorios').value,
        cantBanos: document.getElementById('numBanos').value,
        cantCamas: document.getElementById('numCamas').value,
        tamanoCamas: document.getElementById('cbTamano').value,
        cantPersonasDisp: document.getElementById('cantPersonasDisp').value,
        precio: document.getElementById('numPrecio').value,
        estadoHabitacion: document.getElementById('cbEstado').value,
        idServicioAdicional: document.getElementById('cbServicios').value,
        idTipoHabitacion: document.getElementById('cbTipoHab').value,
        idEmpleado: document.getElementById('cbEmpleado').value,
        idHotel: document.getElementById('cbHotel').value,
    };

    // Identificadores de campos a nombres personalizados
    var nombresCampos = {
        numeroHabitacion: "Número de habitación",
        cantDormitorios: "Cantidad de dormitorios",
        cantBanos: "Cantidad de baños",
        cantCamas: "Cantidad de camas",
        tamanoCamas: "Tamaño de camas",
        cantPersonasDisp: "Cantidad de personas disponibles",
        precio: "Precio",
        estadoHabitacion: "Estado de la habitación",
        idServicioAdicional: "Servicio adicional",
        idTipoHabitacion: "Tipo de habitación",
        idEmpleado: "Empleado a registrar la habitación",
        idHotel: "Hotel",
    };

    // Validación de datos y recopilación de campos vacíos
    let camposVacios = [];
    for (const [key, value] of Object.entries(data)) {
        if (value.trim() === '') {
            // Añade el nombre personalizado del campo a la lista de campos vacíos
            camposVacios.push(nombresCampos[key]);
        }
    }

    if (camposVacios.length > 0) {
        swal("Error", "Le faltan los siguientes campos por rellenar: " + camposVacios.join(', '), "error");
        return; // Detener la ejecución si hay campos vacíos
    }

    $.ajax({
        type: "POST",
        url: url_api + lo_path,
        data: JSON.stringify(data),
        contentType: "application/json",
        dataType: "json",
        success: function(response) {
            swal({
                title: "¡Éxito!",
                text: "Habitación agregada exitosamente!",
                icon: "success",
                button: "Aceptar",
            }).then((value) => {
                $('#modal-agregar-habitacion').modal('hide'); // Oculta el modal
                listarHabitaciones(); 
                limpiarFormulario(); 
            });
        },
        error: function(xhr, status, error) {
            swal("Error", "No se pudo agregar la habitación. Por favor, intenta de nuevo.", "error");
        }
    });
}



function limpiarFormulario() {
    document.getElementById('numeroHabitacion').value = '';
    document.getElementById('cantDormitorios').value = '';
    document.getElementById('numBanos').value = '';
    document.getElementById('numCamas').value = '';
    document.getElementById('cbTamano').value = document.getElementById('cbTamano').options[0].value;
    document.getElementById('cantPersonasDisp').value = '';
    document.getElementById('numPrecio').value = '';
    document.getElementById('cbEstado').value = document.getElementById('cbEstado').options[0].value;
    document.getElementById('cbServicios').value = document.getElementById('cbServicios').options[0].value;
    document.getElementById('cbTipoHab').value = document.getElementById('cbTipoHab').options[0].value;
    document.getElementById('cbEmpleado').value = document.getElementById('cbEmpleado').options[0].value;
    document.getElementById('cbHotel').value = document.getElementById('cbHotel').options[0].value;
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
