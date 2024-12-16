from rest_framework import serializers
from .models import CartItem, Cart
from app.models import Product, Sku

class CartItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='sku.productid.name')
    
    product_price = serializers.DecimalField(source='sku.productid.price', max_digits=10, decimal_places=2)
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = CartItem
        fields = ['id', 'product_name', 'quantity', 'product_price', 'total_price']

    def get_total_price(self, obj):
        return obj.sku.productid.price * obj.quantity

class CartSerializer(serializers.ModelSerializer):
    cart_items = CartItemSerializer(many=True, read_only=True)
    total_amount = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ['id', 'cart_items', 'total_amount']

    def get_total_amount(self, obj):
        return sum(item.sku.productid.price * item.quantity for item in obj.cartitem_set.all())
