from django import forms
from localflavor.us.us_states import US_STATES, STATE_CHOICES
from localflavor.us.forms import USStateField
from models import Type, Client


class ClientSelectionForm(forms.Form):
    client = forms.ModelChoiceField(queryset=Client.objects.all())

    def __init__(self, *args, **kwargs):
        queryset = Client.objects.all()
        if 'user' in kwargs:
            queryset = kwargs['user'].contact.client_set.all()
            del kwargs['user']

        super(ClientSelectionForm, self).__init__(*args, **kwargs)
        self.fields['client'].queryset = queryset

#class PartForm(forms.ModelForm):
class PartForm(forms.Form):
    state = USStateField(widget=forms.Select(choices=(('', 'Select a State'),)+US_STATES))
    form_type = forms.ModelChoiceField(queryset=Type.objects.all())  
    num_items = forms.IntegerField()
    num_batches = forms.IntegerField()
    
    def __init__(self, *args, **kwargs):
        self.project_id = kwargs.pop('project_id', None)
        #del kwargs['project_id']
        super(PartForm, self).__init__(*args, **kwargs)
        if self.project_id:
            self.fields['form_type'].queryset = Type.objects.filter(project_id=self.project_id)

class BatchUploadForm(forms.Form):
    #some logic to get associated Part ID
    #dt now 
    item_count = forms.IntegerField()
    batch_file = forms.FileField()
    

"""
#StackOverflow sample
class AccountDetailsForm(forms.Form):
    
    adminuser = forms.ModelChoiceField(queryset=User.objects.all())
    def __init__(self, *args, **kwargs):
        accountid = kwargs.pop('accountid', None)
        super(AccountDetailsForm, self).__init__(*args, **kwargs)

        if accountid:
            self.fields['adminuser'].queryset = User.objects.filter(account=accountid)

form = AccountDetailsForm(accountid=3)
"""
"""
#IN VIEWS. NOT FORMS. 
def get(self, request, *args, **kwargs):
    context = self.get_context_data(*args, **kwargs)
    proejct_id = request.GET.get('project_id', None)

    if not project_id:
        pass

    form = OrderForm(project_id=project_id)
    context['form'] = form
    self.render_to_response(context)
"""
