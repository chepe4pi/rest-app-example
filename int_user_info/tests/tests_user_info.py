from rest_framework import status
from rest_framework.test import APITestCase
from int_core.tests.tests import AuthorizeForTestsMixin
from int_order.tests.factories import OrderFactory
from ..models import UserInfo
from interview.settings import COMISSION


class UserInfoTestCase(AuthorizeForTestsMixin, APITestCase):
    url = '/api/orders/'

    def setUp(self):
        super(UserInfoTestCase, self).setUp()
        self.order = OrderFactory()
        self.data = {'complete': True}

    def test_check_scores(self):
        response = self.client.patch(self.url + str(self.order.id) + '/', self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        user_info = UserInfo.objects.get(user=self.user)
        self.assertEqual(user_info.score, int(self.order.cost - self.order.cost * COMISSION))

    def test_deny_patch_unauthorized(self):
        self.client.logout()
        response = self.client.patch(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_scores(self):
        url = '/api/scores/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['score'], 0)
