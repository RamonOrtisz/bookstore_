from rest_framework.viewsets import ModelViewSet
<<<<<<< HEAD
from rest_framework.authentication import (
    SessionAuthentication,
    BasicAuthentication,
    TokenAuthentication,
)
from rest_framework.permissions import IsAuthenticated


=======
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

>>>>>>> 3e23122 (dcoker-networks)
from order.models import Order
from order.serializers import OrderSerializer


class OrderViewSet(ModelViewSet):
<<<<<<< HEAD
    authentication_classes = [
        SessionAuthentication,
        BasicAuthentication,
        TokenAuthentication,
    ]
    permission_classes = [IsAuthenticated]
    serializer_class = OrderSerializer

    queryset = Order.objects.all().order_by("id")
=======
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = OrderSerializer
    queryset = Order.objects.all().order_by('id')
>>>>>>> 3e23122 (dcoker-networks)
