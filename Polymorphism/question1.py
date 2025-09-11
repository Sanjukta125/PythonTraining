class ProductSearch:
    def __init__(self, products):
        self.products = products  # List of products (dicts)

    def search(self, name=None, category=None, min_price=None, max_price=None):
        results = self.products

        # Filter by name
        if name:
            results = [p for p in results if name.lower() in p["name"].lower()]

        # Filter by category
        if category:
            results = [p for p in results if p["category"].lower() == category.lower()]

        # Filter by price range
        if min_price is not None and max_price is not None:
            results = [p for p in results if min_price <= p["price"] <= max_price]

        return results


# Sample product list (like a database)
products = [
    {"name": "iPhone 15", "category": "Electronics", "price": 80000},
    {"name": "Samsung Galaxy S23", "category": "Electronics", "price": 75000},
    {"name": "Nike Shoes", "category": "Fashion", "price": 5000},
    {"name": "Levi's Jeans", "category": "Fashion", "price": 3000},
]

# Create search system
search_system = ProductSearch(products)

# --- Test different searches (simulating overloading) ---
print("Search by name:")
print(search_system.search(name="iPhone"))

print(" Search by name + category:")
print(search_system.search(name="Samsung", category="Electronics"))

print(" Search by name + category + price range:")
print(search_system.search(name="Nike", category="Fashion", min_price=4000, max_price=6000))
