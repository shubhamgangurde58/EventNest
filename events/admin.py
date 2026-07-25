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
        "start_time",
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
        "event_date",
        "start_time",
    )

    list_per_page = 10

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    fieldsets = (
        ("Event Information", {
            "fields": (
                "title",
                "description",
                "category",
                "organizer",
            )
        }),

        ("Schedule", {
            "fields": (
                "event_date",
                "registration_deadline",
                "start_time",
                "end_time",
            )
        }),

        ("Venue & Seats", {
            "fields": (
                "venue",
                "total_seats",
                "available_seats",
            )
        }),

        ("Banner", {
            "fields": (
                "event_banner",
            )
        }),

        ("Status", {
            "fields": (
                "status",
            )
        }),

        ("System Information", {
            "fields": (
                "created_at",
                "updated_at",
            )
        }),
    )