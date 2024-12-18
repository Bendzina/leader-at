import django_filters
from .models import Product, Category, Brands, Categoryparams, Productparams, Sku

class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    price = django_filters.RangeFilter()
    category_name = django_filters.CharFilter(field_name='category__name', lookup_expr='icontains')
    brand_name = django_filters.CharFilter(field_name='brand__name', lookup_expr='icontains')

    class Meta:
        model = Product
        fields = ['name', 'price', 'catid', 'brandid']


class CategoryFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Category
        fields = ['name']


class BrandsFilter(django_filters.FilterSet):
    brand = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Brands
        fields = ['brand']


class CategoryparamsFilter(django_filters.FilterSet):
    key = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Categoryparams
        fields = ['key']


class ProductparamsFilter(django_filters.FilterSet):
    key = django_filters.CharFilter(lookup_expr='icontains')
    value = django_filters.CharFilter(lookup_expr='iexact')
    productid = django_filters.NumberFilter(field_name='productid__id') 
    skuid = django_filters.NumberFilter(field_name='skuid__id')

    class Meta:
        model = Productparams
        fields = ['key', 'value', 'productid', 'skuid']


class SkuFilter(django_filters.FilterSet):
    productid = django_filters.NumberFilter()
    class Meta:
        model = Sku
        fields = ['productid']
    
