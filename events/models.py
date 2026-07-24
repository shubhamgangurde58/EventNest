from django.db import models


class Event(models.Model):

    title = models.CharField(max_length=200)

    description = models.TextField()

    venue = models.CharField(max_length=150)

    event_date = models.DateField()

    start_time = models.TimeField()

    end_time = models.TimeField()

    total_seats = models.PositiveIntegerField()

    available_seats = models.PositiveIntegerField()

    event_banner = models.ImageField(
        upload_to='events/',
        blank=True,
        null=True
    )

    status = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title