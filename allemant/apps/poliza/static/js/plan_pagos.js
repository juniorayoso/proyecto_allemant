$(document).ready(function(){
	/********ELEMENTOS A INICIALIZAR **************/


	/*$('#f_inicio').onchange(function() {
        var fecha = $('#f_inicio').val();
        fecha = new Date(fecha);
        for (var i = 0; i < 4; i++) {
            fecha.setDate(fecha.getDate()+30);
            $('#f_'+i).val((fecha.getMonth()+1)+'/'+fecha.getDate()+'/'+fecha.getFullYear());
            
        };
    });  */

	$('#buscar_poliza').click(function(){
		var numero_poliza = $('.num_poliza').val();
		result="";
		cuotas="";
		if (numero_poliza!=""){
	        $.get(GET_PLAN_PAGOS, {numero_poliza:numero_poliza}, function(data){
				/*$('#num_cuotas').val(data['cuotas']);
	        	if ($.isEmptyObject(data)){
	        		alert("El numero de poliza es incorrecto");
	        	}
	        	else{
	        		
	        		result+="<tr class='info'><td>"+data['numero']+"</td>";
	        		result+="<td>"+data['cliente']+"</td>";
	        		result+="<td>"+data['cia']+"</td>";
	        		result+="<td>"+data['ramo']+"</td>";
	        		result+="<td>"+data['moneda']+"</td>";
	        		result+="<td class='text-right'>"+data['monto']+"</td>";
	        		result+="<td id = 'prima' class='text-right'>"+data['prima']+"</td>";
	        		result+="<td class='text-center'>"+data['fecha_inicio']+"</td></tr>";
					$('#poliza').html(result);
					

	        	}	*/
	        	location.href = "/poliza/"+data['id']+"/plan_pagos/";

	        });
	    }
	    else{
	    	alert("Ingrese el numero de poliza");
	    }
    });

	$('#agregar_cuotas').click(function(){
		formularios = parseInt($('#id_form-TOTAL_FORMS').val())
		var numero_cuotas=parseInt($('#num_cuotas').val());
		cuotas=""
		if (numero_cuotas!=0){

			$('#id_form-TOTAL_FORMS').val(formularios+numero_cuotas)
			for (var i = 0; i <= numero_cuotas-1; i++) {
				cuotas+="<tr class='info'>";
				nro_form = formularios + i	
				cuotas+="<td class='hide'><input type='number' id='id_form-"+nro_form+"-id' name='form-"+nro_form+"-id'>";
				cuotas+="<input class='form-control' id='id_form-"+nro_form+"-numero_cuota' name='form-"
				cuotas+=nro_form+"-numero_cuota' value="+(nro_form+1)+"></td>";
				cuotas+="<td>"+(nro_form+1)+"</td>"
				cuotas+="<td ><input class='form-control' id='id_form-"+nro_form+"-numero_cupon' name='form-"
				cuotas+=nro_form+"-numero_cupon'></td>";
				cuotas+="<td ><input class='form-control' id='id_form-"+nro_form+"-monto' name='form-"
				cuotas+=nro_form+"-monto'></td>";
				cuotas+="<td ><input class='inicio datepicker form-control' id='id_form-"+nro_form+"-fecha_vence' name='form-"
				cuotas+=nro_form+"-fecha_vence'></td>";
				
				
				
				cuotas+="<td></td>";
				cuotas+="</tr>";
			};
		};
		$('#cuotas').append(cuotas);
		$('.datepicker').datepicker();
	});
	$('.inicio').change(function() {
		if($(this).val=""){
		    var fecha = $('#f_inicio').val();
		    fecha = new Date(fecha);
		    for (var i = 1; i <= parseInt($('#num_cuotas').val()); i++) {
		        fecha.setDate(fecha.getDate()+30);
		        $('#f_'+i).val((fecha.getMonth()+1)+'/'+fecha.getDate()+'/'+fecha.getFullYear());
		        
		    };
		};
	});

	$('.borrar_cupon').click(function(){
		
		var id_cupon = parseInt($(this).parent().parent().children()[0].children[0].value);
		$.get(BORRAR_CUPON, {id_cupon:id_cupon});
		mensaje = "¿Esta seguro que dese eliminar ese cupon?";
		if(confirm(mensaje)){
			$(this).parent().parent().remove();
			location.href=PLAN_PAGOS;
		}
	});
	$('#id_form-0-numero_cupon').change(function(){
		formularios = parseInt($('#id_form-TOTAL_FORMS').val())
		cupon = parseInt($('#id_form-0-numero_cupon').val())
		for (var i = 1; i < formularios+1; i++) {
			$('#id_form-'+i+'-numero_cupon').val(cupon+i)
		};
	});
});

