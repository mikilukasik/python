class Inputs(object):
    def yn(self):
        'validated y/n input'

        while True:
            ret=raw_input('y/n:')
            if ret in ('y','yes','Y'):
                return 1
            elif ret in ('n','no','N'):
                return 0
            else:
                print "Type 'y' or 'n'"
                
    def lst(self):
        ret_array=[]
        ret=''
        while ret!='/q':
            ret=raw_input("Add to list (type '/q to quit')")
            if ret!='/q':
                ret_array.append(ret)
        
        return ret_array
                              

class Calculator(object):       #unit tests only
    
    def square(self,a):
        return a**2
        
    def adder(self,a,b):
        return a+b