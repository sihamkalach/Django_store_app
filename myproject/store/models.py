from django.db import models 
import datetime 
#categories table  
class Category(models.Model): 
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name 
  
# 
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    image = models.ImageField(upload_to='images')
class User(models.Model):
    name = models.CharField(max_length=50)
    telephone = models.CharField(max_length=20)
    ville = models.CharField(max_length=30)
    address = models.CharField(max_length=255)
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, default='Pending') 

