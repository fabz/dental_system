
from django.db import models

from dental_system.fields import NameField
from dental_system.models import DentalModel


class TreatmentType():
    TREATMENT = 0
    PREVENTIVE = 1
    COSMETICS = 2
    HEAVY = 3

    choices = (
        (TREATMENT, 'Treatment'),
        (PREVENTIVE, 'Preventive'),
        (COSMETICS, 'Cosmetics'),
        (HEAVY, 'Heavy'),
    )


class Treatments(DentalModel):
    name = NameField(db_index=True)
    description = models.TextField()
    treatment_type = models.SmallIntegerField(default=TreatmentType.TREATMENT, db_index=True, choices=TreatmentType.choices)
#     consumables
#     consumables_qty

    def __unicode__(self):
        return "{} - {}".format(self.name, self.treatment_type)
