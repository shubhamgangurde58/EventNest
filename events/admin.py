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

    search_fields = (
        "title",
        "organizer",
        "venue",
    )

    list_filter = (
        "category",
        "status",
        "event_date",
    )

    ordering = ("event_date",)