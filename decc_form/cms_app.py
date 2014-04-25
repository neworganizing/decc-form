from cms.app_base import decc_form
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

class DeccAppHook(decc_form):
    name = _('DECC Apphook')
    urls = ['decc_form.urls']

apphook_pool.register(DeccAppHook)
