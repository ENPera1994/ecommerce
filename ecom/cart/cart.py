
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