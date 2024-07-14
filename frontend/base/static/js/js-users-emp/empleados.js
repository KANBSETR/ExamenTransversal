const url_api = 'http://localhost:9098/api/'; // URL base de tu API
const lo_path = 'empleado/';

function agregarEmpleado() {
    var data = {
        rut: document.getElementById('rutEmpleado').value,
        usuario: document.getElementById('usuario').value,
        clave: document.getElementById('clave').value,
        idCargo: document.getElementById('cargo').value,
        sueldo: document.getElementById('sueldo').value,
    };

    // Identificadores de campos a nombres personalizados
    var nombresCampos = {
        rut: "Rut del empleado",
        usuario: "Usuario del empleado",
        clave: "Clave del empleado",
        idCargo: "Cargo del empleado",
        sueldo: "Sueldo del empleado"
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
                text: "Empleado agregado exitosamente!",
                icon: "success",
                button: "Aceptar",
            }).then((value) => {
                $('#modal-agregar-empleado').modal('hide'); // Oculta el modal
                listarEmpleados(); 
                limpiarFormulario(); 
            });
        },
        error: function(xhr, status, error) {
            swal("Error", "No se pudo agregar el empleado. Por favor, intenta de nuevo.", "error");
        }
    });
}



function limpiarFormulario() {
    document.getElementById('rut').value = '';
    document.getElementById('usuario').value = '';
    document.getElementById('clave').value = '';
    document.getElementById('cargo').value = '';
    document.getElementById('sueldo').value = '';
    

}

