#from classes import Inputs
from classes import ReduceFuncs,PlayWithString,Inputs
#from defs import PlayWithSting

from collections import deque

inputs=Inputs()
reducefuncs=ReduceFuncs()
playWithString=PlayWithString()

def playMoreWithString():
    print 'would you like to play with another string?',
    play_with_string=inputs.yn()

    if play_with_string:
        other_string=raw_input('String to play with:')
        playWithString.playws(other_string)
        playMoreWithString()
   
        
        
        
        
        
        
################################

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
    
print 'Now you can fill up a list.'
lst=inputs.lst()
print 'your list:',lst

print 'would you like to convert this to a queue?',
convert_to_queue=inputs.yn()

if convert_to_queue:
    converted_lst=deque(lst)
    print 'new queue:',converted_lst
    
    print 'would you like to pop this whole queue from the left?',
    pop_queue=inputs.yn()
    
    if pop_queue:
        for x in range(len(converted_lst)):
            print converted_lst.popleft()
  
print 'the highest number in your list:',reducefuncs.highest_number(lst)
longest_string=reducefuncs.longest_string(lst)
print 'the longest string in your list:',longest_string

print 'would you like to play with this string?',
play_with_string=inputs.yn()

if play_with_string:
    playWithString.playws(longest_string)
    playMoreWithString()
else:
    other_string=raw_input('String to play with:')
    playWithString.playws(other_string)
    playMoreWithString()



print
print 'Bye!'

