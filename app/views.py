from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from .filters import ProductFilter, CategoryFilter, BrandsFilter, CategoryparamsFilter, ProductparamsFilter
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.views import APIView
from .models import Product, Category, Brands, Categoryparams, Productparams
from .serializers import ProductSerializer, CategorySerializer, BrandsSerializer, CategoryparamsSerializer, ProductparamsSerializer
from rest_framework import generics


# Product Views
class ProductCreateView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter


class ProductAPI(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Category Views
class CategoryCreateView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = CategoryFilter


class CategoryDetailView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryApi(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Brand Views

class BrandsCreateView(CreateAPIView):
    queryset = Brands.objects.all()
    serializer_class = BrandsSerializer


class BrandsListView(generics.ListAPIView):
    queryset = Brands.objects.all()
    serializer_class = BrandsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = BrandsFilter


class BrandsDetailView(generics.RetrieveAPIView):
    queryset = Brands.objects.all()
    serializer_class = BrandsSerializer


class BrandApi(APIView):
    def get(self, request):
        brands = Brands.objects.all()
        serializer = BrandsSerializer(brands, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = BrandsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


# Categoryparams Views


class CategoryparamsCreateView(CreateAPIView):
    queryset = Categoryparams.objects.all()
    serializer_class = CategoryparamsSerializer



class CategoryparamsListView(generics.ListAPIView):
    queryset = Categoryparams.objects.all()
    serializer_class = CategoryparamsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = CategoryparamsFilter



class CategoryparamsDetailView(generics.RetrieveAPIView):
    queryset = Categoryparams.objects.all()
    serializer_class = CategoryparamsSerializer


class CategoryparamsApi(APIView):
    def get(self, request):
        Categoryparams = Categoryparams.objects.all()
        serializer = CategoryparamsSerializer(Categoryparams, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CategoryparamsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




# Productparams Views

class ProductparamsCreateView(CreateAPIView):
    queryset = Productparams.objects.all()
    serializer_class = ProductparamsSerializer


class ProductparamsListView(generics.ListAPIView):
    queryset = Productparams.objects.all()
    serializer_class = ProductparamsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductparamsFilter

class ProductparamsDetailView(generics.RetrieveAPIView):
    queryset = Productparams.objects.all()
    serializer_class = ProductparamsSerializer


class ProductparamsApi(APIView):
    def get(self, request):
        productparams = Productparams.objects.all()
        serializer = ProductparamsSerializer(productparams, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ProductparamsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)