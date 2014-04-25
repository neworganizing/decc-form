from django.db import models
from django.conf import settings 
import datetime

class Address(models.Model):
    street1 = models.CharField(max_length=255)
    street2 = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=32)

    def __unicode__(self):
        return str(self.street1 + self.city +','+self.state)


class Contact(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    #in user
    #name = models.CharField(max_length=255)
    #email = models.CharField(max_length=255)
    work_phone = models.CharField(max_length=255)
    cell_phone = models.CharField(max_length=255)
    fax = models.CharField(max_length=255)
    added_date = models.DateField()
    modified_date = models.DateField()


class Billable(models.Model):
    contact = models.ForeignKey(Contact)
    address = models.ForeignKey(Address)
    tax_status = models.CharField(max_length=255)
    added_date = models.DateField()
    modified_date = models.DateField()

   
class Project(models.Model):
    #client = models.ForeignKey(Client)
    billable = models.ForeignKey(Billable)
    start_date = models.DateField()
    end_date = models.DateField()
    order_frequency = models.IntegerField()
    estimated_item_count = models.IntegerField()
    notes = models.TextField()
    added_date = models.DateField()
    modified_date = models.DateField()
   
class Client(models.Model):
    address = models.ForeignKey(Address)
    project = models.ForeignKey(Project)
    contacts = models.ManyToManyField(Contact, through='ClientContact')
    org_name = models.CharField(max_length=255)
    added_date = models.DateTimeField()
    modified_date = models.DateTimeField()
       
    def __unicode__(self):
        return str(self.org_name)


class ClientContact(models.Model):
    client = models.ForeignKey(Client)
    contact = models.ForeignKey(Contact)
    order = models.IntegerField()

    
class Type(models.Model):
    project = models.ForeignKey(Project)
    type_name = models.CharField(max_length=255)
    field_notes = models.TextField()
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
    bill_date = models.DateField(null=True, blank=True)
    paid_date = models.DateField(null=True, blank=True)
    

class Part(models.Model):
    order = models.ForeignKey(Order)
    form_type = models.ForeignKey(Type)
    rush = models.BooleanField()
    state = models.CharField(max_length=2)
    item_count = models.IntegerField()
    batch_count = models.IntegerField()
    extras = models.CharField(max_length=255)

    
class Batch(models.Model):
    #PK = 3 digit client_id, 7 digit batch_id, based on last batch from that project
    id = models.PositiveIntegerField(primary_key=True)
    part = models.ForeignKey(Part) 
    committee = models.ForeignKey(Committee, null=True, blank=True)
    client_filename = models.FileField(upload_to='batchfiles/')
    vendor_filename = models.CharField(max_length=255)
    item_count = models.IntegerField()
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
    citizenship = models.CharField(max_length=255)
    age = models.CharField(max_length=10)
    dob_mm = models.CharField(max_length=2)
    dob_dd = models.CharField(max_length=2)
    dob_yy = models.CharField(max_length=4)
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    suffix = models.CharField(max_length=64)
    home_area_code = models.CharField(max_length=16)
    home_phone = models.CharField(max_length=32)
    race = models.CharField(max_length=255)
    party = models.CharField(max_length=255)
    gender = models.CharField(max_length=64)
    date_signed_mm = models.CharField(max_length=2)
    date_signed_dd = models.CharField(max_length=2)
    date_signed_yy = models.CharField(max_length=4)
    mobile_area_code = models.CharField(max_length=16)
    mobile_phone = models.CharField(max_length=32)
    email_address = models.CharField(max_length=255)
    volunteer = models.CharField(max_length=255)
    previous_name = models.CharField(max_length=255)
    bad_image = models.CharField(max_length=32)
    error_code = models.IntegerField()
    addresses = models.ManyToManyField(Address, through='RegistrantAddress')


class RegistrantAddress(models.Model):
    ADDR_TYPE_CHOICES = (
        ('current', 'current address'),
        ('mailing', 'mailing address'),
        ('previous', 'previous address'),
    )
    registrant = models.ForeignKey(Registrant)
    address = models.ForeignKey(Address)
    address_type = models.CharField(max_length=20, choices=ADDR_TYPE_CHOICES)
    
