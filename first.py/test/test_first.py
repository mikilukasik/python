import unittest
 
from app.classes import Calculator
calculator = Calculator()
 
class TddInPythonExample(unittest.TestCase):
 
    def test_calculator_square_method_returns_correct_result(self):
        
        result = calculator.square(2)
        self.assertEqual(4, result)
  
    def test_calculator_add_method_returns_correct_result(self):
       
        result = calculator.adder(2,3)
        self.assertEqual(5, result)
  
if __name__ == '__main__':
    unittest.main()