from datetime import date

from django import forms

from dentists.models import Dentists


FIELDS = ['name', 'phone_number', 'email', 'address', 'birth_place', 'birth_date', 'specialization']


class DentistsNewForm(forms.ModelForm):

    class Meta:
        model = Dentists
        fields = FIELDS

    email = forms.EmailField(required=False, error_messages={"invalid": "Invalid email address"})
    birth_date = forms.DateField(input_formats=['%d-%m-%Y'], initial=date.today().strftime('%d-%m-%Y'), error_messages={"invalid": "Format must be dd-mm-yyyy"})


class DentistsEditForm(forms.ModelForm):

    class Meta:
        model = Dentists
        fields = FIELDS

    email = forms.EmailField(required=False, error_messages={"invalid": "Invalid email address"})
    birth_date = forms.DateField(input_formats=['%d-%m-%Y'], initial=date.today().strftime('%d-%m-%Y'),
                                 error_messages={"invalid": "Format must be dd-mm-yyyy"})
