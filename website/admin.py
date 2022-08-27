from django.contrib import admin
from .models import Messages, ServicesCategory, Services, ProductCategory, Product
# Register your models here.
admin.site.register(Messages)


@admin.register(ServicesCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display =['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    
    
@admin.register(Services)   
class ServicesAdmin(admin.ModelAdmin):
    list_display = ['name','category', 'slug', 'price']
    list_editable = ['price']
    prepopulated_fields = {
        'slug': ('name',)
    }
    
@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display =['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    
    
@admin.register(Product)   
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price','available']
    prepopulated_fields = {
        'slug': ('name',)
    }