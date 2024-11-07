import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def testadd1(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    #Add the following test methods to the TestCalculator class:

    def testadd2(self):
        self.assertEqual(self.calc.add(77, 33), 110)

    def testsubtract1(self):
        self.assertEqual(self.calc.subtract(5, 7), 2)
    def testsubtract2(self):
        self.assertEqual(self.calc.subtract(6, 8), 2)

    def test_multiply1(self):
        self.assertEqual(self.calc.multiply(7, 5), 35)
    def test_multiply2(self):
        self.assertEqual(self.calc.multiply(0, 9), 0)

    def test_divide1(self):
        self.assertEqual(self.calc.divide(8, 2), 4)
    def test_divide2(self):
        self.assertEqual(self.calc.divide(100, 10), 10)

    def test_modulo1(self):
        self.assertEqual(self.calc.modulo(9, 4), 1)
    def test_modulo2(self):
        self.assertEqual(self.calc.modulo(10, 3), 1)

if __name__ == '__main__':
    unittest.main()