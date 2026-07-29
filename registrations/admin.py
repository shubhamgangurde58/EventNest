from django.contrib import admin
from .models import Registration


@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "full_name",
        "email",
        "event",
        "college",
        "year",
        "status",
        "registration_date",
    )

    list_filter = (
        "status",
        "year",
        "event",
    )

    search_fields = (
        "full_name",
        "email",
        "phone",
    )