from datetime import date

from django import forms

from dentists.models import Specialization, Dentists


FIELDS = ['name', 'phone_number', 'email', 'address', 'birth_place', 'birth_date', 'specialization']


class DentistsForm(forms.ModelForm):

    class Meta:
        model = Dentists
        fields = FIELDS
    birth_date = forms.DateField(input_formats=['%d-%m-%Y'], initial=date.today().strftime('%d-%m-%Y'), error_messages={"invalid": "Format must be dd-mm-yyyy"})


class DentistsEditForm(forms.ModelForm):

    class Meta:
        model = Dentists
        fields = FIELDS

    birth_date = forms.DateField(input_formats=['%d-%m-%Y'], initial=date.today().strftime('%d-%m-%Y'), error_messages={"invalid": "Format must be dd-mm-yyyy"})

    def __init__(self, *args, **kwargs):
        kwargs.pop("dentist", None)
        super(DentistsEditForm, self).__init__(*args, **kwargs)
