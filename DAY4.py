"""Local & Global"""
#1
myGlobal = 5
def func1():
    myGlobal = 50
def func2():
    global myGlobal
    myGlobal = 50
def func3():
    print (myGlobal)
func1()
func3()
print("After using Global")
func2()
func3()

"""local variable"""
#2
def f():
    msg = "Local scope..."
    print (msg)
# Global scope
msg = "Global scope..."
f()
print (msg)

#3
a = 1
def f():
	print('Inside f() : ', a)
def g():
	a = 2
	print('Inside g() : ', a)
def h():
	global a
	a = 3
	print('Inside h() : ', a)
print('global : ', a)
f()
print('global : ', a)
g()
print('global : ', a)
h()
print('global : ', a)

#4 Global and local Variables in Functions
def foo(x, y):
    global a
    a = 42
    x,y = y,x
    b = 33
    b = 17
    c = 100
    print(a,b,x,y)
a, b, x, y = 1, 15, 3,4 
foo(17, 4)
print(a, b, x, y)

#5 Global Variables in Nested Functions
def f():
    city = "Hamburg"
    def g():
        global city
        city = "Geneva"
    print("Before calling g: " + city)
    print("Calling g now:")
    g()
    print("After calling g: " + city)   
f()
print("Value of city in main: " + city)

#6 nonlocal Variables
def f():
    city = "Munich"
    def g():
        nonlocal city
        city = "Zurich"
    print("Before calling g: " + city)
    print("Calling g now:")
    g()
    print("After calling g: " + city)
    
city = "Stuttgart"
f()
print("'city' in main: " + city)