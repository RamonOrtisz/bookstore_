import factory
<<<<<<< HEAD

from django.contrib.auth.models import User
from product.factories import ProductFactory

from order.models import Order
=======
from django.contrib.auth.models import User

from order.models import Order
from product.factories import ProductFactory
>>>>>>> 3e23122 (dcoker-networks)


class UserFactory(factory.django.DjangoModelFactory):
    email = factory.Faker("pystr")
    username = factory.Faker("pystr")

    class Meta:
        model = User


class OrderFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory(UserFactory)

    @factory.post_generation
    def product(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for product in extracted:
                self.product.add(product)

    class Meta:
<<<<<<< HEAD
        model = Order
=======
        model = Order
>>>>>>> 3e23122 (dcoker-networks)
