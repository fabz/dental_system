from datetime import date

from django import forms

from customers.models import Customer
from dentists.models import Dentists
from transactions.models import Transactions, TransactionDetail
from treatments.models import Treatments


FIELDS = ['trx_date', 'customer', 'dentist']
DETAIL_FIELDS = ['transaction', 'detail_type', 'detail_id', 'qty', 'discount', 'price']


class TrxNewForm(forms.ModelForm):

    class Meta:
        model = Transactions
        fields = FIELDS

    customer = forms.ModelChoiceField(queryset=Customer.objects.all())
    dentist = forms.ModelChoiceField(queryset=Dentists.objects.all())

    def __init__(self, *args, **kwargs):
        super(TrxNewForm, self).__init__(*args, **kwargs)
        self.fields['trx_date'].initial = date.today()
        self.fields['trx_date'].widget.attrs['readonly'] = True


class TrxEditForm(forms.ModelForm):

    class Meta:
        model = Transactions
        fields = FIELDS

    customer = forms.ModelChoiceField(queryset=Customer.objects.all())
    dentist = forms.ModelChoiceField(queryset=Dentists.objects.all())

    def __init__(self, *args, **kwargs):
        super(TrxEditForm, self).__init__(*args, **kwargs)
        self.fields['trx_date'].initial = date.today()
        self.fields['trx_date'].widget.attrs['readonly'] = True


class TrxDetailNewForm(forms.ModelForm):

    class Meta:
        model = TransactionDetail
        fields = DETAIL_FIELDS
    
    detail_type = forms.CharField() 
    detail_id = forms.IntegerField()
    qty = forms.FloatField()
    discount = forms.FloatField()
    price = forms.FloatField()

    def __init__(self, *args, **kwargs):
        transaction_id = kwargs.pop('transaction_id', None)
        print("transaction_id", transaction_id)
        super(TrxDetailNewForm, self).__init__(*args, **kwargs)
        self.fields['transaction'].initial = Transactions.objects.get(trx_number=transaction_id)
        self.fields['transaction'].widget = forms.HiddenInput()


class TrxDetailEditForm(forms.ModelForm):

    class Meta:
        model = TransactionDetail
        fields = DETAIL_FIELDS
    
    detail_type = forms.CharField() 
    detail_id = forms.IntegerField()
    qty = forms.FloatField()
    discount = forms.FloatField()
    price = forms.FloatField()

    def __init__(self, *args, **kwargs):
        super(TrxDetailEditForm, self).__init__(*args, **kwargs)
        self.fields['transaction'].widget = forms.HiddenInput()
