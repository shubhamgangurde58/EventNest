from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm


def register(request):

    if request.method == "POST":

        form = UserRegisterForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            user = form.save()

            login(request, user)

            messages.success(
                request,
                "Account Created Successfully."
            )

            return redirect("dashboard")

    else:

        form = UserRegisterForm()

    return render(
        request,
        "accounts/register.html",
        {
            "form": form
        }
    )


def login_view(request):

    if request.method == "POST":

        username = request.POST.get("username")

        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user:

            login(request, user)

            return redirect("dashboard")

        messages.error(
            request,
            "Invalid Username or Password."
        )

    return render(
        request,
        "accounts/login.html"
    )


def logout_view(request):

    logout(request)

    messages.success(
        request,
        "Logout Successful."
    )

    return redirect("login")



@login_required
def profile(request):

    return render(

        request,

        "accounts/profile.html",

        {

            "user": request.user

        }

    )


@login_required
def edit_profile(request):

    if request.method == "POST":

        form = UserProfileForm(

            request.POST,

            request.FILES,

            instance=request.user

        )

        if form.is_valid():

            form.save()

            messages.success(

                request,

                "Profile Updated Successfully."

            )

            return redirect("profile")

    else:

        form = UserProfileForm(

            instance=request.user

        )

    return render(

        request,

        "accounts/edit_profile.html",

        {

            "form": form

        }

    )