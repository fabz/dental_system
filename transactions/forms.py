from datetime import date

from django import forms

from customers.models import Customer
from dentists.models import Dentists
from transactions.models import Transactions, TransactionDetail
from treatments.models import Treatments
from dental_system.helpers import create_invoice_number, get_counter_from_cust_id


FIELDS = ('counter', 'trx_number', 'trx_date', 'customer', 'dentist',)
DETAIL_FIELDS = ('transaction', 'detail_type', 'detail_id', 'qty', 'discount', 'price',)


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
        self.fields['trx_number'].initial = False
        self.fields['trx_number'].widget = forms.HiddenInput()
        self.fields['counter'].widget = forms.HiddenInput()

    def clean(self):
        cleaned_data = super(TrxNewForm, self).clean()

        cust_id = cleaned_data['customer'].id
        counter = get_counter_from_cust_id(cust_id)

        cleaned_data['counter'] = counter
        cleaned_data['trx_number'] = create_invoice_number(cust_id, counter)

        print("cleaned_data", cleaned_data)

        return cleaned_data


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
        self.fields['trx_number'].widget.attrs['readonly'] = True
        self.fields['counter'].widget = forms.HiddenInput()


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
        self.fields['transaction'].initial = Transactions.objects.get(id=transaction_id)
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
