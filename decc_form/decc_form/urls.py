from django.conf.urls import patterns, include, url
from form import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'decc_form.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^order/(?P<order_id>[0-9]+)/part/(?P<part_id>[0-9]+)/batch/$', views.BatchView.as_view(template_name='batch_form.html'), name='batch'),
    url(r'^order/(?P<order_id>[0-9]+)/part/$', views.PartView.as_view(template_name='part_form.html'), name='part'),
    url(r'^order/$', views.OrderView.as_view(template_name='order_form.html'), name='order'),
    url(r'^thanks/$', views.ThanksView.as_view(template_name='thanks.html'), name='thanks'),


    url(r'^admin/', include(admin.site.urls)),
)
