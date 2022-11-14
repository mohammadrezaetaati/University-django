from django import forms

from .models import City, Country


class UniversityForm(forms.Form):

    search = forms.CharField(max_length=255, required=False)
    city = forms.ModelMultipleChoiceField(
        queryset=City.objects.all(), to_field_name="name", required=False
    )
    country = forms.ModelMultipleChoiceField(
        queryset=Country.objects.all(), to_field_name="name", required=False
    )
