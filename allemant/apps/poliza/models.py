 # -*- coding: utf-8 -*-
from __future__ import absolute_import
import os
from django.db import models
from apps.core import models as core_models
from apps.cliente import models as cliente_models
from datetime import datetime


class Ramo(core_models.AuditableModel):

    ramo_superior = models.ForeignKey('self',null=True,blank=True,related_name='padre')
    descripcion = models.CharField(max_length=50)

    class Meta:
		verbose_name = 'Ramo'
		verbose_name_plural = 'Ramos' 

    def __unicode__(self):
		self.descripcion.encode('utf-8')
		return unicode(self.descripcion)

class Producto(core_models.AuditableModel):
    ramo = models.ForeignKey(Ramo, related_name='ramo')
    sub_ramo = models.ForeignKey(Ramo, related_name='sub_ramo')
    comision = models.DecimalField(max_digits=10, decimal_places=2)
    cia = models.ForeignKey(core_models.Empresa)
    nombre = models.CharField(max_length=50)

    class Meta:
		verbose_name = 'Producto'
		verbose_name_plural = 'Productos'

    def __unicode__(self):
		self.nombre.encode('utf-8')
		return unicode(self.nombre)

class Poliza(core_models.AuditableModel):

	numero_poliza = models.CharField(max_length=50, unique=True)
	cliente = models.ForeignKey(cliente_models.Cliente,null=True, blank=True)
	cia = models.ForeignKey(core_models.Empresa,null=True, blank=True)
	fecha_inicio = models.DateTimeField('fecha_inicio_cobertura')
	fecha_fin = models.DateTimeField('fecha_fin_cobertura')
	fecha_ingreso = models.DateTimeField('fecha_registro_poliza',auto_now_add=True,
            default=datetime.now(), editable=False)  
	materia_asegurado = models.DecimalField(max_digits=20, decimal_places=2)
	prima = models.DecimalField(max_digits=10, decimal_places=2)
	cantidad_cuotas = models.IntegerField(null=True, blank=True,default=1)
	moneda = models.ForeignKey(core_models.Catalogo, null=True, related_name='moneda',default=1)
	observacion = models.CharField(max_length=300,null=True, blank=True)		
	estado_poliza = models.ForeignKey(core_models.Catalogo, related_name='estado_poliza',default=1)


	class Meta:
		verbose_name = 'Poliza'
		verbose_name_plural = 'Polizas'

	def __unicode__(self):
		return str(self.numero_poliza)

class PlanPagos(core_models.AuditableModel):
	poliza = models.ForeignKey(Poliza,null=True, blank=True)
	numero_cuota = models.IntegerField()
	monto = models.DecimalField(max_digits=10, decimal_places=2)
	fecha_vence = models.DateField() 
	fecha_pago = models.DateField(null=True, blank=True) 
	numero_cupon = models.CharField(max_length=15,null=True, blank=True)
	banco = models.ForeignKey(core_models.Empresa,null=True, blank=True)
	numero_voucher = models.CharField(max_length=20,null=True, blank=True)

	class Meta:
		verbose_name = 'Plan Pago'
		verbose_name_plural = 'Plan Pagos'


	def __unicode__(self):
		return str(self.numero_cuota)

def get_upload_path(instance, filename):
	
   	file_name = "archivos/poliza/" + instance.poliza.numero_poliza + "/"
	if not os.path.exists(file_name):
		os.makedirs(file_name)

	return file_name + filename

class Archivo(models.Model):

	poliza = models.ForeignKey(Poliza,null=True, blank=True)
	archivo = models.FileField(upload_to=get_upload_path)
	observacion = models.CharField(max_length=100,null=True, blank=True)

	class Meta:
		verbose_name = 'Archivo'
		verbose_name_plural = 'Archivos'

	def __unicode__(self):
		return u'poliza : %s == archivo : %s' %(self.poliza, self.archivo)		


# ======================= Importar Excel ========================

class ImportarTrama(models.Model):

	codigo_t = models.CharField(max_length=50)
	nombre_t = models.CharField(max_length=50)
	fecha_t = models.DateField()
	poliza_trama = models.ForeignKey(Poliza, related_name='trama_poliza')

	class Meta:
		verbose_name = 'Importar Trama'
		verbose_name_plural = 'Importar Tramas'


class ImportarDependiente(models.Model):

	fila = models.CharField(max_length=15)
	label = models.CharField(max_length=50, blank=True, null=True)
	valor = models.CharField(max_length=70)
	# nombre_d = models.CharField(max_length=50)
	# fecha_d = models.DateField()
	poliza_independiente = models.ForeignKey(Poliza, related_name='independiente_poliza')


	class Meta:
		verbose_name = 'Importar Dependiente'
		verbose_name_plural = 'Importar Dependientes'


# ===============================================================

class Riesgo(models.Model):

	poliza = models.ForeignKey(Poliza)
	tipo_riesgo = models.ForeignKey(Ramo,related_name='ramo_pp')
	ramo = models.ForeignKey(Ramo, related_name='ramo_p')
	sub_ramo = models.ForeignKey(Ramo, null=True, blank=True, related_name='ramo_h')
	producto = models.ForeignKey(Producto, null=True, blank=True , related_name='producto') 
	materia_asegurada = models.DecimalField(max_digits=20, decimal_places=2)
	prima = models.DecimalField(max_digits=20, decimal_places=2)

	def __unicode__(self):
		return self.tipo_riesgo+"/"+self.ramo 



