from django.shortcuts import render
from rest_framework import generics
from .models import Shipping
from .serializers import ShippingSerializer

class ShippingCreateView(generics.CreateAPIView):
    queryset = Shipping.objects.all()
    serializer_class = ShippingSerializer


class ShippingListView(generics.ListAPIView):
    queryset = Shipping.objects.all()
    serializer_class = ShippingSerializer

