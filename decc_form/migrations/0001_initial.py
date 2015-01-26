# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

try:
    from django.conf import settings
    user_model_name = settings.AUTH_USER_MODEL
except:
    user_model_name = u'auth.User'

class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Address'
        db.create_table(u'decc_form_address', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('street1', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('street2', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('zipcode', self.gf('django.db.models.fields.CharField')(max_length=32, null=True, blank=True)),
        ))
        db.send_create_signal(u'decc_form', ['Address'])

        # Adding model 'Contact'
        db.create_table(u'decc_form_contact', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm[user_model_name], unique=True)),
            ('work_phone', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('cell_phone', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('fax', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('added_date', self.gf('django.db.models.fields.DateField')()),
            ('modified_date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'decc_form', ['Contact'])

        # Adding model 'Billable'
        db.create_table(u'decc_form_billable', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('contact', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['decc_form.Contact'])),
            ('address', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['decc_form.Address'])),
            ('tax_status', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('added_date', self.gf('django.db.models.fields.DateField')()),
            ('modified_date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'decc_form', ['Billable'])

        # Adding model 'Project'
        db.create_table(u'decc_form_project', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('billable', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['decc_form.Billable'])),
            ('start_date', self.gf('django.db.models.fields.DateField')()),
            ('end_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('order_frequency', self.gf('django.db.models.fields.IntegerField')()),
            ('estimated_item_count', self.gf('django.db.models.fields.IntegerField')()),
            ('notes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('added_date', self.gf('django.db.models.fields.DateField')()),
            ('modified_date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'decc_form', ['Project'])

        # Adding model 'Client'
        db.create_table(u'decc_form_client', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('address', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['decc_form.Address'])),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['decc_form.Project'])),
            ('org_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('added_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('modified_date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'decc_form', ['Client'])

        # Adding model 'ClientContact'
        db.create_table(u'decc_form_clientcontact', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('client', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['decc_form.Client'])),
            ('contact', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['decc_form.Contact'])),
            ('order', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'decc_form', ['ClientContact'])

        # Adding model 'Type'
        db.create_table(u'decc_form_type', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['decc_form.Project'])),
            ('type_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('field_notes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('cost_rate', self.gf('django.db.models.fields.DecimalField')(max_digits=4, decimal_places=2)),
            ('cost_noi', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=3)),
        ))
        db.send_create_signal(u'decc_form', ['Type'])

        # Adding model 'Committee'
        db.create_table(u'decc_form_committee', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'decc_form', ['Committee'])

        # Adding M2M table for field projects on 'Committee'
        m2m_table_name = db.shorten_name(u'decc_form_committee_projects')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('committee', models.ForeignKey(orm[u'decc_form.committee'], null=False)),
            ('project', models.ForeignKey(orm[u'decc_form.project'], null=False))
        ))
        db.create_unique(m2m_table_name, ['committee_id', 'project_id'])

        # Adding model 'Order'
        db.create_table(u'decc_form_order', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['decc_form.Project'])),
            ('order_date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 4, 25, 0, 0))),
            ('digital', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('bill_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('paid_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'decc_form', ['Order'])

        # Adding model 'Part'
        db.create_table(u'decc_form_part', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('order', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['decc_form.Order'])),
            ('form_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['decc_form.Type'])),
            ('rush', self.gf('django.db.models.fields.BooleanField')()),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('item_count', self.gf('django.db.models.fields.IntegerField')()),
            ('batch_count', self.gf('django.db.models.fields.IntegerField')()),
            ('van', self.gf('django.db.models.fields.BooleanField')()),
            ('quad', self.gf('django.db.models.fields.BooleanField')()),
            ('match', self.gf('django.db.models.fields.BooleanField')()),
            ('destroy_files', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('return_files', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('extras', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal(u'decc_form', ['Part'])

        # Adding model 'Batch'
        db.create_table(u'decc_form_batch', (
            ('id', self.gf('django.db.models.fields.PositiveIntegerField')(primary_key=True)),
            ('part', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['decc_form.Part'])),
            ('committee', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['decc_form.Committee'], null=True, blank=True)),
            ('client_filename', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('vendor_filename', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('item_count', self.gf('django.db.models.fields.IntegerField')()),
            ('submission_date', self.gf('django.db.models.fields.DateField')()),
            ('processed_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('return_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'decc_form', ['Batch'])

        # Adding model 'Registrant'
        db.create_table(u'decc_form_registrant', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('batch', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['decc_form.Batch'])),
            ('citizenship', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('age', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('dob_mm', self.gf('django.db.models.fields.CharField')(max_length=2, null=True, blank=True)),
            ('dob_dd', self.gf('django.db.models.fields.CharField')(max_length=2, null=True, blank=True)),
            ('dob_yy', self.gf('django.db.models.fields.CharField')(max_length=4, null=True, blank=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('middle_name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('suffix', self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True)),
            ('home_area_code', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
            ('home_phone', self.gf('django.db.models.fields.CharField')(max_length=32, null=True, blank=True)),
            ('race', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('party', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True)),
            ('date_signed_mm', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('date_signed_dd', self.gf('django.db.models.fields.CharField')(max_length=2, null=True, blank=True)),
            ('date_signed_yy', self.gf('django.db.models.fields.CharField')(max_length=4, null=True, blank=True)),
            ('mobile_area_code', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
            ('mobile_phone', self.gf('django.db.models.fields.CharField')(max_length=32, null=True, blank=True)),
            ('email_address', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('volunteer', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('previous_name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('bad_image', self.gf('django.db.models.fields.CharField')(max_length=32, null=True, blank=True)),
            ('error_code', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'decc_form', ['Registrant'])

        # Adding model 'RegistrantAddress'
        db.create_table(u'decc_form_registrantaddress', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('registrant', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['decc_form.Registrant'])),
            ('address', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['decc_form.Address'])),
            ('address_type', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'decc_form', ['RegistrantAddress'])


    def backwards(self, orm):
        # Deleting model 'Address'
        db.delete_table(u'decc_form_address')

        # Deleting model 'Contact'
        db.delete_table(u'decc_form_contact')

        # Deleting model 'Billable'
        db.delete_table(u'decc_form_billable')

        # Deleting model 'Project'
        db.delete_table(u'decc_form_project')

        # Deleting model 'Client'
        db.delete_table(u'decc_form_client')

        # Deleting model 'ClientContact'
        db.delete_table(u'decc_form_clientcontact')

        # Deleting model 'Type'
        db.delete_table(u'decc_form_type')

        # Deleting model 'Committee'
        db.delete_table(u'decc_form_committee')

        # Removing M2M table for field projects on 'Committee'
        db.delete_table(db.shorten_name(u'decc_form_committee_projects'))

        # Deleting model 'Order'
        db.delete_table(u'decc_form_order')

        # Deleting model 'Part'
        db.delete_table(u'decc_form_part')

        # Deleting model 'Batch'
        db.delete_table(u'decc_form_batch')

        # Deleting model 'Registrant'
        db.delete_table(u'decc_form_registrant')

        # Deleting model 'RegistrantAddress'
        db.delete_table(u'decc_form_registrantaddress')


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
        user_model_name: {
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
        u'decc_form.address': {
            'Meta': {'object_name': 'Address'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'street1': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'street2': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'})
        },
        u'decc_form.batch': {
            'Meta': {'object_name': 'Batch'},
            'client_filename': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'committee': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['decc_form.Committee']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.PositiveIntegerField', [], {'primary_key': 'True'}),
            'item_count': ('django.db.models.fields.IntegerField', [], {}),
            'part': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['decc_form.Part']"}),
            'processed_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'return_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'submission_date': ('django.db.models.fields.DateField', [], {}),
            'vendor_filename': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'decc_form.billable': {
            'Meta': {'object_name': 'Billable'},
            'added_date': ('django.db.models.fields.DateField', [], {}),
            'address': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['decc_form.Address']"}),
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['decc_form.Contact']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_date': ('django.db.models.fields.DateField', [], {}),
            'tax_status': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'decc_form.client': {
            'Meta': {'object_name': 'Client'},
            'added_date': ('django.db.models.fields.DateTimeField', [], {}),
            'address': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['decc_form.Address']"}),
            'contacts': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['decc_form.Contact']", 'through': u"orm['decc_form.ClientContact']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_date': ('django.db.models.fields.DateTimeField', [], {}),
            'org_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['decc_form.Project']"})
        },
        u'decc_form.clientcontact': {
            'Meta': {'object_name': 'ClientContact'},
            'client': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['decc_form.Client']"}),
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['decc_form.Contact']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {})
        },
        u'decc_form.committee': {
            'Meta': {'object_name': 'Committee'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'projects': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['decc_form.Project']", 'symmetrical': 'False'})
        },
        u'decc_form.contact': {
            'Meta': {'object_name': 'Contact'},
            'added_date': ('django.db.models.fields.DateField', [], {}),
            'cell_phone': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_date': ('django.db.models.fields.DateField', [], {}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm["+user_model_name+"]", 'unique': 'True'}),
            'work_phone': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'decc_form.order': {
            'Meta': {'object_name': 'Order'},
            'bill_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'digital': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 4, 25, 0, 0)'}),
            'paid_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['decc_form.Project']"})
        },
        u'decc_form.part': {
            'Meta': {'object_name': 'Part'},
            'batch_count': ('django.db.models.fields.IntegerField', [], {}),
            'destroy_files': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'extras': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'form_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['decc_form.Type']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item_count': ('django.db.models.fields.IntegerField', [], {}),
            'match': ('django.db.models.fields.BooleanField', [], {}),
            'order': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['decc_form.Order']"}),
            'quad': ('django.db.models.fields.BooleanField', [], {}),
            'return_files': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'rush': ('django.db.models.fields.BooleanField', [], {}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'van': ('django.db.models.fields.BooleanField', [], {})
        },
        u'decc_form.project': {
            'Meta': {'object_name': 'Project'},
            'added_date': ('django.db.models.fields.DateField', [], {}),
            'billable': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['decc_form.Billable']"}),
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'estimated_item_count': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_date': ('django.db.models.fields.DateField', [], {}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'order_frequency': ('django.db.models.fields.IntegerField', [], {}),
            'start_date': ('django.db.models.fields.DateField', [], {})
        },
        u'decc_form.registrant': {
            'Meta': {'object_name': 'Registrant'},
            'addresses': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['decc_form.Address']", 'null': 'True', 'through': u"orm['decc_form.RegistrantAddress']", 'blank': 'True'}),
            'age': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'bad_image': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'batch': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['decc_form.Batch']"}),
            'citizenship': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'date_signed_dd': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'date_signed_mm': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'date_signed_yy': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'dob_dd': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'dob_mm': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'dob_yy': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'email_address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'error_code': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'home_area_code': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'home_phone': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'middle_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'mobile_area_code': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'mobile_phone': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'party': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'previous_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'race': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'suffix': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'volunteer': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'decc_form.registrantaddress': {
            'Meta': {'object_name': 'RegistrantAddress'},
            'address': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['decc_form.Address']"}),
            'address_type': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'registrant': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['decc_form.Registrant']"})
        },
        u'decc_form.type': {
            'Meta': {'object_name': 'Type'},
            'cost_noi': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '3'}),
            'cost_rate': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '2'}),
            'field_notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['decc_form.Project']"}),
            'type_name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['decc_form']