from datetime import date

from django.db import transaction

from consumables.models import Consumables, ConsumablesPricing


def create_new_consumables(clean_form):
    sku = clean_form['sku']
    name = clean_form['name']
    description = clean_form['description']
    is_sellable = clean_form['is_sellable']
    sell_price = clean_form['sell_price']

    with transaction.atomic():
        cons_obj = Consumables.objects.create(sku=sku, name=name, description=description, is_sellable=is_sellable, quantity=0)
        ConsumablesPricing.objects.create(consumable=cons_obj, start_date=date.today(), sell_price=sell_price)