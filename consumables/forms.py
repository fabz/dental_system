
from django import forms
from django.core.validators import MinLengthValidator, MaxLengthValidator, RegexValidator

from consumables.models import Consumables, ConsumablesPricing
from dental_system.forms import SearchForm
from vendors.models import Vendors


FIELDS = ['sku', 'name', 'description', 'is_sellable']


class ConsumablesForm(forms.ModelForm):

    class Meta:
        model = Consumables
        fields = FIELDS

    sku = forms.Field(label='SKU*', validators=[RegexValidator(regex='^\d{8}$', message='SKU must be 8 digit number'),
                                                MinLengthValidator(8), MaxLengthValidator(8)], widget=forms.TextInput(attrs={'size': '8', 'maxlength': '8'}))
    name = forms.Field(label='Name*')
    description = forms.CharField(label='Description*', widget=forms.Textarea())
    is_sellable = forms.BooleanField(label='Is Sellable?', required=False)
    sell_price = forms.FloatField(label='Sell Price (in IDR)')


class ConsumablesEditForm(forms.ModelForm):

    class Meta:
        model = Consumables
        fields = FIELDS

    sku = forms.Field(label='SKU', widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    name = forms.Field(label='Name', widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    description = forms.CharField(label='Description*', widget=forms.Textarea())
    is_sellable = forms.BooleanField(label='Is Sellable?*', required=False)
    sell_price = forms.FloatField(label='Sell Price (in IDR)')

    def __init__(self, *args, **kwargs):
        cons_price_id = kwargs.pop("consumable", None)
        print(cons_price_id)
        if cons_price_id:
            self.fields['sell_price'].initial = float(ConsumablesPricing.objects.get(consumables=cons_price_id).sell_price)
        super(ConsumablesEditForm, self).__init__(*args, **kwargs)


class ConsumableSearchForm(SearchForm):

    sku = forms.CharField(required=False, label='Search by SKU')
    name = forms.CharField(required=False, label='Search by Name')
    is_sellable = forms.BooleanField(required=False, label='Filter Sell')


class ConsumablesStockinForm(forms.ModelForm):

    class Meta:
        model = Consumables
        fields = ['sku', 'name', 'vendors', 'mutation_qty', 'price_pcs']

    sku = forms.Field(label='SKU', widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    name = forms.Field(label='Name', widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    vendors = forms.ModelChoiceField(queryset=Vendors.objects.all(), empty_label=None)
    mutation_qty = forms.IntegerField(label='Stock In Quantity')
    price_pcs = forms.FloatField(label='Price per Piece')


class ConsumablesStockinEditForm(forms.ModelForm):

    class Meta:
        model = Consumables
        fields = FIELDS

    sku = forms.Field(label='SKU*', validators=[RegexValidator(regex='^\d{8}$', message='SKU must be 8 digit number'),
                                                MinLengthValidator(8), MaxLengthValidator(8)], widget=forms.TextInput(attrs={'size': '8', 'maxlength': '8'}))
    name = forms.Field(label='Name*')
    mutation_qty = forms.IntegerField()
    price_pcs = forms.FloatField()
    # vendors = forms.Field() #Need to select choice from Vendor model

    def __init__(self, *args, **kwargs):
        kwargs.pop("consumable", None)
        super(ConsumablesEditForm, self).__init__(*args, **kwargs)


class ConsumablesStockOutForm(forms.ModelForm):

    class Meta:
        model = Consumables
        fields = ['sku', 'name', 'vendors', 'mutation_qty', 'price_pcs']

    sku = forms.Field(label='SKU', widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    name = forms.Field(label='Name', widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    vendors = forms.ModelChoiceField(queryset=Vendors.objects.all(), empty_label=None)
    mutation_qty = forms.IntegerField(label='Stock Out Quantity')
    price_pcs = forms.FloatField(label='Price per Piece')
