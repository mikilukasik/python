from classes import Inputs
inputs=Inputs()

userName=raw_input('UserName:') #, please input your name:"

print "Hello",userName+", what's going on?"
goingOn=raw_input('Answer:')

print 'would you like me to put that here a thousand times?',
wannaSeeThat=inputs.askYN()

if wannaSeeThat:
    for x in range(1000):
        print goingOn,
else:
    print 'Good choice.',
    











print
print 'Bye!'

