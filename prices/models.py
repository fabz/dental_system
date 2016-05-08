from django.db import models

from dental_system.models import DentalModel
from treatments.models import Treatments


class Prices(DentalModel):
    treatments = models.ForeignKey(Treatments)  # You can use this for unique ID patient
    price = models.CharField(max_length=30)

    def __unicode__(self):
        return "{} - {}".format(self.name, self.phone_number)


class PricesHistories(DentalModel):
    price = models.ForeignKey(Prices)
    start_date = models.DateField()
    end_date = models.DateField(null=True)
