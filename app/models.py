from django.db import models

class Brands(models.Model):
    id = models.BigAutoField(primary_key=True)
    brand = models.CharField(max_length=50)


class Product(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    catid = models.IntegerField(null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(null=False)
    brandid = models.ForeignKey(Brands, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Productparams(models.Model):
    id = models.BigAutoField(primary_key=True)
    productid = models.ForeignKey(Product, on_delete=models.CASCADE)
    key = models.CharField(max_length=100)
    value = models.CharField(max_length=200)

    def __str__(self):
        return self.key

class Categoryparams(models.Model):
    id = models.BigAutoField(primary_key=True)
    catid = models.ForeignKey(Category, on_delete=models.CASCADE)
    key = models.CharField(max_length=100)






