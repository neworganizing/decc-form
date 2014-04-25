from django.contrib import messages
from django.views.generic import TemplateView, CreateView, DetailView
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render_to_response
from django.forms.formsets import formset_factory
#from braces.views import LoginRequiredMixin

from .models import Order, Part, Client, Type, Batch, Project
from .forms import ClientSelectionForm, PartForm, BatchUploadForm, BatchFormSet
import datetime as dt


#first arg: LoginRequiredMixin
class OrderView(TemplateView):
    
    def get(self, request, *args, **kwargs):
        context = super(OrderView, self).get_context_data(*args, **kwargs)
        context['form'] = ClientSelectionForm(user=request.user)
        return self.render_to_response(context)
        
    def post(self, request, *args, **kwargs):
        context = super(OrderView, self).get_context_data(*args, **kwargs)
        context['form'] = ClientSelectionForm(request.POST)
        
        if context['form'].is_valid():
            client = context['form'].cleaned_data['client']
            if client:
                project_id = client.project_id
        else:
            return self.render_to_response(context)

        order_data = {
            'project_id': project_id,
            'order_date': dt.datetime.today()
        }

        order = Order(**order_data)
        order.save()
        return HttpResponseRedirect('/order/{0}/part/'.format(order.id))


class PartView(TemplateView):
    form_class = PartForm

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(*args, **kwargs)

        try:
            order = Order.objects.get(pk=kwargs['order_id'])
        except Order.DoesNotExist:
            raise Http404
        
        form = PartForm(project_id=order.project_id)
        context['form'] = form
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(*args, **kwargs)
        form = PartForm(request.POST)

        if form.is_valid():
            order = Order.objects.get(pk=kwargs.pop('order_id', None))
            state = request.POST.get('state')
            form_type = Type.objects.get(pk=request.POST.get('form_type'))
            item_count = request.POST.get('num_items')
            batch_count = request.POST.get('num_batches')
            rush = request.POST.get('rush', False)
            part = Part(order=order, state=state, form_type=form_type, item_count=item_count, batch_count=batch_count, rush=rush)
            part.save()
            return HttpResponseRedirect('/order/{0}/part/{1}/batch/'.format(part.order.id, part.id))
        else:
            print form.errors

            return self.render_to_response(context)


class BatchView(TemplateView):
   
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(*args, **kwargs)
        items = Part.objects.get(pk=kwargs['part_id']).batch_count 
        print 'items: {}'.format(items)
        initial = []
        for i in range(items):
            initial.append({'part': kwargs['part_id']})
        project_id = Order.objects.get(pk=kwargs['order_id']).project_id
        BatchUploadFormSet = formset_factory(BatchUploadForm, extra=0, formset=BatchFormSet)
        formset  = BatchUploadFormSet(initial=initial, project_id=project_id)
        context['formset'] = formset
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        context = super(BatchView, self).get_context_data(*args, **kwargs)
        BatchUploadFormSet = formset_factory(BatchUploadForm, extra=0, formset=BatchFormSet)
        formset = BatchUploadFormSet(request.POST, request.FILES)
        context['formset'] = formset
        
        if formset.is_valid():
            for form in formset:
                print 'form'
                part = Part.objects.get(pk=form.cleaned_data['part'])
                client_filename = form.cleaned_data['client_filename']
                item_count = form.cleaned_data['item_count']
                batch = Batch(part=part, client_filename=client_filename, item_count=item_count)
                batch.save()
            return HttpResponseRedirect('/thanks/')
        else:
            return self.render_to_response(context)
    