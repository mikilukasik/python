def askYN():
    ret=raw_input('y/n:')
    if ret=='y':
        return 1
    elif ret=='n':
        return 0
    else:
        print "Type 'y' or 'n'"
        askYN()



userName=raw_input('UserName:') #, please input your name:"

print "Hello",userName+", what's going on?"
goingOn=raw_input('Ansver:')

print 'would you like me to put that here a million times?'
wannaSeeThatChar=askYN()

if wannaSeeThatChar:
    for x in range(1000000):
        print x,
else:
    print 'Good choice.'
    
















print 'Bye!'
