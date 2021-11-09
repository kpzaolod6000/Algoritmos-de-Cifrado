$(document).ready(function() {

	$('#encrypt').on('click', function(event) {
		event.preventDefault();
        let v_key = $('#key').val();
        if (v_key != '' && v_key <= 25) {
            $.ajax({
                data : {
                    message_ : $('#message').val(),
                    key_ : $('#key').val(),
                    c_d : 'cifrar'
                },
                type : 'POST',
                url : '/request_Ci_Cesar',
                success: function(html) {
                    //alert(html.status);
                    // $("#message").html(html.result);
                    $('#message').val(html.result);
                }
        
            });
            
        }else if (v_key == '' ) {
            alert("La clave esta vacia");
        }else{
            alert("La clave esta fuera del modulo");
        }
		
	
    });

    
	$('#decrypt').on('click', function(event) {

		event.preventDefault();
        let v_key = $('#key').val();
        if (v_key != '' && v_key <= 25) {
            $.ajax({
                data : {
                    message_ : $('#message').val(),
                    key_ : $('#key').val(),
                    c_d : 'descifrar'
                },
                type : 'POST',
                url : '/request_Ci_Cesar',
                success: function(html) {
                    //alert(html.status);
                    // $("#message").html(html.result);
                    $('#message').val(html.result);
                }
            });
        }else if (v_key == '' ) {
            alert("La clave esta vacia");
        }else{
            alert("La clave esta fuera del modulo");
        }
		

	});

});