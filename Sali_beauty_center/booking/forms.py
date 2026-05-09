from django import forms
from .models import Appointment, Service
from users.models import Employee


class AppointmentForm(forms.ModelForm):
    # multiple services field
    services = forms.ModelMultipleChoiceField(
        queryset=Service.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    class Meta:
        model = Appointment
        fields = ['employee', 'date']