from django import forms
from .models import Registration


class RegistrationForm(forms.ModelForm):

    class Meta:
        model = Registration

        fields = [
            "full_name",
            "email",
            "phone",
            "college",
            "department",
            "year",
        ]

        widgets = {
            "full_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter Full Name"
            }),

            "email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "Enter Email"
            }),

            "phone": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter Mobile Number"
            }),

            "college": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "College Name"
            }),

            "department": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Department"
            }),

            "year": forms.Select(attrs={
                "class": "form-select"
            }),
        }