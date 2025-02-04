import json

from django.urls import reverse
from rest_framework.test import APIClient, APITestCase
from rest_framework.views import status

from product.factories import CategoryFactory
from product.models import Category


class CategoryViewSet(APITestCase):
    client = APIClient()

    def setUp(self):
        self.category = CategoryFactory(title="books")

    def test_get_all_category(self):
<<<<<<< HEAD
        response = self.client.get(reverse("category-list", kwargs={"version": "v1"}))
=======
        response = self.client.get(
            reverse("category-list", kwargs={"version": "v1"}))
>>>>>>> 3e23122 (dcoker-networks)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        category_data = json.loads(response.content)

<<<<<<< HEAD
        self.assertEqual(category_data["results"][0]["title"], self.category.title)
=======
        self.assertEqual(category_data['results'][0]["title"], self.category.title)
>>>>>>> 3e23122 (dcoker-networks)

    def test_create_category(self):
        data = json.dumps({"title": "technology"})

        response = self.client.post(
            reverse("category-list", kwargs={"version": "v1"}),
            data=data,
            content_type="application/json",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        created_category = Category.objects.get(title="technology")

<<<<<<< HEAD
        self.assertEqual(created_category.title, "technology")
=======
        self.assertEqual(created_category.title, "technology")
>>>>>>> 3e23122 (dcoker-networks)
