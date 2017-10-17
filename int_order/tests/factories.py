import factory
from int_core.tests.factories import UserFactory
from int_order.models import Order
from faker import Faker

faker = Faker()


class OrderFactory(factory.django.DjangoModelFactory):
    owner = factory.SubFactory(UserFactory)
    cost = factory.LazyAttribute(lambda obj: faker.random_int(min=0, max=10000))

    class Meta:
        model = Order
