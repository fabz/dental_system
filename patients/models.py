from django.db import models
from django.db.models.fields import TimeField, DateField, TextField

from dental_system.fields import NameField
from dental_system.models import DentalModel


class PatientsData(DentalModel):
    patients_number = NameField(db_index=True)  # You can use this for unique ID patient
    name = NameField(db_index=True)
    date_of_birth = DateField()
    address = TextField()
    phone_number = models.CharField(max_length=30, db_index=True)

    def __unicode__(self):
        return "{} - {}".format(self.name, self.phone_number)
