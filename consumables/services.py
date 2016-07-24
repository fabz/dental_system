from datetime import date
from django.utils import timezone
from django.db import transaction

from consumables.models import *
from vendors.models import *


def create_new_consumables(clean_form):
    sku = clean_form['sku']
    name = clean_form['name']
    description = clean_form['description']
    is_sellable = clean_form['is_sellable']
    sell_price = clean_form['sell_price']

    with transaction.atomic():
        cons_obj = Consumables.objects.create(sku=sku, name=name, description=description, is_sellable=is_sellable, quantity=0)
        ConsumablesPricing.objects.create(consumable=cons_obj, start_date=date.today(), sell_price=sell_price)


def create_new_consumables_mutation(clean_form):
    mutation_type = clean_form['mutation_type']
    sku = clean_form['sku']
    vendors = clean_form['vendors']
    mutation_qty = clean_form['mutation_qty']
    price_pcs = clean_form['price_pcs']
    remarks = clean_form['remarks']

    cons_obj = Consumables.objects.get(sku=sku)
    vendor_obj = Vendors.objects.get(name=vendors)

    if int(mutation_type) == 0:
        '''Stock In'''
        cons_obj.quantity += int(mutation_qty)
        cons_obj.save()
        ConsumablesStockMutation.objects.create(consumable=cons_obj, mutation_qty=mutation_qty, price_pcs=price_pcs, vendors=vendor_obj, remarks = remarks)
    else:
        '''Stock Out'''
        cons_obj.quantity = cons_obj.quantity - int(mutation_qty)
        cons_obj.save()
        ConsumablesStockMutation.objects.create(consumable=cons_obj, mutation_qty=-(mutation_qty), price_pcs=price_pcs, vendors=vendor_obj, remarks = remarks)


def create_new_pricing(consumablespricing_obj, sell_price, sku):
    '''
    create consumables price history
    '''
    time_updated = timezone.now()
    cons_obj = Consumables.objects.get(sku=sku)

    consumablespricing_obj.end_date = time_updated
    consumablespricing_obj.save()

    ConsumablesPricing.objects.create(consumable=cons_obj, sell_price=sell_price, start_date=time_updated)
