from django.shortcuts import render, get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse
from django.contrib import messages


def cartSummary(request):
    cart = Cart(request)
    cartProducts = cart.getProds
    totals = cart.cartTotal()
    return render(request, 'cartSumary.html', {'cartProducts':cartProducts, 'totals':totals})


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
        messages.success(request, ("Agregado al Carrito"))
        return response

def cartDelete(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        # Get stuff
        productId = str(request.POST.get('productId'))
        # Call delete Function in Cart
        cart.delete(product=productId)
        response = JsonResponse({'product':productId})
        #return redirect('cart_summary')
        messages.success(request, ("Eliminado del carrito"))
        return response
