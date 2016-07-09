from datetime import date

from django import forms
from django.core.validators import MinLengthValidator, MaxLengthValidator

from consumables.models import Consumables
from dental_system.forms import SearchForm


FIELDS = ['sku','name','description','is_sellable']


class ConsumablesForm(forms.ModelForm):

    class Meta:
        model = Consumables
        fields = FIELDS
    
    sku = forms.Field(label='SKU*', validators=[MinLengthValidator(8),MaxLengthValidator(8)], widget=forms.TextInput(attrs={'size':'8', 'maxlength':'8'}))
    name = forms.Field(label='Name*')
    description = forms.CharField(label='Description*', widget=forms.Textarea())
    is_sellable = forms.BooleanField(label='Is Sellable?*')


class ConsumablesEditForm(forms.ModelForm):

    class Meta:
        model = Consumables
        fields = FIELDS

    sku = forms.Field(label='SKU*')
    name = forms.Field(label='Name*')
    description = forms.CharField(label='Description*', widget=forms.Textarea())
    is_sellable = forms.BooleanField(label='Is Sellable?*')

    def __init__(self, *args, **kwargs):
        kwargs.pop("consumable", None)
        super(ConsumablesEditForm, self).__init__(*args, **kwargs)


class ConsumableSearchForm(SearchForm):
    
    sku = forms.CharField(required=False, label='Search by SKU')
    name = forms.CharField(required=False, label='Search by Name')
    is_sellable = forms.BooleanField(required=False, label='Filter Sell')