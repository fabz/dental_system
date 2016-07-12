from django.db import models

from dental_system.models import DentalModel
from treatments.models import Treatments


class Prices(DentalModel):
    treatments = models.OneToOneField(Treatments)  # You can use this for unique ID patient
    price = models.CharField(max_length=30)

    def __str__(self):
        return "{} - {}".format(self.treatments, self.price)


class PricesHistories(DentalModel):
    price = models.ForeignKey(Prices)
    start_date = models.DateField()
    end_date = models.DateField(null=True)
