function cargarDatosSelect(url, selectId, valueField, textField, defaultText = "Seleccione una opción") {
    fetch(url) //Solicitud url 
        .then(response => response.json()) // Resp Jsonn
        .then(data => {
            console.log(data); 
            const select = document.querySelector(selectId);
            select.innerHTML = ''; 

            
            const defaultOption = document.createElement('option'); //Op Predeterminado
            defaultOption.textContent = defaultText;
            defaultOption.value = '';
            select.appendChild(defaultOption);

            // Opciones obtenidas de la API
            data.forEach(item => {
                const option = document.createElement('option');
                option.value = item?.[valueField]; 
                option.textContent = item?.[textField]; 
                select.appendChild(option);
            });
        })
        .catch(error => console.error('Error:', error));
}

$(document).ready(function() {
    // URL base de tu API
    const url_api = 'http://localhost:9098/api/';

    //"idHotel": 1,
    //"idFPago": 2,
    //"idEmpleado": 1,
    //"idUsuario": 1
    // Llama a cargarDatosSelect con la URL completa formada por la URL base + path específico
    cargarDatosSelect(url_api + 'hotel', '#cbHotel', 'idHotel', 'nombre');
    cargarDatosSelect(url_api + 'formaPago', '#cbFormaPago', 'idFPago', 'nombre');
    cargarDatosSelect(url_api + 'usuario', '#cbUsuario', 'idUsuario', 'usuario');
    cargarDatosSelect(url_api + 'empleado', '#cbEmpleado', 'idEmpleado', 'rut');
});

// Para guardar datos estaticos en la bd
$('#btnGuardar').click(function() {
    const estadoEvento = $('#cbEstado').val();
    const url_api = 'http://localhost:9098/api/evento/'; 

    const datosEvento = {
        estado: estadoEvento,
    };

    $.ajax({
        type: "POST",
        url: url_api, 
        contentType: "application/json", 
        data: JSON.stringify(datosEvento), 
        success: function(response) {
            console.log('Datos guardados correctamente:', response);
        },
        error: function(error) {
            console.error('Error al guardar los datos:', error);
        }
    });
});