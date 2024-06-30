/*
Usuario
Correo
Contraseña
Repetir contraseña
*/
const url_api = 'http://localhost:9098/api/'; 
const lo_path = 'usuario/';
const registroUrl = url_api + lo_path;

$(document).ready(function() {
    $('#btRegistrarse').click(function(e) {
        e.preventDefault(); // Evita que el formulario se envíe de la manera tradicional

        const datosUsuario = {
            usuario: $('#usuario').val(),
            correo: $('#correo').val(),
            contrasena: $('#contrasena').val(),
        };

        // Verificar si alguno de los campos está vacío antes de enviar la solicitud
        if (!datosUsuario.usuario || !datosUsuario.correo || !datosUsuario.contrasena) {
            Swal.fire({
                icon: 'error',
                title: 'Oops...',
                text: 'Faltan campos por rellenar!',
            });
            return;
        }

        $.ajax({
            url: registroUrl, 
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify(datosUsuario),
            success: function(response) {
                Swal.fire({
                    icon: 'success',
                    title: '¡Registrado!',
                    text: 'Usuario registrado exitosamente. ¡Muchas gracias!',
                    confirmButtonText: 'Ok'
                }).then((result) => {
                    if (result.value) {
                        window.location.href = '/inicioSesion'; 
                    }
                });
            },
            error: function(xhr, status, error) {
                console.error('Error al registrar el usuario:', xhr.responseText);
                Swal.fire({
                    icon: 'error',
                    title: 'Error al registrar',
                    text: 'No se pudo registrar el usuario. Por favor, inténtalo de nuevo.',
                });
            }
        });
    });
});