import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:

        #new testcase for add method
        self.assertEqual(self.calc.add(0, 2), 2)
        self.assertEqual(self.calc.add(-1, -2), -3)

    def test_subtract(self):
        #new testcase for subtract method
        self.assertEqual(self.calc.subtract(0, 2), -2)
        self.assertEqual(self.calc.subtract(-1, -2), 1)  

    def test_multiply(self):
        #new testcase for multiply method
        self.assertEqual(self.calc.multiply(5, 2), 10)
        self.assertEqual(self.calc.multiply(2, -5), -10)               

if __name__ == '__main__':
    unittest.main()