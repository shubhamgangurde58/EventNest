from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db import IntegrityError

from events.models import Event
from .models import Registration
from .forms import RegistrationForm
from django.db.models import Q


def register_event(request, event_id):

    event = get_object_or_404(Event, id=event_id)

    if not event.status:
        messages.error(request, "Registration Closed.")
        return redirect("event_detail", id=event.id)

    if event.available_seats <= 0:
        messages.error(request, "No seats available.")
        return redirect("event_detail", id=event.id)

    if request.method == "POST":

        form = RegistrationForm(request.POST)

        if form.is_valid():

            email = form.cleaned_data["email"].strip().lower()

            if Registration.objects.filter(
                event=event,
                email__iexact=email
            ).exists():

                messages.warning(
                    request,
                    "You have already registered for this event."
                )

                return redirect("event_detail", id=event.id)

            registration = form.save(commit=False)
            registration.event = event
            registration.email = email

            try:
                registration.save()

                event.available_seats -= 1
                event.save()
                messages.success(
                    request,
                    "Registration Successful."

                )

            except IntegrityError:

                messages.warning(
                    request,
                    "You have already registered for this event."
                )

            return redirect("event_detail", id=event.id)

    else:

        form = RegistrationForm()

    return render(
        request,
        "registrations/register_event.html",
        {
            "form": form,
            "event": event
        }
    )

def cancel_registration(request, id):

    registration = get_object_or_404(
        Registration,
        id=id
    )

    if request.method == "POST":

        if registration.status != "Cancelled":

            registration.status = "Cancelled"
            registration.save()

            event = registration.event
            event.available_seats += 1
            event.save()

            messages.success(
                request,
                "Registration Cancelled Successfully."
            )

        return redirect("registration_list")

    return render(
        request,
        "registrations/cancel_registration.html",
        {
            "registration": registration
        }
    )



def registration_list(request):

    query = request.GET.get("q", "")

    registrations = Registration.objects.select_related("event")

    if query:

        registrations = registrations.filter(

            Q(full_name__icontains=query) |
            Q(email__icontains=query) |
            Q(event__title__icontains=query)

        )

    return render(

        request,

        "registrations/registration_list.html",

        {

            "registrations": registrations,

            "query": query

        }

    )


def registration_detail(request, id):

    registration = get_object_or_404(

        Registration,

        id=id

    )

    return render(

        request,

        "registrations/registration_detail.html",

        {

            "registration": registration

        }

    )

def update_registration_status(request, id, status):

    registration = get_object_or_404(
        Registration,
        id=id
    )

    if status in ["Pending", "Confirmed", "Cancelled"]:

        if registration.status != "Cancelled" and status == "Cancelled":

            registration.event.available_seats += 1
            registration.event.save()

        elif registration.status == "Cancelled" and status != "Cancelled":

            if registration.event.available_seats > 0:
                registration.event.available_seats -= 1
                registration.event.save()

        registration.status = status
        registration.save()

        messages.success(
            request,
            "Registration Status Updated Successfully."
        )

    return redirect("registration_detail", id=registration.id)