const url_api = 'http://localhost:9098/api/'; // URL base de tu API
const lo_path = 'usuario/';

function agregarUsuario() {
    var data = {
        usuario: document.getElementById('usuario').value,
        //nombre: document.getElementById('nombre').value,
        correo: document.getElementById('correo').value,
        contrasena: document.getElementById('contrasena').value,
    };

    // Identificadores de campos a nombres personalizados
    var nombresCampos = {
        usuario: "Nombre de usuario",
        //nombre: "Nombre",
        correo: "Correo electronico",
        contrasena: "Contraseña",
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
                text: "Usuario agregado exitosamente!",
                icon: "success",
                button: "Aceptar",
            }).then((value) => {
                $('#modal-agregar-usuario').modal('hide'); // Oculta el modal
                listarUsuarios(); 
                limpiarFormulario(); 
            });
        },
        error: function(xhr, status, error) {
            swal("Error", "No se pudo agregar el usuario. Por favor, intenta de nuevo.", "error");
        }
    });
}



function limpiarFormulario() {
    document.getElementById('usuario').value = '';
    //document.getElementById('nombre').value = '';
    document.getElementById('correo').value = '';
    document.getElementById('contrasena').value = '';
}

