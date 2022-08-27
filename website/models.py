from enum import auto
from time import timezone
from django.db import models
from django import utils
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Messages(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone = PhoneNumberField()
    email = models.EmailField()
    message = models.TextField(max_length=150)
    time_created = models.DateTimeField(auto_now_add=True)
    
    # def __str__(self):
    #     return f"{self.first_name} {self.last_name} {self.time_created}" 
    

class ServicesCategory(models.Model):
    name=models.CharField(max_length=100, db_index=True)
    slug=models.SlugField(max_length=100,unique=True)
    
    class Meta:
        ordering =('name',)
        verbose_name = 'category'
        verbose_name_plural = 'Service Categories'

    def __str__(self):
        return self.name
        
class Services(models.Model):
    category=models.ForeignKey(ServicesCategory,on_delete=models.CASCADE)
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100,unique=True)
    description = models.TextField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    class Meta:
        ordering = ('category',)
        index_together = (('id','slug'),)
        
    def __str__(self):
        return self.name

class ProductCategory(models.Model):
    name=models.CharField(max_length=100, db_index=True)
    slug=models.SlugField(max_length=100,unique=True)
    
    class Meta:
        ordering =('name',)
        verbose_name = 'category'
        verbose_name_plural = 'Product Categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('website:product_list',args=[self.slug])
    
class Product(models.Model):
    category=models.ForeignKey(ProductCategory,on_delete=models.CASCADE)
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100,unique=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d',blank=True)
    description = models.TextField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('name',)
        index_together = (('id','slug'),)
        
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('website:product_detail',args=[self.id, self.slug])
    
    

