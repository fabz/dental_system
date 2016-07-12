
from django.db import models

from dental_system.fields import NameField
from dental_system.models import DentalModel, get_value


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

    def get_value(self, stats):
        return get_value(self, stats)


class Treatments(DentalModel):
    name = NameField(db_index=True, unique=True)
    description = models.TextField()
    treatment_type = models.SmallIntegerField(default=TreatmentType.TREATMENT, db_index=True, choices=TreatmentType.choices)
#     consumables
#     consumables_qty

    def __str__(self):
        return "{} - {}".format(self.name, TreatmentType.get_value(TreatmentType, self.treatment_type))
