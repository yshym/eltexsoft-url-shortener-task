from rest_framework import serializers

from .models import ShortURL
from .utils import client_ip


class ShortURLCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortURL
        fields = ('redirect_url', 'short_id',)
        read_only_fields = ('short_id',)

    def create(self, validated_data):
        return ShortURL.objects.create(
            redirect_url=validated_data.get('redirect_url'),
            creator_ip=client_ip(self.context.get('request')),
        )


class ShortURLStatsRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortURL
        fields = ('transitions_number',)
        read_only_fields = ('transitions_number',)
