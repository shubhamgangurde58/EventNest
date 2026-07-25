from django.contrib import admin
from .models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "category",
        "organizer",
        "venue",
        "event_date",
        "available_seats",
        "status",
    )

    list_filter = (
        "category",
        "status",
        "event_date",
    )

    search_fields = (
        "title",
        "organizer",
        "venue",
    )

    ordering = (
        "-event_date",
    )

    list_per_page = 10