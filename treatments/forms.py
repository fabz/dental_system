from datetime import date

from django import forms

from dentists.models import Dentists
from treatments.models import Treatments


FIELDS = ['name', 'description', 'treatment_type']


class TreatmentsNewForm(forms.ModelForm):

    class Meta:
        model = Treatments
        fields = FIELDS


class TreatmentsEditForm(forms.ModelForm):

    class Meta:
        model = Treatments
        fields = FIELDS

    birth_date = forms.DateField(input_formats=['%d-%m-%Y'], initial=date.today().strftime('%d-%m-%Y'), error_messages={"invalid": "Format must be dd-mm-yyyy"})

    def __init__(self, *args, **kwargs):
        kwargs.pop("dentist", None)
        super(TreatmentsEditForm, self).__init__(*args, **kwargs)
