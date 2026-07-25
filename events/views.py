from django.shortcuts import render


def add_event(request):

    return render(
        request,
        "events/add_event.html"
    )


def event_list(request):

    return render(
        request,
        "events/event_list.html"
    )