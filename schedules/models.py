from django.db import models
from django.db.models.fields import TimeField

from dental_system.fields import NameField
from dental_system.models import DentalModel
from dentists.models import Dentists
from customers.models import Customer


class ScheduleName(DentalModel):
    day = NameField(db_index=True)
    time_start = TimeField()
    time_end = TimeField()


class DentistsSchedules(DentalModel):

    class Meta:
        index_together = [["schedule_date", "time_start"], ["schedule_date", "time_start", "time_end"], ]

    dentists = models.ForeignKey(Dentists)
    schedule_date = models.DateField(db_index=True)
    time_start = models.TimeField(db_index=True)
    time_end = models.TimeField(db_index=True)

    def __unicode__(self):
        return "{} - {}".format(self.product, self.category.name)


class Appointments(DentalModel):
    customer = models.ForeignKey(Customer)
    dentist = models.ForeignKey(Dentists)
    date = models.DateTimeField()
    anamnese = models.TextField()
