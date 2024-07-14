import unittest 
from simple_calculator import SimpleCalculator
 
class TestSimpleCalcultor(unittest.TestCase):
    def setUp(self) :
        self.calc = SimpleCalculator()

    def test_add(self):
        self.assertEqual(self.calc.add(2,3), 5)
        

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(10,8), 2)
        self.assertEqual(self.calc.subtract(8,10), -2)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(8,10), 80)
        self.assertEqual(self.calc.multiply(8,-10), -80)
        self.assertEqual(self.calc.multiply(-8,-10), 80)

    def test_divide(self):
        try:
            self.assertEqual(self.calc.divide(8,10), 0.8)
            self.assertEqual(self.calc.divide(8, 0), None)
        except ZeroDivisionError as e:
            print(e)


