from django.contrib import messages
from django.views.generic import TemplateView, CreateView, DetailView

#from braces.views import LoginRequiredMixin

from .models import Part, Order

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

            
    def post(self, request, *args, **kwargs):
        context = super(OrderView, self).get_context_data(*args, **kwargs)

        default_order_data = {
            'project_id': request.user.project_id,
            'order_date': dt.datetime.today()
        }

        form = get_form(request.POST, initial=default_order_data)

        if form.is_valid():
            order = form.save()
            #TODO: add specific order_id to url
            return HttpResponsRedirect('/order/{0}/part/'.format(order_id))
        #else: 

class PartView(TemplateView):

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(*args, **kwargs)
        project_id = request.GET.get('project_id', None)
        
        if not project_id:
            pass
            
        form = OrderForm(project_id=project_id)
        context['form'] = form
        self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        

        if form.is_valid():
            part = form.save()

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
