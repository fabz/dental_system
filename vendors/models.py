from dental_system.fields import NameField
from dental_system.models import DentalModel


class Vendors(DentalModel):
    name = NameField()

    def __unicode__(self):
        return "{}".format(self.name)
