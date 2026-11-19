# Shopping Cart Service
# Contributor: Checkout & Order Team
CART = []
def add_to_cart(product_id):
    CART.append(product_id)
    return len(CART)
