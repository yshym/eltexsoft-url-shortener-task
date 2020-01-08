from django.views.generic import RedirectView

from .models import ShortURL

class ShortURLRedirectView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return ShortURL.objects.get(short_id=kwargs.get('short_id')).redirect_url
