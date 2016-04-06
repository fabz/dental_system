from django.db import models
from django.db.models.fields import TimeField

from dental_system.fields import NameField
from dental_system.models import DentalModel
from dentists.models import Dentists


class ScheduleName(DentalModel):
    day = NameField(db_index=True)
    time_start = TimeField()
    time_end = TimeField()


class DentistsSchedules(DentalModel):
    dentists = models.ForeignKey(Dentists)
    schedule = models.ForeignKey(ScheduleName)

    def __unicode__(self):
        return "{} - {}".format(self.product, self.category.name)
