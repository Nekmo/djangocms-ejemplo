# cms_apps.py
from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _


class PollsApphook(CMSApp):
    name = _("Polls Apphook")

    def get_urls(self, page=None, language=None, **kwargs):
        return ["polls.urls"]  # Ahora el urls de la app se carga con esto

apphook_pool.register(PollsApphook)
