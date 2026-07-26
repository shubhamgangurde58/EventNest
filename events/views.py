from django.shortcuts import render, redirect, get_object_or_404
from .models import Event
from .forms import EventForm
from django.db.models import Q

# Home Page
def home(request):
    return render(request, "home.html")


# Event List
def event_list(request):

    query = request.GET.get("q")

    if query:

        events = Event.objects.filter(

            Q(title__icontains=query) |
            Q(category__icontains=query) |
            Q(venue__icontains=query) |
            Q(organizer__icontains=query)

        )

    else:

        events = Event.objects.all()

    return render(
        request,
        "events/event_list.html",
        {
            "events": events,
            "query": query
        }
    )


# Add Event
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