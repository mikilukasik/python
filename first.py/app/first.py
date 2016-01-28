from classes import Inputs

from collections import deque
queue=deque([])

inputs=Inputs()

userName=raw_input('UserName:') 

print "Hello",userName+", what's going on?"
goingOn=raw_input('Answer:')

print 'would you like me to put that here a thousand times?',
wannaSeeThat=inputs.yn()

if wannaSeeThat:
    for x in range(1000):
        print goingOn,
else:
    print 'Good choice.',
    
print 'now you can fill up a list.'
lst=inputs.lst()
print 'your list:',lst

print 'would you like to convert this to a queue?'
convert_to_queue=inputs.yn()

if convert_to_queue:
    converted_lst=deque(lst)
    print 'new queue:',converted_lst
    
    print 'would you like to pop this whole queue from the left?'
    pop_queue=inputs.yn()
    
    if pop_queue:
        for x in range(len(converted_lst)):
            print converted_lst.popleft()
    
def highest(x,y):

    if int(y)>int(x):
        return y
    else:
        return x
    
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

    
numbers=filter(is_number,lst)
print 'the highest number in your list:',reduce(highest,numbers)
#convert_to_queue=inputs.yn()









print
print 'Bye!'

