from django.shortcuts import render
from django.utils.timezone import now

from events.models import Event
from registrations.models import Registration

from django.contrib.auth.decorators import login_required

from accounts.decorators import faculty_required

from django.db.models import Count
from django.db.models.functions import TruncMonth
from django.contrib.auth.decorators import login_required
from accounts.decorators import faculty_required
import json


def home(request):
    return render(request, "dashboard/home.html")

    
@login_required(login_url="login")
def dashboard(request):

    total_events = Event.objects.count()

    active_events = Event.objects.filter(
        status=True
    ).count()

    upcoming_events = Event.objects.filter(
        event_date__gte=now().date()
    ).count()

    total_registrations = Registration.objects.count()

    confirmed = Registration.objects.filter(
        status="Confirmed"
    ).count()

    pending = Registration.objects.filter(
        status="Pending"
    ).count()

    cancelled = Registration.objects.filter(
        status="Cancelled"
    ).count()

    recent_registrations = (
        Registration.objects
        .select_related("event")
        .order_by("-registration_date")[:5]
    )

    upcoming = (
        Event.objects
        .filter(
            event_date__gte=now().date(),
            status=True
        )
        .order_by("event_date")[:5]
    )

    monthly_data = (
        Registration.objects
        .annotate(month=TruncMonth("registration_date"))
        .values("month")
        .annotate(total=Count("id"))
        .order_by("month")
    )

    months = []
    totals = []

    for item in monthly_data:
        months.append(item["month"].strftime("%b"))
        totals.append(item["total"])


    status_labels = [
        "Confirmed",
        "Pending",
        "Cancelled"
    ]

    status_counts = [
        confirmed,
        pending,
        cancelled
    ]

    context = {
        "total_events": total_events,
        "active_events": active_events,
        "upcoming_events": upcoming_events,
        "total_registrations": total_registrations,
        "confirmed": confirmed,
        "pending": pending,
        "cancelled": cancelled,
        "recent_registrations": recent_registrations,
        "upcoming": upcoming,
        "chart_months": json.dumps(months),
        "chart_totals": json.dumps(totals),
        "status_labels": json.dumps(status_labels),
        "status_counts": json.dumps(status_counts),
    }

    return render(
        request,
        "dashboard/dashboard.html",
        context
    )