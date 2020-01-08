from rest_framework.generics import CreateAPIView

from .models import ShortURL
from .serializers import ShortURLSerializer


class ShortURLCreateAPIView(CreateAPIView):
    serializer_class = ShortURLSerializer
