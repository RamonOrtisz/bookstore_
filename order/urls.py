<<<<<<< HEAD
from django.urls import path, include
=======
from django.urls import include, path
>>>>>>> 3e23122 (dcoker-networks)
from rest_framework import routers

from order import viewsets

router = routers.SimpleRouter()
router.register(r"order", viewsets.OrderViewSet, basename="order")

<<<<<<< HEAD
urlpatterns = [path("", include(router.urls))]
=======

urlpatterns = [
    path("", include(router.urls)),
]
>>>>>>> 3e23122 (dcoker-networks)
