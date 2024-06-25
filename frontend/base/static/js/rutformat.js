function dgv(T) { //digito verificador
    var M = 0, S = 1;
    for (; T; T = Math.floor(T / 10))
        S = (S + T % 10 * (9 - M++ % 6)) % 11;
    return S ? S - 1 : 'k';
}

document.addEventListener('DOMContentLoaded', function() {
    var rutField = document.getElementById('id_rut');
    if (rutField) {
        rutField.addEventListener('input', function (e) {
            var target = e.target;

            // Elimina los puntos y guiones del valor actual
            var rawValue = target.value.replace(/\./g, '').replace(/-/g, '');

            // Almacena el valor sin formato en un campo oculto
            document.getElementById('dv').value = rawValue;

            // Calcula el dígito verificador y lo agrega al campo 'dv'
            var dv = dgv(parseInt(rawValue, 10));
            document.getElementById('dv').value = dv;
        });
    }
});