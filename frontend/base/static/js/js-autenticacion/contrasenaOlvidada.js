document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('form-restablecimiento'); // Asegúrate de agregar este ID al formulario en tu HTML

    form.addEventListener('submit', function(e) {
        e.preventDefault(); // Evita el envío tradicional del formulario

        const usuario = document.getElementById('usuario').value;
        const correo = document.getElementById('correo').value;

        // Validación básica
        if (!usuario || !correo) {
            Swal.fire('Error', 'Por favor, completa todos los campos.', 'error');
            return;
        }

        // Aquí, reemplaza 'url_del_servidor' con la URL a la que debes enviar los datos para el proceso de restablecimiento
        fetch('url_del_servidor', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ usuario, correo }),
        })
        .then(response => response.json())
        .then(data => {
            // Manejar la respuesta del servidor
            if (data.success) {
                Swal.fire('Enviado', 'Revisa tu correo electrónico para restablecer tu contraseña.', 'success');
            } else {
                Swal.fire('Error', data.message, 'error');
            }
        })
        .catch(error => {
            console.error('Error:', error);
            Swal.fire('Error', 'Hubo un problema con la solicitud de restablecimiento de contraseña.', 'error');
        });
    });
});