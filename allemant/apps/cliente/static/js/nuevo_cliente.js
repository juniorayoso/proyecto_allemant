$(document).ready(function(){
	$('.mapa').click(function(){
		var calle = $(this).parent().parent().children()[2].children[0].value;
		var ubigeo = $(this).parent().parent().children()[4].children[0][1].text;
		window.open("https://www.google.com/maps/place/"+calle+" "+ubigeo+" Perú",'_blank');

	});
	
	$('#mas_fono').click(function(){
		

		formulario = parseInt($('#id_telefono-TOTAL_FORMS').val());
		$('#id_telefono-TOTAL_FORMS').val(formulario+1);
		var result="";
		var row = $('#id_telefono-0-operador').clone(true);
		result+="<div class='form-group'>";
		result+="<div class='col-md-2 col-md-offset-1'>";

		result+="<select class='form-control' id='id_telefono-";
		result+=formulario+"-operador' name='telefono-"+formulario+"-operador' >";
		result+=row.html();
		result+="</select>";
		result+="</div>";
		result+="<div class='col-sm-2'>";
		result+="<input class='form-control' placeholder='Número' id='id_telefono-"
		result+=formulario+"-numero' name='telefono-"+formulario+"-numero' />"; 
		result+="</div>";
		result+="<div class='col-sm-2'>";
		result+="<button type='button' id='menos' class='btn btn-danger'><i class='icon-minus-2'></i></button>"
		result+="</div>";
		result+="</div>";
		
		$(result).insertAfter($("#telefono"));
		ActivarBotones();
		
	});

	$('#mas_email').click(function(){
		

		formulario = parseInt($('#id_email-TOTAL_FORMS').val());
		$('#id_email-TOTAL_FORMS').val(formulario+1);
		var result="";
		result+="<div class='form-group'>";
		result+="<div class='col-sm-4 col-md-offset-1'>";

		result+="<input maxlength='75' type='email' placeholder='Ingrese e-mail' class='form-control' id='id_email-";
		result+=formulario+"-email' name='email-"+formulario+"-email' >";
		result+="</input>";
		result+="</div>";
		
		result+="<div class='col-sm-1'>";
		result+="<button type='button' id='menos' class='btn btn-danger'><i class='icon-minus-2'></i></button>"
		result+="</div>";
		result+="</div>";
		
		$(result).insertAfter($("#email"));
		ActivarBotones();
		
	});

	$('#mas_direccion').click(function(){
		

		formulario = parseInt($('#id_direccion-TOTAL_FORMS').val());
		$('#id_direccion-TOTAL_FORMS').val(formulario+1);
		var result="";
		result+="<div class='form-group'>";
		result+="<div class='col-sm-4 col-md-offset-1'>";

		result+="<input maxlength='40' type='text' placeholder='Avenida / Calle' class='form-control' id='id_direccion-";
		result+=formulario+"-av_calle' name='direccion-"+formulario+"-av_calle' >";
		result+="</input>";
		result+="</div>";
		result+="<div class='col-sm-2 '>";

		result+="<input maxlength='20' type='text' placeholder='# / Dpto / Oficina / Interior' class='form-control' id='id_direccion-";
		result+=formulario+"-interior' name='direccion-"+formulario+"-interior' >";
		result+="</input>";
		result+="</div>";
		
		var row = $('#id_direccion-0-ubigeo').clone(true);
		result+="<div class='col-md-2'>";

		result+="<select class='form-control' id='id_direccion-";
		result+=formulario+"-ubigeo' name='direccion-"+formulario+"-ubigeo' >";
		result+=row.html();
		result+="</select>";
		result+="</div>";

		var row1 = $('#id_direccion-0-distrito').clone(true);
		result+="<div class='col-md-2'>";

		result+="<select class='form-control' id='id_direccion-";
		result+=formulario+"-distrito' name='direccion-"+formulario+"-distrito' >";
		result+=row1.html();
		result+="</select>";
		result+="</div>";
		result+="<div class='col-sm-1'>";
		result+="<button type='button' id='menos' class='btn btn-danger'><i class='icon-minus-2'></i></button>"
		result+="</div>";
		result+="</div>";
		
		$(result).insertAfter($("#direccion"));
		ActivarBotones();
		
	});



	function ActivarBotones(){
		$('#menos').click(function(){
			$(this).parent().parent().remove();
		});

	};
	



});