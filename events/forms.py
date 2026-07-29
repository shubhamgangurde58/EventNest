from django import forms
from .models import Event


class EventForm(forms.ModelForm):

    class Meta:

        model = Event

        fields = "__all__"

        widgets = {

            "title": forms.TextInput(attrs={
                "class": "form-control"
            }),

            "category": forms.Select(attrs={
                "class": "form-select"
            }),

            "organizer": forms.TextInput(attrs={
                "class": "form-control"
            }),

            "venue": forms.TextInput(attrs={
                "class": "form-control"
            }),

            "event_date": forms.DateInput(attrs={
                "type": "date",
                "class": "form-control"
            }),

            "registration_deadline": forms.DateInput(attrs={
                "type": "date",
                "class": "form-control"
            }),

            "start_time": forms.TimeInput(attrs={
                "type": "time",
                "class": "form-control"
            }),

            "end_time": forms.TimeInput(attrs={
                "type": "time",
                "class": "form-control"
            }),

            "total_seats": forms.NumberInput(attrs={
                "class": "form-control"
            }),

            "available_seats": forms.NumberInput(attrs={
                "class": "form-control"
            }),

            "description": forms.Textarea(attrs={
                "rows": 5,
                "class": "form-control"
            }),

            "event_banner": forms.ClearableFileInput(attrs={
                "class": "form-control"
            }),

            "status": forms.CheckboxInput(attrs={
                "class": "form-check-input"
            }),

        }