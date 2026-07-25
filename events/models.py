from datetime import date
from django.db import models


class Event(models.Model):

    CATEGORY_CHOICES = [
        ("Workshop", "Workshop"),
        ("Seminar", "Seminar"),
        ("Hackathon", "Hackathon"),
        ("Competition", "Competition"),
        ("Webinar", "Webinar"),
    ]

    title = models.CharField(
        max_length=200
    )

    description = models.TextField()

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default="Workshop"
    )

    organizer = models.CharField(
        max_length=150
    )

    venue = models.CharField(
        max_length=150
    )

    event_date = models.DateField()

    registration_deadline = models.DateField(
        default=date.today
    )

    start_time = models.TimeField()

    end_time = models.TimeField()

    total_seats = models.PositiveIntegerField(
        default=0
    )

    available_seats = models.PositiveIntegerField(
        default=0
    )

    event_banner = models.ImageField(
        upload_to="events/",
        blank=True,
        null=True
    )

    status = models.BooleanField(
        default=True,
        help_text="True = Active, False = Inactive"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ["event_date", "start_time"]
        verbose_name = "Event"
        verbose_name_plural = "Events"

    def __str__(self):
        return self.title