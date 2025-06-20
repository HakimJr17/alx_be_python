import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """
    Test suite for the SimpleCalculator class, covering addition,
    subtraction, multiplication, and division operations.
    """

    def setUp(self):
        """
        Set up the SimpleCalculator instance before each test method is run.
        This ensures each test starts with a fresh calculator object.
        """
        self.calc = SimpleCalculator()

    def test_addition(self):
        """
        Test the add method with various numerical inputs,
        including positive, negative, and zero values.
        """
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-5, -5), -10)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(100, 0), 100)
        self.assertEqual(self.calc.add(2.5, 3.5), 6.0) # Test with floats

    def test_subtraction(self):
        """
        Test the subtract method with various numerical inputs,
        including positive, negative, and zero values.
        """
        self.assertEqual(self.calc.subtract(5, 2), 3)
        self.assertEqual(self.calc.subtract(2, 5), -3)
        self.assertEqual(self.calc.subtract(10, 10), 0)
        self.assertEqual(self.calc.subtract(-1, -1), 0)
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertEqual(self.calc.subtract(7.5, 2.5), 5.0) # Test with floats

    def test_multiply(self):
        """
        Test the multiply method with various numerical inputs,
        including positive, negative, zero, and fractional values.
        """
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(-2, -3), 6)
        self.assertEqual(self.calc.multiply(5, 0), 0)
        self.assertEqual(self.calc.multiply(0, 5), 0)
        self.assertEqual(self.calc.multiply(2.5, 2), 5.0) # Test with floats
        self.assertEqual(self.calc.multiply(0.5, 0.5), 0.25) # Test with floats

    def test_divide(self):
        """
        Test the divide method with various numerical inputs,
        including normal division and the critical edge case of division by zero.
        """
        self.assertEqual(self.calc.divide(10, 2), 5.0)
        self.assertEqual(self.calc.divide(5, 2), 2.5)
        self.assertEqual(self.calc.divide(-10, 2), -5.0)
        self.assertEqual(self.calc.divide(10, -2), -5.0)
        self.assertEqual(self.calc.divide(-10, -2), 5.0)
        self.assertEqual(self.calc.divide(0, 5), 0.0) # Division of zero by non-zero
        self.assertIsNone(self.calc.divide(10, 0)) # Test division by zero, expecting None
        self.assertIsNone(self.calc.divide(0, 0))  # Test 0 divided by 0, expecting None

# This block allows you to run the tests directly from the command line:
# python -m unittest test_simple_calculator.py
if __name__ == '__main__':
    unittest.main()