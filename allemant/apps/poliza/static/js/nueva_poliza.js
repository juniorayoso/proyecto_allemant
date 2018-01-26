$(document).ready(function(){

	function copiar_select(campo){
		var row = $('#id_form-0-'+campo).clone(true);
		result="";
		result+="<td>";

		result+="<select class='form-control' id='id_form-";
		result+=formulario+"-"+campo+"' name='form-"+formulario+"-"+campo+"' >";
		result+=row.html();
		result+="</select>";
		result+="</td>";
		return result;
	};
	$('#mas_riesgo').bind("click",function(){
		formulario = parseInt($('#id_form-TOTAL_FORMS').val());
		$('#id_form-TOTAL_FORMS').val(formulario+1);
		result="";
		result+="<tr>";
		result+=copiar_select("tipo_riesgo");
		result+=copiar_select("ramo");
		result+=copiar_select("sub_ramo");
		result+=copiar_select("producto");

		result+="<td>";
		result+="<input class='form-control'  id='id_form-"
		result+=formulario+"-materia_asegurada' name='form-"+formulario+"-materia_asegurada' />"; 
		result+="</td>";
		result+="<td>";
		result+="<input class='form-control'  id='id_form-"
		result+=formulario+"-prima' name='form-"+formulario+"-prima' />"; 
		result+="</td>";
		result+="<td>";
		result+="<button type='button' id='menos_riesgo' class='btn btn-danger'><i class='icon-minus-2'></i></button>"
		result+="</td>";
		result+="</tr>";
		
		$('#ramos').append(result);
		activar_botones();
	});

	
});

function activar_botones(){
	$('#menos_riesgo').click(function(){
		$(this).parent().parent().remove();
	});
};