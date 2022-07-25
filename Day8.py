# """Encapsulation"""
#1 Creating a base class
class Base:
	def __init__(self):
		self._a = 2
class Derived(Base):
	def __init__(self):
		Base.__init__(self)
		print("Calling protected member of base class: ", self._a)
		self._a = 3
		print("Calling modified protected member outside class: ", self._a)
obj1 = Derived()
obj2 = Base()
print("Accessing protected member of obj1: ", obj1._a)
print("Accessing protected member of obj2: ", obj2._a)


#2 illustrating public members & public access modifier 
class pub_mod:
    def __init__(self, name, age):
        self.name = name;
        self.age = age;
 
    def Age(self):  
        print("Age: ", self.age) 
obj = pub_mod("Jason", 35);
print("Name: ", obj.name)  
obj.Age()


#5 illustrating protected members & protected access modifier 
class details:
    _name="Jason"
    _age=35
    _job="Developer"
class pro_mod(details):
    def __init__(self):
        print(self._name)
        print(self._age)
        print(self._job)
obj = pro_mod()
print("Name:",obj._name)
print("Age:",obj._age)
print("Job:",obj._job)


#6
class Person:
    def __init__(self, name, age=0):
        self.name = name
        self.age = age
 
    def display(self):
        print(self.name)
        print(self.age)
 
person = Person('Dev', 30)
person.display()
print(person.name)
print(person.age)


#7 Python program demonstrate  
#abstract base class work   
from abc import ABC, abstractmethod   
class Car(ABC):   
    def mileage(self):   
        pass  
  
class Tesla(Car):   
    def mileage(self):   
        print("The mileage is 30kmph") 
class Suzuki(Car):   
    def mileage(self):   
        print("The mileage is 25kmph ")   
class Duster(Car):   
     def mileage(self):   
          print("The mileage is 24kmph ")   
  
class Renault(Car):   
    def mileage(self):   
            print("The mileage is 27kmph ")  
  
t= Tesla ()   
t.mileage()    
r = Renault()   
r.mileage()    
s = Suzuki()   
s.mileage()
d = Duster()   
d.mileage()