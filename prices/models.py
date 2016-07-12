from django.db import models

from dental_system.models import DentalModel
from treatments.models import Treatments


class Prices(DentalModel):
    treatments = models.OneToOneField(Treatments)  # You can use this for unique ID patient
    price = models.FloatField()

    def __str__(self):
        return "{} - {}".format(self.treatments, self.price)


class PricesHistories(DentalModel):
    price = models.ForeignKey(Prices)
    sell_price = models.FloatField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True)
