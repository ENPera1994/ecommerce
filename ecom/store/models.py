from django.db import models
import datetime

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Customer(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=20)
    password = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.firstName} {self.lastName}'

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    dimension = models.IntegerField(default=0)
    cantRoom = models.IntegerField(default=0)
    cantFloor = models.IntegerField(default=0)
    description = models.CharField(max_length=250, default='', blank=True, null=True)
    image = models.ImageField(upload_to='uploads/product/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    # Add Sale Stuff
    inSale = models.BooleanField(default=False)
    salePrice = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Order(models.Model):
    date = models.DateField(default=datetime.datetime.today)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    adress = models.CharField(max_length=100, default='', blank=True)
    phone = models.CharField(max_length=25, default='', blank=True)
    status =models.BooleanField(default=False)

    def __str__(self):
        return f'{self.customer} {self.product}'