def printMax(x,y):
    '''Prints the maximun of two numbers.
	
	the two values must be integers.'''
    x=int(x)
    y=int(y)
    if  x>y:
        print x,'is maximum'
    else:
        print y,'is maximum'
		
printMax(3,4)
print printMax.__doc__
help(printMax)