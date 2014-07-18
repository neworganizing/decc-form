import datetime

from django.conf import settings 
from django.db import models


class Address(models.Model):
    street1 = models.CharField(max_length=255, null=True, blank=True)
    street2 = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=255, null=True, blank=True)
    zipcode = models.CharField(max_length=32, null=True, blank=True)

    def __unicode__(self):
        return str(self.street1 + self.city +','+self.state)


class Contact(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    #in user
    #name = models.CharField(max_length=255)
    #email = models.CharField(max_length=255)
    work_phone = models.CharField(max_length=255, null=True, blank=True)
    cell_phone = models.CharField(max_length=255, null=True, blank=True)
    fax = models.CharField(max_length=255, null=True, blank=True)
    added_date = models.DateField(auto_now_add=True)
    modified_date = models.DateField(auto_now=True)

    def __unicode__(self):
        return str(self.user)


class Billable(models.Model):
    contact = models.ForeignKey(Contact)
    address = models.ForeignKey(Address)
    org_name = models.CharField(max_length=255)
    tax_status = models.CharField(max_length=255)
    added_date = models.DateField(auto_now_add=True)
    modified_date = models.DateField(auto_now=True)

    def __unicode__(self):
        return str(self.org_name)


class Project(models.Model):
    #client = models.ForeignKey(Client)
    billable = models.ForeignKey(Billable)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    invoice_date = models.DateField(null=True, blank=True)
    order_frequency = models.IntegerField(null=True, blank=True)
    estimated_item_count = models.IntegerField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    added_date = models.DateField(auto_now_add=True)
    modified_date = models.DateField(auto_now=True)
   
    def __unicode__(self):
        return str('{}: {} - {}'.format(self.id, self.start_date, self.end_date))


class Client(models.Model):
    address = models.ForeignKey(Address)
    project = models.ForeignKey(Project)
    contacts = models.ManyToManyField(Contact, through='ClientContact')
    org_name = models.CharField(max_length=255)
    added_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
       
    def __unicode__(self):
        return str(self.org_name)


class ClientContact(models.Model):
    client = models.ForeignKey(Client)
    contact = models.ForeignKey(Contact)
    order = models.IntegerField()

    
class Type(models.Model):
    project = models.ForeignKey(Project)
    type_name = models.CharField(max_length=255)
    field_notes = models.TextField(null=True, blank=True)
    cost_rate = models.DecimalField(max_digits=4, decimal_places=2)
    cost_noi = models.DecimalField(max_digits=5, decimal_places=3)

    def __unicode__(self):
        return str(self.type_name)


class Committee(models.Model):
    name = models.CharField(max_length=255)
    projects = models.ManyToManyField(Project)

    def __unicode__(self):
        return str(self.name)


class Order(models.Model):
    project = models.ForeignKey(Project)
    order_date = models.DateField(default=datetime.datetime.today())
    digital = models.BooleanField(default=True)
    bill_date = models.DateField(null=True, blank=True)
    paid_date = models.DateField(null=True, blank=True)
    
    def __unicode__(self):
        return str('{}: {}'.format(self.id, self.order_date))


class Part(models.Model):
    order = models.ForeignKey(Order)
    form_type = models.ForeignKey(Type)
    rush = models.BooleanField()
    state = models.CharField(max_length=2)
    item_count = models.IntegerField()
    batch_count = models.IntegerField()
    van = models.BooleanField()
    quad = models.BooleanField()
    match = models.BooleanField()
    destroy_files = models.BooleanField(default=False)
    return_files = models.BooleanField(default=False)
    extras = models.CharField(max_length=255, null=True, blank=True)

    def __unicode__(self):
        return str('{}: {}'.format(self.id, self.state))

class Batch(models.Model):
    #PK = 3 digit client_id, 7 digit batch_id, based on last batch from that project
    id = models.PositiveIntegerField(primary_key=True)
    part = models.ForeignKey(Part) 
    committee = models.ForeignKey(Committee, null=True, blank=True)
    client_filename = models.FileField(upload_to='batchfiles/')
    vendor_filename = models.CharField(max_length=255)
    item_count = models.IntegerField(null=True, blank=True)
    final_item_count = models.IntegerField(null=True, blank=True)
    submission_date = models.DateField()
    processed_date = models.DateField(null=True, blank=True)
    return_date = models.DateField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            proj_id = self.part.order.project.id
            c_id = str(Client.objects.get(project=proj_id).id)
            print 'c_id: {}'.format(c_id)
            while len(c_id) < 3:
                c_id = '0' + c_id
            try:
                b_id = str(Batch.objects.filter(id__startswith=int(c_id)).order_by('-id')[0].id + 1)[-7:] 
            except (Batch.DoesNotExist, IndexError) as e:
                b_id = str(1)
            while len(b_id) < 7:
                b_id = '0' + b_id
            self.vendor_filename = c_id + b_id + '.pdf'
            self.id = int(c_id + b_id)
            self.submission_date = datetime.datetime.today()
        super(Batch, self).save(*args, **kwargs)


class Registrant(models.Model):
    batch = models.ForeignKey(Batch)
    citizenship = models.CharField(max_length=255, null=True, blank=True)
    age = models.CharField(max_length=10, null=True, blank=True)
    dob_mm = models.CharField(max_length=2, null=True, blank=True)
    dob_dd = models.CharField(max_length=2, null=True, blank=True)
    dob_yy = models.CharField(max_length=4, null=True, blank=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    middle_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    suffix = models.CharField(max_length=64, null=True, blank=True)
    home_area_code = models.CharField(max_length=16, null=True, blank=True)
    home_phone = models.CharField(max_length=32, null=True, blank=True)
    race = models.CharField(max_length=255, null=True, blank=True)
    party = models.CharField(max_length=255, null=True, blank=True)
    gender = models.CharField(max_length=64, null=True, blank=True)
    date_signed_mm = models.CharField(max_length=2, null=True, blank=True)
    date_signed_dd = models.CharField(max_length=2, null=True, blank=True)
    date_signed_yy = models.CharField(max_length=4, null=True, blank=True)
    mobile_area_code = models.CharField(max_length=16, null=True, blank=True)
    mobile_phone = models.CharField(max_length=32, null=True, blank=True)
    email_address = models.CharField(max_length=255, null=True, blank=True)
    volunteer = models.CharField(max_length=255, null=True, blank=True)
    previous_name = models.CharField(max_length=255, null=True, blank=True)
    bad_image = models.CharField(max_length=32, null=True, blank=True)
    error_code = models.IntegerField(null=True, blank=True)
    addresses = models.ManyToManyField(Address, through='RegistrantAddress', null=True, blank=True)


class RegistrantAddress(models.Model):
    ADDR_TYPE_CHOICES = (
        ('current', 'current address'),
        ('mailing', 'mailing address'),
        ('previous', 'previous address'),
    )
    registrant = models.ForeignKey(Registrant)
    address = models.ForeignKey(Address)
    address_type = models.CharField(max_length=20, choices=ADDR_TYPE_CHOICES)
    
