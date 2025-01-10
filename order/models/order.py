from django.db import models
from django.contrib.auth.models import User

<<<<<<< HEAD
from product.models.product import Product
=======
from product.models import Product
>>>>>>> 3e23122 (dcoker-networks)


class Order(models.Model):
    product = models.ManyToManyField(Product, blank=False)
<<<<<<< HEAD
    user = models.ForeignKey(User, on_delete=models.CASCADE)
=======
    user = models.ForeignKey(User, on_delete=models.CASCADE)
>>>>>>> 3e23122 (dcoker-networks)
