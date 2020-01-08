from django.db.models.signals import pre_save

from .models import ShortURL

def pre_save_short_url_receiver(sender, instance, *args, **kwargs):
    instance.short_id = instance.uuid.hex[:6]

pre_save.connect(pre_save_short_url_receiver, sender=ShortURL)
