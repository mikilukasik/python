import unittest
 
from app.first import SquareForTesting
 
class TddInPythonExample(unittest.TestCase):
 
    def test_calculator_add_method_returns_correct_result(self):
        sq = SquareForTesting()
        result = sq(2)
        self.assertEqual(4, result)