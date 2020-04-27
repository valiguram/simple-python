import sys
import unittest

from src.main import add, inc


class MainTestCase(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(add(2,2), 4)

    def test_inc(self):
        self.assertEqual(inc(5),6)

if __name__ == "__main__":
    unittest.main()