class LocalDefs(object):
                        
    def getfirsthalf(self,string,includemiddle=True):
        ln=len(string)
        if(includemiddle):
            return string[:ln/2+ln%2]
        else:
            return string[:ln/2]
            
            
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

localDefs=LocalDefs()

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
            ret=raw_input("Add to list (type '/q' when done)")
            if ret!='/q':
                ret_list.append(ret)
        
        return ret_list
                              


class ReduceFuncs(object):
    
    def highest_number(self,lst):
        tmp=filter(localDefs.is_number,lst)
        if len(tmp)>0: 
            return reduce(localDefs.highest,tmp)
       
    def longest_string(self,lst):
        tmp=filter(localDefs.is_string,lst)
        if len(tmp)>0:
            return reduce(localDefs.longest,tmp)
            
            

class PlayWithString(object):

    def playws(self,string,includemiddle=True):
    
        str_includemiddle=localDefs.getfirsthalf(string)    # could be localDefs.getfirsthalf(string,True)
        str_nomiddle=localDefs.getfirsthalf(string,False)
    
        print 'getfirsthalf (include middle char):',str_includemiddle
        print 'getfirsthalf (exclude middle char):',str_nomiddle
        
        if includemiddle:    
            return str_includemiddle
        else:
            return str_nomiddle
        
 
class Etc(object):

    def callwithNameAndTitle(self,name='',title=''):
    
       if name and title:
        
            return title+' '+name
        
       else:
            
            return name+title 

#################################unit tests only

class Calculator(object):       
    
    def square(self,a):
        return a**2
        
    def adder(self,a,b):
        return a+b
        
        