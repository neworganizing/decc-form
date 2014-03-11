from django.db import models

class Address(models.Model):
    street1 = models.CharField(max_length=255)
    street2 = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=32)

    def __str__(self):
        return str(self.street1 + self.city +','+self.state)

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    work_phone = models.CharField(max_length=255)
    cell_phone = models.CharField(max_length=255)
    fax = models.CharField(max_length=255)
    added_date = models.DateField()
    modified_date = models.DateField()

class Client(models.Model):
    org_name = models.CharField(max_length=255)
    added_date = models.DateTimeField()
    modified_date = models.DateTimeField()
    address_id = models.ForeignKey(Address)
    contacts = models.ManyToManyField(Contact, through='ClientContact')
    
    def __str__(self):
        return str(self.org_name)

class ClientContact(models.Model):
    client_id = models.ForeignKey(Client)
    contact_id = models.ForeignKey(Contact)
    order = models.IntegerField()

class Billable(models.Model):
    tax_status = models.CharField(max_length=255)
    added_date = models.DateField()
    modified_date = models.DateField()
    contact_id = models.ForeignKey(Contact)
    address_id = models.ForeignKey(Address)

class Project(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    order_frequency = models.IntegerField()
    estimated_item_count = models.IntegerField()
    notes = models.TextField()
    added_date = models.DateField()
    modified_date = models.DateField()
    client_id = models.ForeignKey(Client)
    billable_id = models.ForeignKey(Billable)

class Type(models.Model):
    type_name = models.CharField(max_length=255)
    field_notes = models.TextField()
    project_id = models.ForeignKey(Project)
    cost_rate = models.DecimalField(max_digits=4, decimal_places=2)
    cost_noi = models.DecimalField(max_digits=5, decimal_places=3)

class Order(models.Model):
    order_date = models.DateField()
    bill_date = models.DateField()
    paid_date = models.DateField()
    project_id = models.ForeignKey(Project)

class Part(models.Model):
    rush = models.BooleanField()
    state = models.CharField(max_length=2)
    item_count = models.IntegerField()
    batch_count = models.IntegerField()
    extras = models.CharField(max_length=255)
    order_id = models.ForeignKey(Order)
    type_id = models.ForeignKey(Type)

class Batch(models.Model):
    #NEEDS SPECIAL PRIMARY KEY
    client_filename = models.CharField(max_length=255)
    vendor_filename = models.CharField(max_length=255)
    item_count = models.IntegerField()
    submission_date = models.DateField()
    processed_date = models.DateField()
    return_date = models.DateField()
    part_id = models.ForeignKey(Part)

class Registrant(models.Model):
    batch_id = models.ForeignKey(Batch)
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
    
