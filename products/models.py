from django.db import models


class Categories(models.Model):
    title = models.CharField(max_length=20)

    class Meta:
        ordering = ['id']
        indexes = [
            models.Index(fields=['id'])
        ]


class Products(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    price = models.FloatField()
    image = models.ImageField(upload_to='products/products')
    category_id = models.ForeignKey(Categories, on_delete=models.CASCADE)
    country = models.CharField(max_length=20)

    class Meta:
        ordering = ['id']
        indexes = [
            models.Index(fields=['id'])
        ]


class FeaturedProducts(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    price = models.FloatField()
    image = models.ImageField(upload_to='products/products')

    class Meta:
        ordering = ['id']
        indexes = [
            models.Index(fields=['id'])
        ]

