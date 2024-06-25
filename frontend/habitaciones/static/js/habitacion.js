const url_api = 'http://localhost:9010/api/'; // URL base de tu API
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




$.ajax({
    type: "GET",
    url: url_api + lo_path, 
    success: function(hoteles) {
        console.log(hoteles); // Esto imprimirá en la consola la respuesta del backend
        var selectHotel = $('#cdHotel'); 
        hoteles.forEach(function(hotel) {
            selectHotel.append($('<option>', {
                value: hotel.idHotel, 
                text: hotel.nombre
            }));
        });
    },
    error: function() {
        alert('Error al cargar los hoteles');
    }
});














// var url_api= 'http://localhost:9010/venta/'    
// //var lo_path = 'persona/'
// var lo_path = 'libro/'

// function leer() {
//     var idLibro = document.getElementById('txIdLibro').value;
//     var pathUrl = url_api + lo_path + idLibro;

//     $.ajax({
//         type: "GET",
//         url: pathUrl,
//         cache: false,
//         dataType: "json",
//         beforeSend: function () {
//             console.log('Cargando libro...');
//         },
//         error: function (xhr, status, error) {
//             console.error('Error al cargar libro:', error);
//             console.log('Detalles del error:', xhr.responseText);
//             mostrarMensaje('error', 'Error al cargar libro', 'Hubo un problema al cargar el libro.');
//             limpiarLibro();
//         },
//         success: function (data) {
//             console.log('Libro recibido:', data);

//             if (!data) {
//                 console.log('No se recibió respuesta válida');
//                 mostrarMensaje('error', 'Libro no encontrado', 'No se encontró el libro con el ID proporcionado.');
//                 limpiarLibro();
//                 return;
//             }

//             mostrarMensaje('success', 'Libro encontrado', 'Se encontró el libro correctamente.');

//             // Establecer los valores en los campos del formulario
//             document.getElementById('txIdLibro').value = data.idLibro;
//             document.getElementById('txTitulo').value = data.titulo;
//             document.getElementById('cbEditorial').value = data.editorial.toString();
//             document.getElementById('cbCategoria').value = data.categoria.toString();
//             document.getElementById('cbGenero').value = data.genero.toString();
//             document.getElementById('cbIdioma').value = data.idioma.toString();
//             document.getElementById('cbTapa').value = data.tapa.toString();
//             document.getElementById('cbOrigen').value = data.origen.toString();
//             document.getElementById('cbEstado').value = data.estado.toString();
//         }
//     });
// }

// function mostrarMensaje(icono, titulo, mensaje) {
//     Swal.fire({
//         icon: icono,
//         title: titulo,
//         text: mensaje,
//         showConfirmButton: false,
//         timer: 1500
//     });
// }

// // Función para limpiar los campos del formulario
// function limpiarCampos() {
//     document.getElementById('txIdLibro').value = "";
//     document.getElementById('txTitulo').value = "";
//     document.getElementById('cbEditorial').selectedIndex = 0; // Reiniciar el select
//     document.getElementById('cbCategoria').selectedIndex = 0; // Reiniciar el select
//     document.getElementById('cbGenero').selectedIndex = 0; // Reiniciar el select
//     document.getElementById('cbIdioma').selectedIndex = 0; // Reiniciar el select
//     document.getElementById('cbTapa').selectedIndex = 0; // Reiniciar el select
//     document.getElementById('cbOrigen').selectedIndex = 0; // Reiniciar el select
//     document.getElementById('cbEstado').selectedIndex = 0; // Reiniciar el select
// }


// function agregarLibro() {
//     var data = {
//         idLibro: document.getElementById('txIdLibro').value,
//         titulo: document.getElementById('txTitulo').value,
//         editorial: document.getElementById('cbEditorial').value,
//         categoria: document.getElementById('cbCategoria').value,
//         genero: document.getElementById('cbGenero').value,
//         idioma: document.getElementById('cbIdioma').value,
//         tapa: document.getElementById('cbTapa').value,
//         origen: document.getElementById('cbOrigen').value,
//         estado: document.getElementById('cbEstado').value,
//     };

//     $.ajax({
//         type: "POST",
//         url: url_api + lo_path,
//         data: JSON.stringify(data),
//         contentType: "application/json",
//         dataType: "json",
//         beforeSend: function () {
//             console.log('Agregando libro...');
//         },
//         // success: function (response) {
//         //     console.log('Respuesta recibida:', response);

//         //     if (response.ok) {
//         //         agregadoMensaje('success', 'Libro agregado', 'El libro se agregó correctamente.');
//         //         // Después de agregar correctamente, cargar los datos del nuevo libro
//         //         leer();
//         //     } else {
//         //         agregadoMensaje('error', 'Error al agregar libro', 'Hubo un problema al intentar agregar el libro.');
//         //     }
//         // },
//         // error: function (xhr, status, error) {
//         //     console.error('Error:', error);
//         //     console.log('Detalles del error:', xhr.responseText);
//         //     agregadoMensaje('error', 'Error al agregar libro', 'Hubo un problema al intentar agregar el libro.');
//         // }
//     });
// }

// function agregadoMensaje(icono, titulo, mensaje) {
//     Swal.fire({
//         icon: icono,
//         title: titulo,
//         text: mensaje,
//         showConfirmButton: false,
//         timer: 1500
//     });
// }   


// function modificarLibro() {
//     var idLibro = document.getElementById('txIdLibro').value;

//     var data = {
//         idLibro: idLibro,  // Ensure idLibro is included in the data payload
//         titulo: document.getElementById('txTitulo').value,
//         editorial: document.getElementById('cbEditorial').value,
//         categoria: document.getElementById('cbCategoria').value,
//         genero: document.getElementById('cbGenero').value,
//         idioma: document.getElementById('cbIdioma').value,
//         tapa: document.getElementById('cbTapa').value,
//         origen: document.getElementById('cbOrigen').value,
//         estado: document.getElementById('cbEstado').value
//     };

//     $.ajax({
//         type: "PUT",
//         url: url_api + lo_path + idLibro + "/",
//         data: JSON.stringify(data),
//         contentType: "application/json",
//         dataType: "json",
//         success: function(response) {
//             alert('Libro actualizado correctamente');
//             leer();  // Assuming this function refreshes your data view
//         },
//         error: function(xhr, status, error) {
//             console.error('Error:', error);
//             console.log('Detalles del error:', xhr.responseText);
//             alert('Error al actualizar libro: ' + xhr.responseText);
//         }
//     });
// }

// function eliminarLibro() {
//     var idLibro = document.getElementById('txIdLibro').value;

//     $.ajax({
//         type: "DELETE",
//         url: url_api + lo_path + idLibro,
//         dataType: "json",
//         success: function(response) {
//             if (!response.OK) {
//                 alert(response.msg);
//                 return;
//             }
//             alert('Libro eliminado correctamente');
//             limpiarLibro();
//         },
//         error: function(xhr, status, error) {
//             console.error('Error:', error);
//             console.log('Detalles del error:', xhr.responseText);
//             alert('Error al eliminar libro: ' + xhr.responseText);
//         }
//     });
// }

// function limpiarLibro() {
//     document.getElementById('txIdLibro').value = "";
//     document.getElementById('txTitulo').value = "";
//     document.getElementById('cbEditorial').selectedIndex = 0; // Reiniciar el select
//     document.getElementById('cbCategoria').selectedIndex = 0; // Reiniciar el select
//     document.getElementById('cbGenero').selectedIndex = 0; // Reiniciar el select
//     document.getElementById('cbIdioma').selectedIndex = 0; // Reiniciar el select
//     document.getElementById('cbTapa').selectedIndex = 0; // Reiniciar el select
//     document.getElementById('cbOrigen').selectedIndex = 0; // Reiniciar el select
//     document.getElementById('cbEstado').selectedIndex = 0; // Reiniciar el select
// }

// function actualizarLibro() {
//     var idLibro = document.getElementById('txIdLibro').value;

//     var data = {
//         idLibro: idLibro,
//         titulo: document.getElementById('txTitulo').value,
//         editorial: document.getElementById('cbEditorial').value,
//         categoria: document.getElementById('cbCategoria').value,
//         genero: document.getElementById('cbGenero').value,
//         idioma: document.getElementById('cbIdioma').value,
//         tapa: document.getElementById('cbTapa').value,
//         origen: document.getElementById('cbOrigen').value,
//         estado: document.getElementById('cbEstado').value,
//     };

//     $.ajax({
//         type: "PUT",
//         url: url_api + lo_path + idLibro,
//         data: JSON.stringify(data),
//         contentType: "application/json",
//         dataType: "json",
//         success: function(response) {
//             if (!response.OK) {
//                 alert(response.msg);
//                 return;
//             }
//             alert('Libro actualizado correctamente');
//         },
//         error: function(xhr, status, error) {
//             console.error('Error:', error);
//             console.log('Detalles del error:', xhr.responseText);
//             alert('Error al actualizar libro: ' + xhr.responseText);
//         }
//     });
// }
