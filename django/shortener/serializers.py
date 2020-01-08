from rest_framework import serializers

from .models import ShortURL


class ShortURLSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortURL
        fields = ('redirect_url', 'short_id',)
        read_only_fields = (
            'short_id',
        )

    def create(self, validated_data):
        return ShortURL.objects.create(
            redirect_url=validated_data.get('redirect_url'),
        )
