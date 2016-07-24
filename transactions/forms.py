from datetime import date

from django import forms

from customers.models import Customer
from dentists.models import Dentists
from transactions.models import Transactions
from treatments.models import Treatments


FIELDS = ['trx_date', 'customer', 'dentist']


class TrxNewForm(forms.ModelForm):

    class Meta:
        model = Transactions
        fields = FIELDS

    customer = forms.ModelChoiceField(queryset=Customer.objects.all())
    dentist = forms.ModelChoiceField(queryset=Dentists.objects.all())
    Treatments = forms.ModelMultipleChoiceField(queryset=Treatments.objects.all(), widget=forms.CheckboxSelectMultiple())

    def __init__(self, *args, **kwargs):
        super(TrxNewForm, self).__init__(*args, **kwargs)
        self.fields['trx_date'].initial = date.today()
        self.fields['trx_date'].widget.attrs['readonly'] = True
