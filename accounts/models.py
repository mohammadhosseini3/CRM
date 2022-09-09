from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE,null=True)
    name = models.CharField(max_length=200,null = True)
    phone = models.CharField(max_length=200,null = True)
    email = models.CharField(max_length=200,null = True)
    date_created = models.DateTimeField(auto_now_add = True,null = True)
    profile_pic = models.ImageField(default= 'user.png' , null=True,blank=True)
    def __str__(self):
        return self.user.username

class Tag(models.Model):
    name = models.CharField(max_length=200,null = True)
    def __str__(self):
        return self.name

class Product(models.Model):
    CATEGORY = (
        ('indoor','Indoor'),
        ('outdoor','Outdoor')
    )
    name = models.CharField(max_length=200,null = True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=1000,null = True,choices=CATEGORY)
    description = models.CharField(max_length=200,null=True)
    date_created = models.DateTimeField(auto_now_add = True,null = True)
    tags = models.ManyToManyField(Tag)
    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS = (
        ('pending','Pending'),
        ('out for delivery','Out for delivery'),
        ('delivered','Delivered')
    )
    customer = models.ForeignKey('Customer',null=True,on_delete = models.SET_NULL)
    product = models.ForeignKey('Product',null=True,on_delete = models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    status = models.CharField(max_length=200,choices=STATUS,null=True)
    note = models.CharField(max_length=1000,null=True)
    def __str__(self):
        return self.product.name