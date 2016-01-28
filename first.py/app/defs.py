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

class ReduceFuncs(object):
    
            
    def highest_number(self,lst):
        return reduce(highest,filter(is_number,lst))

        
    def longest_string(self,lst):
        return reduce(longest,filter(is_string,lst))

        