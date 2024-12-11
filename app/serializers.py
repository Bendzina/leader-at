from rest_framework import serializers
from .models import Product, Category, Brands, Categoryparams, Productparams

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']



class BrandsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brands
        fields = ['id', 'brand']


class CategoryparamsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoryparams
        fields = '__all__'
        

class ProductparamsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productparams
        fields = '__all__'

