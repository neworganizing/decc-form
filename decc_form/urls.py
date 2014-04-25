from django.conf.urls import patterns, include, url
import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^order/(?P<order_id>[0-9]+)/part/(?P<part_id>[0-9]+)/batch/$', views.BatchView.as_view(template_name='decc_form/batch_form.html'), name='batch'),
    url(r'^order/(?P<order_id>[0-9]+)/part/$', views.PartView.as_view(template_name='decc_form/part_form.html'), name='part'),
    url(r'^order/$', views.OrderView.as_view(template_name='decc_form/order_form.html'), name='order'),
    #url(r'^thanks/$', views.ThanksView.as_view(template_name='form/thanks.html'), name='thanks'),


    url(r'^admin/', include(admin.site.urls)),
)
