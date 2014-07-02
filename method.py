#=========================method=================================
def sayHello():
    print '''hello world'''
sayHello()


def printMax(a,b):
    if a>b:
	    print a, 'is maximum'
    else:
	    print b, 'is maximun'
printMax(5,4)

#!/usr/bin/python
# Filename: func_local.py

def func(x):
    print 'x is', x
    x = 2
    print 'Changed local x to', x

x = 50
func(x)
print 'x is still', x

#global
def func():
    global x

    print 'x is', x
    x = 2
    print 'Changed local x to', x

x = 50
func()
print 'Value of x is', x

def say(message='abc', times = 1):
    print message * times

say('Hello')
say('helloworld',5)

#=============================
def someFunction():
    pass
a =someFunction()
print(a)