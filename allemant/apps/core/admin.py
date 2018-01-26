from django.contrib import admin
from apps.core import models ,forms
# Register your models here.

class TipoCatalogoAdmin(admin.ModelAdmin):
	search_fields = ['nombre']
	list_display = ("id", "nombre")

class CatalogoAdmin(admin.ModelAdmin):
	search_fields = ['dato']
	list_display = ("id", "tipo_catalogo" , "tipo_dato" , "dato" , "abreviatura" , "valor1" , "valor2" )


class EmpresaAdmin(admin.ModelAdmin):
    
    form = forms.EmpresaForm



admin.site.register(models.TipoCatalogo,TipoCatalogoAdmin)
admin.site.register(models.Catalogo,CatalogoAdmin)
admin.site.register(models.Persona)
admin.site.register(models.Empresa,EmpresaAdmin)
admin.site.register(models.Ubigeo)
admin.site.register(models.Distrito)
admin.site.register(models.Direccion)
admin.site.register(models.Telefono)
admin.site.register(models.Email)







