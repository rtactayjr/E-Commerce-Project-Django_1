from django.shortcuts import render, get_object_or_404, redirect

from products.models import Product
from category.models import Category

# Create your views here.
def store(request, category_slug=None):
    categories = None
    products = None
    
    if category_slug != None:
        categories = get_object_or_404(Category, category_slug=category_slug)
        products = Product.objects.all().filter(category=categories, is_available=True)
        product_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True).order_by('id')
        product_count = products.count()
        
    context = {
        'products': products,
        'product_count':product_count
    }
    return render(request, 'store/store.html', context)