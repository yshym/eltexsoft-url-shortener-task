from django.urls import path

from .views import ShortURLRedirectView
from .apiviews import ShortURLCreateAPIView


urlpatterns = [
    path('api/', ShortURLCreateAPIView.as_view(), name='url_create'),
    path('<slug:short_id>/', ShortURLRedirectView.as_view(), name='url_redirect'),
]
