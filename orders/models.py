from django.db import models
from django.contrib.auth.models import User
from app.models import Product, Sku

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Cart of user {self.user.username}'
    

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    sku = models.ForeignKey(Sku, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.sku.productid.name} - {self.quantity}"

# Create your models here.
