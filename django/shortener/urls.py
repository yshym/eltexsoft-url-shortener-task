from django.urls import path

from .views import ShortURLRedirectView
from .apiviews import (
    ShortURLCreateAPIView,
    ShortURLStatsRetrieveAPIView,
    ShortURLDestroyAPIView,
)


urlpatterns = [
    path('api/', ShortURLCreateAPIView.as_view(), name='url_create'),
    path('api/<slug:short_id>/', ShortURLDestroyAPIView.as_view(), name='url_delete'),
    path('api/<slug:short_id>/stats/', ShortURLStatsRetrieveAPIView.as_view(), name='url_stats'),
    path('<slug:short_id>/', ShortURLRedirectView.as_view(), name='url_redirect'),
]
