from django.db import models
from django.db.models.fields import TimeField, DateField, TextField

from dental_system.fields import NameField
from dental_system.models import DentalModel
from treatments.models import Treatments


class Prices(DentalModel):
    treatments = models.ForeignKey(Treatments)  # You can use this for unique ID patient
    price = models.CharField(max_length=30)
    is_promo = models.BooleanField(default=False)

    def __unicode__(self):
        return "{} - {}".format(self.name, self.phone_number)


class PricesHistories(DentalModel):
    prices = models.ForeignKey(Prices)
    old_data = models.TextField()
    new_data = models.TextField()
    updated_price_time = models.DateTimeField()
    updated_price_by = NameField()
