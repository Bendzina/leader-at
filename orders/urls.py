from django.urls import path
from .views import CartView, AddCartItemView, UpdateCartItemView, DeleteCartItemView, OrderDetailView, CheckoutView

urlpatterns = [
    path('cart/', CartView.as_view(), name='cart'),
    path('cart/add/<int:pk>/', AddCartItemView.as_view(), name='add_cart_item'),
    path('cart/update/<int:pk>/', UpdateCartItemView.as_view(), name='update_cart_item'),
    path('cart/delete/<int:pk>/', DeleteCartItemView.as_view(), name='delete_cart_item'),
    path('order/<int:pk>/', OrderDetailView.as_view(), name='order_detail'),
    path('cart/checkout/', CheckoutView.as_view(), name='checkout'),
]
