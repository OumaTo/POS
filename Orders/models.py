from collections.abc import Iterable
from django.db import models

from Products.models import Product

# Create your models here.
class Order(models.Model):
    stat = (
        ('pending', 'Pending'),
        ('Completed', 'Completed'),
        ('Canceled', 'Canceled')
    )
    Item = models.ForeignKey(Product, on_delete=models.CASCADE)
    Quantity = models.IntegerField()
    Total = models.IntegerField(default=100)
    Date = models.DateField(auto_now_add=True)
    Status = models.CharField(max_length=200, choices=stat ,default='Pending')


    def __str__(self):
        return f'{self.Item} {self.Status}'

