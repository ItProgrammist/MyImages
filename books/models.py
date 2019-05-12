from django.db import models

from categories.models import Category


class Book(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=300)
    price = models.IntegerField()
    category = models.ForeignKey(
        to=Category,
        related_name='books',
        on_delete=models.CASCADE,
    )

