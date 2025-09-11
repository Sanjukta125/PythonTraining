# Base Class
class Payment:
    def pay(self, amount):
        raise NotImplementedError("Subclass must override this method")


# Derived Class: Credit Card
class CreditCardPayment(Payment):
    def pay(self, amount):
        return f"Paid ₹{amount} using Credit Card"


# Derived Class: UPI
class UPIPayment(Payment):
    def pay(self, amount):
        return f"Paid ₹{amount} using UPI"


# Derived Class: Cash on Delivery
class CODPayment(Payment):
    def pay(self, amount):
        return f"Payment of ₹{amount} will be made on delivery"


# ---------------- TEST ----------------
payments = [
    CreditCardPayment(),
    UPIPayment(),
    CODPayment()
]

for method in payments:
    print(method.pay(1500))
