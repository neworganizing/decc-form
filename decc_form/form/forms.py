from django import forms
from django.contrib.localflavor import US
from models import Type

#class PartForm(forms.ModelForm):
class PartForm(forms.Form):
    state = forms.USStateField() #forms.CharField(max_length=255) #eventual choice drop down
    form_type = forms.ModelChoiceField(queryset=Type.objects.filter(project_id=self.project_id))#forms.CharField(max_length=255) #eventual fill w/user specific options
    num_items = forms.IntegerField()
    num_batches = forms.IntegerField()
    
    def __init__(self, *args, **kwargs):
        self.project_id = kwargs['project_id']
        del kwargs['project_id']
        super(PartForm, self).__init__(*args, **kwargs)


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
