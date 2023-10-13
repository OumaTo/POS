from django.db import models


# Create your models here.
class Shelf(models.Model):
    shelf_no = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True)

    def __str__(self):
        return self.shelf_no
     

class Category(models.Model):
    category= models.CharField(max_length=200)

    def __str__(self):
        return self.category


class Product(models.Model):
    Name = models.CharField(max_length=200)
    Price = models.IntegerField(default=100)
    Shelf_No = models.ForeignKey(Shelf, on_delete=models.SET_DEFAULT, default=1)
    Quantity = models.IntegerField(default=1)
    Category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    Description = models.TextField()
    Arrival_Date = models.DateField(auto_now_add=True)
    Manufactured_Date = models.DateField(null=True)
    Expiry_Date = models.DateField(null=True)
    Brand = models.CharField(max_length=200, null = True)
    Distributor = models.CharField(max_length=200)
    Photo = models.ImageField(null=True)
    

    condition=(
        ('spoilt','spoilt'),
        ('Good','Good')
    )
    Condition = models.CharField(max_length=200, choices=condition, default='Good')

    def __str__(self):
        return (f'{self.Name}')


class Distributor(models.Model):
    name = models.CharField(max_length=200)
    product = models.CharField(max_length=200)

    def __str__(self):
        return self.name


