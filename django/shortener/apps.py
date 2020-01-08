from django.apps import AppConfig


class ShortenerConfig(AppConfig):
    name = 'shortener'

    def ready(self):
        from . import signals
