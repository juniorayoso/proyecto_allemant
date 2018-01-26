# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Empleado'
        db.create_table(u'administrativo_empleado', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('audt_usuario_creo', self.gf('django.db.models.fields.related.ForeignKey')(related_name='empleado_created_related', null=True, to=orm['auth.User'])),
            ('audt_fecha_creacion', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2015, 1, 10, 0, 0), auto_now_add=True, blank=True)),
            ('audt_activo', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('audt_fecha_modificacion', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
            ('audt_usuario_modificacion', self.gf('django.db.models.fields.related.ForeignKey')(related_name='empleado_modified_related', null=True, to=orm['auth.User'])),
            ('audt_fecha_eliminacion', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('audt_usuario_eliminacion', self.gf('django.db.models.fields.related.ForeignKey')(related_name='empleado_deleted_related', null=True, to=orm['auth.User'])),
            ('persona', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Persona'])),
            ('area_empleado', self.gf('django.db.models.fields.related.ForeignKey')(related_name='area_empleado', to=orm['core.Catalogo'])),
            ('cargo_empleado', self.gf('django.db.models.fields.related.ForeignKey')(related_name='cargo_empleado', to=orm['core.Catalogo'])),
            ('fecha_inicio', self.gf('django.db.models.fields.DateField')(null=True)),
            ('fecha_cese', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('estado_allemant', self.gf('django.db.models.fields.related.ForeignKey')(related_name='estado_allemant', to=orm['core.Catalogo'])),
        ))
        db.send_create_signal(u'administrativo', ['Empleado'])

        # Adding model 'Funcionario'
        db.create_table(u'administrativo_funcionario', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('audt_usuario_creo', self.gf('django.db.models.fields.related.ForeignKey')(related_name='funcionario_created_related', null=True, to=orm['auth.User'])),
            ('audt_fecha_creacion', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2015, 1, 10, 0, 0), auto_now_add=True, blank=True)),
            ('audt_activo', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('audt_fecha_modificacion', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
            ('audt_usuario_modificacion', self.gf('django.db.models.fields.related.ForeignKey')(related_name='funcionario_modified_related', null=True, to=orm['auth.User'])),
            ('audt_fecha_eliminacion', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('audt_usuario_eliminacion', self.gf('django.db.models.fields.related.ForeignKey')(related_name='funcionario_deleted_related', null=True, to=orm['auth.User'])),
            ('persona', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Persona'])),
            ('empresa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Empresa'])),
            ('area_funcionario', self.gf('django.db.models.fields.related.ForeignKey')(related_name='area_funcionario', to=orm['core.Catalogo'])),
            ('cargo_funcionario', self.gf('django.db.models.fields.related.ForeignKey')(related_name='cargo_funcionario', to=orm['core.Catalogo'])),
            ('estado_funcionario', self.gf('django.db.models.fields.related.ForeignKey')(related_name='estado_funcionario', to=orm['core.Catalogo'])),
        ))
        db.send_create_signal(u'administrativo', ['Funcionario'])

        # Adding model 'Cuentas_Bancos'
        db.create_table(u'administrativo_cuentas_bancos', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('audt_usuario_creo', self.gf('django.db.models.fields.related.ForeignKey')(related_name='cuentas_bancos_created_related', null=True, to=orm['auth.User'])),
            ('audt_fecha_creacion', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2015, 1, 10, 0, 0), auto_now_add=True, blank=True)),
            ('audt_activo', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('audt_fecha_modificacion', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
            ('audt_usuario_modificacion', self.gf('django.db.models.fields.related.ForeignKey')(related_name='cuentas_bancos_modified_related', null=True, to=orm['auth.User'])),
            ('audt_fecha_eliminacion', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('audt_usuario_eliminacion', self.gf('django.db.models.fields.related.ForeignKey')(related_name='cuentas_bancos_deleted_related', null=True, to=orm['auth.User'])),
            ('persona', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Persona'], null=True, blank=True)),
            ('empresa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Empresa'], null=True, blank=True)),
            ('entidad_financiera', self.gf('django.db.models.fields.related.ForeignKey')(related_name='entidad_finaciera', to=orm['core.Empresa'])),
            ('moneda', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Catalogo'], null=True)),
            ('nro_cuenta', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('nro_cuenta_cci', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'administrativo', ['Cuentas_Bancos'])

        # Adding model 'DocVenta'
        db.create_table(u'administrativo_docventa', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('audt_usuario_creo', self.gf('django.db.models.fields.related.ForeignKey')(related_name='docventa_created_related', null=True, to=orm['auth.User'])),
            ('audt_fecha_creacion', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2015, 1, 10, 0, 0), auto_now_add=True, blank=True)),
            ('audt_activo', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('audt_fecha_modificacion', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
            ('audt_usuario_modificacion', self.gf('django.db.models.fields.related.ForeignKey')(related_name='docventa_modified_related', null=True, to=orm['auth.User'])),
            ('audt_fecha_eliminacion', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('audt_usuario_eliminacion', self.gf('django.db.models.fields.related.ForeignKey')(related_name='docventa_deleted_related', null=True, to=orm['auth.User'])),
            ('numero_documento', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
            ('serie_documento', self.gf('django.db.models.fields.CharField')(unique=True, max_length=10)),
            ('tipo_documento', self.gf('django.db.models.fields.related.ForeignKey')(related_name='tipo_doc_venta', to=orm['core.Catalogo'])),
            ('persona', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Persona'], null=True, blank=True)),
            ('empresa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Empresa'], null=True, blank=True)),
            ('ruc', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('fecha_emision', self.gf('django.db.models.fields.DateTimeField')()),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('importe', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('porcentaje', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=0)),
            ('igv', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('total', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('moneda', self.gf('django.db.models.fields.related.ForeignKey')(related_name='moneda_doc', to=orm['core.Catalogo'])),
            ('son', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('estado_doc_venta', self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name='estado_doc_venta', to=orm['core.Catalogo'])),
            ('forma_pago', self.gf('django.db.models.fields.related.ForeignKey')(related_name='forma_pago', to=orm['core.Catalogo'])),
        ))
        db.send_create_signal(u'administrativo', ['DocVenta'])


    def backwards(self, orm):
        # Deleting model 'Empleado'
        db.delete_table(u'administrativo_empleado')

        # Deleting model 'Funcionario'
        db.delete_table(u'administrativo_funcionario')

        # Deleting model 'Cuentas_Bancos'
        db.delete_table(u'administrativo_cuentas_bancos')

        # Deleting model 'DocVenta'
        db.delete_table(u'administrativo_docventa')


    models = {
        u'administrativo.cuentas_bancos': {
            'Meta': {'object_name': 'Cuentas_Bancos'},
            'audt_activo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'audt_fecha_creacion': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2015, 1, 10, 0, 0)', 'auto_now_add': 'True', 'blank': 'True'}),
            'audt_fecha_eliminacion': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'audt_fecha_modificacion': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'audt_usuario_creo': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'cuentas_bancos_created_related'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'audt_usuario_eliminacion': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'cuentas_bancos_deleted_related'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'audt_usuario_modificacion': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'cuentas_bancos_modified_related'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'empresa': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Empresa']", 'null': 'True', 'blank': 'True'}),
            'entidad_financiera': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'entidad_finaciera'", 'to': u"orm['core.Empresa']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'moneda': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Catalogo']", 'null': 'True'}),
            'nro_cuenta': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'nro_cuenta_cci': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'persona': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Persona']", 'null': 'True', 'blank': 'True'})
        },
        u'administrativo.docventa': {
            'Meta': {'object_name': 'DocVenta'},
            'audt_activo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'audt_fecha_creacion': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2015, 1, 10, 0, 0)', 'auto_now_add': 'True', 'blank': 'True'}),
            'audt_fecha_eliminacion': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'audt_fecha_modificacion': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'audt_usuario_creo': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'docventa_created_related'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'audt_usuario_eliminacion': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'docventa_deleted_related'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'audt_usuario_modificacion': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'docventa_modified_related'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'empresa': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Empresa']", 'null': 'True', 'blank': 'True'}),
            'estado_doc_venta': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'related_name': "'estado_doc_venta'", 'to': u"orm['core.Catalogo']"}),
            'fecha_emision': ('django.db.models.fields.DateTimeField', [], {}),
            'forma_pago': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'forma_pago'", 'to': u"orm['core.Catalogo']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'igv': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'importe': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'moneda': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'moneda_doc'", 'to': u"orm['core.Catalogo']"}),
            'numero_documento': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'persona': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Persona']", 'null': 'True', 'blank': 'True'}),
            'porcentaje': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '0'}),
            'ruc': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'serie_documento': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '10'}),
            'son': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'tipo_documento': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'tipo_doc_venta'", 'to': u"orm['core.Catalogo']"}),
            'total': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'})
        },
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
        u'administrativo.funcionario': {
            'Meta': {'object_name': 'Funcionario'},
            'area_funcionario': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'area_funcionario'", 'to': u"orm['core.Catalogo']"}),
            'audt_activo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'audt_fecha_creacion': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2015, 1, 10, 0, 0)', 'auto_now_add': 'True', 'blank': 'True'}),
            'audt_fecha_eliminacion': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'audt_fecha_modificacion': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'audt_usuario_creo': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'funcionario_created_related'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'audt_usuario_eliminacion': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'funcionario_deleted_related'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'audt_usuario_modificacion': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'funcionario_modified_related'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'cargo_funcionario': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'cargo_funcionario'", 'to': u"orm['core.Catalogo']"}),
            'empresa': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Empresa']"}),
            'estado_funcionario': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'estado_funcionario'", 'to': u"orm['core.Catalogo']"}),
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

    complete_apps = ['administrativo']