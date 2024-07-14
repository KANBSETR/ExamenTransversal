const url_api = 'http://localhost:9098/api/'; // URL base de tu API
const lo_path = 'evento/';

function agregarEvento() {
    var estadoString = document.getElementById('cbEstadoEvento').value; // Obtener el valor del select como string
    var estadoBooleano; // Variable para almacenar el valor booleano

    // Convertir el valor string a booleano
    if (estadoString === "Disponible") {
        estadoBooleano = true;
    } else if (estadoString === "No disponible/En mantenimiento") {
        estadoBooleano = false;
    }

    // Asegúrate de obtener los valores de fechaInicioEvento y fechaFinEvento correctamente
    var fechaInicioEvento = document.getElementById('fechaInicioEvento').value;
    var fechaFinEvento = document.getElementById('fechaFinEvento').value;
    var precioEvento = document.getElementById('precioEvento').value; // Asegúrate de que esta línea exista para definir precioEvento

    var data = {
        nombre: document.getElementById('nombreEvento').value,
        fechaInicio: fechaInicioEvento ? (new Date(fechaInicioEvento).toISOString() || '') : '',
        fechaTermino: fechaFinEvento ? (new Date(fechaFinEvento).toISOString() || '') : '',
        descripcion: document.getElementById('descripcionEvento').value,
        precio: precioEvento ? parseInt(precioEvento, 10) : NaN, // Convertir a número solo si no está vacío
        estado: estadoBooleano,
        idEmpleado: document.getElementById('cbEmpleado').value,
        idFPago: document.getElementById('cbFormaPago').value,
        idHotel: document.getElementById('cbHotel').value,
        idUsuario: document.getElementById('cbUsuario').value,
    };


    // Identificadores de campos a nombres personalizados
    var nombresCampos = {
        nombre: "Nombre de evento",
        fechaInicio: "Fecha de inicio",
        fechaTermino: "Fecha de término",
        descripcion: "Descripción",
        precio: "Precio",
        estado: "Estado",
        idEmpleado: "Empleado",
        idFPago: "Forma de pago",
        idHotel: "Hotel",
        idUsuario: "Usuario",
    };

    data.fechaInicio = isValidDate(fechaInicioEvento) ? new Date(fechaInicioEvento).toISOString() : '';
    data.fechaTermino = isValidDate(fechaFinEvento) ? new Date(fechaFinEvento).toISOString() : '';

    // Función para validar fechas
    function isValidDate(dateString) {
        var date = new Date(dateString);
        return date instanceof Date && !isNaN(date);
    }

    // Validación de datos y recopilación de campos vacíos
    let camposVacios = [];
    for (const [key, value] of Object.entries(data)) {
        // Verifica si el valor es una cadena y está vacío después de quitar espacios en blanco
        if (typeof value === 'string' && value.trim() === '') {
            camposVacios.push(nombresCampos[key]);
        } else if (value === null || value === undefined) { // Verifica si el valor es nulo o indefinido
            camposVacios.push(nombresCampos[key]);
        } else if (typeof value === 'number' && isNaN(value)) { // Verifica si el valor es un número pero no es válido (NaN)
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
                text: "Evento agregado exitosamente!",
                icon: "success",
                button: "Aceptar",
            }).then((value) => {
                $('#modal-agregar-evento').modal('hide'); // Oculta el modal
                listarEventos(); 
                limpiarFormulario(); 
            });
        },
        error: function(xhr, status, error) {
            swal("Error", "No se pudo agregar el evento. Por favor, intenta de nuevo.", "error");

        }
    });
}


function limpiarFormulario() {
    document.getElementById('nombreEvento').value = '';
    document.getElementById('fechaInicioEvento').value = '';
    document.getElementById('fechaFinEvento').value = '';
    document.getElementById('descripcionEvento').value = '';
    document.getElementById('precioEvento').value = '';
    document.getElementById('cbEstadoEvento').value = document.getElementById('cbEstadoEvento').options[0].value;
    document.getElementById('cbEmpleado').value = document.getElementById('cbEmpleado').options[0].value;
    document.getElementById('cbFormaPago').value = document.getElementById('cbFormaPago').options[0].value;
    document.getElementById('cbHotel').value = document.getElementById('cbHotel').options[0].value;
    document.getElementById('cbUsuario').value = document.getElementById('cbUsuario').options[0].value;
}

// function actualizar() {
//     var idEvento = document.getElementById('idEvento').value;
//     var data = {
//         nombre: document.getElementById('txNombreEvento').value,
//         fechaInicio: document.getElementById('dtfechaInicioEvento').value,
//         fechaTermino: document.getElementById('dtfechaFinEvento').value,
//         descripcion: document.getElementById('taDescripcion').value,
//         precio: document.getElementById('numPrecio').value,
//         estado: document.getElementById('cbEstado').value,
//         idEmpleado: document.getElementById('cbEmpleado').value,
//         idFPago: document.getElementById('cbPago').value,
//         idHotel: document.getElementById('cbHotel').value,
//         idUsuario: document.getElementById('cbUsuario').value,
//     };

//     $.ajax({
//         type: "PUT",
//         url: url_api + lo_path + idEvento,
//         data: JSON.stringify(data),
//         contentType: "application/json",
//         dataType: "json",
//         success: function(response) {
//             if (!response.OK) {
//                 alert(response.msg);
//                 return;
//             }
//             //Poner el swal 
//             alert('Evento actualizado correctamente');
//         },
//         error: function(xhr, status, error) {
//             console.error('Error:', error);
//             console.log('Detalles del error:', xhr.responseText);
//             alert('Error al actualizar el evento: ' + xhr.responseText);
//         }
//     });
// }

// function eliminar() {
//     var idEvento = document.getElementById('idEvento').value;
//     $.ajax({
//         type: "DELETE",
//         url: url_api + lo_path + idEvento,
//         dataType: "json",
//         success: function(response) {
//             if (!response.OK) {
//                 alert(response.msg);
//                 return;
//             }
//             alert('Evento eliminado correctamente');
//         },
//         error: function(xhr, status, error) {
//             console.error('Error:', error);
//             console.log('Detalles del error:', xhr.responseText);
//             alert('Error al eliminar el evento: ' + xhr.responseText);
//         }
//     });
// }
