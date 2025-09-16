# test_math_functions.py
import unittest
import math_functions

class TestMathFunctions(unittest.TestCase):

    def test_factorial(self):
        self.assertEqual(math_functions.factorial(0), 1)   
        self.assertEqual(math_functions.factorial(4), 24)  

        with self.assertRaises(ValueError):
            math_functions.factorial(-3)

    def test_is_prime(self):

        self.assertTrue(math_functions.is_prime(31)) 
        self.assertTrue(math_functions.is_prime(17))  
        self.assertFalse(math_functions.is_prime(0))  

    def test_area_of_circle(self):
       
        self.assertAlmostEqual(math_functions.area_of_circle(4), 50.26548, places=5)
        self.assertAlmostEqual(math_functions.area_of_circle(0), 0.0, places=5)

       
        with self.assertRaises(ValueError):
            math_functions.area_of_circle(-2)

if __name__ == "__main__":
    unittest.main()
