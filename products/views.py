
from django.shortcuts import render, redirect
from django.views import View

from products.models import Products, Categories, FeaturedProducts


class LandingPageView(View):
    def get(self, request):
        products = Products.objects.all()
        categories = Categories.objects.all()
        context = {
            'products': products,
            'categories': categories
        }
        return render(request, "landing.html", context)


class ShopView(View):
    def get(self, request):
        products = Products.objects.all()
        categories = Categories.objects.all()
        featured = FeaturedProducts.objects.all()
        context = {
            'product': products,
            'categories': categories,
            "featured": featured
        }
        return render(request, "products/shop.html", context)


class ShopDetailView(View):
    def get(self, request):
        products = Products.objects.all()
        categories = Categories.objects.all()
        featured = FeaturedProducts.objects.all()
        context = {
            'product': products,
            'categories': categories,
            "featured": featured
        }
        return render(request, "products/shop_detail.html", context)


class ProductListView(View):
    def get(self, request):
        search = request.GET.get("search")
        if not search:
            products = Products.objects.all()
            return render(request, "products/products_list.html", context={"products": products})
        else:
            products = Products.objects.filter(title__icontains=search) | Products.objects.filter(title__icontains=search)
            if not products:
                return redirect("landing")
            else:
                context = {
                    "products": products,
                    "search": search
                }
            return render(request, "products/products_list.html", context)


class ContactView(View):
    def get(self, request):
        return render(request, "products/contact.html")


class CartView(View):
    def cart(self, request):
        products = Products.objects.all()
        context = {"products": products}
        return render(request, "products/cart.html", context)


class AboutView(View):
    def about(self, request):
        products = Products.objects.all()
        context = {"products": products}
        return render(request, "products/cart.html", context)


class HelpView(View):
    def help(self, request):
        products = Products.objects.all()
        context = {"products": products}
        return render(request, "products/cart.html", context)


class CheckoutView(View):
    def help(self, request):
        products = Products.objects.all()
        context = {"products": products}
        return render(request, "products/cart.html", context)






