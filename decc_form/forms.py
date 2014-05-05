from django import forms
from django.forms.formsets import BaseFormSet
from django.utils.functional import cached_property

from localflavor.us.forms import USStateField
from localflavor.us.us_states import US_STATES

from models import Client, Committee, Part, Project, Type


class ClientSelectionForm(forms.Form):
    client = forms.ModelChoiceField(queryset=Client.objects.all())

    def __init__(self, *args, **kwargs):
        queryset = Client.objects.all()
        if 'user' in kwargs:
            queryset = kwargs['user'].contact.client_set.all()
            del kwargs['user']

        super(ClientSelectionForm, self).__init__(*args, **kwargs)
        self.fields['client'].queryset = queryset


class PartForm(forms.ModelForm):
    class Meta:
        model = Part    
        fields = ['order', 'state', 'form_type', 'item_count', 
                  'batch_count', 'rush', 'van', 'quad', 'match']
    state = USStateField(widget=forms.Select(choices=(('', 'Select a State'),)+US_STATES))
    form_type = forms.ModelChoiceField(queryset=Type.objects.all())  

    def __init__(self, *args, **kwargs):
        self.project_id = kwargs.pop('project_id', None)
        self.order = kwargs.pop('order', None)
        super(PartForm, self).__init__(*args, **kwargs)
        self.fields['order'].widget = forms.HiddenInput()
        self.fields['order'].label = ''
        self.fields['order'].initial = self.order
        if self.project_id:
            self.fields['form_type'].queryset = Type.objects.filter(project_id=self.project_id)
            

class BatchFormSet(BaseFormSet):
    @cached_property
    def forms(self):
        forms = [self._construct_form(i, queryset=self.queryset, visible=self.visible) for i in xrange(self.total_form_count())]
        return forms

    def __init__(self, *args, **kwargs):
        self.project_id = kwargs.pop('project_id', None)
        self.visible = kwargs.pop('visible', None)
        super(BatchFormSet, self).__init__(*args, **kwargs)
        if self.project_id:
            project = Project.objects.get(pk=self.project_id)
            self.queryset = project.committee_set.all()
        

class BatchUploadForm(forms.Form):
    part = forms.IntegerField(widget=forms.HiddenInput())
    committee = forms.ModelChoiceField(queryset=Committee.objects.all(), label='If applicable, select your VAN Committee')
    item_count = forms.IntegerField(required=True)
    client_filename = forms.FileField(required=True)

    def __init__(self, *args, **kwargs):
        self.queryset = kwargs.pop('queryset', None)
        self.visible = kwargs.pop('visible', None)
        super(BatchUploadForm, self).__init__(*args, **kwargs)
        if self.visible:
            self.fields['committee'].queryset = self.queryset
        else:
            self.fields['committee'].widget=forms.HiddenInput()
            self.fields['committee'].label = ''
            self.fields['committee'].required=False
            

