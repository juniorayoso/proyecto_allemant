from __future__ import absolute_import

from django.db import models
from django.contrib.auth import models as auth_models
from datetime import datetime

# Create your models here.
class AuditableModel(models.Model):
    audt_usuario_creo = models.ForeignKey(auth_models.User,
            editable=False,
            null=True,
            related_name="%(class)s_created_related")
    audt_fecha_creacion = models.DateTimeField(auto_now_add=True,
            default=datetime.now(), editable=False)
    
    audt_activo = models.BooleanField(default=True,editable=False) #registro act/desact

    audt_fecha_modificacion = models.DateTimeField(auto_now=True, editable=False,
            null=True)
    audt_usuario_modificacion = models.ForeignKey(auth_models.User,
            editable=False,
            null=True,
            related_name="%(class)s_modified_related")
    audt_fecha_eliminacion = models.DateTimeField(editable=False, null=True)
    audt_usuario_eliminacion = models.ForeignKey(auth_models.User,
            editable=False,
            null=True,
            related_name="%(class)s_deleted_related")
    
    class Meta:
        """Meta class for AuditableModel"""
        abstract = True

class TipoCatalogo(models.Model):

    nombre = models.CharField(max_length=30)
    
    def __unicode__(self):
        return self.nombre 

class Catalogo(models.Model):

    tipo_catalogo = models.ForeignKey(TipoCatalogo)
    tipo_dato = models.CharField(max_length=5)
    dato = models.CharField(max_length=100)
    abreviatura = models.CharField(max_length=5,null=True,blank=True)
    valor1 = models.CharField(max_length=30,null=True,blank=True)
    valor2 = models.CharField(max_length=30,null=True,blank=True)
    
    def __unicode__(self):
        return self.dato


class Persona(AuditableModel):

    dni = models.CharField(max_length=15,unique=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    estado_civil = models.ForeignKey(Catalogo, related_name="estado_civil")
    fecha_nacimiento = models.DateField(null=True)
    sexo = models.ForeignKey(Catalogo, related_name="sexo")

    def __unicode__(self):
        return self.nombre +" " + self.apellido

class Empresa(AuditableModel):

    ruc = models.CharField(max_length=20)
    razon_social = models.CharField(max_length=50)
    giro_negocio = models.ForeignKey(Catalogo,related_name='giro',null=True)

    def __unicode__(self):
        return self.razon_social


class Ubigeo(models.Model):
   departamento = models.CharField(max_length=30)
   provincia = models.CharField(max_length=30)

   def __unicode__(self):
       return self.departamento+"/"+self.provincia


class Distrito(models.Model):

   ubigeo = models.ForeignKey(Ubigeo)
   nombre = models.CharField(max_length=30)

   def __unicode__(self):
       return self.nombre

class Direccion(models.Model):

    persona = models.ForeignKey(Persona,null=True,blank=True) 
    empresa = models.ForeignKey(Empresa,null=True,blank=True)
    av_calle = models.CharField(max_length=40)
    interior = models.CharField(max_length=20)
    ubigeo = models.ForeignKey(Ubigeo)
    distrito = models.ForeignKey(Distrito)

    def __unicode__(self):
        return self.av_calle + "-" +self.interior

   
class Telefono(models.Model):

    numero = models.CharField(max_length=15)
    operador = models.ForeignKey(Catalogo ,related_name="operador")
    persona= models.ForeignKey(Persona,null=True,blank=True) 
    empresa= models.ForeignKey(Empresa,null=True,blank=True)
    def __unicode__(self):
        return self.numero
        

class Email(models.Model):

    tipo = models.ForeignKey(Catalogo,null=True,blank=True)
    email = models.EmailField()
    persona= models.ForeignKey(Persona,null=True,blank=True) 
    empresa = models.ForeignKey(Empresa,null=True,blank=True)

    def __unicode__(self):
        return self.email


