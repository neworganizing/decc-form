from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from .models import *

class ContactAdmin(admin.ModelAdmin):
    fields = ('user', 'work_phone', 'cell_phone', 'fax',)
    list_display = ('user',)
    ordering = ('user',)

class ContactInline(admin.StackedInline):
    model = Contact
    extra = 0

class ClientAdmin(admin.ModelAdmin):
    fields = ('address', 'project', 'contacts', 'org_name',)
    list_display = ('org_name', 'project', 'address',)
    ordering = ('org_name',)

    inlines = [ContactInline,]

class AddressAdmin(admin.ModelAdmin):
    fields = ['street1', 'street2', 'city', 'state', 'zipcode']
    list_display = ('id', 'street1', 'street2', 'city', 'state', 'zipcode')
    ordering = ('state',)
    

class ProjectAdmin(admin.ModelAdmin):
    fields = ['start_date', 'end_date', 'estimated_item_count', 'notes']
    list_display = ['id', 'start_date', 'end_date']

    
class TypeAdmin(admin.ModelAdmin):
    fields = ['project', 'type_name', 'field_notes', 'cost_rate', 'cost_noi']
    list_display = ['id', 'type_name', 'project']


class CommitteeAdmin(admin.ModelAdmin):
    fields = ['name', 'projects']
    list_display = ['id', 'name']


class OrderAdmin(admin.ModelAdmin):
    fields = ['project', 'order_date', 'digital', 'bill_date', 'paid_date']
    list_display = ['id', 'order_date', 'digital']


class PartAdmin(admin.ModelAdmin):
    fields = ['order', 'form_type', 'rush',
              'state', 'item_count', 'batch_count',
              'van', 'quad', 'match', 'destroy_files', 
              'return_files', 'extras']
    list_display = ['id', 'order', 'state']
    

class BatchAdmin(admin.ModelAdmin):
    fields = ['id', 'part', 'committee', 
              'client_filename', 'vendor_filename', 
              'item_count', 'submission_date', 
              'processed_date', 'return_date']

    list_display = ['id']

class RegistrantAdmin(admin.ModelAdmin):
    exclude = ['id']

admin.site.register(Client, ClientAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Committee, CommitteeAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Part, PartAdmin)
admin.site.register(Batch, BatchAdmin)
#admin.site.register(Registrant, RegistrantAdmin)
