from rest_framework import status
from rest_framework.test import APITestCase
from int_core.tests.tests import AuthorizeForTestsMixin
from .factories import OrderFactory
from ..serializers.order import OrderSerializer
from ..models import Order


class OrderTestCase(AuthorizeForTestsMixin, APITestCase):
    url = '/api/orders/'

    def setUp(self):
        super(OrderTestCase, self).setUp()
        self.order = OrderFactory()
        self.expected = OrderSerializer(self.order).data
        self.data = {'complete': True}

    def test_set_complete(self):
        response = self.client.patch(self.url + str(self.order.id) + '/', self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Order.objects.get(id=self.order.id).complete, True)

    def test_get_obj(self):
        response = self.client.get(self.url + str(self.order.id) + '/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(dict(response.data), self.expected)

    def test_get_list_obj(self):
        order2 = OrderFactory()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn(self.expected, response.data)

    def test_deny_patch_twice(self):
        response = self.client.patch(self.url + str(self.order.id) + '/', self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.client.patch(self.url + str(self.order.id) + '/', self.data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_deny_set_cost(self):
        self.data = {'cost': 1232}
        self.client.patch(self.url + str(self.order.id) + '/', self.data)
        self.assertNotEqual(Order.objects.get(id=self.order.id).cost, self.data['cost'])
