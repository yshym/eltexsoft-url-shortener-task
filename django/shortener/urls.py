from django.urls import path

from .views import ShortURLRedirectView


urlpatterns = [
    path('<slug:short_id>', ShortURLRedirectView.as_view(), name='url_redirect'),
]
