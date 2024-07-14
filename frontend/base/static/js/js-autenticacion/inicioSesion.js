const url_api = 'http://localhost:9098/api/';
const lo_path = 'usuario/';
const inicioSesionUrl = url_api + lo_path;
const correoUsuarioUrl = url_api + lo_path + 'correo/';

$(document).ready(function() {
    $('#btIniciaSesion').click(function(e) {
        e.preventDefault(); // Evita el envío tradicional del formulario

        // Verificar si el usuario está autenticado al cargar la página
        const usuarioAutenticado = localStorage.getItem('usuarioAutenticado');
        const usuarioCorreo = localStorage.getItem('usuarioMostrar');
        if (usuarioAutenticado) {
            actualizarUIUsuario(usuarioCorreo);
        }


        const datosInicioSesion = {
            correo: $('#txCorreo').val(), // Asegúrate de que el HTML tenga un elemento con id="txCorreo"
            contrasena: $('#txPassword').val(), // Asegúrate de que el HTML tenga un elemento con id="txPassword"
        };

        if (!datosInicioSesion.correo || !datosInicioSesion.contrasena) {
            Swal.fire({
                icon: 'error',
                title: 'Oops...',
                text: '¡Todos los campos son obligatorios!',
            });
            return;
        }

        $.ajax({
            url: correoUsuarioUrl + datosInicioSesion.correo + '/',
            type: 'GET',
            success: function(responseUsuario) {
                console.log('Nombre de usuario:', responseUsuario);
                // Guardar datos de usuario y estado de autenticación
                localStorage.setItem('usuarioMostrar', datosInicioSesion.correo);
                localStorage.setItem('usuarioAutenticado', true);
                actualizarUIUsuario(datosInicioSesion.correo);
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

function cerrarSesion() {
    // Limpiar datos de usuario del almacenamiento local
    localStorage.removeItem('usuarioMostrar');
    localStorage.removeItem('usuarioAutenticado');
    
    // Actualizar la UI para reflejar que el usuario no está autenticado
    $('#usuario-info').html(`
        <div id="login-link">
            <a href="/inicioSesion" class="nav-link d-flex lh-1 text-reset p-0">
                <span>Inicio de Sesión</span>
            </a>
        </div>
        <div id="register-link">
            <a href="/registro" class="nav-link d-flex lh-1 text-reset p-0">
                <span>Registrarse</span>
            </a>
        </div>
    `);
}

function actualizarUIUsuario(usuario) {
    $('#usuario-info').html(`
        <a href="#" class="nav-link d-flex lh-1 text-reset p-0">
            <span>Bienvenido, ${usuario}</span>
        </a>
    `);
    $('#login-link, #register-link').hide(); // Asegúrate de que el HTML tenga elementos con id="login-link" y "register-link"
}



// // Objetivo: Realizar la autenticación de un usuario en el sistema.
// // var url_host = 'http://localhost:9098'
// var url_api_login= url_host + '/apix/token/'    
// 
// function segurLogin() {
//     var formData = new FormData();
//     formData.append('username', document.getElementById('txCorreo').value);
//     formData.append('password', document.getElementById('txPassword').value);
// 
//     $.ajax({
//         type: "POST",      // GET, PUT, POST, DELETE
//         data: formData,  // Envio deParámetro
//         async: false,      // Sincrónico
//         url: url_api_login ,  // Url de la API
//         contentType: false,
//         processData: false,
//         cache: false,
//         beforeSend: function (data){
//             console.log('... cargando...');
//         }
//         , error: function (data) {
//             console.log('Tenemos problemas Houston ' + JSON.stringify(data));
//         },
//         success: function (data) {
//             console.log("Login=>",data)
//             if (data.access){
//                 // Grabamos en LocalStorage
//                 //localStorage.removeItem("url_token_access");
//                 //localStorage.removeItem("url_token_refresh");
// 
//                 //localStorage.setItem("url_token_access", data.access);
//                 //localStorage.setItem("url_token_refresh", data.refresh);
//                 
//                 // Redirección a la página de productos de la misma url
//                 window.location.href = "/";
//                 return
// //                alert(data.refresh)
// //                alert(data.access)
//                 }
//         }
//     });
// }
