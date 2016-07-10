from datetime import date

from django import forms
from django.forms.models import inlineformset_factory
from django.core.validators import MinLengthValidator, MaxLengthValidator,RegexValidator

from consumables.models import *
from dental_system.forms import SearchForm


FIELDS = ['sku','name','description','is_sellable']


class ConsumablesForm(forms.ModelForm):

    class Meta:
        model = Consumables
        fields = FIELDS
    
    sku = forms.Field(label='SKU*', validators=[RegexValidator(regex='^\d{8}$', message='SKU must be 8 digit number'),MinLengthValidator(8),MaxLengthValidator(8)], widget=forms.TextInput(attrs={'size':'8', 'maxlength':'8'}))
    name = forms.Field(label='Name*')
    description = forms.CharField(label='Description*', widget=forms.Textarea())
    is_sellable = forms.BooleanField(label='Is Sellable?', required=False)
    sell_price = forms.FloatField(label='Sell Price (in IDR)')


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