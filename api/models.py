import uuid

from django.db import models

from core.models import TimeStampModel


class Coupon(TimeStampModel):
    number = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    count = models.IntegerField(default=0)

    class Meta:
        db_table = 'coupons'
