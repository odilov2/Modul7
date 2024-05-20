from django.contrib import admin
from .models import Products, Categories, FeaturedProducts
from import_export.admin import ImportExportModelAdmin
# Register your models here.


@admin.register(Products)
class ProductsAdmin(ImportExportModelAdmin):
    list_display = ['id', 'title', 'price', 'description']
    list_display_links = ['title']
    search_fields = ['title', 'price']
    ordering = ['id']


@admin.register(Categories)
class CategoriesAdmin(ImportExportModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['title']
    search_fields = ['title']
    ordering = ['id']


@admin.register(FeaturedProducts)
class FeaturedAdmin(ImportExportModelAdmin):
    list_display = ['id', 'title', 'price', 'description']
    list_display_links = ['title']
    search_fields = ['title', 'price']
    ordering = ['id']
