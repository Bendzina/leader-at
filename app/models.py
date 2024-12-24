from django.db import models

class Store(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.name



class Brands(models.Model):
    id = models.BigAutoField(primary_key=True)
    brand = models.CharField(max_length=50)
    
    def __str__(self):
        return self.brand

class Category(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    catid = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(null=False)
    brandid = models.ForeignKey(Brands, on_delete=models.CASCADE)
    

    # New fields for shipping information
    weight = models.DecimalField(max_digits=10, decimal_places=2, default=1, null=False, help_text="Weight in kg")
    length = models.DecimalField(max_digits=10, decimal_places=2, default=5, null=False, help_text="Length in cm")
    width = models.DecimalField(max_digits=10, decimal_places=2, default=5, null=False, help_text="Width in cm")
    height = models.DecimalField(max_digits=10, decimal_places=2, default=5, null=False, help_text="Height in cm")

    storeid = models.ForeignKey(Store, on_delete=models.CASCADE, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class Sku(models.Model):
    id = models.BigAutoField(primary_key=True)
    productid = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.productid)



class Productparams(models.Model):
    id = models.BigAutoField(primary_key=True)
    productid = models.ForeignKey(Product, on_delete=models.CASCADE)
    skuid = models.ForeignKey(Sku, on_delete=models.CASCADE, null=True)
    key = models.CharField(max_length=100)
    value = models.CharField(max_length=200)

    def __str__(self):
        return self.key

class Categoryparams(models.Model):
    id = models.BigAutoField(primary_key=True)
    catid = models.ForeignKey(Category, on_delete=models.CASCADE)
    key = models.CharField(max_length=100)

    def __str__(self):
        return self.key
    







