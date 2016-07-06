from django import forms
from datetime import date
from customers.models import Customer

FIELDS = ['customer_type', 'name', 'place_of_birth', 'date_of_birth', 'phone_number1', 'phone_number2', 'email', 'address']


class CustomersForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = FIELDS
    
    name = forms.Field(label='Name*')
    place_of_birth = forms.Field(label='Place of Birth*')
    
    #please help
    #address = forms.CharField(label='Address*', widget=forms.TextInput(attrs={'size':'40', 'height':'300'}))
    #^^ Gw mau ubah label jadi "Address*", tapi kalau di override text box nya jadi kecil..
    
    phone_number1 = forms.Field(label='Phone Number 1*')
    phone_number2 = forms.Field(label='Phone Number 2', required=False)
    email = forms.EmailField(required=False, error_messages={"invalid": "Invalid email address"})
    date_of_birth = forms.DateField(label='D.O.B* (dd-mm-yyyy)', input_formats=['%d-%m-%Y'], error_messages={"invalid": "Format must be dd-mm-yyyy"})


class CustomersEditForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = FIELDS

    name = forms.Field(label='Name*')
    place_of_birth = forms.Field(label='Place of Birth*')
    phone_number1 = forms.Field(label='Phone Number 1*')
    phone_number2 = forms.Field(label='Phone Number 2', required=False)
    email = forms.EmailField(required=False, error_messages={"invalid": "Invalid email address"})
    date_of_birth = forms.DateField(label='D.O.B* (dd-mm-yyyy)', input_formats=['%d-%m-%Y'], error_messages={"invalid": "Format must be dd-mm-yyyy"})
    
    def __init__(self, *args, **kwargs):
        kwargs.pop("customer", None)
        super(CustomersEditForm, self).__init__(*args, **kwargs)
