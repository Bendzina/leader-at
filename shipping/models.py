from django.db import models

class Shipping(models.Model):
    SHIPPING_METHODS = [
        ('standard', 'Standard'),
        ('express', 'Express')
    ]

    Shipping_method = models.CharField(max_length=10, choices=SHIPPING_METHODS)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_time = models.IntegerField()
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.shipping_method} to {self.country}"