from django.contrib import messages
from django.views.generic import TemplateView, CreateView, DetailView

#from braces.views import LoginRequiredMixin

from .models import Part

class IndexView(TemplateView):
    template_name = 'index.html'

class OrderCreateView(CreateView):
    model = Order
    success_msg = 'Order successfully started'

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

class PartDetailView(DetailView):
    model = Part

