
from dental_system.fields import NameField
from dental_system.models import DentalModel


class Treatments(DentalModel):
    name = NameField(db_index=True)

    def __unicode__(self):
        return "{}".format(self.name)
