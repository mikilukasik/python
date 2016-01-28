class Inputs(object):
    def askYN(self):
        'validated y/n input'

        ret=raw_input('y/n:')
        if ret=='y':
            return 1
        elif ret=='n':
            return 0
        else:
            print "Type 'y' or 'n'"
            return self.askYN()

class Calculator(object):
    
    def square(self,a):
        return a**2
        
    def adder(self,a,b):
        return a+b