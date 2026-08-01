from django.http import request
from django.shortcuts import render, redirect, get_object_or_404
from django.template import context
from .models import Event
from .forms import EventForm
from django.db.models import Q
from django.utils.timezone import now
from django.core.paginator import Paginator
from django.db.models import Q
from django.utils.timezone import now
from django.contrib.auth.decorators import login_required
from accounts.decorators import admin_required

# Home Page
def home(request):
    return render(request, "home.html")


def event_list(request):

    query = request.GET.get("q", "")
    category = request.GET.get("category", "")

    events = Event.objects.all()

    if query:
        events = events.filter(
            Q(title__icontains=query) |
            Q(category__icontains=query) |
            Q(venue__icontains=query) |
            Q(organizer__icontains=query)
        )

    if category:
        events = events.filter(category=category)

    paginator = Paginator(events, 5)

    page_number = request.GET.get("page")

    page_obj = paginator.get_page(page_number)

    context = {

        "events": page_obj,

        "page_obj": page_obj,

        "query": query,

        "selected_category": category,

        "categories": Event.CATEGORY_CHOICES,

        "total_events": Event.objects.count(),

        "active_events": Event.objects.filter(status=True).count(),

        "upcoming_events": Event.objects.filter(
            event_date__gte=now().date()
        ).count(),

    }

    return render(
        request,
        "events/event_list.html",
        context
    )



# Add Event
@login_required
@admin_required
def add_event(request):

    if request.method == "POST":

        form = EventForm(request.POST, request.FILES)

        if form.is_valid():

            print("FORM VALID")
            print(request.FILES)

            form.save()

            return redirect("event_list")

        else:

            print("FORM INVALID")
            print(form.errors)

    else:

        form = EventForm()

    return render(request,
                  "events/add_event.html",
                  {"form": form})


def event_detail(request, id):
    event = get_object_or_404(Event, id=id)

    return render(
        request,
        "events/event_detail.html",
        {"event": event}
    )

@login_required
@admin_required
def edit_event(request, id):

    event = get_object_or_404(Event, id=id)

    if request.method == "POST":

        form = EventForm(
            request.POST,
            request.FILES,
            instance=event
        )

        if form.is_valid():

            form.save()

            return redirect("event_list")

    else:

        form = EventForm(instance=event)

    return render(
        request,
        "events/edit_event.html",
        {
            "form": form,
            "event": event
        }
    )

@login_required
@admin_required
def delete_event(request, id):

    event = get_object_or_404(Event, id=id)

    if request.method == "POST":

        event.delete()

        return redirect("event_list")

    return render(
        request,
        "events/delete_event.html",
        {
            "event": event
        }
    )


   