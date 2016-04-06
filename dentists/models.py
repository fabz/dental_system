from django.db import models

from dental_system.fields import NameField
from dental_system.models import DentalModel


class Specialization:
    GENERAL_PRACTITIONER = 0
    PERIODONTIC = 1
    ORAL_AND_MAXILLOFACIAL_SURGERY = 2
    ENDODONTIC = 3
    ORTHODONTIC = 4
    PROSTHODONTIC = 5
    PEDODONTIC = 6

    choices = (
        (GENERAL_PRACTITIONER, 'GP'),
        (PERIODONTIC, 'Perio'),
        (ORAL_AND_MAXILLOFACIAL_SURGERY, 'Bedah Mulut'),
        (ENDODONTIC, 'Konservasi Gigi'),
        (ORTHODONTIC, 'Ortho'),
        (PROSTHODONTIC, 'Prostho'),
        (PEDODONTIC, 'Pedo'),
    )

    def get_value(self, stats):
        for choice in self.choices:
            if(choice[0] == stats):
                return choice[1]

        return 'Unlimited (blank)'


class Dentists(DentalModel):
    name = NameField(unique=True)
    specialization = models.SmallIntegerField(default=0, db_index=True, choices=Specialization.choices)

    def __repr__(self):
        return '{} - {}'.format(self.name, Specialization.get_value(self.specialization))
