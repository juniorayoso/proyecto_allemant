# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TipoCatalogo'
        db.create_table(u'core_tipocatalogo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'core', ['TipoCatalogo'])

        # Adding model 'Catalogo'
        db.create_table(u'core_catalogo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tipo_catalogo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.TipoCatalogo'])),
            ('tipo_dato', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('dato', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('abreviatura', self.gf('django.db.models.fields.CharField')(max_length=5, null=True, blank=True)),
            ('valor1', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('valor2', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
        ))
        db.send_create_signal(u'core', ['Catalogo'])

        # Adding model 'Persona'
        db.create_table(u'core_persona', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('audt_usuario_creo', self.gf('django.db.models.fields.related.ForeignKey')(related_name='persona_created_related', null=True, to=orm['auth.User'])),
            ('audt_fecha_creacion', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2015, 1, 10, 0, 0), auto_now_add=True, blank=True)),
            ('audt_activo', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('audt_fecha_modificacion', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
            ('audt_usuario_modificacion', self.gf('django.db.models.fields.related.ForeignKey')(related_name='persona_modified_related', null=True, to=orm['auth.User'])),
            ('audt_fecha_eliminacion', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('audt_usuario_eliminacion', self.gf('django.db.models.fields.related.ForeignKey')(related_name='persona_deleted_related', null=True, to=orm['auth.User'])),
            ('dni', self.gf('django.db.models.fields.CharField')(unique=True, max_length=15)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('apellido', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('estado_civil', self.gf('django.db.models.fields.related.ForeignKey')(related_name='estado_civil', to=orm['core.Catalogo'])),
            ('fecha_nacimiento', self.gf('django.db.models.fields.DateField')(null=True)),
            ('sexo', self.gf('django.db.models.fields.related.ForeignKey')(related_name='sexo', to=orm['core.Catalogo'])),
        ))
        db.send_create_signal(u'core', ['Persona'])

        # Adding model 'Empresa'
        db.create_table(u'core_empresa', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('audt_usuario_creo', self.gf('django.db.models.fields.related.ForeignKey')(related_name='empresa_created_related', null=True, to=orm['auth.User'])),
            ('audt_fecha_creacion', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2015, 1, 10, 0, 0), auto_now_add=True, blank=True)),
            ('audt_activo', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('audt_fecha_modificacion', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
            ('audt_usuario_modificacion', self.gf('django.db.models.fields.related.ForeignKey')(related_name='empresa_modified_related', null=True, to=orm['auth.User'])),
            ('audt_fecha_eliminacion', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('audt_usuario_eliminacion', self.gf('django.db.models.fields.related.ForeignKey')(related_name='empresa_deleted_related', null=True, to=orm['auth.User'])),
            ('ruc', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('razon_social', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('giro_negocio', self.gf('django.db.models.fields.related.ForeignKey')(related_name='giro', null=True, to=orm['core.Catalogo'])),
        ))
        db.send_create_signal(u'core', ['Empresa'])

        # Adding model 'Ubigeo'
        db.create_table(u'core_ubigeo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('departamento', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('provincia', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'core', ['Ubigeo'])

        # Adding model 'Distrito'
        db.create_table(u'core_distrito', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ubigeo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Ubigeo'])),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'core', ['Distrito'])

        # Adding model 'Direccion'
        db.create_table(u'core_direccion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('persona', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Persona'], null=True, blank=True)),
            ('empresa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Empresa'], null=True, blank=True)),
            ('av_calle', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('interior', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('ubigeo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Ubigeo'])),
            ('distrito', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Distrito'])),
        ))
        db.send_create_signal(u'core', ['Direccion'])

        # Adding model 'Telefono'
        db.create_table(u'core_telefono', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('numero', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('operador', self.gf('django.db.models.fields.related.ForeignKey')(related_name='operador', to=orm['core.Catalogo'])),
            ('persona', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Persona'], null=True, blank=True)),
            ('empresa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Empresa'], null=True, blank=True)),
        ))
        db.send_create_signal(u'core', ['Telefono'])

        # Adding model 'Email'
        db.create_table(u'core_email', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tipo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Catalogo'], null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('persona', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Persona'], null=True, blank=True)),
            ('empresa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Empresa'], null=True, blank=True)),
        ))
        db.send_create_signal(u'core', ['Email'])


    def backwards(self, orm):
        # Deleting model 'TipoCatalogo'
        db.delete_table(u'core_tipocatalogo')

        # Deleting model 'Catalogo'
        db.delete_table(u'core_catalogo')

        # Deleting model 'Persona'
        db.delete_table(u'core_persona')

        # Deleting model 'Empresa'
        db.delete_table(u'core_empresa')

        # Deleting model 'Ubigeo'
        db.delete_table(u'core_ubigeo')

        # Deleting model 'Distrito'
        db.delete_table(u'core_distrito')

        # Deleting model 'Direccion'
        db.delete_table(u'core_direccion')

        # Deleting model 'Telefono'
        db.delete_table(u'core_telefono')

        # Deleting model 'Email'
        db.delete_table(u'core_email')


    models = {
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
        u'core.direccion': {
            'Meta': {'object_name': 'Direccion'},
            'av_calle': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'distrito': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Distrito']"}),
            'empresa': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Empresa']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interior': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'persona': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Persona']", 'null': 'True', 'blank': 'True'}),
            'ubigeo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Ubigeo']"})
        },
        u'core.distrito': {
            'Meta': {'object_name': 'Distrito'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'ubigeo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Ubigeo']"})
        },
        u'core.email': {
            'Meta': {'object_name': 'Email'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'empresa': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Empresa']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'persona': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Persona']", 'null': 'True', 'blank': 'True'}),
            'tipo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Catalogo']", 'null': 'True', 'blank': 'True'})
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
        u'core.telefono': {
            'Meta': {'object_name': 'Telefono'},
            'empresa': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Empresa']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numero': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'operador': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'operador'", 'to': u"orm['core.Catalogo']"}),
            'persona': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Persona']", 'null': 'True', 'blank': 'True'})
        },
        u'core.tipocatalogo': {
            'Meta': {'object_name': 'TipoCatalogo'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'core.ubigeo': {
            'Meta': {'object_name': 'Ubigeo'},
            'departamento': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'provincia': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['core']