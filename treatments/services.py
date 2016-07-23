from django.db import transaction

from prices.models import Prices
from prices.services import create_price_history
from treatments.models import Treatments


def create_new_treatments(clean_form):
    with transaction.atomic():
        treat_obj = Treatments.objects.create(name=clean_form['name'], description=clean_form['description'], treatment_type=clean_form['treatment_type'])
        price_obj = Prices.objects.create(treatments=treat_obj, price=clean_form['sell_price'])
        create_price_history(price_obj)
