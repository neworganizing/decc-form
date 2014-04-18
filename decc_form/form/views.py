from django.contrib import messages
from django.views.generic import TemplateView, CreateView, DetailView
from django.http import HttpResponseRedirect, Http404

#from braces.views import LoginRequiredMixin

from .models import Order, Part, Client
from .forms import ClientSelectionForm, PartForm
import datetime as dt

class IndexView(TemplateView):
    template_name = 'index.html'

"""
#first arg: LoginRequiredMixin
class OrderCreateView(CreateView):
    model = Order
    success_msg = 'Order successfully started'
"""

#first arg: LoginRequiredMixin
class OrderView(TemplateView):
    #template_name = 'order_form.html'

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

        if form.is_valid():
            part = form.save()
            #TODO: figure out order_id save situation 
            #return HttpResponseRedirect('/order/{0}/part{1}/'.format(order_id, part_id))
            return HttpResponseRedirect('/order/X/part{1}/'.format(part_id))
        else:
            return self.render_to_response(context)

"""
#Experiment with CBVs gone horribly wrong

class PartActionMixin(object):
    fields = ('state', 'item_count', 'batch_count', 'type_id')
    
    @property
    def success_msg(self):
        return NotImplemented

    def form_valid(self, form):
        messages.info(self.request, self.success_msg)
        return super(PartActionMixin, self).form_valid(form)

#first arg: LoginRequiredMixin
class PartCreateView(PartActionMixin, CreateView):
    model = Part
    success_msg = 'Part successfully created'

#first arg: LoginRequiredMixin
class PartDetailView(DetailView):
    model = Part

"""
