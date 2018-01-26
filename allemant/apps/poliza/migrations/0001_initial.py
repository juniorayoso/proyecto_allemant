# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Ramo'
        db.create_table(u'poliza_ramo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('audt_usuario_creo', self.gf('django.db.models.fields.related.ForeignKey')(related_name='ramo_created_related', null=True, to=orm['auth.User'])),
            ('audt_fecha_creacion', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2015, 1, 10, 0, 0), auto_now_add=True, blank=True)),
            ('audt_activo', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('audt_fecha_modificacion', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
            ('audt_usuario_modificacion', self.gf('django.db.models.fields.related.ForeignKey')(related_name='ramo_modified_related', null=True, to=orm['auth.User'])),
            ('audt_fecha_eliminacion', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('audt_usuario_eliminacion', self.gf('django.db.models.fields.related.ForeignKey')(related_name='ramo_deleted_related', null=True, to=orm['auth.User'])),
            ('ramo_superior', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='padre', null=True, to=orm['poliza.Ramo'])),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'poliza', ['Ramo'])

        # Adding model 'Producto'
        db.create_table(u'poliza_producto', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('audt_usuario_creo', self.gf('django.db.models.fields.related.ForeignKey')(related_name='producto_created_related', null=True, to=orm['auth.User'])),
            ('audt_fecha_creacion', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2015, 1, 10, 0, 0), auto_now_add=True, blank=True)),
            ('audt_activo', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('audt_fecha_modificacion', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
            ('audt_usuario_modificacion', self.gf('django.db.models.fields.related.ForeignKey')(related_name='producto_modified_related', null=True, to=orm['auth.User'])),
            ('audt_fecha_eliminacion', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('audt_usuario_eliminacion', self.gf('django.db.models.fields.related.ForeignKey')(related_name='producto_deleted_related', null=True, to=orm['auth.User'])),
            ('ramo', self.gf('django.db.models.fields.related.ForeignKey')(related_name='ramo', to=orm['poliza.Ramo'])),
            ('sub_ramo', self.gf('django.db.models.fields.related.ForeignKey')(related_name='sub_ramo', to=orm['poliza.Ramo'])),
            ('comision', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('cia', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Empresa'])),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'poliza', ['Producto'])

        # Adding model 'Poliza'
        db.create_table(u'poliza_poliza', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('audt_usuario_creo', self.gf('django.db.models.fields.related.ForeignKey')(related_name='poliza_created_related', null=True, to=orm['auth.User'])),
            ('audt_fecha_creacion', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2015, 1, 10, 0, 0), auto_now_add=True, blank=True)),
            ('audt_activo', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('audt_fecha_modificacion', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
            ('audt_usuario_modificacion', self.gf('django.db.models.fields.related.ForeignKey')(related_name='poliza_modified_related', null=True, to=orm['auth.User'])),
            ('audt_fecha_eliminacion', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('audt_usuario_eliminacion', self.gf('django.db.models.fields.related.ForeignKey')(related_name='poliza_deleted_related', null=True, to=orm['auth.User'])),
            ('numero_poliza', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
            ('cliente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cliente.Cliente'], null=True, blank=True)),
            ('cia', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Empresa'], null=True, blank=True)),
            ('fecha_inicio', self.gf('django.db.models.fields.DateTimeField')()),
            ('fecha_fin', self.gf('django.db.models.fields.DateTimeField')()),
            ('fecha_ingreso', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2015, 1, 10, 0, 0), auto_now_add=True, blank=True)),
            ('materia_asegurado', self.gf('django.db.models.fields.DecimalField')(max_digits=20, decimal_places=2)),
            ('prima', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('cantidad_cuotas', self.gf('django.db.models.fields.IntegerField')(default=1, null=True, blank=True)),
            ('moneda', self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name='moneda', null=True, to=orm['core.Catalogo'])),
            ('observacion', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('estado_poliza', self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name='estado_poliza', to=orm['core.Catalogo'])),
        ))
        db.send_create_signal(u'poliza', ['Poliza'])

        # Adding model 'PlanPagos'
        db.create_table(u'poliza_planpagos', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('audt_usuario_creo', self.gf('django.db.models.fields.related.ForeignKey')(related_name='planpagos_created_related', null=True, to=orm['auth.User'])),
            ('audt_fecha_creacion', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2015, 1, 10, 0, 0), auto_now_add=True, blank=True)),
            ('audt_activo', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('audt_fecha_modificacion', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
            ('audt_usuario_modificacion', self.gf('django.db.models.fields.related.ForeignKey')(related_name='planpagos_modified_related', null=True, to=orm['auth.User'])),
            ('audt_fecha_eliminacion', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('audt_usuario_eliminacion', self.gf('django.db.models.fields.related.ForeignKey')(related_name='planpagos_deleted_related', null=True, to=orm['auth.User'])),
            ('poliza', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['poliza.Poliza'], null=True, blank=True)),
            ('numero_cuota', self.gf('django.db.models.fields.IntegerField')()),
            ('monto', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('fecha_vence', self.gf('django.db.models.fields.DateField')()),
            ('fecha_pago', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('numero_cupon', self.gf('django.db.models.fields.CharField')(max_length=15, null=True, blank=True)),
            ('banco', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Empresa'], null=True, blank=True)),
            ('numero_voucher', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
        ))
        db.send_create_signal(u'poliza', ['PlanPagos'])

        # Adding model 'Archivo'
        db.create_table(u'poliza_archivo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('poliza', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['poliza.Poliza'], null=True, blank=True)),
            ('archivo', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('observacion', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'poliza', ['Archivo'])

        # Adding model 'ImportarTrama'
        db.create_table(u'poliza_importartrama', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('codigo_t', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('nombre_t', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('fecha_t', self.gf('django.db.models.fields.DateField')()),
            ('poliza_trama', self.gf('django.db.models.fields.related.ForeignKey')(related_name='trama_poliza', to=orm['poliza.Poliza'])),
        ))
        db.send_create_signal(u'poliza', ['ImportarTrama'])

        # Adding model 'ImportarDependiente'
        db.create_table(u'poliza_importardependiente', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fila', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('valor', self.gf('django.db.models.fields.CharField')(max_length=70)),
            ('poliza_independiente', self.gf('django.db.models.fields.related.ForeignKey')(related_name='independiente_poliza', to=orm['poliza.Poliza'])),
        ))
        db.send_create_signal(u'poliza', ['ImportarDependiente'])

        # Adding model 'Riesgo'
        db.create_table(u'poliza_riesgo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('poliza', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['poliza.Poliza'])),
            ('tipo_riesgo', self.gf('django.db.models.fields.related.ForeignKey')(related_name='ramo_pp', to=orm['poliza.Ramo'])),
            ('ramo', self.gf('django.db.models.fields.related.ForeignKey')(related_name='ramo_p', to=orm['poliza.Ramo'])),
            ('sub_ramo', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='ramo_h', null=True, to=orm['poliza.Ramo'])),
            ('producto', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='producto', null=True, to=orm['poliza.Producto'])),
            ('materia_asegurada', self.gf('django.db.models.fields.DecimalField')(max_digits=20, decimal_places=2)),
            ('prima', self.gf('django.db.models.fields.DecimalField')(max_digits=20, decimal_places=2)),
        ))
        db.send_create_signal(u'poliza', ['Riesgo'])


    def backwards(self, orm):
        # Deleting model 'Ramo'
        db.delete_table(u'poliza_ramo')

        # Deleting model 'Producto'
        db.delete_table(u'poliza_producto')

        # Deleting model 'Poliza'
        db.delete_table(u'poliza_poliza')

        # Deleting model 'PlanPagos'
        db.delete_table(u'poliza_planpagos')

        # Deleting model 'Archivo'
        db.delete_table(u'poliza_archivo')

        # Deleting model 'ImportarTrama'
        db.delete_table(u'poliza_importartrama')

        # Deleting model 'ImportarDependiente'
        db.delete_table(u'poliza_importardependiente')

        # Deleting model 'Riesgo'
        db.delete_table(u'poliza_riesgo')


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
        },
        u'poliza.archivo': {
            'Meta': {'object_name': 'Archivo'},
            'archivo': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'observacion': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'poliza': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['poliza.Poliza']", 'null': 'True', 'blank': 'True'})
        },
        u'poliza.importardependiente': {
            'Meta': {'object_name': 'ImportarDependiente'},
            'fila': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'poliza_independiente': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'independiente_poliza'", 'to': u"orm['poliza.Poliza']"}),
            'valor': ('django.db.models.fields.CharField', [], {'max_length': '70'})
        },
        u'poliza.importartrama': {
            'Meta': {'object_name': 'ImportarTrama'},
            'codigo_t': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'fecha_t': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre_t': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'poliza_trama': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'trama_poliza'", 'to': u"orm['poliza.Poliza']"})
        },
        u'poliza.planpagos': {
            'Meta': {'object_name': 'PlanPagos'},
            'audt_activo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'audt_fecha_creacion': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2015, 1, 10, 0, 0)', 'auto_now_add': 'True', 'blank': 'True'}),
            'audt_fecha_eliminacion': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'audt_fecha_modificacion': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'audt_usuario_creo': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'planpagos_created_related'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'audt_usuario_eliminacion': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'planpagos_deleted_related'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'audt_usuario_modificacion': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'planpagos_modified_related'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'banco': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Empresa']", 'null': 'True', 'blank': 'True'}),
            'fecha_pago': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'fecha_vence': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'monto': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'numero_cuota': ('django.db.models.fields.IntegerField', [], {}),
            'numero_cupon': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'numero_voucher': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'poliza': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['poliza.Poliza']", 'null': 'True', 'blank': 'True'})
        },
        u'poliza.poliza': {
            'Meta': {'object_name': 'Poliza'},
            'audt_activo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'audt_fecha_creacion': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2015, 1, 10, 0, 0)', 'auto_now_add': 'True', 'blank': 'True'}),
            'audt_fecha_eliminacion': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'audt_fecha_modificacion': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'audt_usuario_creo': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'poliza_created_related'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'audt_usuario_eliminacion': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'poliza_deleted_related'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'audt_usuario_modificacion': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'poliza_modified_related'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'cantidad_cuotas': ('django.db.models.fields.IntegerField', [], {'default': '1', 'null': 'True', 'blank': 'True'}),
            'cia': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Empresa']", 'null': 'True', 'blank': 'True'}),
            'cliente': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cliente.Cliente']", 'null': 'True', 'blank': 'True'}),
            'estado_poliza': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'related_name': "'estado_poliza'", 'to': u"orm['core.Catalogo']"}),
            'fecha_fin': ('django.db.models.fields.DateTimeField', [], {}),
            'fecha_ingreso': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2015, 1, 10, 0, 0)', 'auto_now_add': 'True', 'blank': 'True'}),
            'fecha_inicio': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'materia_asegurado': ('django.db.models.fields.DecimalField', [], {'max_digits': '20', 'decimal_places': '2'}),
            'moneda': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'related_name': "'moneda'", 'null': 'True', 'to': u"orm['core.Catalogo']"}),
            'numero_poliza': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'observacion': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'prima': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'})
        },
        u'poliza.producto': {
            'Meta': {'object_name': 'Producto'},
            'audt_activo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'audt_fecha_creacion': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2015, 1, 10, 0, 0)', 'auto_now_add': 'True', 'blank': 'True'}),
            'audt_fecha_eliminacion': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'audt_fecha_modificacion': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'audt_usuario_creo': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'producto_created_related'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'audt_usuario_eliminacion': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'producto_deleted_related'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'audt_usuario_modificacion': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'producto_modified_related'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'cia': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Empresa']"}),
            'comision': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'ramo': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'ramo'", 'to': u"orm['poliza.Ramo']"}),
            'sub_ramo': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sub_ramo'", 'to': u"orm['poliza.Ramo']"})
        },
        u'poliza.ramo': {
            'Meta': {'object_name': 'Ramo'},
            'audt_activo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'audt_fecha_creacion': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2015, 1, 10, 0, 0)', 'auto_now_add': 'True', 'blank': 'True'}),
            'audt_fecha_eliminacion': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'audt_fecha_modificacion': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'audt_usuario_creo': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'ramo_created_related'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'audt_usuario_eliminacion': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'ramo_deleted_related'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'audt_usuario_modificacion': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'ramo_modified_related'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ramo_superior': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'padre'", 'null': 'True', 'to': u"orm['poliza.Ramo']"})
        },
        u'poliza.riesgo': {
            'Meta': {'object_name': 'Riesgo'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'materia_asegurada': ('django.db.models.fields.DecimalField', [], {'max_digits': '20', 'decimal_places': '2'}),
            'poliza': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['poliza.Poliza']"}),
            'prima': ('django.db.models.fields.DecimalField', [], {'max_digits': '20', 'decimal_places': '2'}),
            'producto': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'producto'", 'null': 'True', 'to': u"orm['poliza.Producto']"}),
            'ramo': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'ramo_p'", 'to': u"orm['poliza.Ramo']"}),
            'sub_ramo': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'ramo_h'", 'null': 'True', 'to': u"orm['poliza.Ramo']"}),
            'tipo_riesgo': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'ramo_pp'", 'to': u"orm['poliza.Ramo']"})
        }
    }

    complete_apps = ['poliza']