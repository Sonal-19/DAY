"Single inheritance"
class A:
    def f1(self):
        print('A')
class B(A):
    def f2(self):
        print(B)
ob = B()
ob.f1()
ob.f2() 

#2 single inheritance
class Parent:
	def func1(self):
		print("This function is in parent class.")
class Child(Parent):
	def func2(self):
		print("This function is in child class.")
object = Child()
object.func1()
object.func2()
      

"Multilevel Inheritance"
class A():
    def f1(self):
        print('A')
class B(A):
    def f2(self):
        print('B')
class C(B):
    def f3(self):
        print('c')
ob = C()
ob.f1()
ob.f2()
ob.f3()


#2multilevel inheritance
class Grandfather:
	def __init__(self, grandfathername):
		self.grandfathername = grandfathername
class Father(Grandfather):
	def __init__(self, fathername, grandfathername):
		self.fathername = fathername
		Grandfather.__init__(self, grandfathername)
class Son(Father):
	def __init__(self, sonname, fathername, grandfathername):
		self.sonname = sonname
		Father.__init__(self, fathername, grandfathername)
	def print_name(self):
		print('Grandfather name :', self.grandfathername)
		print("Father name :", self.fathername)
		print("Son name :", self.sonname)
s1 = Son('Prince', 'Rampal', 'Lal mani')
print(s1.grandfathername)
s1.print_name()


"Multiple Inheritance"
class A():
    def f1(self):
        print('A')
class B(A):
    def f2(self):
        print('B')
class C(B, A):
    def f3(self):
        print("A :", self.A)
        print("B :", self.B)
ob = C()
ob.f1()
ob.f2()
ob.f3()


#3
class Mother:
	mothername = ""
	def mother(self):
		print(self.mothername)
class Father:
	fathername = ""
	def father(self):
		print(self.fathername)
class Son(Mother, Father):
	def parents(self):
		print("Father :", self.fathername)
		print("Mother :", self.mothername)
s1 = Son()
s1.fathername = "RAM"
s1.mothername = "SITA"
s1.parents()


"""Hierarchical inheritance"""
#1
class A():
    def f1(self):
        print('A')
class B(A):
    def f2(self):
        print('B')
class C(A):
    def f3(self):
        print('C')
ob = C(A)
ob.f2()
ob.f3()

#2
class A():
    def f1(self):
        print('A')
class B(A):
    def f2(self):
        print('B')
class C(B):
    def f3(self):
        print('C')
ob = C(B)
ob.f1()
ob.f3()

#3
class Parent:
	def func1(self):
		print("This function is in parent class.")
class Child1(Parent):
	def func2(self):
		print("This function is in child 1.")
class Child2(Parent):
	def func3(self):
		print("This function is in child 2.")
object1 = Child1()
object2 = Child2()
object1.func1()
object1.func2()
object2.func1()
object2.func3()

"""Hybrid Inheritance"""
class School:
	def func1(self):
		print("This function is in school.")
class Student1(School):
	def func2(self):
		print("This function is in student 1. ")
class Student2(School):
	def func3(self):
		print("This function is in student 2.")
class Student3(Student1, School):
	def func4(self):
		print("This function is in student 3.")
object = Student3()
object.func1()
object.func2()

"""Super function"""
class Emp():
	def __init__(self, id, name, Add):
		self.id = id
		self.name = name
		self.Add = Add
class Freelance(Emp):
	def __init__(self, id, name, Add, Emails):
		super().__init__(id, name, Add)
		self.Emails = Emails
Emp_1 = Freelance(103, "Suraj kr gupta", "Noida" , "KKK@gmails")
print('The ID is:', Emp_1.id)
print('The Name is:', Emp_1.name)
print('The Address is:', Emp_1.Add)
print('The Emails is:', Emp_1.Emails)

#2
class Animals:
	def __init__(self):
		self.legs = 4
		self.domestic = True
		self.tail = True
		self.mammals = True
	def isMammal(self):
		if self.mammals:
			print("It is a mammal.")
	def isDomestic(self):
		if self.domestic:
			print("It is a domestic animal.")
class Dogs(Animals):
	def __init__(self):
		super().__init__()
	def isMammal(self):
		super().isMammal()
class Horses(Animals):
	def __init__(self):
		super().__init__()
	def hasTailandLegs(self):
		if self.tail and self.legs == 4:
			print("Has legs and tail")
Tom = Dogs()
Tom.isMammal()
Bruno = Horses()
Bruno.hasTailandLegs()

"""Polymorphism"""
#1
def add(x, y, z = 0):
	return x + y+z
print(add(2, 3))
print(add(2, 3, 4))

#2
class India():
	def capital(self):
		print("New Delhi is the capital of India.")
	def language(self):
		print("Hindi is the most widely spoken language of India.")
	def type(self):
		print("India is a developing country.")
class USA():
	def capital(self):
		print("Washington, D.C. is the capital of USA.")
	def language(self):
		print("English is the primary language of USA.")
	def type(self):
		print("USA is a developed country.")
obj_ind = India()
obj_usa = USA()
for country in (obj_ind, obj_usa):
	country.capital()
	country.language()
	country.type()

"""Polymorphism in addition operator"""
num1 = 1
num2 = 2
print(num1+num2)


str1 = "Python"
str2 = "Programming"
print(str1+" "+str2)

"""Polymorphic len() function"""
print(len("Programiz"))
print(len(["Python", "Java", "C"]))
print(len({"Name": "John", "Address": "Nepal"}))

""" Polymorphism in Class Methods"""
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")
    def make_sound(self):
        print("Meow")
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def info(self):
        print(f"I am a dog. My name is {self.name}. I am {self.age} years old.")
    def make_sound(self):
        print("Bark")
cat1 = Cat("Kitty", 2.5)
dog1 = Dog("Fluffy", 4)
for animal in (cat1, dog1):
    animal.make_sound()
    animal.info()
    animal.make_sound()


"""Method Overriding"""
from math import pi
class Shape:
    def __init__(self, name):
        self.name = name
    def area(self):
        pass
    def fact(self):
        return "I am a two-dimensional shape."
    def __str__(self):
        return self.name
class Square(Shape):
    def __init__(self, length):
        super().__init__("Square")
        self.length = length

    def area(self):
        return self.length**2
    def fact(self):
        return "Squares have each angle equal to 90 degrees."
class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius
    def area(self):
        return pi*self.radius**2
a = Square(4)
b = Circle(7)
print(b)
print(b.fact())
print(a.fact())
print(b.area())



# import statement example
# to import standard module math

import math
print("The value of pi is", math.pi)


# importing built-in module math 
import math 

# using square root(sqrt) function contained 
# in math module 
print(math.sqrt(25)) 

# using pi function contained in math module 
print(math.pi) 

# 2 radians = 114.59 degrees 
print(math.degrees(2)) 

# 60 degrees = 1.04 radians 
print(math.radians(60)) 

# Sine of 2 radians 
print(math.sin(2)) 

# Cosine of 0.5 radians 
print(math.cos(0.5)) 

# Tangent of 0.23 radians 
print(math.tan(0.23)) 

# 1 * 2 * 3 * 4 = 24 
print(math.factorial(4)) 

# importing built in module random 
import random 

# printing random integer between 0 and 5 
print(random.randint(0, 5)) 

# print random floating point number between 0 and 1 
print(random.random()) 

# random number between 0 and 100 
print(random.random() * 100) 

List = [1, 4, True, 800, "python", 27, "hello"] 

# using choice function in random module for choosing 
# a random element from a set such as a list 
print(random.choice(List)) 


# importing built in module datetime 
import datetime 
from datetime import date 
import time  
print(time.time()) 
print(date.fromtimestamp(454554)) 


#1 CURRENNT DAY TIME QUESTION
import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))

#2 importing datetime module for now()
import datetime
current_time = datetime.datetime.now()
print("current date and time :", current_time)


# #3 importing datetime module for now()
import datetime
# using now() to get current time
current_time = datetime.datetime.now()
# Printing attributes of now().
print("The attributes of now() are :")
print("Year :", current_time.year)
print("Month : ", current_time.month)
print("Day : ", current_time.day)
print("Hour : ", current_time.hour)
print("Minute : ", current_time.minute)
print("Second :", current_time.second)
print("Microsecond :", current_time.microsecond)