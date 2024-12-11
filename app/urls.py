from django.urls import path
from .views import ProductListView, ProductCreateView, ProductAPI, CategoryListView, CategoryDetailView, CategoryApi, BrandsDetailView, BrandsListView, BrandApi, CategoryparamsListView, CategoryparamsApi, CategoryparamsDetailView, ProductparamsListView, ProductparamsDetailView, ProductparamsApi
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # Product URLs
    path('products/', ProductListView.as_view(), name='product-list-view'),
    path('products-create/', ProductCreateView.as_view(), name='product-create-view'),
    path('products-api/', ProductAPI.as_view(), name='product-api'),

    # Category URLs
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('categories-api/', CategoryApi.as_view(), name='category-api'),

    # Brand URLs
    path('brands/', BrandsListView.as_view(), name='brand-list'),
    path('brands/<int:pk>/', BrandsDetailView.as_view(), name='brand-detail'),
    path('brands-api/', BrandApi.as_view(), name='brand-api'),
    


    # Catparams URLs
    path('categoryparams/', CategoryparamsListView.as_view(), name='categoryparams-list'),
    path('categoryparams/<int:pk>/', CategoryparamsDetailView.as_view(), name='categoryparams-detail'),
    path('categoryparams-api/', CategoryparamsApi.as_view(), name='categoryparams-api'),

    # Productparams URLs
    path('productparams/', ProductparamsListView.as_view(), name='productparams-list'),
    path('productparams/<int:pk>/', ProductparamsDetailView.as_view(), name='productparams-detail'),
    path('productparams-api/', ProductparamsApi.as_view(), name='productparams-api'),


    # Token URLs
    # path('app/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('app/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]


# http://127.0.0.1:8000/products-list/

