import unittest
from sum_numbers import add_numbers

class TestAddNumbers(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(add_numbers(10, 20), 30)

    def test_zero(self):
        self.assertEqual(add_numbers(0, 0), 0)

    def test_negative_numbers(self):
        self.assertEqual(add_numbers(-10, -20), -30)

    def test_positive_and_negative(self):
        self.assertEqual(add_numbers(100, -50), 50)

    def test_decimal_numbers(self):
        self.assertAlmostEqual(add_numbers(10.5, 20.3), 30.8)

if __name__ == "__main__":
    unittest.main()