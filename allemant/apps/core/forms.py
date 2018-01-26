# -- coding: utf-8 --
from django import forms
from apps.core import models, constants


class PersonaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PersonaForm, self).__init__(*args, **kwargs)
        self.fields['sexo'].queryset = models.Catalogo.objects.filter(tipo_catalogo=constants.ID_SEXO)
        self.fields['estado_civil'].queryset = models.Catalogo.objects.filter(tipo_catalogo=constants.ID_ESTADO_CIVIL)
 
        
        for field, campo in self.fields.iteritems():
        	if field=='fecha_nacimiento':
        		campo.widget.attrs['class'] = 'datepicker form-control' 
        	else:
        		campo.widget.attrs['class'] = 'form-control'
    class Meta:        
        model = models.Persona
        
class DireccionForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		kwargs['initial'] = {'distrito':1,'ubigeo':1}
		super(DireccionForm, self).__init__(*args, **kwargs) 
		self.fields['av_calle'].widget.attrs['placeholder'] = "Avenida/Calle"  
		self.fields['interior'].widget.attrs['placeholder'] = "#/Dpto/Oficina/Interior"  
		for field, campo in self.fields.iteritems():
			campo.widget.attrs['class'] = 'form-control'
    
	class Meta:        
		model = models.Direccion
		fields = ('ubigeo','distrito','av_calle','interior')

class TelefonoForm(forms.ModelForm):
	
	def __init__(self, *args, **kwargs):
		super(TelefonoForm, self).__init__(*args, **kwargs)

		self.fields['numero'].widget.attrs['placeholder'] = 'Número'
		self.fields['operador'].empty_label = '<< Seleccione >>'

		self.fields['operador'].queryset = models.Catalogo.objects.filter(tipo_catalogo=constants.ID_OPERADOR)  
		for field, campo in self.fields.iteritems():
			campo.widget.attrs['class'] = 'form-control'	
    
	class Meta:        
		model = models.Telefono
		fields = ('numero','operador')
		

class EmailForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(EmailForm, self).__init__(*args, **kwargs)  
		self.fields['email'].widget.attrs['placeholder'] = "Ingrese e-mail" 
		for field, campo in self.fields.iteritems():
			campo.widget.attrs['class'] = 'form-control'
    
	class Meta:        
		model = models.Email
		fields = ['email']



class EmpresaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):

       super(EmpresaForm, self).__init__(*args, **kwargs)
       self.fields['giro_negocio'].queryset = models.Catalogo.objects.filter(tipo_catalogo=constants.ID_GIRO_NEGOCIO)
       for field, campo in self.fields.iteritems():
               campo.widget.attrs['class']='form-control'

    class Meta:        
        model = models.Empresa 
        
