def highest(x,y):

    if y>x:
        return y
    else:
        return x
        
def longest(x,y):

    if len(y)>len(x):
        return y
    else:
        return x
    
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def is_string(s):

    if isinstance(s, basestring):

        try:
            float(s)
            return False
        except ValueError:
            return True
    
    else:
        return False

class LocalDefs(object):
                        
    def getfirsthalf(self,string,includemiddle=True):
        ln=len(string)
        if(includemiddle):
            return string[:ln/2+ln%2]
        else:
            return string[:ln/2]

localDefs=LocalDefs()

class ReduceFuncs(object):
    
    def highest_number(self,lst):
        tmp=filter(is_number,lst)
        if len(tmp)>0: 
            return reduce(highest,tmp)
       
    def longest_string(self,lst):
        tmp=filter(is_string,lst)
        if len(tmp)>0:
            return reduce(longest,tmp)
            
            

class PlayWithString(object):

    def playws(self,string):
    
        print 'getfirsthalf (includemiddle:true):',localDefs.getfirsthalf(string)
        print 'getfirsthalf (includemiddle:false):',localDefs.getfirsthalf(string,False)
        
        
 
 
class Inputs(object):
    def yn(self):
        """validated y/n input"""

        while True:
            ret=raw_input('y/n:')
            if ret in ('y','yes','Y'):
                return 1
            elif ret in ('n','no','N'):
                return 0
            else:
                print "Type 'y' or 'n'"
                
    def lst(self):
        """fills a new list until /q entered"""
    
        ret_list=[]
        ret=''
        while ret!='/q':
            ret=raw_input("Add to list (type '/q to quit')")
            if ret!='/q':
                ret_list.append(ret)
        
        return ret_list
                              

class Calculator(object):       #unit tests only
    
    def square(self,a):
        return a**2
        
    def adder(self,a,b):
        return a+b