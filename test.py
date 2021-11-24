import unittest
from program import factorial

class TestFactorial(unittest.TestCase):
    def test_mul1(self):
        result1 = factorial(5)
        self.assertEqual(result1, 120)
    def test_mul2(self):
        result2 = factorial(0)
        self.assertEqual(result2, 1)
    def test_mul3(self):
        result3 = factorial(10)
        self.assertEqual(result3, 3628800)


if __name__ == '__main__':
    unittest.main()
