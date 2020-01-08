from django.contrib import admin

from .models import ShortURL


@admin.register(ShortURL)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('short_id', 'redirect_url')
    readonly_fields = ('short_id',)
    list_filter = ('redirect_url',)
    search_fields = ('redirect_url',)
