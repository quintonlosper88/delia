from unicodedata import category
from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.views.generic import CreateView
from .forms import MessageModelForm
from .models import ServicesCategory, Services,ProductCategory,Product
# Create your views here.
def index(request):
    
    categories = ProductCategory.objects.all()
    context = {'categories':categories}
    return render(request,'website/index.html',context)

def about(request):
    return render(request,'website/about.html',{})


def blog(request):
    return render(request,'website/blog.html',{})


def shopping_view(request):
    return render(request,'website/shop.html',{})

def services(request, category_slug=None):
    category=None
    categories = ServicesCategory.objects.all()
    services = Services.objects.all()
    if category_slug:
        category = get_object_or_404(ServicesCategory, slug=category_slug)
        services = services.filter(category=category)
  
    return render(request,
                  'website/service.html',{
                      'category':category,
                      'categories':categories,
                      'services': services
                  })
    

def portfolio(request):
    return render(request,'website/portfolio.html',{})

def contact(request):
    form=MessageModelForm()
    if request.method=='POST':
        form=MessageModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('website/')
    context={
            'form':form
        }
    return render(request,'website/contact.html',context)

# def product_list(request, category_slug=None):
#     category=None
#     categories = ProductCategory.objects.all()
#     products = Product.objects.filter(available=True)
#     if category_slug:
#         category = get_object_or_404(ProductCategory, slug=category_slug)
#         products = products.filter(ProductCategory=category)
#     return render(request,'website/product_list.html',{
#         'category':category,
#         'categories':categories,
#         'products':products
#     })

def product_list(request, category_slug=None):
    return render(request,'website/product_list.html',{})

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    return render(request,'website/product_detail.html',{'product':product})

def service_list(request, category_slug=None):
    category=None
    categories = ServicesCategory.objects.all()
    services = Services.objects.filter(available = True)
    if category_slug:
        category = get_object_or_404(ServicesCategory, slug=category_slug)
        services = services.filter(category=category)
    return render(request,
                  'website/service.html',{
                  'categories':categories,
                  'services': services
                  })
    