from django.db import models

from dental_system.fields import CodeField
from dental_system.models import DentalModel
from vendors.models import Vendors


class Consumables(DentalModel):
    name = models.CharField(max_length=255, unique=True, db_index=True)
    reference_code = CodeField()
    description = models.TextField()
    vendor = models.ForeignKey(Vendors)

    def __unicode__(self):
        return "{} - {}".format(self.name, self.vendor.name)


class ConsumablesPrice(DentalModel):
    consumable = models.ForeignKey(Consumables)
    start_date = models.DateField()
    end_date = models.DateField(null=True)
    price = models.FloatField()
