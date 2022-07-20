"""Arithematic operator"""
a = 15
b = 3
print(a + b)    #addition 0f two numbers
print(a-b)      #subtracton 0f two numbers
print(a*b)      #multiplication 0f two numbers
print(a/b)      #division 0f two numbers
print(a%b)      #modulus 0f two numbers
print(a//b)     #do 0f two numbers
print(a**b)     #do 0f two numbers

"""Comparision/Relational Operators"""
a = 67
b = 45
print(a>b)
print(a<b)
print(a<=b)
print(a>=b)
print(a==b)
print(a!=b)

"""Logical operators"""
a = 9
b = 5
print(a>b and b>a)
print(a>b and b<a)
print(a>b or b>a)
print(a<b or a<b)
print(not(b>a))

"""Assignment operators"""
a = 7
a += 3
print(a)

a = 7
a -= 3
print(a)

a = 7
a *= 3
print(a)

a = 7
a /= 3
print(a)

a = 7
a %= 3
print(a)

a = 7
a //= 3
print(a)

a = 7
a **= 3
print(a)

a = 7
a >>= 3
print(a)

a = 7
a <<= 3
print(a)


"""Bitwise Operator"""
a = 4
b = 5 
print("a & b =", a & b)     #bitwise and operation
print("a | b =", a | b)     #bitwise or operation
print (" ~b =", ~b)         #bitwise not operation
print("a ^ b =", a ^ b)     #bitwise xor operation

a = 10
b = 2
print("a >> b =", a >> b)      #bitwise right side operation
print("a << b =", a << b)      ##bitwise left side operation


"""identity operator"""
a = 10
b = 10
print(a is b)           #is operation
print(a is not b)       #is not operation
a = 10 
b = 20
print(a is b)           #is operation
print(a is not b)       #is not operation


"""Membership operator"""
x = ["apple", "banana"]
print("banana" in x)            #Membership in operator
print("banana" not in x)        #Membership not in operator

x = ["5", "9"]
print("9" in x)                 #Membership in operator
print("9" not in x)             #Membership not in operator


"""LOOPS"""
#!
a = 15
b = 4
if (a>b):
    print("hello")

#2
a = 15
b = 140
if (a > b):
    print("hello")
else:
    print("hi")

#3
b = 40
c = 45
if(b>c):
    print('h')
else:
    print('l')

#4
a = 14
b = 20
c = 64
if(b>c):
    print('h')
elif(a>c):
    print('l')
elif(b==c):
    print('r')
else:
    print('s')

for x in range(10):
    print(x)

for x in range(21,31):
    print(x)

# conditional statements
# if statement 
a= 4
b= 3
if (a>b):
    print ("hello")


# if else statement 
a= 4
b= 7
if (a>b):
    print ("hello")
else:
     print ("h")

a= 14
b=20
c=64
if (b>c):
   print ("H")
elif (a>c):
    print ("L")
elif (b==c):
    print ("R")
else:
    print ("LH")


# looping statements
for x in range (10):
    print(x)


for x in range (10):
     for y in range (11,15):
       print (x,y)


row = int(input("Enter number of rows: "))
print("Square pattern is: ")
for i in range(1,row+1):
    for j in range(1,row+1):
        print("*", end="")
    print()


# while loop
a=10
while (a<=100):
    print ("hello")  


# break    
num = 0
for i in range(10):
	num += 1
	if num == 8:
		break
	print("The num has value:", num)
print("Out of loop")

num = 0
for i in range(10):
	num += 1
	if num == 5:
		break
	print("The num has value:", num)
print("Out of loop")


# continue
# Python program to
# demonstrate continue
# statement

for i in range(1, 11):
	if i == 6:
		continue
	else:
		print(i, end=" ")


"""Square pattern program"""
for i in range(0, 5):                         # Create a list of rows
    for j in range(0, 5):                     # Create a list of columns
        print("*", end="")
    print()

"""Program to print half pyramid using"""
for x in range(1, 5):
    for y in range(1, x+1):
        print("*", end = " ")
    print()

rows = int(input("Enter number of rows: "))
for i in range(rows):
    for j in range(i+1):
        print("* ", end="")
    print()

"""Program to print half pyramid a using numbers"""
rows = int(input("Enter number of rows: "))
for i in range(rows):
    for j in range(i+1):
        print(j+1, end=" ")
    print()

"""Program to print half pyramid using alphabets"""
rows = int(input("Enter number of rows: "))
ascii_value = 65
for i in range(rows):
    for j in range(i+1):
        alphabet = chr(ascii_value)
        print(alphabet, end=" ")
    ascii_value += 1
    print()

"""Inverted half pyramid using"""   
for x in range(5):
    for y in range(5-x):
        print("*", end = " ")
    print()

rows = int(input("Enter number of rows: "))
for i in range(rows, 0, -1):
    for j in range(0, i):
        print("* ", end=" ")
    print("\n")

"""Inverted half pyramid using numbers"""
rows = int(input("Enter number of rows: "))
for i in range(rows, 0, -1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()

"""Program to print full pyramid using"""
for x in range(1, 5):
    for y in range(1, x+1):
        print("*", end = " ")
    print()
for x in range(5):
    for y in range(5-x):
        print("*", end = " ")
    print()

"""Program to print full pyramid using"""
rows = int(input("Enter number of rows: "))
k = 0
for i in range(1, rows+1):
    for space in range(1, (rows-i)+1):
        print(end="  ")
    while k!=(2*i-1):
        print("* ", end="")
        k += 1
    k = 0
    print() 

"""Full Pyramid of Numbers"""
rows = int(input("Enter number of rows: "))
k = 0
count=0
count1=0
for i in range(1, rows+1):
    for space in range(1, (rows-i)+1):
        print("  ", end="")
        count+=1
    while k!=((2*i)-1):
        if count<=rows-1:
            print(i+k, end=" ")
            count+=1
        else:
            count1+=1
            print(i+k-(2*count1), end=" ")
        k += 1
    count1 = count = k = 0
    print()
    rows = int(input("Enter number of rows: "))

"""Inverted full pyramid of"""
for i in range(row, 1, -1):
    for space in range(0, row-i):
        print("  ", end="")
    for j in range(i, 2*i-1):
        print("* ", end="")
    for j in range(1, i-1):
        print("* ", end="")
    print()
