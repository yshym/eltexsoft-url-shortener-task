from django.views.generic import RedirectView

from .models import ShortURL

class ShortURLRedirectView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        short_url = ShortURL.objects.get(short_id=kwargs.get('short_id'))
        short_url.transitions_number += 1
        short_url.save()

        return short_url.redirect_url
