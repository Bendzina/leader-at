from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from .models import Cart, CartItem
from app.models import Product, Sku
from .serializers import CartSerializer
from rest_framework.permissions import IsAuthenticated



class CartView(APIView):
    def get(self, request):
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_items = CartItem.objects.filter(cart=cart)
        serializer = CartSerializer(cart)
        return Response(serializer.data)

class AddCartItemView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, pk):
        try:
            # პროდუქტის მოძიება
            product = Product.objects.get(pk=pk)
            sku = Sku.objects.get(productid=product)

            # კალათის მოძიება ან შექმნა
            cart, created = Cart.objects.get_or_create(user=request.user)

            # CartItem-ის მოძიება ან შექმნა
            cart_item, cart_item_created = CartItem.objects.get_or_create(cart=cart, sku=sku)
            
            if not cart_item_created:
                cart_item.quantity += 1
            else:
                cart_item.quantity = 1
            cart_item.save()

            return Response({'status': 'success', 'message': 'Item added to cart'}, status=200)

        except Product.DoesNotExist:
            return Response({'status': 'error', 'message': 'Product not found'}, status=404)
        
        except Sku.DoesNotExist:
            return Response({'status': 'error', 'message': 'Sku not found for the product'}, status=404)
        
        except Exception as e:
            return Response({'status': 'error', 'message': str(e)}, status=500)
class UpdateCartItemView(APIView):
    def post(self, request, pk):
        try:
            cart_item = CartItem.objects.get(pk=pk)
            quantity = int(request.data.get('quantity'))
            if quantity == 0:
                cart_item.delete()
                return Response({'status': 'success', 'message': 'Item removed from cart'}, status=status.HTTP_200_OK)
            elif quantity <= cart_item.sku.productid.stock:
                cart_item.quantity = quantity
                cart_item.save()
                return Response({'status': 'success', 'message': 'Cart item updated'}, status=status.HTTP_200_OK)
            else:
                return Response({'status': 'error', 'message': 'Not enough stock'}, status=status.HTTP_400_BAD_REQUEST)
        except CartItem.DoesNotExist:
            return Response({'status': 'error', 'message': 'Cart item not found'}, status=status.HTTP_404_NOT_FOUND)

class DeleteCartItemView(APIView):
    def post(self, request, pk):
        try:
            cart_item = CartItem.objects.get(pk=pk)
            cart_item.delete()
            return Response({'status': 'success', 'message': 'Item removed from cart'}, status=status.HTTP_200_OK)
        except CartItem.DoesNotExist:
            return Response({'status': 'error', 'message': 'Cart item not found'}, status=status.HTTP_404_NOT_FOUND)
