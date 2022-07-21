"""Plaindrome"""
#1
def ispalindrome(s):
    return s == s[::-1]
s = "mam"
s = ispalindrome(s)
if s:
    print("yes")
else:
    print("no")

#2
num = int(input("enter a value"))
temp = num
rev = 0
while(num>0):
    dig = num % 10
    rev = rev * 10 + dig
    num == num // 10
    if (temp == rev):
        print("this value is a palindrome number")
    else:
        print("this value is not a palindrome number")

"""List"""
#1
list = ["book", "copy", "pen"]
print(list)

#2
list = ["book", "copy", "pen", "book"]
print(list)

#3
list = ["book", "copy", "pen"]
print(len(list))

#4
list = ["book", "789", "pen", "45"]
print(len(list))

#5
list = ["book", "true", "6767", "pen", "false"]             #Print the first item of the list
print(list[0])
list = ["book", "true", "6767", "pen", "false"]             #Print the fourth item of the list
print(list[3])
list = ["book", "true", "6767", "pen", "false"]             #Print the first item of the list
print(list[-3])
list = ["book", "true", "6767", "pen", "false"]             #Print the lastfirst item of the list
print(list[-1])

#6
list = ["book", "true", "6767", "pen", "false", "copy"]             #Return the third, fourth, and fifth, sixth item
print(list[2:6])
list = ["book", "true", "6767", "pen", "false", "copy"]             #returns the items from the beginning to, but NOT including, "pen"
print(list[:3])
list = ["book", "true", "6767", "pen", "false", "copy"]             
print(list[2:])
list = ["book", "true", "6767", "pen", "false", "copy"]             
print(list[-6:-2])

#7
list = ["book", "copy", "pen"]
if "apple" in list:
    print("yes, apple in list")

"""CHANGE ITEM"""
#1
list = ["black", "white", "red", "blue", "yellow"]
list[1] = "pink"
print(list)

#2
list = ["black", "white", "red", "blue", "yellow"]
list[1:4] = "green", "orange"
print(list)

#3
list = ["black", "white", "red", "blue", "yellow"]
list[0:5] = "green", "orange"
print(list)

#4
list = ["black", "white", "red", "blue", "yellow"]
list[1:3] = "green", "orange"
print(list)

"""INSERT ITEM"""
#1
list = ["black", "white", "red", "blue", "yellow"]
list.insert(2, "green")
print(list)

list = ["black", "white", "red", "blue", "yellow"]
list.insert(2, "green")
list.insert(4, "orange")
print(list)

list = ["black", "white", "red", "blue", "yellow"]
list.insert(0, "pink")
list.insert(6, "purple")
print(list)

#ADD LIST ITEM (APPEND)
list = ["black", "white", "blue"]
list.append("red")
print(list)

#EXTEND LIST (Add the elements of tropical to list)
list = ["black", "blue", "brown"]
tropical = ["white", "sky", "red"]
list.extend(tropical)
print(list)

l = [1,2,3]
n = int(input("enter the no. of elements in the list: "))
for x in range(0,2):
    l.append(input("enter the item: "))
print("printing the list item: ")
for x in l:
    print(x, end = " ")

"""REMOVE LIST ITEM"""
list = ["yellow", "red", "black", "orange"]
list.remove("black")
print(list)

list = ["yellow", "red", "black", "orange"]
list.pop(2)
print(list)

list = ["yellow", "red", "black", "orange"]
list.pop()
print(list)

list = ["yellow", "red", "black", "orange"]
del list[0]
print(list)

list = ["yellow", "red", "black", "orange"]
del list[3]
print(list)

list = ["yellow", "red", "black", "orange"]
del list[0:2]
print(list)

list = ["yellow", "red", "black", "orange"]
del list[2:3]
print(list)

list = ["yellow", "red", "black", "orange"]
del list[0:3]
print(list)

"""set issubset()"""
#1
A = {1, 2, 3}
B = {1, 2, 3, 4, 5}
print(A.issubset(B))

#2
A = {'a', 'c', 'e'}
B = {'a', 'b', 'c', 'd', 'e'}
print('A is subset of B:', A.issubset(B))
print('B is subset of A:', B.issubset(A))

"""set symmetric_difference"""
#1
A = {'a', 'b', 'c', 'd'}
B = {'c', 'd', 'e'}
result = A.symmetric_difference(B)
print(result)

#2
A = {'python', 'java', 'c++'}
B = {'python', 'javascript', 'c'}
result = A.symmetric_difference(B)
print(result)

"""python frozenset() function"""
#1
mylist = ['black', 'white', 'red']
x = frozenset(mylist) 
print(mylist)
print(x)

#2
mylist =  ['apple', 'banana', 'cherry']
x = frozenset(mylist)
x[1] = "strawberry"
print(x[1])

#3
A = frozenset([1, 2, 3, 4])
B = frozenset([3, 4, 5, 6])
C = A.copy()
print(C)
print(A.union(B))
print(A.intersection(B))
print(A.difference(B))
print(A.symmetric_difference(B))

#4
A = frozenset([1, 2, 3, 4])
B = frozenset([3, 4, 5, 6])
C = frozenset([5, 6])
print(A.isdisjoint(C))
print(C.issubset(B))
print(B.issubset(C))

"""Dictionary"""
#1
thisdict =	{"brand": "Ford", "model": "Mustang", "year": 1964 }
print(thisdict)

#2
thisdict =	{"brand": "Ford", "model": "Mustang", "year": 1964 }
print(thisdict["brand"])

#3 Changing and adding Dictionary Elements
my_dict = {'name': 'Jack', 'age': 26}
my_dict['age'] = 27
print(my_dict)
my_dict['address'] = 'Downtown'
print(my_dict)
