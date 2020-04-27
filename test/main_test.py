import sys
import unittest

from src.main import add, inc, mutiply, divide


class MainTestCase(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(add(2,2), 4)

    def test_inc(self):
        self.assertEqual(inc(5),6)

    def test_multiply(self):
        self.assertEqual(mutiply(2,3), 6)

    def test_division_nonZero(self):
        self.assertEqual(divide(6,2), 3)

    def test_division_zero(self):
        self.assertRaises( ZeroDivisionError, divide, 6, 0)

if __name__ == "__main__":
    unittest.main()