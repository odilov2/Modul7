
from django.urls import path, include
from .views import (ProductsAPIViewSet, UsersAPIViewSet,
                    FeaturedProductsAPIViewSet, CategoriesAPIViewSet)
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

router = DefaultRouter()
router.register('products', viewset=ProductsAPIViewSet)
router.register('categories', viewset=CategoriesAPIViewSet)
router.register('featuredproducts', viewset=FeaturedProductsAPIViewSet)
router.register('users', viewset=UsersAPIViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', views.obtain_auth_token),
]
