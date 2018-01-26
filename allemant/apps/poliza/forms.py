from django import forms
from apps.poliza import constants as poliza_constants
from apps.core import constants as core_constants
from apps.core import models as core_models
from apps.poliza import models as poliza_models
from apps.administrativo import models as administrativo_models
from datetime import datetime


class PolizaForm(forms.ModelForm):


	def __init__(self, *args, **kwargs):
		super(PolizaForm, self).__init__(*args, **kwargs)
		
		self.fields['cliente'].empty_label = "<<< Buscar Cliente >>>"
		self.fields['cia'].empty_label = "<<< Seleccione >>>"
		
		self.fields['moneda'].queryset = core_models.Catalogo.objects.filter(tipo_catalogo=poliza_constants.ID_MONEDA) 
		self.fields['estado_poliza'].queryset = core_models.Catalogo.objects.filter(tipo_catalogo=poliza_constants.ID_ESTADO_POLIZA) 
		self.fields['cia'].queryset = core_models.Empresa.objects.filter(giro_negocio=poliza_constants.ID_CIA) 
		#self.fields['observacion'] = forms.CharField(widget=forms.Textarea (attrs={'rows': 3,'cols': 100}))
		self.fields['cliente'].widget.attrs['id'] = "busqueda_cliente" 
		for field, campo in self.fields.iteritems():
			if field == 'fecha_inicio':
				campo.widget.attrs['class'] = 'datepicker form-control'
				campo.input_formats = ('%d/%m/%Y',)		
			else:
				if field == 'fecha_fin':
					campo.input_formats = ('%d/%m/%Y',)
					campo.widget.attrs['class'] = 'datepicker form-control'
				else:
					campo.widget.attrs['class'] = 'form-control'
  					


	class Meta:        
		model = poliza_models.Poliza
		widgets = {
		    'observacion' : forms.Textarea (attrs={ 'placeholder': 'Agregue una nota' , 'rows': 2,'cols': 100}),
		    'fecha_inicio': forms.TextInput(attrs = {'placeholder': '   Inicio Vigencia'}),
		    'fecha_fin'   : forms.TextInput(attrs = {'placeholder': '   Fin Vigencia'}),
		    'cantidad_cuotas': forms.TextInput(attrs = {'placeholder': '1'}),
		    
		}

######################

class ProductoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):

		super(ProductoForm, self).__init__(*args, **kwargs)
		padres = poliza_models.Ramo.objects.filter(ramo_superior=None)
		self.fields['ramo'].queryset = padres
		hijos=poliza_models.Ramo.objects.none()
		for padre in padres:

			temp = poliza_models.Ramo.objects.filter(ramo_superior=padre)
			hijos = hijos | temp

		self.fields['sub_ramo'].queryset = hijos
       
    class Meta:        
        model = poliza_models.Producto 


class ArchivoForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(ArchivoForm, self).__init__(*args, **kwargs)
    
	class Meta:
		model = poliza_models.Archivo


class PlanPagosForm(forms.ModelForm):
	"""docstring for  PlanPagosForm"""
	def __init__(self, *args, **kwargs):
		super( PlanPagosForm, self).__init__(*args, **kwargs)
		for field, campo in self.fields.iteritems():
			if field == 'fecha_vence' or field == 'fecha_pago' :
				campo.widget.attrs['class'] = 'datepicker form-control'
			else:
					
				campo.widget.attrs['class'] = 'form-control' 

	class Meta:
		model = poliza_models.PlanPagos 


class RiesgoForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super( RiesgoForm, self).__init__(*args, **kwargs)
		self.fields['ramo'].empty_label = "<<< Seleccione Ramo >>>"
		self.fields['sub_ramo'].empty_label = "<<< Seleccione Sub Ramo >>>"
		self.fields['producto'].empty_label = "<<< Seleccione Producto >>>"

		for field, campo in self.fields.iteritems():
			campo.widget.attrs['class'] = 'form-control'

	class Meta:

		model = poliza_models.PlanPagos 


# ================== Importar Excel ====================


class TramaForm(forms.Form):
	file_trama = forms.FileField(label='Suba su Excel') 


class IndependienteForm(forms.Form):
	file_independiente = forms.FileField(label='Suba su Excel') 


# ======================================================

	model = poliza_models.Riesgo 

class CobranzaForm(forms.Form):

	cia = forms.CharField()
	estado = forms.CharField()
	area = forms.CharField()
	vendedor = forms.CharField()
	fecha_inicio = forms.DateField(initial=datetime.today().date())
	fecha_fin = forms.DateField(initial=datetime.today().date())
	liquidacion = forms.CharField() 

	def __init__(self, *args, **kwargs):
		super(CobranzaForm, self).__init__(*args, **kwargs)
		self.fields['cia'] = forms.ModelChoiceField(core_models.Empresa.objects.filter(giro_negocio=poliza_constants.ID_CIA))
		#self.fields['estado'] = forms.ModelChoiceField(core_models.Empresa.objects.filter(giro_negocio=poliza_constants.ID_CIA))
		self.fields['area'] = forms.ModelChoiceField(core_models.Catalogo.objects.filter(tipo_catalogo=core_constants.ID_AREA_SUPERVISORA))
		self.fields['vendedor'] = forms.ModelChoiceField(administrativo_models.Empleado.objects.filter())
		for field, campo in self.fields.iteritems():
			if field == 'fecha_inicio':
				campo.widget.attrs['class'] = 'datepicker form-control'
			else:
				if field == 'fecha_fin':
					campo.widget.attrs['class'] = 'datepicker form-control'
				else:
					campo.widget.attrs['class'] = 'form-control'

