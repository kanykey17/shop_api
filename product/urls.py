from django.urls import path
from .views import (
    CategoryListAPIView,
    CategoryDetailAPIView,
    ProductListAPIView,
    ProductDetailAPIView,
    ProductReviewListAPIView,
    ReviewListAPIView,
    ReviewDetailAPIView,
)

urlpatterns = [
    path('api/v1/categories/', CategoryListAPIView.as_view()),
    path('api/v1/categories/<int:pk>/', CategoryDetailAPIView.as_view()),

    path('api/v1/products/', ProductListAPIView.as_view()),
    path('api/v1/products/<int:pk>/', ProductDetailAPIView.as_view()),
    path('api/v1/products/reviews/', ProductReviewListAPIView.as_view()),

    path('api/v1/reviews/', ReviewListAPIView.as_view()),
    path('api/v1/reviews/<int:pk>/', ReviewDetailAPIView.as_view()),
]