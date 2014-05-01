import datetime as dt

from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.forms.formsets import formset_factory
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render_to_response
from django.views.generic import TemplateView

from braces.views import LoginRequiredMixin

from .models import Batch, Order, Part
from .forms import ClientSelectionForm, PartForm, BatchUploadForm, BatchFormSet


class OrderView(LoginRequiredMixin, TemplateView):
    login_url='/users/login'

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


class PartView(LoginRequiredMixin, TemplateView):
    login_url='/users/login'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(*args, **kwargs)

        try:
            order = Order.objects.get(pk=kwargs['order_id'])
        except Order.DoesNotExist:
            raise Http404

        if 'part_id' in kwargs:
            part = Part.objects.get(pk=kwargs['part_id'])
            form = PartForm(instance=part, project_id=order.project_id)
        else:
            form = PartForm(project_id=order.project_id, order=order)

        context['form'] = form
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(*args, **kwargs)
        if 'part_id' in kwargs:
            p = Part.objects.get(pk=kwargs['part_id'])
            form = PartForm(request.POST, instance=p)
        else:
            form = PartForm(request.POST)
        
        if form.is_valid():
            part = form.save()
            return HttpResponseRedirect('/order/{0}/part/{1}/batch/'.format(part.order_id, part.id))
        else:
            print form.errors
            return self.render_to_response(context)


class BatchView(LoginRequiredMixin, TemplateView):
    login_url='/users/login'
   
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(*args, **kwargs)
        
        part = Part.objects.get(pk=kwargs['part_id'])
        context['part'] = part

        items = part.batch_count
        initial = []
        for i in xrange(items):
            initial.append({'part': kwargs['part_id']})

        project_id = Order.objects.get(pk=kwargs['order_id']).project_id
        visible = Part.objects.get(pk=kwargs['part_id']).van

        BatchUploadFormSet = formset_factory(BatchUploadForm, extra=0, formset=BatchFormSet)
        formset  = BatchUploadFormSet(initial=initial, project_id=project_id, visible=visible)

        context['formset'] = formset
        context['link'] = '/order/{0}/part/{1}/edit'.format(part.order_id, part.id)
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        context = super(BatchView, self).get_context_data(*args, **kwargs)
        BatchUploadFormSet = formset_factory(BatchUploadForm, extra=0, formset=BatchFormSet)
        visible = Part.objects.get(pk=kwargs['part_id']).van
        formset = BatchUploadFormSet(request.POST, request.FILES, project_id=Order.objects.get(pk=kwargs['order_id']).project_id, visible=visible)
        context['formset'] = formset
        
        if formset.is_valid():
            for form in formset:
                print 'form'
                part = Part.objects.get(pk=form.cleaned_data['part'])
                client_filename = form.cleaned_data['client_filename']
                item_count = form.cleaned_data['item_count']
                try:
                    committee = form.cleaned_data['committee']
                except:
                    pass
                batch = Batch(part=part, client_filename=client_filename, item_count=item_count, committee=committee)
                batch.save()
                subject = 'Thank you for your DECC Order!'
                message = 'TEST MESSAGE'
                from_email = settings.EMAIL_HOST_USER
                to_list = [request.user.email] #decc@neworganizing.com
                send_mail(subject, message, from_email, to_list, fail_silently=True)
            return HttpResponseRedirect('/thanks/')
        else:
            return self.render_to_response(context)

