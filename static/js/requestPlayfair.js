$(document).ready(function () {

    $('#Calculate').on('click', function (event) {
        event.preventDefault();
        let v_key = $('#keyPF').val();
        let v_message = $('#messagePF').val();
        let tam_M = parseInt($('.tam-selected:checked').val());
        if (v_key != '' && v_message != '') {
            $.ajax({
                data: {
                    messagePF: v_message,
                    keyPF: v_key,
                    tam_matrix: tam_M,
                    c_d_: $('#inputState').val()
                },
                type: 'POST',
                url: '/request_Playfair',
                success: function (html) {
                    
                    $('#textTR').val(html.result);
                    $('#preproccesTR').val(html.preprocess);
                
                    let event_data = '';
                    let len_m = tam_M; //aca va si hay un radiobutton
                    

                    $.each(html, function (index, value) {
                        if (index == 'keyMatrx') {
                            
                            let words = ""
                            
                            for (let j = 0; j < value.length; j++) {
                                if (value[j] != " ") {
                                    words += value[j]
                                }
                            }

                            event_data += '<tr>';
                            for (let i = 0; i < words.length; i++) {
                                 if (i == len_m) {
                                    len_m += tam_M;
                                    
                                    event_data += '</tr>';
                                    event_data += '<tr>';
                                    event_data += '<td>' +'&nbsp;&nbsp;&nbsp;&nbsp;' + words[i]+ '</td>';
                                }
                                else{
                                    event_data += '<td>' +'&nbsp;&nbsp;&nbsp;&nbsp;' + words[i]+ '</td>';
                                }
                            }
                        }  
                    
                    });
                    $("#key-matrix").empty();
                    $("#title-key-matrix").empty();
                    $("#title-key-matrix").append('Matriz de clave')
                    $("#key-matrix").append(event_data);
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