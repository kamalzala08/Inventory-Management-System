from django.db import models
from django.contrib.auth.models import User

CATEGORY = (
    ('Stationary', 'Stationary'),
    ('Electronics', 'Electronics'),
    ('Food', 'Food'),
)


class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    quantity = models.PositiveIntegerField(null=True)
    category = models.CharField(max_length=50, choices=CATEGORY, null=True)
    
    
    def __str__(self):
        return self.name
    

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    orderby = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    order_quantity = models.PositiveIntegerField(null=True)
    date = models.DateField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "Orders" ##to change table name
    
    def __str__(self):
        return f'{self.orderby}-{self.product}'
    