
from django.contrib import admin
from django.urls import path
from .views import index, about, portfolio,contact,services,blog,product_list,product_detail,shopping_view

app_name='website'
urlpatterns = [
    path('', index,name='index'),
    path('about/', about,name='about'),
    path('porfolio/', portfolio,name='portfolio'),
    path('contact/', contact,name='contact'),
    path('services/', services,name='services'),
    path('blog/', blog,name='blog'),
    path('shop/', shopping_view,name='shop'),
    path('<slug:category_slug>/', product_list,name='product_list'),
    path('<int:id>/<slug:slug>/', product_detail, name='product_detail'),

    
]
