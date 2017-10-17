import random

from rest_framework.permissions import IsAuthenticated

from int_core.filters.backend import IsNotCompleteFilterBackend
from rest_framework.viewsets import ModelViewSet

from int_order.business_logic import set_scores, create_test_orders
from int_order.serializers.order import OrderSerializer
from int_order.models import Order
from rest_framework.views import Response


class OrderViewSet(ModelViewSet):
    filter_backends = (IsNotCompleteFilterBackend,)
    permission_classes = [IsAuthenticated]
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        set_scores(kwargs['pk'], serializer, self.request.user)
        return Response(serializer.data)

    # TODO this part exists just for creation test data by request
    def list(self, request, *args, **kwargs):
        create_test_orders(request.user)
        super().list(self, request, *args, **kwargs)
        return super().list(self, request, *args, **kwargs)

    class Meta:
        model = Order
