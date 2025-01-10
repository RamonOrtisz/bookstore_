from rest_framework.viewsets import ModelViewSet
<<<<<<< HEAD
=======
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
>>>>>>> 3e23122 (dcoker-networks)

from product.models import Product
from product.serializers.product_serializer import ProductSerializer


class ProductViewSet(ModelViewSet):
<<<<<<< HEAD
    serializer_class = ProductSerializer

    def get_queryset(self):  # Queryset (2/2)
        return Product.objects.all().order_by("id")
=======
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all().order_by('id')
    
>>>>>>> 3e23122 (dcoker-networks)
