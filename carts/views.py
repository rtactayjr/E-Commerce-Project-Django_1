from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist

from products.models import Product
from . models import Cart, CartItem

# Create your views here.

def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

def add_to_cart(request, product_id):
    # Get the product first
    product = Product.objects.get(id=product_id)
    
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        
    except Cart.DoesNotExist:
        
        cart = Cart.objects.create(
            cart_id=_cart_id(request),
        )
        
        cart.save()
        
        # Put product inside the cart (combine product with cart)
        try:
            cart_item = CartItem.objects.get(product=product, cart=cart)
            cart_item.quantity += 1
            cart_item.save()
        except CartItem.DoesNotExist:
            cart_item = CartItem.objects.create(
                product=product, 
                quantity=1, 
                cart=cart
                )
            cart_item.save()
        
    return render(request,'store/product_detail.html')
            
def cart(request, total=0, quantity=0, cart_items=None):
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        
        # loop through cart_items
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            quantity += cart_item.quantity
        tax = (2 * total) /100
        grand_total = total + tax
        
    except ObjectDoesNotExist:
        pass
    context = {
        'total': total,
        'quantity': quantity,
        'cart_items': cart_items,
        'tax': tax,
        'grand_total': grand_total,
        
    }
    return render(request, 'carts/cart.html', context)