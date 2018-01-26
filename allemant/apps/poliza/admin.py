from django.contrib import admin
from apps.poliza import models,forms
# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    
    form = forms.ProductoForm

admin.site.register(models.Poliza)
admin.site.register(models.Archivo)
admin.site.register(models.Ramo)
admin.site.register(models.Riesgo)
admin.site.register(models.Producto,ProductoAdmin)
admin.site.register(models.PlanPagos)
