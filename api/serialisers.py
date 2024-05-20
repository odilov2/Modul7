from rest_framework import serializers
from products.models import Categories, Products, FeaturedProducts
from users.models import Users


class CategoriesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categories
        fields = '__all__'


class ProductsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Products
        fields = '__all__'


class FeaturedProductsSerializer(serializers.ModelSerializer):

    class Meta:
        model = FeaturedProducts
        fields = '__all__'


class UsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = '__all__'
