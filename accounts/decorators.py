from functools import wraps

from django.contrib import messages
from django.shortcuts import redirect


def admin_required(view_func):

    @wraps(view_func)
    def wrapper(request, *args, **kwargs):

        if not request.user.is_authenticated:

            messages.warning(
                request,
                "Please login first."
            )

            return redirect("login")

        if request.user.role == "ADMIN":

            return view_func(
                request,
                *args,
                **kwargs
            )

        messages.error(
            request,
            "Access Denied. Admin permission required."
        )

        return redirect("home")

    return wrapper


def faculty_required(view_func):

    @wraps(view_func)
    def wrapper(request, *args, **kwargs):

        if not request.user.is_authenticated:

            messages.warning(
                request,
                "Please login first."
            )

            return redirect("login")

        if request.user.role in [

            "ADMIN",

            "FACULTY"

        ]:

            return view_func(
                request,
                *args,
                **kwargs
            )

        messages.error(
            request,
            "Access Denied. Faculty permission required."
        )

        return redirect("home")

    return wrapper


def student_required(view_func):

    @wraps(view_func)
    def wrapper(request, *args, **kwargs):

        if not request.user.is_authenticated:

            messages.warning(
                request,
                "Please login first."
            )

            return redirect("login")

        if request.user.role == "STUDENT":

            return view_func(
                request,
                *args,
                **kwargs
            )

        messages.error(
            request,
            "Access Denied. Student permission required."
        )

        return redirect("home")

    return wrapper