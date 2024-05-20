from django.urls import path

from products.views import ShopView, ShopDetailView, ProductListView, ContactView, CartView, AboutView, HelpView, CheckoutView

urlpatterns = [
    path('shop/', ShopView.as_view(), name='shop'),
    path('shopdetail/', ShopDetailView.as_view(), name='shop-detail'),
    path('products_detail/', ProductListView.as_view(), name='products-detail'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('cart/', CartView.as_view(), name='cart'),
    path('about/', AboutView.as_view(), name='about'),
    path('help/', HelpView.as_view(), name='help'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
]