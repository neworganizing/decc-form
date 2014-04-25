# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Contact'
        db.create_table(u'form_contact', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('work_phone', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('cell_phone', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('fax', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('added_date', self.gf('django.db.models.fields.DateField')()),
            ('modified_date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'form', ['Contact'])

        # Adding model 'Project'
        db.create_table(u'form_project', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('start_date', self.gf('django.db.models.fields.DateField')()),
            ('end_date', self.gf('django.db.models.fields.DateField')()),
            ('order_frequency', self.gf('django.db.models.fields.IntegerField')()),
            ('estimated_item_count', self.gf('django.db.models.fields.IntegerField')()),
            ('notes', self.gf('django.db.models.fields.TextField')()),
            ('added_date', self.gf('django.db.models.fields.DateField')()),
            ('modified_date', self.gf('django.db.models.fields.DateField')()),
            ('client_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['form.Client'])),
            ('billable_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['form.Billable'])),
        ))
        db.send_create_signal(u'form', ['Project'])

        # Adding model 'Address'
        db.create_table(u'form_address', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('street1', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('street2', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('zipcode', self.gf('django.db.models.fields.CharField')(max_length=32)),
        ))
        db.send_create_signal(u'form', ['Address'])

        # Adding model 'Client'
        db.create_table(u'form_client', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('org_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('added_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('modified_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('address_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['form.Address'])),
        ))
        db.send_create_signal(u'form', ['Client'])

        # Adding model 'ClientContact'
        db.create_table(u'form_clientcontact', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('client_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['form.Client'])),
            ('contact_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['form.Contact'])),
            ('order', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'form', ['ClientContact'])

        # Adding model 'Billable'
        db.create_table(u'form_billable', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tax_status', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('added_date', self.gf('django.db.models.fields.DateField')()),
            ('modified_date', self.gf('django.db.models.fields.DateField')()),
            ('contact_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['form.Contact'])),
            ('address_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['form.Address'])),
        ))
        db.send_create_signal(u'form', ['Billable'])

        # Adding model 'Registrant'
        db.create_table(u'form_registrant', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('batch_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['form.Batch'])),
            ('citizenship', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('age', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('dob_mm', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('dob_dd', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('dob_yy', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('middle_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('suffix', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('home_area_code', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('home_phone', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('race', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('party', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('date_signed_mm', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('date_signed_dd', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('date_signed_yy', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('mobile_area_code', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('mobile_phone', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('email_address', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('volunteer', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('previous_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('bad_image', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('error_code', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'form', ['Registrant'])

        # Adding model 'Part'
        db.create_table(u'form_part', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('item_count', self.gf('django.db.models.fields.IntegerField')()),
            ('extras', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('cost', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=2)),
            ('order_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['form.Order'])),
            ('type_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['form.Type'])),
        ))
        db.send_create_signal(u'form', ['Part'])

        # Adding model 'Type'
        db.create_table(u'form_type', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('field_notes', self.gf('django.db.models.fields.TextField')()),
            ('project_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['form.Project'])),
        ))
        db.send_create_signal(u'form', ['Type'])

        # Adding model 'Batch'
        db.create_table(u'form_batch', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('client_filename', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('vendor_filename', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('item_count', self.gf('django.db.models.fields.IntegerField')()),
            ('submission_date', self.gf('django.db.models.fields.DateField')()),
            ('processed_date', self.gf('django.db.models.fields.DateField')()),
            ('return_date', self.gf('django.db.models.fields.DateField')()),
            ('part_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['form.Part'])),
        ))
        db.send_create_signal(u'form', ['Batch'])

        # Adding model 'Order'
        db.create_table(u'form_order', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('order_date', self.gf('django.db.models.fields.DateField')()),
            ('bill_date', self.gf('django.db.models.fields.DateField')()),
            ('paid_date', self.gf('django.db.models.fields.DateField')()),
            ('project_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['form.Project'])),
        ))
        db.send_create_signal(u'form', ['Order'])

        # Adding model 'RegistrantAddress'
        db.create_table(u'form_registrantaddress', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('registrant', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['form.Registrant'])),
            ('address', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['form.Address'])),
            ('address_type', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'form', ['RegistrantAddress'])


    def backwards(self, orm):
        # Deleting model 'Contact'
        db.delete_table(u'form_contact')

        # Deleting model 'Project'
        db.delete_table(u'form_project')

        # Deleting model 'Address'
        db.delete_table(u'form_address')

        # Deleting model 'Client'
        db.delete_table(u'form_client')

        # Deleting model 'ClientContact'
        db.delete_table(u'form_clientcontact')

        # Deleting model 'Billable'
        db.delete_table(u'form_billable')

        # Deleting model 'Registrant'
        db.delete_table(u'form_registrant')

        # Deleting model 'Part'
        db.delete_table(u'form_part')

        # Deleting model 'Type'
        db.delete_table(u'form_type')

        # Deleting model 'Batch'
        db.delete_table(u'form_batch')

        # Deleting model 'Order'
        db.delete_table(u'form_order')

        # Deleting model 'RegistrantAddress'
        db.delete_table(u'form_registrantaddress')


    models = {
        u'form.address': {
            'Meta': {'object_name': 'Address'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'street1': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'street2': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        },
        u'form.batch': {
            'Meta': {'object_name': 'Batch'},
            'client_filename': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item_count': ('django.db.models.fields.IntegerField', [], {}),
            'part_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['form.Part']"}),
            'processed_date': ('django.db.models.fields.DateField', [], {}),
            'return_date': ('django.db.models.fields.DateField', [], {}),
            'submission_date': ('django.db.models.fields.DateField', [], {}),
            'vendor_filename': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'form.billable': {
            'Meta': {'object_name': 'Billable'},
            'added_date': ('django.db.models.fields.DateField', [], {}),
            'address_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['form.Address']"}),
            'contact_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['form.Contact']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_date': ('django.db.models.fields.DateField', [], {}),
            'tax_status': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'form.client': {
            'Meta': {'object_name': 'Client'},
            'added_date': ('django.db.models.fields.DateTimeField', [], {}),
            'address_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['form.Address']"}),
            'contacts': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['form.Contact']", 'through': u"orm['form.ClientContact']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_date': ('django.db.models.fields.DateTimeField', [], {}),
            'org_name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'form.clientcontact': {
            'Meta': {'object_name': 'ClientContact'},
            'client_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['form.Client']"}),
            'contact_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['form.Contact']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {})
        },
        u'form.contact': {
            'Meta': {'object_name': 'Contact'},
            'added_date': ('django.db.models.fields.DateField', [], {}),
            'cell_phone': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_date': ('django.db.models.fields.DateField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'work_phone': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'form.order': {
            'Meta': {'object_name': 'Order'},
            'bill_date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order_date': ('django.db.models.fields.DateField', [], {}),
            'paid_date': ('django.db.models.fields.DateField', [], {}),
            'project_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['form.Project']"})
        },
        u'form.part': {
            'Meta': {'object_name': 'Part'},
            'cost': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '2'}),
            'extras': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item_count': ('django.db.models.fields.IntegerField', [], {}),
            'order_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['form.Order']"}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'type_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['form.Type']"})
        },
        u'form.project': {
            'Meta': {'object_name': 'Project'},
            'added_date': ('django.db.models.fields.DateField', [], {}),
            'billable_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['form.Billable']"}),
            'client_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['form.Client']"}),
            'end_date': ('django.db.models.fields.DateField', [], {}),
            'estimated_item_count': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_date': ('django.db.models.fields.DateField', [], {}),
            'notes': ('django.db.models.fields.TextField', [], {}),
            'order_frequency': ('django.db.models.fields.IntegerField', [], {}),
            'start_date': ('django.db.models.fields.DateField', [], {})
        },
        u'form.registrant': {
            'Meta': {'object_name': 'Registrant'},
            'addresses': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['form.Address']", 'through': u"orm['form.RegistrantAddress']", 'symmetrical': 'False'}),
            'age': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'bad_image': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'batch_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['form.Batch']"}),
            'citizenship': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'date_signed_dd': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'date_signed_mm': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'date_signed_yy': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'dob_dd': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'dob_mm': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'dob_yy': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'email_address': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'error_code': ('django.db.models.fields.IntegerField', [], {}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'home_area_code': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'home_phone': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'middle_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'mobile_area_code': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'mobile_phone': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'party': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'previous_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'race': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'suffix': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'volunteer': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'form.registrantaddress': {
            'Meta': {'object_name': 'RegistrantAddress'},
            'address': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['form.Address']"}),
            'address_type': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'registrant': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['form.Registrant']"})
        },
        u'form.type': {
            'Meta': {'object_name': 'Type'},
            'field_notes': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['form.Project']"}),
            'type_name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['form']