from datetime import date

from django import forms

from transactions.models import Transactions


FIELDS = ['trx_date', 'customer', 'total_amount', 'dentist']


class TrxNewForm(forms.ModelForm):

    class Meta:
        model = Transactions
        fields = FIELDS
#     birth_date = forms.DateField(input_formats=['%d-%m-%Y'], initial=date.today().strftime('%d-%m-%Y'), error_messages={"invalid": "Format must be dd-mm-yyyy"})

    def __init__(self, *args, **kwargs):
        super(TrxNewForm, self).__init__(*args, **kwargs)
        self.fields['trx_date'].initial = date.today()
        self.fields['trx_date'].widget.attrs['readonly'] = True