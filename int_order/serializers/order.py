from rest_framework import serializers
from ..models import Order


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ('id', 'complete', 'cost')
        read_only_fields = ('id', 'cost')
