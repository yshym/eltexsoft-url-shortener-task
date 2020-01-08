from django.db import models

import uuid


class ShortURL(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    redirect_url = models.URLField()
    short_id = models.CharField(blank=True, max_length=6)

    def __str__(self):
        return self.short_id
