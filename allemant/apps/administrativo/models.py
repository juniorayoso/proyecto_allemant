from django.db import models
from apps.core import models as core_models
from datetime import datetime

# Create your models here.

class Empleado(core_models.AuditableModel):
    persona = models.ForeignKey(core_models.Persona)
    area_empleado =  models.ForeignKey(core_models.Catalogo ,related_name="area_empleado")
    cargo_empleado =  models.ForeignKey(core_models.Catalogo ,related_name="cargo_empleado")
    fecha_inicio = models.DateField(null=True)
    fecha_cese = models.DateField(null=True,blank=True)
    estado_allemant = models.ForeignKey(core_models.Catalogo ,related_name="estado_allemant")

    def __unicode__(self):
        return  self.persona.nombre



class Funcionario(core_models.AuditableModel):
	persona = models.ForeignKey(core_models.Persona)
	empresa = models.ForeignKey(core_models.Empresa)
	area_funcionario = models.ForeignKey(core_models.Catalogo, related_name="area_funcionario")
	cargo_funcionario = models.ForeignKey(core_models.Catalogo, related_name="cargo_funcionario")
	estado_funcionario = models.ForeignKey(core_models.Catalogo, related_name="estado_funcionario")
	def __unicode__(self):
         return self.persona.nombre+" " +self.persona.apellido



class Cuentas_Bancos(core_models.AuditableModel):
	persona = models.ForeignKey(core_models.Persona,null=True,blank=True)
	empresa = models.ForeignKey(core_models.Empresa,null=True,blank=True)
	entidad_financiera = models.ForeignKey(core_models.Empresa,  related_name="entidad_finaciera")
	moneda = models.ForeignKey(core_models.Catalogo, null=True)
	nro_cuenta = models.CharField(max_length=20)
	nro_cuenta_cci = models.CharField(max_length=30)
  
	def __unicode__(self):
         return self.nro_cuenta+" " +self.empresa.razon_social+" " +self.empresa_entidad_financiera.razon_social
 

class DocVenta(core_models.AuditableModel):
	numero_documento = models.CharField(max_length=50, unique=True)
	serie_documento = models.CharField(max_length=10, unique=True)
	tipo_documento = models.ForeignKey(core_models.Catalogo,related_name="tipo_doc_venta")
	persona = models.ForeignKey(core_models.Persona,null=True,blank=True)
	empresa = models.ForeignKey(core_models.Empresa,null=True,blank=True)
	ruc = models.CharField(max_length=20,null=True,blank=True)
	fecha_emision = models.DateTimeField()
	descripcion = models.CharField(max_length=300,null=True, blank=True)
	importe = models.DecimalField(max_digits=10, decimal_places=2)
	porcentaje = models.DecimalField(max_digits=10, decimal_places=0)
	igv = models.DecimalField(max_digits=10, decimal_places=2)
	total = models.DecimalField(max_digits=10, decimal_places=2)
	moneda = models.ForeignKey(core_models.Catalogo, related_name='moneda_doc')
	son = models.CharField(max_length=300,null=True, blank=True)
	estado_doc_venta = models.ForeignKey(core_models.Catalogo, related_name='estado_doc_venta',default=1)
	forma_pago = models.ForeignKey(core_models.Catalogo, related_name='forma_pago')

	def __unicode__(self):
		if self.empresa:
			return str(self.numero_documento)+" " +self.empresa.razon_social
		else:
			return str(self.numero_documento)+" " +self.persona.nombre+" " +self.persona.apellido
