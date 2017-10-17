from int_core.tests.factories import UserFactory


class AuthorizeForTestsMixin(object):

    def setUp(self):
        self.user = UserFactory()
        self.client.force_authenticate(user=self.user)
