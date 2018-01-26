from django.contrib import admin
from apps.administrativo import models,forms
#from apps.core import models as core_models


class EmpleadoAdmin(admin.ModelAdmin):
    
    form = forms.EmpleadoForm

class FuncionarioAdmin(admin.ModelAdmin):
    
    form = forms.FuncionarioForm


admin.site.register(models.Empleado,EmpleadoAdmin)
admin.site.register(models.Funcionario,FuncionarioAdmin)
admin.site.register(models.Cuentas_Bancos)
admin.site.register(models.DocVenta)



