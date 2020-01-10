from rest_framework.generics import (
    CreateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
)
from rest_framework.response import Response

from .models import ShortURL
from .serializers import (
    ShortURLSerializer,
    ShortURLStatsRetrieveSerializer,
)
from .utils import client_ip
from .permissions import IsCreator


class ShortURLCreateAPIView(CreateAPIView):
    serializer_class = ShortURLSerializer


class ShortURLStatsRetrieveAPIView(RetrieveAPIView):
    queryset = ShortURL.objects.all()
    serializer_class = ShortURLStatsRetrieveSerializer
    permission_classes = [IsCreator]
    lookup_field = 'short_id'


class ShortURLDestroyAPIView(DestroyAPIView):
    queryset = ShortURL.objects.all()
    permission_classes = [IsCreator]
    lookup_field = 'short_id'
