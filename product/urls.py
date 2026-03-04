from django.urls import path
from .views import (
    CategoryListCreateAPIView,
    CategoryDetailAPIView,
    ProductListCreateAPIView,
    ProductDetailAPIView,
    ProductReviewListAPIView,
    ReviewListCreateAPIView,
    ReviewDetailAPIView
)

urlpatterns = [

    path('api/v1/categories/', CategoryListCreateAPIView.as_view()),
    path('api/v1/categories/<int:pk>/', CategoryDetailAPIView.as_view()),

    path('api/v1/products/', ProductListCreateAPIView.as_view()),
    path('api/v1/products/<int:pk>/', ProductDetailAPIView.as_view()),
    path('api/v1/products/reviews/', ProductReviewListAPIView.as_view()),

    path('api/v1/reviews/', ReviewListCreateAPIView.as_view()),
    path('api/v1/reviews/<int:pk>/', ReviewDetailAPIView.as_view()),
]