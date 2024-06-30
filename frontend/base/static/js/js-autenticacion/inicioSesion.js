const url_api = 'http://localhost:9098/api/';
const lo_path = 'usuario/';
const inicioSesionUrl = url_api + lo_path;
const correoUsuarioUrl = url_api + lo_path + 'correo/';

$(document).ready(function() {
    $('#btIniciaSesion').click(function(e) {
        e.preventDefault(); // Evita el envío tradicional del formulario

        const datosInicioSesion = {
            usuario: $('#usuario').val(),
            contrasena: $('#contrasena').val(),
        };

        if (!datosInicioSesion.usuario || !datosInicioSesion.contrasena) {
            Swal.fire({
                icon: 'error',
                title: 'Oops...',
                text: '¡Todos los campos son obligatorios!',
            });
            return;
        }

        $.ajax({
            url: correoUsuarioUrl + datosInicioSesion.usuario + '/',
            type: 'GET',
            success: function(responseCorreo) {
                console.log('Correo del usuario:', responseCorreo);
                localStorage.setItem('usuarioMostrar', datosInicioSesion.usuario); 
                actualizarUIUsuario(datosInicioSesion.usuario);
                Swal.fire({
                    icon: 'success',
                    title: 'Inicio de sesión exitoso',
                    text: 'Has iniciado sesión correctamente.',
                }).then((result) => {
                    window.location.href = '/reserva/';
                });
            },
            error: function(xhr, status, error) {
                Swal.fire({
                    icon: 'error',
                    title: 'Error al obtener el correo',
                    text: 'No se pudo obtener el correo del usuario.',
                });
            }
        });
    });
});

function actualizarUIUsuario(usuario) {
    $('#usuario-info').html(`
        <a href="#" class="nav-link d-flex lh-1 text-reset p-0">
            <span>Bienvenido, ${usuario}</span>
        </a>
    `);
    $('#login-link, #register-link').hide(); // los ocultas
}