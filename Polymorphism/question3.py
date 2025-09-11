class Discount:
    # Simulating static polymorphism with default parameters
    def apply_discount(self, price, flat=0, percent=0, bogo=False, quantity=1):
        final_price = price * quantity

        # Apply Flat Discount
        if flat > 0:
            final_price -= flat

        # Apply Percentage Discount
        if percent > 0:
            final_price -= (final_price * percent) / 100

        # Apply Buy One Get One
        if bogo:
            # Pay only for half the items (rounded up)
            payable_qty = (quantity // 2) + (quantity % 2)
            final_price = price * payable_qty

        return max(final_price, 0)  # Ensure price doesn't go negative


# ---------------- TEST ----------------
d = Discount()

# Flat discount
print("Flat Discount:", d.apply_discount(1000, flat=200))  

# Percentage discount
print("Percentage Discount:", d.apply_discount(1000, percent=10))  

# Buy One Get One (for 5 items)
print("BOGO Discount:", d.apply_discount(500, bogo=True, quantity=5))  
