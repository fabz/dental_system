from django import forms

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

    def __init__(self, *args, **kwargs):
        kwargs.pop("treatment", None)
        super(TreatmentsEditForm, self).__init__(*args, **kwargs)
