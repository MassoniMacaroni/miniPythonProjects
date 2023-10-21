import unittest
from code.calculator import Calculator

class testTheCalculator(unittest.TestCase):
    
    def setUp(self):
        self.calc = Calculator(1, 2)
        
    def test_Addition(self):
        self.assertEqual(self.calc.addition(), 3)
        
    def test_Subtraction(self):
        self.assertEqual(self.calc.subtraction(), -1)
    
    def test_Multiplication(self):
        self.assertEqual(self.calc.multiplication(), 2)
    
    def test_Division(self):
        self.assertEqual(self.calc.division(), .5)

if __name__ == "__main__":
    unittest.main()