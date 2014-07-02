number=23
running =true
while running:
    guess=int(raw_input('Enter an integer:'))
	
    if guess==number:
	    running=false
	    print 'Congratulations, you guessed it.' 
	elif guess<number:
	    print 'No,it is a little higher than that'
	else:
	    print 'No,it is a littele lower than that'
else:
    print 'the while loop is over'
	
print 'done'