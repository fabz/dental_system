from django import forms

from prices.models import Prices
from treatments.models import Treatments


FIELDS = ['treatments', 'price']


class PricesEditForm(forms.ModelForm):

    class Meta:
        model = Prices
        fields = FIELDS

    treatments = forms.ModelChoiceField(queryset=Treatments.objects.all())