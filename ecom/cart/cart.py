from store.models import Product
class Cart():
    def __init__(self, request):
        self.session = request.session

        # Get the current session key if it exist
        cart = self.session.get('sessionKey')

        # If the user is new, no session key. Create one
        if 'sessionKey' not in request.session:
            cart = self.session['sessionKey'] = {}

        # Make sure cart is available on all pages of site
        self.cart = cart

    def add(self, product):
        productId = str(product.id)

        # logic
        if productId in self.cart:
            pass
        else:
            self.cart[productId] = {'price': str(product.price)}
        
        self.session.modified = True

    def __len__(self):
        return len(self.cart)
    
    def getProds(self):
        # Get IDs from cart
        productIds =self.cart.keys()
        # Use IDs to lookup products in database model
        products = Product.objects.filter(id__in=productIds)
        return products
