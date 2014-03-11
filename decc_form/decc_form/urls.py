from django.conf.urls import patterns, include, url
from form import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'decc_form.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^order/part/', views.PartCreateView.as_view(template_name='part_form.html'), name='part'),
    url('r^order/', views.OrderCreateView.as_view(template_name='order_form.html'), name='order'),

    url(r'^admin/', include(admin.site.urls)),
)
