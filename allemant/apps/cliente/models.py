from __future__ import absolute_import
from django.db import models
from apps.core import models as core_models
from apps.administrativo import models as administrativo_models


# Create your models here.

class Cliente(core_models.AuditableModel):

	persona = models.ForeignKey(core_models.Persona,null=True,blank=True)
	empresa = models.ForeignKey(core_models.Empresa,null=True,blank=True)
	estado = models.ForeignKey(core_models.Catalogo, related_name="estado",null=True, default=1)
	grupo_economico = models.ForeignKey(core_models.Catalogo, related_name="grupo_economico",null=True,blank=True)
	ejecutivo = models.ForeignKey(core_models.Catalogo, related_name="area_ejecutiva",null=True)
	area = models.ForeignKey(core_models.Catalogo, related_name="area_supervisora",null=True)
	supervisor = models.ForeignKey(core_models.Catalogo, related_name="supervisor",null=True)
	vendedor = models.ForeignKey(administrativo_models.Empleado,null=True,blank=True)
	clasificacion =  models.ForeignKey(core_models.Catalogo,related_name="clasificacion_cliente",null=True,blank=True)
	descripcion =  models.TextField(max_length = 300,null=True,blank=True)


	class Meta:
		verbose_name = 'Cliente'
		verbose_name_plural = 'Clientes'
	
	def __unicode__(self):

		if self.empresa:
			return self.empresa.razon_social
		else:
			return self.persona.nombre+" " +self.persona.apellido



#  =========================== Perfil ==============================


class TipoPerfil(models.Model):
	activate = models.BooleanField()
	nombre = models.CharField(max_length=200)


	class Meta:
		verbose_name = 'Tipo Perfil'
		verbose_name_plural = 'Tipo Perfiles'

	def __unicode__(self):
		return u'%s' %self.nombre


class CatalogoPerfil(models.Model):
	activate = models.BooleanField()
	nombre_c = models.CharField(max_length=200)	
	tipo_p = models.ForeignKey(TipoPerfil)

	class Meta:
		verbose_name = 'Catalogo Perfil'
		verbose_name_plural = 'Catalogo Perfiles'


	def __unicode__(self):
		return u'%s' %self.nombre_c


class Perfil(models.Model):
	# activate = models.BooleanField()
	catalogo_p1 = models.ForeignKey(CatalogoPerfil, related_name='catalogo_p1', null=True)
	catalogo_p2 = models.ForeignKey(CatalogoPerfil, related_name='catalogo_p2', null=True)
	catalogo_p3 = models.ForeignKey(CatalogoPerfil, related_name='catalogo_p3', null=True)
	catalogo_p4 = models.ForeignKey(CatalogoPerfil, related_name='catalogo_p4', null=True)
	cliente_p = models.ForeignKey(Cliente, related_name='cliente_perfil')
	descripcion = models.TextField()

	class Meta:
		verbose_name = 'Perfil'
		verbose_name_plural = 'Perfiles'


	def __unicode__(self):
		return u'%s' %self.cliente_p.persona
	# 	return self.cliente_p.persona.nombre+" " +self.persona.apellido


#  =================================================================