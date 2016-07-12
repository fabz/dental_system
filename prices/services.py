from django.db import transaction
from django.utils import timezone

from prices.models import PricesHistories


@transaction.atomic
def create_price_history(price_obj):
    time_updated = timezone.now()
    try:
        price_history_obj = PricesHistories.objects.get(price=price_obj, end_date=None)
        price_history_obj.end_date = time_updated
        price_history_obj.save()
    except PricesHistories.DoesNotExist:
        pass

    PricesHistories.objects.create(price=price_obj, sell_price=price_obj.price, start_date=time_updated)
