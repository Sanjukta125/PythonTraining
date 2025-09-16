# math_functions.py

import math

def factorial(n: int) -> int:
    """Return factorial of n"""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    return 1 if n == 0 else math.prod(range(1, n + 1))

def is_prime(n: int) -> bool:
    """Return True if n is prime"""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def area_of_circle(radius: float) -> float:
    """Return area of a circle"""
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius * radius
