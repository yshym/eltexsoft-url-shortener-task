from rest_framework.generics import (
    CreateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
)
from rest_framework.permissions import BasePermission

from .models import ShortURL
from .serializers import (
    ShortURLCreateSerializer,
    ShortURLStatsRetrieveSerializer,
)
from .utils import client_ip


class IsCreator(BasePermission):
    message = 'Only creator of the url is able to view stats.'

    def has_permission(self, request, view):
        return client_ip(request) == view.get_object().creator_ip



class ShortURLCreateAPIView(CreateAPIView):
    serializer_class = ShortURLCreateSerializer


class ShortURLStatsRetrieveAPIView(RetrieveAPIView):
    model = ShortURL
    serializer_class = ShortURLStatsRetrieveSerializer
    permission_classes = [IsCreator]

    def get_object(self):
        obj = self.model.objects.get(short_id=self.kwargs.get('short_id'))
        return obj
