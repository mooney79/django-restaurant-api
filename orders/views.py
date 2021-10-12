from rest_framework import generics
from .serializers import OrderSerializer
from .models import Order

class OrderListAPIView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer