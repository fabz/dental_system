from datetime import date

from django import forms

from vendors.models import Vendors
from dental_system.forms import SearchForm


FIELDS = ['name']


class VendorsForm(forms.ModelForm):

    class Meta:
        model = Vendors
        fields = FIELDS

    name = forms.Field(label='Name*')


class VendorsEditForm(forms.ModelForm):

    class Meta:
        model = Vendors
        fields = FIELDS

    name = forms.Field(label='Name*')

    def __init__(self, *args, **kwargs):
        kwargs.pop("vendor", None)
        super(VendorsEditForm, self).__init__(*args, **kwargs)


class VendorSearchForm(SearchForm):
    
    
    name = forms.CharField(required=False, label='Search by Name')
