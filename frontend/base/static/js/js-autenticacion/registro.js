/*
Usuario
Correo
Contraseña
Repetir contraseña
*/
const url_api = 'http://localhost:9010/api/'; // URL base de tu API
const lo_path = 'usuario/';

// Paso 1: Definir la URL completa
const registroUrl = url_api + lo_path;

// Paso 2: Crear el objeto de datos del usuario
// Asegúrate de validar que las contraseñas coincidan antes de enviar el objeto
const datosUsuario = {
  usuario: document.getElementById('usuario').value,
  correo: document.getElementById('correo').value,
  contrasena: document.getElementById('contrasena').value,
  repetirContrasena: document.getElementById('repetir-contrasena').value,
};
// Validación de contraseña
if (datosUsuario.contrasena !== datosUsuario.repetirContrasena) {
  console.error('Las contraseñas no coinciden.');
  // Aquí puedes detener el proceso y mostrar un mensaje al usuario
} else {
  // Paso 3: Convertir los datos del usuario a JSON
  const datosUsuarioJSON = JSON.stringify({
    usuario: datosUsuario.usuario,
    correo: datosUsuario.correo,
    contrasena: datosUsuario.contrasena,
    // No incluir repetirContraseña en el objeto enviado al servidor
  });

  // Paso 4: Configurar la solicitud AJAX
  $.ajax({
    type: 'POST',
    url: registroUrl,
    contentType: 'application/json',
    data: datosUsuarioJSON,

    success: function(response) {
      // Paso 6: Manejar respuesta exitosa
      console.log('Usuario registrado con éxito:', response);
      // Aquí puedes redirigir al usuario o mostrar un mensaje de éxito
    },
    error: function(error) {
      // Manejar respuesta de error
      console.error('Error al registrar el usuario:', error);
      // Mostrar mensaje de error al usuario
    }
  });
}