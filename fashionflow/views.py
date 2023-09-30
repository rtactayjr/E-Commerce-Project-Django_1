from django.shortcuts import render

from products.models import Product
from category.models import Category

def homepage(request):
    categories = Category.objects.all().order_by('category_name')

    # #Get the review rating
    # for product in products:
    #     reviews = ReviewRating.objects.filter(product_id=product.id, status=True)
    
    context = {
        'categories': categories,
        
    }

    return render(request, 'core/homepage.html', context)