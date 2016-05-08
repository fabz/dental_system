from django.db import models
from django.db.models.fields import TimeField, DateField, TextField

from dental_system.fields import NameField, CodeField
from dental_system.models import DentalModel


class CustomerType():
    PATIENT = 0
    PROSPECT = 1


class Customer(DentalModel):
    customer_type = models.SmallIntegerField(default=CustomerType.PATIENT, db_index=True, choices=CustomerType.choices)
    name = NameField(db_index=True)
    phone_number1 = models.CharField(max_length=20, db_index=True)
    phone_number2 = models.CharField(max_length=20, db_index=True, null=True)
    place_of_birth = models.CharField(max_length=100, null=True)
    date_of_birth = DateField()
    email = models.CharField(max_length=100, null=True, db_index=True)
    address = TextField()
    id_number = CodeField(db_index=True)
    photo = models.TextField()

    def __unicode__(self):
        return "{} - {}".format(self.name, self.phone_number1)
