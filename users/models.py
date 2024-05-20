from django.db import models


class Users(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    username = models.CharField(max_length=20)

    class Meta:
        ordering = ['id']
        indexes = [
            models.Index(fields=['id'])
        ]