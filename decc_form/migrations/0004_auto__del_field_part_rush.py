# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Part.rush'
        db.delete_column(u'form_part', 'rush')


    def backwards(self, orm):
        # Adding field 'Part.rush'
        db.add_column(u'form_part', 'rush',
                      self.gf('django.db.models.fields.BooleanField')(default=''),
                      keep_default=False)


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
            'batch_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'extras': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
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
            'cost_noi': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '5', 'decimal_places': '3'}),
            'cost_rate': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '4', 'decimal_places': '2'}),
            'field_notes': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['form.Project']"}),
            'type_name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['form']