from datetime import date

from django import forms

from dentists.models import Specialization, Dentists


FIELDS = ['name', 'phone_number', 'email', 'address', 'birth_place', 'birth_date', 'specialization']


class DentistsForm(forms.ModelForm):

    class Meta:
        model = Dentists
        fields = FIELDS
    #     categories = forms.MultipleChoiceField(required=True)
    #     code = forms.CharField(max_length=70, label=label, required=required, help_text=help_text)
#     name = forms.CharField(max_length=255, label="Name", required=True)
#     phone_number = forms.CharField(max_length=25, label="Phone Number", required=True)
#     email = forms.CharField(max_length=255, label="Email")
#     address = forms.CharField(widget=forms.Textarea)
#     birth_place = forms.CharField(max_length=255, label="Birth place")
    birth_date = forms.DateField(input_formats=['%d-%m-%Y'], initial=date.today().strftime('%d-%m-%Y'), error_messages={"invalid": "Format must be dd-mm-yyyy"})
#     specialization = forms.ChoiceField(choices=Specialization.choices, required=True)
#
#     def __init__(self, *args, **kwargs):
#         super(DentistsForm, self).__init__(*args, **kwargs)
#
#     def clean(self):
#         super(DentistsForm, self).clean()
#         return self.cleaned_data


class DentistsEditForm(forms.ModelForm):

    class Meta:
        model = Dentists
        fields = FIELDS

    birth_date = forms.DateField(input_formats=['%d-%m-%Y'], initial=date.today().strftime('%d-%m-%Y'), error_messages={"invalid": "Format must be dd-mm-yyyy"})

    def __init__(self, *args, **kwargs):
        kwargs.pop("dentist", None)
        super(DentistsEditForm, self).__init__(*args, **kwargs)
