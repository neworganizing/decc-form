# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

try:
    from django.contrib.auth import get_user_model
except ImportError:
    from django.contrib.auth.models import User
else:
    User = get_user_model()

user_orm_label = '%s.%s' % (User._meta.app_label, User._meta.object_name)
user_model_label = '%s.%s' % (User._meta.app_label, User._meta.module_name)

class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Address'
        db.create_table(u'decc_form_address', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('street1', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('street2', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('zipcode', self.gf('django.db.models.fields.CharField')(max_length=32)),
        ))
        db.send_create_signal(u'decc_form', ['Address'])

        # Adding model 'Contact'
        db.create_table(u'decc_form_contact', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm[user_orm_label], unique=True)),
            ('work_phone', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('cell_phone', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('fax', self.gf('django.db.models.fields.CharField')(max_length=255)),
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
            ('end_date', self.gf('django.db.models.fields.DateField')()),
            ('order_frequency', self.gf('django.db.models.fields.IntegerField')()),
            ('estimated_item_count', self.gf('django.db.models.fields.IntegerField')()),
            ('notes', self.gf('django.db.models.fields.TextField')()),
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
            ('field_notes', self.gf('django.db.models.fields.TextField')()),
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
            ('extras', self.gf('django.db.models.fields.CharField')(max_length=255)),
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
        user_model_label: {
            'Meta': {
                'object_name': User.__name__,
                'db_table': "'%s'" % User._meta.db_table
                },
            User._meta.pk.attname: (
                'django.db.models.fields.AutoField', [],
                {'primary_key': 'True', 
                 'db_column': "'%s'" % User._meta.pk.column}
            ),
        },
        u'decc_form.address': {
            'Meta': {'object_name': 'Address'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'street1': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'street2': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'max_length': '32'})
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
            'cell_phone': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_date': ('django.db.models.fields.DateField', [], {}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm["+user_orm_label+"]", 'unique': 'True'}),
            'work_phone': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'decc_form.order': {
            'Meta': {'object_name': 'Order'},
            'bill_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 4, 25, 0, 0)'}),
            'paid_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['decc_form.Project']"})
        },
        u'decc_form.part': {
            'Meta': {'object_name': 'Part'},
            'batch_count': ('django.db.models.fields.IntegerField', [], {}),
            'extras': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'form_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['decc_form.Type']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item_count': ('django.db.models.fields.IntegerField', [], {}),
            'order': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['decc_form.Order']"}),
            'rush': ('django.db.models.fields.BooleanField', [], {}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        },
        u'decc_form.project': {
            'Meta': {'object_name': 'Project'},
            'added_date': ('django.db.models.fields.DateField', [], {}),
            'billable': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['decc_form.Billable']"}),
            'end_date': ('django.db.models.fields.DateField', [], {}),
            'estimated_item_count': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_date': ('django.db.models.fields.DateField', [], {}),
            'notes': ('django.db.models.fields.TextField', [], {}),
            'order_frequency': ('django.db.models.fields.IntegerField', [], {}),
            'start_date': ('django.db.models.fields.DateField', [], {})
        },
        u'decc_form.registrant': {
            'Meta': {'object_name': 'Registrant'},
            'addresses': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['decc_form.Address']", 'through': u"orm['decc_form.RegistrantAddress']", 'symmetrical': 'False'}),
            'age': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'bad_image': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'batch': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['decc_form.Batch']"}),
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
            'field_notes': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['decc_form.Project']"}),
            'type_name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['decc_form']
