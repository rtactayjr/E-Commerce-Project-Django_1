from django.shortcuts import render

from products.models import Product

# Create your views here.
def store(request):
    products = Product.objects.all().filter(is_available=True).order_by('id')

    context = {
        'products': products
    }
    return render(request, 'store/store.html', context)