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










print
print 'Bye!'

