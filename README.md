#DECC Website

##Setup
Add the following details to an email-settings file before deploy 

```
EMAIL_USE_TLS = EMAIL_USE_TLS
EMAIL_HOST = EMAIL_HOST
EMAIL_HOST_USER = EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = EMAIL_HOST_PASSWORD
EMAIL_PORT = EMAIL_PORT
```

##Overview
This is a online form to help automate DECC order processing. Clients can fill out their form and upload their files here. Upon completion, confirmation emails will be sent to the Client and to the DECC team (decc@neworganizing.com). 

##Models

**Address**

Contains general address information.

**Contact**

Links to the Django auth_user, where name, email and pw are stored.
Contains supplemental user data.

**Billable**

Includes references to Contact, Address.
Provides tax status for the partner org.

**Project**

Project is the top level representation of a DECC order.
Represented by start and end dates.
References Billable.

**Client**

Represents the actual DECC client (read: organization).
References a single, specific Project.

**ClientContact**

Clients have a first contact and a second contact, ranked according to priority.
Contacts may belong to multiple organizations.

**Type**

Projects have different types associated with them (eg. Voter Registration Card).
Each type of processing has costs associated with it.
cost_rate is the cost charged to the client, cost_noi is the charge to NOI from the vendor.

**Committee**

Represents an organization in VAN that a project may be associated with.

**Order**

References Project
One level below Project, Order is the first thing created with the web form.
It mostly just represents the dates associated with the order.
`digital` defaults to True for the online submit form, paper entries will be submitted manually and should be False.

**Part**

References Order
Each order may have multiple associated Parts
Part contains the important details about the order
Clients can specify the following:
- `form_type`: the type of form they are submitting (which is pre-populated and specific to their Project)
- `state`: 2 letter state abbreviation 
- `batch_count`: the number of file uploads, or batches, associated with this Part
- `item_count`: the number of individual cards/forms in total 
- `van`: whether or not the batches will be associated with VAN Committees
- `rush`: whether or not the part must be rushed, which will cost more
- `quad`: whether or not the part will involved Quad processing 
- `match`: whether or not the part should be matched to any vendor files (eg. Catalist)
- `destroy_files`: whether or not the files should be destroyed securely (PAPER RECORDS ONLY)
- `return_files`: whether or not the files should be returned to the org (PAPER RECORDS ONLY)


**Batch**

References Part.
Each part may have multiple associated Batches.
These are the actual file uploads with the data that will be processed.
If `van` is true in the Batch's Part, the specific committee will be chosen here.
`item_count` is confirmed here.
`client_filename` is whatever the client named their file, preserving their naming system.
`save()` calculates the `id` and `vendor_filename`.
`vendor_filename` is a 10 digit value calculated based on the 3 digit Client id and a 7 digit batch id. The batch id is incrememted each time a new batch is uploaded to the Project. The `id` is the `vendor_filename` without the .pdf extension and cast to an integer (which means that the prepended 0s will be gone).

**Registrant**

This model contains all the data that is actually found on the cards/forms in the batches.
Formatting may be inconsistent, so all fields are chars and null.

**RegistrantAddress**

ManyToMany field allowing one address model to be used for the various needs throughout this database.

##Views
**OrderView**





##Tasks




