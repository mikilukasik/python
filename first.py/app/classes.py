class Inputs(object):
    def yn(self):
        'validated y/n input'

        ret=raw_input('y/n:')
        if ret in ('y','yes','Y'):
            return 1
        elif ret in ('n','no','N'):
            return 0
        else:
            print "Type 'y' or 'n'"
            return self.yn()

class Calculator(object):
    
    def square(self,a):
        return a**2
        
    def adder(self,a,b):
        return a+b