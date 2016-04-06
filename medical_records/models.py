from django.db import models
from django.db.models.fields import TimeField, DateField, TextField

from dental_system.fields import NameField
from dental_system.models import DentalModel
from patients.models import PatientsData
from treatments.models import Treatments
from dentists.models import Dentists


class MedicalRecord(DentalModel):
    patient = models.ForeignKey(PatientsData)  # You can use this for unique ID patient
    treatment = models.ForeignKey(Treatments)
    dentist = models.ForeignKey(Dentists)
    description = models.TextField()

    def __unicode__(self):
        return "{} - {}".format(self.patient.name, self.treatment.name)
