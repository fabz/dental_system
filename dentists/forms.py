from django import forms
from dentists.models import Specialization


class DentistsForm(forms.Form):
    #     categories = forms.MultipleChoiceField(required=True)
    #     code = forms.CharField(max_length=70, label=label, required=required, help_text=help_text)
    name = forms.CharField(max_length=255, label="Name", required=True)
    phone_number = forms.CharField(max_length=25, label="Phone Number", required=True)
    email = forms.CharField(max_length=255, label="Email")
    address = forms.CharField(widget=forms.Textarea)
    birth_place = forms.CharField(max_length=255, label="Birth place")
#     birth_date = forms.DateField(input_formats='%d-%m-%Y')
    specialization = forms.ChoiceField(choices=Specialization.choices, required=True)

    def __init__(self, *args, **kwargs):
        super(DentistsForm, self).__init__(*args, **kwargs)

    def clean(self):
        super(DentistsForm, self).clean()
#         self = clean_product_form(self)

        # Add Stop and Alert Level Validation
        cleaned_data = self.cleaned_data
        print(cleaned_data)
        return self.cleaned_data

    def save(self, commit=True):
        return None
