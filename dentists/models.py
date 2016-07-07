from django.db import models
from dental_system.fields import NameField, CodeField
from dental_system.models import DentalModel, get_value


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
        return get_value(self, stats)


class Dentists(DentalModel):
    name = NameField()
    phone_number = models.CharField(unique=True, db_index=True, max_length=20)
    email = models.CharField(unique=True, max_length=100)
    address = models.TextField(null=True)
    birth_place = models.CharField(null=True, max_length=100)
    birth_date = models.DateField(null=True)
    specialization = models.SmallIntegerField(default=Specialization.GENERAL_PRACTITIONER, db_index=True, choices=Specialization.choices)

    def __str__(self):
        return '{} - {}'.format(self.name, Specialization.get_value(Specialization, self.specialization))
