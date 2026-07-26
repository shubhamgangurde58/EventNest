from django.shortcuts import render, redirect
from .models import Event
from .forms import EventForm


# Home Page
def home(request):
    return render(request, "home.html")


# Event List
def event_list(request):
    events = Event.objects.all()
    return render(request, "events/event_list.html", {
        "events": events
    })


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