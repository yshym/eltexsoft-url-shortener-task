from django.db import models

import uuid


class ShortURL(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    redirect_url = models.URLField()
    short_id = models.CharField(blank=True, max_length=6)
    creator_ip = models.CharField(blank=True, max_length=15)
    transitions_number = models.IntegerField(default=0)

    def __str__(self):
        return self.short_id

    def save(self, *args, **kwargs):
        self.short_id = self.uuid.hex[:6]
        super().save(*args, **kwargs)
