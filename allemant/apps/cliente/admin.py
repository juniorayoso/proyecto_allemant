from django.contrib import admin
from apps.cliente import models 
# Register your models here.

admin.site.register(models.Cliente)
admin.site.register(models.TipoPerfil)
admin.site.register(models.CatalogoPerfil)
admin.site.register(models.Perfil)