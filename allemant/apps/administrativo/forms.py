# -- coding: utf-8 --

from django import forms
from apps.core import models as core_models
from apps.administrativo import models 
from apps.administrativo import constants 


class EmpleadoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):

       super(EmpleadoForm, self).__init__(*args, **kwargs)
       self.fields['area_empleado'].queryset = core_models.Catalogo.objects.filter(tipo_catalogo=constants.ID_AREA_EMPLEADO)
       self.fields['cargo_empleado'].queryset = core_models.Catalogo.objects.filter(tipo_catalogo=constants.ID_CARGO_EMPLEADO)
       self.fields['estado_allemant'].queryset = core_models.Catalogo.objects.filter(tipo_catalogo=constants.ID_ESTADO_EMPLEADO)

    class Meta:        
        model = models.Empleado 


class FuncionarioForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):

       super(FuncionarioForm, self).__init__(*args, **kwargs)
       self.fields['area_funcionario'].queryset = core_models.Catalogo.objects.filter(tipo_catalogo=constants.ID_AREA_FUNCIONARIO)
       self.fields['cargo_funcionario'].queryset = core_models.Catalogo.objects.filter(tipo_catalogo=constants.ID_CARGO_FUNCIONARIO)
       self.fields['estado_funcionario'].queryset = core_models.Catalogo.objects.filter(tipo_catalogo=constants.ID_ESTADO_FUNCIONARIO)

    class Meta:        
        model = models.Funcionario 


class DocVentaForm(forms.ModelForm):
  
    def __init__(self, *args, **kwargs):
      super(DocVentaForm, self).__init__(*args, **kwargs)
      self.fields['persona'].empty_label = "Persona"
      self.fields['empresa'].empty_label = "Empresa"
      self.fields['moneda'].empty_label = "Seleccione Moneda "
    
      self.fields['moneda'].queryset = core_models.Catalogo.objects.filter(tipo_catalogo=constants.ID_MONEDA) 
      
      #self.fields['cliente'].widget.attrs['id'] = "busqueda_persona" 
      #self.fields['cliente'].widget.attrs['id'] = "busqueda_empresa"

      for field, campo in self.fields.iteritems():
        if field == 'fecha_emision':
          campo.widget.attrs['class'] = 'datepicker form-control'
          campo.input_formats = ('%d/%m/%Y',) 
        else:
          campo.widget.attrs['class'] = 'form-control'

    class Meta:        
        model = models.DocVenta
        widgets = {
            'descripcion' : forms.Textarea (attrs={ 'placeholder': 'Agregue el detalle' , 'rows': 5,'cols': 100}),
        }
