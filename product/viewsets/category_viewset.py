from rest_framework.viewsets import ModelViewSet

from product.models import Category
from product.serializers.category_serializer import CategorySerializer


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer

    def get_queryset(self):
<<<<<<< HEAD
        return Category.objects.all().order_by("id")
=======
        return Category.objects.all().order_by('id')
>>>>>>> 3e23122 (dcoker-networks)
