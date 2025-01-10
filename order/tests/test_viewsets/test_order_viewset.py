import json

from django.urls import reverse
<<<<<<< HEAD
from rest_framework.authtoken.models import Token

from rest_framework import status
from rest_framework.test import APIClient, APITestCase
=======
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from rest_framework.authtoken.models import Token
>>>>>>> 3e23122 (dcoker-networks)

from order.factories import OrderFactory, UserFactory
from order.models import Order
from product.factories import CategoryFactory, ProductFactory
from product.models import Product


class TestOrderViewSet(APITestCase):

    client = APIClient()

    def setUp(self):
<<<<<<< HEAD
        self.user = UserFactory()
        token = Token.objects.create(user=self.user)  # added
        token.save()  # added

=======
        self.user = UserFactory()  # Serve para criar um usuário para os testes
        token = Token.objects.create(user=self.user)
        token.save()
>>>>>>> 3e23122 (dcoker-networks)
        self.category = CategoryFactory(title="technology")
        self.product = ProductFactory(
            title="mouse", price=100, category=[self.category]
        )
        self.order = OrderFactory(product=[self.product])

    def test_order(self):
<<<<<<< HEAD
        token = Token.objects.get(user__username=self.user.username)  # added
        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)  # added
        response = self.client.get(reverse("order-list", kwargs={"version": "v1"}))
=======
        token = Token.objects.get(user__username=self.user.username)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)
        response = self.client.get(
            reverse("order-list", kwargs={"version": "v1"}))
>>>>>>> 3e23122 (dcoker-networks)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        order_data = json.loads(response.content)
<<<<<<< HEAD

        self.assertEqual(
            order_data["results"][0]["product"][0]["title"], self.product.title
        )
        self.assertEqual(
            order_data["results"][0]["product"][0]["price"], self.product.price
        )
        self.assertEqual(
            order_data["results"][0]["product"][0]["active"], self.product.active
        )
        self.assertEqual(
            order_data["results"][0]["product"][0]["category"][0]["title"],
=======
        self.assertEqual(order_data['results'][0]["product"][0]["title"], self.product.title)
        self.assertEqual(order_data['results'][0]["product"][0]["price"], self.product.price)
        self.assertEqual(order_data['results'][0]["product"][0]["active"], self.product.active)
        self.assertEqual(
            order_data['results'][0]["product"][0]["category"][0]["title"],
>>>>>>> 3e23122 (dcoker-networks)
            self.category.title,
        )

    def test_create_order(self):
<<<<<<< HEAD
        token = Token.objects.get(user__username=self.user.username)  # added
        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)  # added

=======
        token = Token.objects.get(user__username=self.user.username)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)
>>>>>>> 3e23122 (dcoker-networks)
        user = UserFactory()
        product = ProductFactory()
        data = json.dumps({"products_id": [product.id], "user": user.id})

        response = self.client.post(
            reverse("order-list", kwargs={"version": "v1"}),
            data=data,
            content_type="application/json",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

<<<<<<< HEAD
        created_order = Order.objects.get(user=user)
=======
        created_order = Order.objects.get(user=user)
>>>>>>> 3e23122 (dcoker-networks)
