document.getElementById('botonActualizar').addEventListener('click', function() {
    fetch('modalActualizar.html')
        .then(response => response.text())
        .then(html => {
            document.getElementById('contenedorModal').innerHTML = html;

        })
        .catch(error => {
            console.error('Error al cargar el modal:', error);
        });
});
