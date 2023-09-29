from django.shortcuts import render


def homepage(request):
    # products = Product.objects.all().filter(is_available=True).order_by('created_date')

    # #Get the review rating
    # for product in products:
    #     reviews = ReviewRating.objects.filter(product_id=product.id, status=True)
    
    # context = {
    #     'products': products,
    #     'reviews': reviews,
    # }

    return render(request, 'core/homepage.html',)