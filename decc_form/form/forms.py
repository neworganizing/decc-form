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


class PartForm(forms.Form):
    state = USStateField(widget=forms.Select(choices=(('', 'Select a State'),)+US_STATES))
    form_type = forms.ModelChoiceField(queryset=Type.objects.all())  
    num_items = forms.IntegerField()
    num_batches = forms.IntegerField()
    rush = forms.BooleanField(label='Check this box if your order must be rushed', required=False)

    def __init__(self, *args, **kwargs):
        self.project_id = kwargs.pop('project_id', None)
        super(PartForm, self).__init__(*args, **kwargs)
        if self.project_id:
            self.fields['form_type'].queryset = Type.objects.filter(project_id=self.project_id)


class BatchUploadForm(forms.Form):
    part = forms.IntegerField(widget=forms.HiddenInput())
    item_count = forms.IntegerField(required=True)
    client_filename = forms.FileField(required=True)

