class Cart:
    def __init__(self):
        self.items = {}  # store products as {product_name: quantity}

    # Simulating static polymorphism using default arguments
    def add_product(self, name=None, quantity=1, name2=None, quantity2=1):
        # Add first product
        if name:
            if name in self.items:
                self.items[name] += quantity
            else:
                self.items[name] = quantity

        # Add second product (optional)
        if name2:
            if name2 in self.items:
                self.items[name2] += quantity2
            else:
                self.items[name2] = quantity2

    def show_cart(self):
        return self.items



cart = Cart()

# Add single product
cart.add_product("iPhone", 2)

# Add another single product (default quantity = 1)
cart.add_product("Shoes")

# Add two products in one call
cart.add_product("Laptop", 1, "Headphones", 3)

print("Cart Items:", cart.show_cart())
