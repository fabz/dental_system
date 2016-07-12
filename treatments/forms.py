from django import forms
from treatments.models import Treatments
from prices.models import Prices


class TreatmentsEditPriceForm(forms.Form):

    sell_price = forms.FloatField(label='Sell Price (in IDR)')

    def __init__(self, *args, **kwargs):
        treat_id = kwargs.pop('treat_id', None)
        super(TreatmentsEditPriceForm, self).__init__(*args, **kwargs)
        print(treat_id)
        treatment = Treatments.objects.get(id=treat_id)

        try:
            self.fields['sell_price'].initial = Prices.objects.get(treatments=treatment).price
        except Prices.DoesNotExist:
            self.fields['sell_price'].initial = 0
