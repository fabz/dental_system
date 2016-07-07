from datetime import date

from django import forms

from customers.models import Customer
from transactions.models import Transactions


FIELDS = ['trx_date', 'customer', 'total_amount', 'dentist']


class TrxNewForm(forms.ModelForm):

    class Meta:
        model = Transactions
        fields = FIELDS

    customer = forms.ModelChoiceField(queryset=Customer.objects.all())

    def __init__(self, *args, **kwargs):
        super(TrxNewForm, self).__init__(*args, **kwargs)
        self.fields['trx_date'].initial = date.today()
        self.fields['trx_date'].widget.attrs['readonly'] = True
