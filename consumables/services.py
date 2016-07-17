from datetime import date

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


def create_new_consumables_stockin(clean_form):
    sku = clean_form['sku']
    name = clean_form['name']
    vendors = clean_form['vendors']
    mutation_qty = clean_form['mutation_qty']
    price_pcs = clean_form['price_pcs']
    
    quantity = Consumables.objects.get(sku=sku).quantity
    cons_obj = Consumables.objects.get(sku=sku)
    vendor_obj = Vendors.objects.get(name=vendors)

    with transaction.atomic():
        Consumables.objects.get(sku=sku).update(quantity = quantity+mutation_qty)
        ConsumablesStockMutation.objects.create(consumable=cons_obj, mutation_qty = mutation_qty, price_pcs = price_pcs, vendors = vendor_obj)
        
def create_new_consumables_stockout(clean_form):
    sku = clean_form['sku']
    name = clean_form['name']
    vendors = clean_form['vendors']
    mutation_qty = clean_form['mutation_qty']
    price_pcs = clean_form['price_pcs']
    
    quantity = Consumables.objects.get(sku=sku).quantity
    cons_obj = Consumables.objects.get(sku=sku)
    vendor_obj = Vendors.objects.get(name=vendors)

    with transaction.atomic():
        Consumables.objects.get(sku=sku).update(quantity = quantity+mutation_qty)
        ConsumablesStockMutation.objects.create(consumable=cons_obj, mutation_qty = mutation_qty, price_pcs = price_pcs, vendors = vendor_obj)

def create_new_pricing(clean_form):
    sku = clean_form['sku']
    name = clean_form['name']
    description = clean_form['description']
    is_sellable = clean_form['is_sellable']
    sell_price = clean_form['sell_price']
    
    cons_obj = Consumables.objects.get(sku=sku)
    price_obj = ConsumablesPricing.objects.get(consumable=cons_obj, end_date=None)

    #print(price_obj)
    
    with transaction.atomic():
        price_obj.end_date=date.today()
        price_obj.save()
        ConsumablesPricing.objects.create(consumable=cons_obj, start_date=date.today(), sell_price=sell_price)