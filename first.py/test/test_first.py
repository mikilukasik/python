import unittest
 
from app.classes import Calculator,PlayWithString,Etc

calculator = Calculator()
playWithString = PlayWithString()
etc = Etc()

class test_calculator(unittest.TestCase):
 
    def test_calculator_square_method_returns_correct_result(self):
        
        result = calculator.square(2)
        self.assertEqual(4, result)
  
    def test_calculator_add_method_returns_correct_result(self):
       
        result = calculator.adder(2,3)
        self.assertEqual(5, result)
        
class test_playwithstring(unittest.TestCase):
  
    def test_playwithstring_half_inc(self):
       
        result = playWithString.playws('hhh')
        self.assertEqual('hh', result)
    
    def test_playwithstring_no_half_inc(self):
       
        result = playWithString.playws('hhh',False)
        self.assertEqual('h', result)
    


class test_etc(unittest.TestCase):
     
    def test_callwithNameAndTitle_function(self):
        
        result = etc.callwithNameAndTitle('miki','mr')
        self.assertEqual('mr miki',result)
        
        result = etc.callwithNameAndTitle('','')
        self.assertEqual('',result)
        
        result = etc.callwithNameAndTitle('miki','')
        self.assertEqual('miki',result)
        
        result = etc.callwithNameAndTitle('miki')
        self.assertEqual('miki',result)
        
        result = etc.callwithNameAndTitle('','miki')
        self.assertEqual('miki',result)
        
        result = etc.callwithNameAndTitle()
        self.assertEqual('',result)
        
        
    def test_anyArgs_function(self):
        
        result = etc.anyArgs('mr','miki','lukasik')
        self.assertEqual('mr miki lukasik',result)
        
        result = etc.anyArgs()
        self.assertEqual('',result)
        
        result = etc.anyArgs([1,2,'rrr',[4,5]])
        self.assertEqual('',result)
        
    

if __name__ == '__main__':
    unittest.main()