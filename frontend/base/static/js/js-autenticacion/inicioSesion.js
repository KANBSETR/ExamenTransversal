// Objetivo: Realizar la autenticación de un usuario en el sistema.
var url_host = 'http://localhost:9098'
var url_api_login= url_host + '/apix/token/'    

function segurLogin() {
    var formData = new FormData();
    formData.append('username', document.getElementById('txEmail').value);
    formData.append('password', document.getElementById('txPassword').value);

    $.ajax({
        type: "POST",      // GET, PUT, POST, DELETE
        data: formData,  // Envio deParámetro
        async: false,      // Sincrónico
        url: url_api_login ,  // Url de la API
        contentType: false,
        processData: false,
        cache: false,
        beforeSend: function (data){
            console.log('... cargando...');
        }
        , error: function (data) {
            console.log('Tenemos problemas Houston ' + JSON.stringify(data));
        },
        success: function (data) {
            console.log("Login=>",data)
            if (data.access){
                // Grabamos en LocalStorage
                localStorage.removeItem("url_token_access");
                localStorage.removeItem("url_token_refresh");

                localStorage.setItem("url_token_access", data.access);
                localStorage.setItem("url_token_refresh", data.refresh);
                
                // Redirección a la página de productos de la misma url
                document.location.href = "/admin/habitaciones";
                return
//                alert(data.refresh)
//                alert(data.access)
                }
        }
    });
}