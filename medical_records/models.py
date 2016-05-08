from django.db import models

from dental_system.models import DentalModel
from treatments.models import Treatments
from dentists.models import Dentists
from customers.models import Customer


class MedicalRecord(DentalModel):
    customer = models.ForeignKey(Customer)
    treatment = models.ForeignKey(Treatments)
    dentist = models.ForeignKey(Dentists)
    date = models.DateTimeField()
    anamnese = models.TextField()
    diagnosis = models.TextField()

    def __unicode__(self):
        return "{} - {}".format(self.patient.name, self.treatment.name)
