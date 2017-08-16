from django.db import models

from customers.models import Customer
from dental_system.models import DentalModel
from dentists.models import Dentists


class Transactions(DentalModel):
    trx_number = models.CharField(max_length=80, db_index=True)  # You can use this for unique ID patient
    trx_date = models.DateTimeField(db_index=True)
    customer = models.ForeignKey(Customer)
    total_amount = models.CharField(max_length=12)
    dentist = models.ForeignKey(Dentists)
    counter = models.SmallIntegerField(default=1)

    def __unicode__(self):
        return "{}".format(self.trx_number)


class TransactionDetail(DentalModel):
    transaction = models.ForeignKey(Transactions)
    detail_type = models.CharField(db_index=True, max_length=100)
    detail_id = models.IntegerField(db_index=True)
    qty = models.FloatField()
    discount = models.FloatField()
    price = models.FloatField()

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        from treatments.models import Treatments
        treatment_obj = eval(self.detail_type).objects.get(id=self.detail_id)
        self.price = treatment_obj.prices.price - self.discount
        return DentalModel.save(self, force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)

#     def treatment_price(self):
#         treatment_obj = eval(self.detail_type).objects.get(id=self.detail_id)
#         print('treatment', treatment_obj.prices.price)
#         return treatment_obj.prices.price
