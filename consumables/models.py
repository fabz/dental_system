from django.db import models

from dental_system.fields import CodeField
from dental_system.models import DentalModel
from vendors.models import Vendors


class Consumables(DentalModel):
    sku = CodeField(db_index=True)
    name = models.CharField(max_length=255, unique=True, db_index=True)
    description = models.TextField()
    is_sellable = models.BooleanField()
    quantity = models.IntegerField()
    

    def __unicode__(self):
        return "{} - {}".format(self.name, self.vendor.name)


class ConsumablesPricing(DentalModel):
    consumable = models.ForeignKey(Consumables)
    start_date = models.DateField()
    end_date = models.DateField(null=True)
    sell_price = models.FloatField()

class ConsumablesStockMutation(DentalModel):
    consumable = models.ForeignKey(Consumables)
    mutation_qty = models.IntegerField()
    price_pcs = models.FloatField()
    vendors = models.ForeignKey(Vendors)


