from django.contrib import admin

from .models import ShortURL


@admin.register(ShortURL)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('short_id', 'redirect_url')
    readonly_fields = ('short_id', 'creator_ip', 'transitions_number')
    list_filter = ('redirect_url',)
    search_fields = ('redirect_url',)
