from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User



class UserRegisterForm(UserCreationForm):

    class Meta:

        model = User

        fields = [

            "first_name",

            "last_name",

            "username",

            "email",

            "phone",

            "department",

            "role",

            "profile_image",

            "password1",

            "password2",

        ]

        widgets = {

            "first_name": forms.TextInput(attrs={
                "class": "form-control"
            }),

            "last_name": forms.TextInput(attrs={
                "class": "form-control"
            }),

            "username": forms.TextInput(attrs={
                "class": "form-control"
            }),

            "email": forms.EmailInput(attrs={
                "class": "form-control"
            }),

            "phone": forms.TextInput(attrs={
                "class": "form-control"
            }),

            "department": forms.TextInput(attrs={
                "class": "form-control"
            }),

            "role": forms.Select(attrs={
                "class": "form-select"
            }),

            "profile_image": forms.FileInput(attrs={
                "class": "form-control"
            }),

        }

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class": "form-control"
        })
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class": "form-control"
        })
    )


class UserProfileForm(forms.ModelForm):

    class Meta:

        model = User

        fields = [

            "first_name",
            "last_name",
            "email",
            "phone",
            "department",
            "profile_image",

        ]

        widgets = {

            "first_name": forms.TextInput(attrs={
                "class": "form-control"
            }),

            "last_name": forms.TextInput(attrs={
                "class": "form-control"
            }),

            "email": forms.EmailInput(attrs={
                "class": "form-control"
            }),

            "phone": forms.TextInput(attrs={
                "class": "form-control"
            }),

            "department": forms.TextInput(attrs={
                "class": "form-control"
            }),

            "profile_image": forms.FileInput(attrs={
                "class": "form-control"
            }),

        }