import json

from django.urls import reverse
<<<<<<< HEAD
=======

>>>>>>> 3e23122 (dcoker-networks)
from rest_framework.test import APIClient, APITestCase
from rest_framework.views import status

from order.factories import UserFactory
from product.factories import CategoryFactory, ProductFactory
from product.models import Product
<<<<<<< HEAD
=======
from rest_framework.authtoken.models import Token
>>>>>>> 3e23122 (dcoker-networks)


class TestProductViewSet(APITestCase):
    client = APIClient()

    def setUp(self):
        self.user = UserFactory()
<<<<<<< HEAD
=======
        token = Token.objects.create(user=self.user)
        token.save()
>>>>>>> 3e23122 (dcoker-networks)

        self.product = ProductFactory(
            title="pro controller",
            price=200.00,
        )

    def test_get_all_product(self):
<<<<<<< HEAD
        response = self.client.get(reverse("product-list", kwargs={"version": "v1"}))
=======
        token = Token.objects.get(user__username=self.user.username)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)
        response = self.client.get(
            reverse("product-list", kwargs={"version": "v1"}))
>>>>>>> 3e23122 (dcoker-networks)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        product_data = json.loads(response.content)

<<<<<<< HEAD
        self.assertEqual(product_data["results"][0]["title"], self.product.title)
        self.assertEqual(product_data["results"][0]["price"], self.product.price)
        self.assertEqual(product_data["results"][0]["active"], self.product.active)

    def test_create_product(self):
        category = CategoryFactory()
        data = json.dumps(
            {"title": "notebook", "price": 800.00, "categories_id": [category.id]}
        )
=======
        self.assertEqual(product_data['results'][0]["title"], self.product.title)
        self.assertEqual(product_data['results'][0]["price"], self.product.price)
        self.assertEqual(product_data['results'][0]["active"], self.product.active)

    def test_create_product(self):
        token = Token.objects.get(user__username=self.user.username)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)
        category = CategoryFactory()
        data = json.dumps({
            "title": "notebook",
            "price": 800.00,
            "categories_id": [category.id]
        })
>>>>>>> 3e23122 (dcoker-networks)

        response = self.client.post(
            reverse("product-list", kwargs={"version": "v1"}),
            data=data,
            content_type="application/json",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        created_product = Product.objects.get(title="notebook")

        self.assertEqual(created_product.title, "notebook")
<<<<<<< HEAD
        self.assertEqual(created_product.price, 800.00)
=======
        self.assertEqual(created_product.price, 800.00)
>>>>>>> 3e23122 (dcoker-networks)
