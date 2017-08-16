from datetime import date

from django import forms

from consumables.models import Consumables
from customers.models import Customer
from dental_system.helpers import create_invoice_number, get_counter_from_cust_id
from dentists.models import Dentists
from transactions.models import Transactions, TransactionDetail
from treatments.models import Treatments


FIELDS = ('counter', 'trx_number', 'trx_date', 'customer', 'dentist',)
DETAIL_FIELDS = ('transaction', 'detail_type', 'detail_id', 'qty', 'discount', 'price',)
TRX_DETAIL_FIELDS = ('transaction', 'customer', 'detail_type', 'detail_id', 'qty', 'discount')


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
        fields = TRX_DETAIL_FIELDS

#     transaction = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    customer = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    detail_type = forms.ChoiceField(label='Transaction Type', widget=forms.Select(
    ), choices=(('Treatments', 'Treatments'), ('Consumables', 'Consumables')))
    detail_id = forms.ChoiceField(label='Transaction Detail',
                                  choices=Treatments.objects.all().values_list('id', 'name'))

    def __init__(self, *args, **kwargs):
        transaction_id = kwargs.pop('transaction_id', None)
        super(TrxDetailNewForm, self).__init__(*args, **kwargs)
        self.fields['transaction'].initial = Transactions.objects.get(id=transaction_id)
        self.fields['transaction'].widget = forms.HiddenInput()
        self.fields['customer'].initial = Transactions.objects.get(id=transaction_id).customer
        print(self.fields)


class TrxDetailEditForm(forms.ModelForm):

    class Meta:
        model = TransactionDetail
        fields = TRX_DETAIL_FIELDS

    customer = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    detail_type = forms.ChoiceField(label='Transaction Type', widget=forms.Select(
    ), choices=(('Treatments', 'Treatments'), ('Consumables', 'Consumables')))
    detail_id = forms.ChoiceField(label='Transaction Detail',
                                  choices=Treatments.objects.all().values_list('id', 'name'))

    def __init__(self, *args, **kwargs):
        super(TrxDetailEditForm, self).__init__(*args, **kwargs)
        if 'instance' in kwargs:
            transaction_id = kwargs['instance'].transaction.id
            self.fields['transaction'].widget = forms.HiddenInput()
            self.fields['transaction'].initial = Transactions.objects.get(id=transaction_id)
            self.fields['qty'].widget = forms.HiddenInput()
            self.fields['qty'].initial = 1
            self.fields['qty'].widget = forms.HiddenInput()
            self.fields['transaction'].widget = forms.HiddenInput()
            self.fields['customer'].initial = Transactions.objects.get(id=transaction_id).customer
