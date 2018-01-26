from django import forms
from apps.cliente import models,constants
from apps.core import models as core_models


class ClienteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
		super(ClienteForm, self).__init__(*args, **kwargs)
		self.fields['grupo_economico'].queryset = core_models.Catalogo.objects.filter(tipo_catalogo=constants.ID_GRUPO_ECONOMICO)  
		self.fields['supervisor'].queryset = core_models.Catalogo.objects.filter(tipo_catalogo=constants.ID_SUPERVISOR)   
		self.fields['ejecutivo'].queryset = core_models.Catalogo.objects.filter(tipo_catalogo=constants.ID_EJECUTIVO)   
		self.fields['estado'].queryset = core_models.Catalogo.objects.filter(tipo_catalogo=constants.ID_ESTADO)   

		for field, campo in self.fields.iteritems():
			campo.widget.attrs['class'] = 'form-control'

    class Meta:        
        model = models.Cliente 
        widgets = {
     		'descripcion' : forms.Textarea (attrs={ 'placeholder': 'Agregue una nota' , 'rows': 3,'cols': 100}),}



class PerfilForm(forms.ModelForm):

	catalogo_p1 = forms.ModelChoiceField(queryset=models.CatalogoPerfil.objects.none(), widget=forms.RadioSelect)
	catalogo_p2 = forms.ModelChoiceField(queryset=models.CatalogoPerfil.objects.none(), widget=forms.RadioSelect)
	catalogo_p3 = forms.ModelChoiceField(queryset=models.CatalogoPerfil.objects.none(), widget=forms.RadioSelect)
	catalogo_p4 = forms.ModelChoiceField(queryset=models.CatalogoPerfil.objects.none(), widget=forms.RadioSelect)


	def __init__(self, *args, **kwargs):
		
		# se le esta pasando el parametro cliente con el valor none por default
		cliente = kwargs.pop('cliente', None)

		super(PerfilForm, self).__init__(*args, **kwargs)

		# if cliente:
		# 	print 'entro a cliente'
			# self.fields['cliente_p'].empty_label = None 
		self.fields['cliente_p'].widget = forms.HiddenInput() 
		self.fields['cliente_p'].initial = cliente

		self.fields['catalogo_p1'].queryset = models.CatalogoPerfil.objects.filter(tipo_p=constants.ID_1RO, activate=True)
		self.fields['catalogo_p1'].empty_label = None 

		self.fields['catalogo_p2'].queryset = models.CatalogoPerfil.objects.filter(tipo_p=constants.ID_2DO, activate=True)
		self.fields['catalogo_p2'].empty_label = None 

		self.fields['catalogo_p3'].queryset = models.CatalogoPerfil.objects.filter(tipo_p=constants.ID_3RO, activate=True)
		self.fields['catalogo_p3'].empty_label = None 

		self.fields['catalogo_p4'].queryset = models.CatalogoPerfil.objects.filter(tipo_p=constants.ID_4TO, activate=True)
		self.fields['catalogo_p4'].empty_label = None 


	class Meta:
		model = models.Perfil


	def clean(self):
		cleaned_data = self.cleaned_data
		cliente_p = cleaned_data.get('cliente_p')
		print "cleaned_data cliente es : %s" %cliente_p
		return super(PerfilForm, self).clean()