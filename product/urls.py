<<<<<<< HEAD
from django.urls import path, include
=======
from django.urls import include, path
>>>>>>> 3e23122 (dcoker-networks)
from rest_framework import routers

from product import viewsets

router = routers.SimpleRouter()
router.register(r"product", viewsets.ProductViewSet, basename="product")
router.register(r"category", viewsets.CategoryViewSet, basename="category")

<<<<<<< HEAD
urlpatterns = [path("", include(router.urls))]
=======
urlpatterns = [
    path("", include(router.urls)),
]
>>>>>>> 3e23122 (dcoker-networks)
