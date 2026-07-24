from django.contrib import admin
from .models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'title',
        'venue',
        'event_date',
        'available_seats',
        'status',
    )

    list_filter = (
        'status',
        'event_date',
    )

    search_fields = (
        'title',
        'venue',
    )

    ordering = ('-created_at',)