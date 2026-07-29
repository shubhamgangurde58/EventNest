from django.db import models
from events.models import Event


class Registration(models.Model):

    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("Confirmed", "Confirmed"),
        ("Cancelled", "Cancelled"),
    ]

    YEAR_CHOICES = [
        ("FY", "FY"),
        ("SY", "SY"),
        ("TY", "TY"),
        ("Final", "Final"),
    ]

    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name="registrations"
    )

    full_name = models.CharField(max_length=150)

    email = models.EmailField()

    phone = models.CharField(max_length=15)

    college = models.CharField(max_length=200)

    department = models.CharField(max_length=100)

    year = models.CharField(
        max_length=20,
        choices=YEAR_CHOICES
    )

    registration_date = models.DateTimeField(auto_now_add=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Pending"
    )

    class Meta:
        ordering = ["-registration_date"]

        constraints = [
            models.UniqueConstraint(
                fields=["event", "email"],
                name="unique_event_registration"
            )
        ]

    def __str__(self):
        return f"{self.full_name} - {self.event.title}"