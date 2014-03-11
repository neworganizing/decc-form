from django import forms


#seperate batch upload form? or part of this?

#class OrderForm(forms.ModelForm):
class OrderForm(forms.Form):
    state = forms.CharField(max_length=255) #eventual choice drop down
    form_type = forms.CharField(max_length=255) #eventual fill w/user specific options
    num_items = forms.IntegerField()
    num_batches = forms.IntegerField()
    
