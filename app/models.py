from django.db import models
from django.contrib.auth.models import User


# Create your models here.

CATEGORY_CHOICES = (
    ('ML', 'Milk'),
    ('DL', 'Dairy'),
    ('IC', 'Ice Cream'),
)

class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField()
    image = models.ImageField(upload_to='product')
    category = models.CharField(choices=CATEGORY_CHOICES,  max_length=5,null=True, blank=True)
    def __str__(self):
        return self.title
    
class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def total_cost(self):
        return self.quantity * self.product.price

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    total_cost = models.FloatField()
    ordered_date = models.DateTimeField(auto_now_add=True)
    

    