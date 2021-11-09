$(document).ready(function () {

    $('#DecryptTI').on('click', function (event) {
        event.preventDefault();
        let v_key = $('#keyTI').val();
        let v_message = $('#messageTI').val();

        if (v_key != '' && v_message != '') {
            $.ajax({
                data: {
                    messageTI: v_message,
                    keyTI: v_key,
                },
                type: 'POST',
                url: '/request_TransInterrumpida',
                success: function (html) {
                    
                    $('#textTI').val(html.result);
                }

            });

        } else if (v_message == '' && v_key == '') {
            alert("Los campos estan vacios")
        } else if (v_key == '') {
            alert("La clave esta vacia");
        } else if (v_message == '') {
            alert("No se encontro texto ");
        }
    });
});