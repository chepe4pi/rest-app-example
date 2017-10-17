from django.db import models
from int_core.models import TimestampableModel
from django.contrib.auth.models import User


class UserInfo(TimestampableModel):
    user = models.ForeignKey(User, null=True)
    score = models.PositiveIntegerField(default=0)
