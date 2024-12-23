from django.urls import path
from .views import ShippingCreateView, ShippingListView

urlpatterns = [
    path('shipping/', ShippingCreateView.as_view(), name='shipping_create'),
    path('shipping/list/', ShippingListView.as_view(), name='shipping_list'),
]