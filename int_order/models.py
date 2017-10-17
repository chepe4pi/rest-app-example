from django.db import models
from int_core.models import TimestampableModel
from django.contrib.auth.models import User


class Order(TimestampableModel):
    owner = models.ForeignKey(User, related_name='owner')
    worker = models.ForeignKey(User, null=True, blank=True, related_name='worker')
    cost = models.PositiveIntegerField()
    complete = models.BooleanField(default=False)
