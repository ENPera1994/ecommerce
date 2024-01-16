from django.shortcuts import render, get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse

def cartSummary(request):
    cart = Cart(request)
    cartProducts = cart.getProds
    return render(request, 'cartSumary.html', {'cartProducts':cartProducts})


def cartAdd(request):
    #  Get the cart
    cart = Cart(request)
    # Test for POST
    if request.POST.get('action') == 'post':
        
        # Get the stuff
        productId = int(request.POST.get('productId'))
        
        # lookup product in DB
        product = get_object_or_404(Product, id=productId)
        
        # save to a session
        cart.add(product=product)

        # Get cart quantity
        cartQuantity = cart.__len__()

        # Return response
        response = JsonResponse({'qty': cartQuantity})
        return response

def cartDelete(request):
    pass
