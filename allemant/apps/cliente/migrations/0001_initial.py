# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Cliente'
        db.create_table(u'cliente_cliente', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('audt_usuario_creo', self.gf('django.db.models.fields.related.ForeignKey')(related_name='cliente_created_related', null=True, to=orm['auth.User'])),
            ('audt_fecha_creacion', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2015, 1, 10, 0, 0), auto_now_add=True, blank=True)),
            ('audt_activo', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('audt_fecha_modificacion', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
            ('audt_usuario_modificacion', self.gf('django.db.models.fields.related.ForeignKey')(related_name='cliente_modified_related', null=True, to=orm['auth.User'])),
            ('audt_fecha_eliminacion', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('audt_usuario_eliminacion', self.gf('django.db.models.fields.related.ForeignKey')(related_name='cliente_deleted_related', null=True, to=orm['auth.User'])),
            ('persona', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Persona'], null=True, blank=True)),
            ('empresa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Empresa'], null=True, blank=True)),
            ('estado', self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name='estado', null=True, to=orm['core.Catalogo'])),
            ('grupo_economico', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='grupo_economico', null=True, to=orm['core.Catalogo'])),
            ('ejecutivo', self.gf('django.db.models.fields.related.ForeignKey')(related_name='area_ejecutiva', null=True, to=orm['core.Catalogo'])),
            ('area', self.gf('django.db.models.fields.related.ForeignKey')(related_name='area_supervisora', null=True, to=orm['core.Catalogo'])),
            ('supervisor', self.gf('django.db.models.fields.related.ForeignKey')(related_name='supervisor', null=True, to=orm['core.Catalogo'])),
            ('vendedor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['administrativo.Empleado'], null=True, blank=True)),
            ('clasificacion', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='clasificacion_cliente', null=True, to=orm['core.Catalogo'])),
            ('descripcion', self.gf('django.db.models.fields.TextField')(max_length=300, null=True, blank=True)),
        ))
        db.send_create_signal(u'cliente', ['Cliente'])

        # Adding model 'TipoPerfil'
        db.create_table(u'cliente_tipoperfil', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('activate', self.gf('django.db.models.fields.BooleanField')()),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'cliente', ['TipoPerfil'])

        # Adding model 'CatalogoPerfil'
        db.create_table(u'cliente_catalogoperfil', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('activate', self.gf('django.db.models.fields.BooleanField')()),
            ('nombre_c', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('tipo_p', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cliente.TipoPerfil'])),
        ))
        db.send_create_signal(u'cliente', ['CatalogoPerfil'])

        # Adding model 'Perfil'
        db.create_table(u'cliente_perfil', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('catalogo_p1', self.gf('django.db.models.fields.related.ForeignKey')(related_name='catalogo_p1', null=True, to=orm['cliente.CatalogoPerfil'])),
            ('catalogo_p2', self.gf('django.db.models.fields.related.ForeignKey')(related_name='catalogo_p2', null=True, to=orm['cliente.CatalogoPerfil'])),
            ('catalogo_p3', self.gf('django.db.models.fields.related.ForeignKey')(related_name='catalogo_p3', null=True, to=orm['cliente.CatalogoPerfil'])),
            ('catalogo_p4', self.gf('django.db.models.fields.related.ForeignKey')(related_name='catalogo_p4', null=True, to=orm['cliente.CatalogoPerfil'])),
            ('cliente_p', self.gf('django.db.models.fields.related.ForeignKey')(related_name='cliente_perfil', to=orm['cliente.Cliente'])),
            ('descripcion', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'cliente', ['Perfil'])


    def backwards(self, orm):
        # Deleting model 'Cliente'
        db.delete_table(u'cliente_cliente')

        # Deleting model 'TipoPerfil'
        db.delete_table(u'cliente_tipoperfil')

        # Deleting model 'CatalogoPerfil'
        db.delete_table(u'cliente_catalogoperfil')

        # Deleting model 'Perfil'
        db.delete_table(u'cliente_perfil')


    models = {
        u'administrativo.empleado': {
            'Meta': {'object_name': 'Empleado'},
            'area_empleado': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'area_empleado'", 'to': u"orm['core.Catalogo']"}),
            'audt_activo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'audt_fecha_creacion': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2015, 1, 10, 0, 0)', 'auto_now_add': 'True', 'blank': 'True'}),
            'audt_fecha_eliminacion': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'audt_fecha_modificacion': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'audt_usuario_creo': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'empleado_created_related'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'audt_usuario_eliminacion': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'empleado_deleted_related'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'audt_usuario_modificacion': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'empleado_modified_related'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'cargo_empleado': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'cargo_empleado'", 'to': u"orm['core.Catalogo']"}),
            'estado_allemant': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'estado_allemant'", 'to': u"orm['core.Catalogo']"}),
            'fecha_cese': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'fecha_inicio': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'persona': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Persona']"})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'cliente.catalogoperfil': {
            'Meta': {'object_name': 'CatalogoPerfil'},
            'activate': ('django.db.models.fields.BooleanField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre_c': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'tipo_p': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cliente.TipoPerfil']"})
        },
        u'cliente.cliente': {
            'Meta': {'object_name': 'Cliente'},
            'area': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'area_supervisora'", 'null': 'True', 'to': u"orm['core.Catalogo']"}),
            'audt_activo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'audt_fecha_creacion': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2015, 1, 10, 0, 0)', 'auto_now_add': 'True', 'blank': 'True'}),
            'audt_fecha_eliminacion': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'audt_fecha_modificacion': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'audt_usuario_creo': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'cliente_created_related'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'audt_usuario_eliminacion': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'cliente_deleted_related'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'audt_usuario_modificacion': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'cliente_modified_related'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'clasificacion': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'clasificacion_cliente'", 'null': 'True', 'to': u"orm['core.Catalogo']"}),
            'descripcion': ('django.db.models.fields.TextField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'ejecutivo': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'area_ejecutiva'", 'null': 'True', 'to': u"orm['core.Catalogo']"}),
            'empresa': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Empresa']", 'null': 'True', 'blank': 'True'}),
            'estado': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'related_name': "'estado'", 'null': 'True', 'to': u"orm['core.Catalogo']"}),
            'grupo_economico': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'grupo_economico'", 'null': 'True', 'to': u"orm['core.Catalogo']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'persona': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Persona']", 'null': 'True', 'blank': 'True'}),
            'supervisor': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'supervisor'", 'null': 'True', 'to': u"orm['core.Catalogo']"}),
            'vendedor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['administrativo.Empleado']", 'null': 'True', 'blank': 'True'})
        },
        u'cliente.perfil': {
            'Meta': {'object_name': 'Perfil'},
            'catalogo_p1': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'catalogo_p1'", 'null': 'True', 'to': u"orm['cliente.CatalogoPerfil']"}),
            'catalogo_p2': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'catalogo_p2'", 'null': 'True', 'to': u"orm['cliente.CatalogoPerfil']"}),
            'catalogo_p3': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'catalogo_p3'", 'null': 'True', 'to': u"orm['cliente.CatalogoPerfil']"}),
            'catalogo_p4': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'catalogo_p4'", 'null': 'True', 'to': u"orm['cliente.CatalogoPerfil']"}),
            'cliente_p': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'cliente_perfil'", 'to': u"orm['cliente.Cliente']"}),
            'descripcion': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'cliente.tipoperfil': {
            'Meta': {'object_name': 'TipoPerfil'},
            'activate': ('django.db.models.fields.BooleanField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'core.catalogo': {
            'Meta': {'object_name': 'Catalogo'},
            'abreviatura': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'dato': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tipo_catalogo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.TipoCatalogo']"}),
            'tipo_dato': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'valor1': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'valor2': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'})
        },
        u'core.empresa': {
            'Meta': {'object_name': 'Empresa'},
            'audt_activo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'audt_fecha_creacion': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2015, 1, 10, 0, 0)', 'auto_now_add': 'True', 'blank': 'True'}),
            'audt_fecha_eliminacion': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'audt_fecha_modificacion': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'audt_usuario_creo': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'empresa_created_related'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'audt_usuario_eliminacion': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'empresa_deleted_related'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'audt_usuario_modificacion': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'empresa_modified_related'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'giro_negocio': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'giro'", 'null': 'True', 'to': u"orm['core.Catalogo']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'razon_social': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'ruc': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'core.persona': {
            'Meta': {'object_name': 'Persona'},
            'apellido': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'audt_activo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'audt_fecha_creacion': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2015, 1, 10, 0, 0)', 'auto_now_add': 'True', 'blank': 'True'}),
            'audt_fecha_eliminacion': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'audt_fecha_modificacion': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'audt_usuario_creo': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'persona_created_related'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'audt_usuario_eliminacion': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'persona_deleted_related'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'audt_usuario_modificacion': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'persona_modified_related'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'dni': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '15'}),
            'estado_civil': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'estado_civil'", 'to': u"orm['core.Catalogo']"}),
            'fecha_nacimiento': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'sexo': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sexo'", 'to': u"orm['core.Catalogo']"})
        },
        u'core.tipocatalogo': {
            'Meta': {'object_name': 'TipoCatalogo'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['cliente']