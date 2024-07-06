const url_api = 'http://localhost:9098/api/'; // URL base de tu API
const lo_path = 'servicioAdicional/';

function agregarServicio() {
    var data = {
        nombre: document.getElementById('txNombreServicio').value,
        descripcion: document.getElementById('taDescripcion').value,
        precio: document.getElementById('numPrecio').value,
    };

    // Identificadores de campos a nombres personalizados
    var nombresCampos = {
        nombre: "Nombre del servicio",
        descripcion: "Descripción del servicio",
        precio: "Precio del servicio",
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
                text: "Servicio agregado exitosamente!",
                icon: "success",
                button: "Aceptar",
            }).then((value) => {
                $('#modal-agregar-servicio').modal('hide'); // Oculta el modal
                listarServicios(); 
                limpiarFormulario(); 
            });
        },
        error: function(xhr, status, error) {
            swal("Error", "No se pudo agregar la habitación. Por favor, intenta de nuevo.", "error");
        }
    });
}


function limpiarFormulario() {
    document.getElementById('txNombreServicio').value = '';
    document.getElementById('taDescripcion').value = '';
    document.getElementById('numPrecio').value = '';
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
