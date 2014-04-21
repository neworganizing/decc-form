from django.contrib import messages
from django.views.generic import TemplateView, CreateView, DetailView
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render_to_response

#from braces.views import LoginRequiredMixin

from .models import Order, Part, Client, Type
from .forms import ClientSelectionForm, PartForm, BatchUploadForm
import datetime as dt

class IndexView(TemplateView):
    template_name = 'index.html'

class ThanksView(TemplateView):
    template_name = 'thanks.html'
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
        form = PartForm(request.POST)

        if form.is_valid():
            order = Order.objects.get(pk=kwargs.pop('order_id', None))
            state = request.POST.get('state')
            form_type = Type.objects.get(pk=request.POST.get('form_type'))
            item_count = request.POST.get('num_items')
            batch_count = request.POST.get('num_batches')
            part = Part(order=order, state=state, form_type=form_type, item_count=item_count, batch_count=batch_count, rush=False)
            part.save()
            return HttpResponseRedirect('/order/{0}/part/{1}/batch/'.format(part.order.id, part.id))
        else:
            return self.render_to_response(context)

class BatchView(TemplateView):

    def post(self, request, *args, **kwargs):
        context = super(BatchView, self).get_context_data(*args, **kwargs)
        form = BatchUploadForm(request.POST, request.FILES)

        if form.is_valid():
            handle_upload(request.FILES['batch_file'])
            return HttpResponseRedirect('/thanks/')
        else:
            form = BatchUploadForm()
        return render_to_response(context)
            
"""
Django Docs
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return render_to_response('upload.html', {'form': form})
"""
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
