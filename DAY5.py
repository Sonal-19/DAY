"""CLASS AND OBJECT"""
#1 Create a Class
class MyClass:
    x = 8
print(MyClass)

#2 Create Object
class MyClass:
    x = 8
p1 = MyClass()
print(p1.x)

#3 The __init__() Function
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
p1 = Person("Jack", 36)
print(p1.name)
print(p1.age)

#4 The __init__() Function
class person:
        def __init__(self, name, age, address):
            self.name = name
            self.age = age
            self.address = address
p1 = person("jack", 36, "london")
print(p1.name)
print(p1.age)
print(p1.address)

#5 Object Methods
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def myfunc(self):
    print("Hello my name is " + self.name)
p1 = Person("John", 36)
p1.myfunc()

#6 The self Parameter
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)
p1 = Person("John", 36)
p1.myfunc()

#7 Modify object properies
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def myfunc(self):
    print("Hello my name is " + self.name)
p1 = Person("John", 36)
p1.age = 40
print(p1.age)

