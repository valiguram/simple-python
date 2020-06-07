import sys
import unittest

from src.main import add, inc, mutiply, subt


class MainTestCase(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(add(2,2), 4)

    def test_inc(self):
        self.assertEqual(inc(5),6)

    def test_multiply(self):
        self.assertEqual(mutiply(2,3), 6)
    
    def test_subtract(self):
        self.assertEqual(subt(5,3), 2)

if __name__ == "__main__":
    unittest.main()