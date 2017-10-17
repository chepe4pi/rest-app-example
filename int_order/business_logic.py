from django.db.transaction import atomic

from int_order.models import Order
from int_user_info.models import UserInfo
from interview.settings import COMISSION


@atomic
def set_scores(order_id, serializer, user):
    UserInfo.objects.get_or_create(user=user)
    Order.objects.select_for_update().get(id=order_id)
    user_info = UserInfo.objects.select_for_update().get(user=user)
    serializer.save(worker=user)
    scores = serializer.instance.cost - serializer.instance.cost * COMISSION
    user_info.score += scores
    user_info.save()
    serializer.save()
