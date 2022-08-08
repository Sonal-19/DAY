#1
print('print')
f=open('test.txt','r')
print(f.read())

#2
print('print')
f=open('test.txt','r+')
f.write("Good Morning")
print('char',f.read())

#3
print('print')
f=open('test.txt','r+')
f.write("Good Morning")
f.writelines(["harpreet","kamal","gurpreet"])
print('char',f.read())

4
print('print')
f=open('test.txt','r+')
f.write("Good Morning")
f.writelines(["harpreet\n","kamal\n","gurpreet\n"])
f.close()
t=open('test.txt','r')
l=t.readlines()
for x in l:
    print(x)
print('char',f.read())

#5
f=open('test1.txt','a')
f.writelines(["suman\n","sam\n"])
f.close()
g=open('test1.txt','r')
print(g.read())

#6
f=open('test.txt','a')
f.writelines(["suman\n","sam\n"])
f.close()
g=open('test.txt','r')

#7
f=open('test.txt','a')
f.writelines(["suman\n","sam\n"])
f.close()
g=open('test.txt','r')
print(g.read(5))
print(g.read(10))

#8
f=open('test.txt','a')
f.writelines(["suman\n","sam\n"])
f.close()
g=open('test.txt','r')
print(g.read(10))
print(g.read(20))

#9
f=open('test.txt','a')
f.writelines(["suman\n","sam\n"])
f.close()
g=open('test.txt','r')
print(g.read(5))
g.seek(0)
print(g.read(10))


#10 Python program to draw square
# using Turtle Programming
import turtle
skk = turtle.Turtle()
for i in range(4):
	skk.forward(50)
	skk.right(90)
turtle.done()


#11 Python program to draw star
# using Turtle Programming
import turtle
star = turtle.Turtle()
star.right(75)
star.forward(100)
for i in range(4):
	star.right(144)
	star.forward(100)
turtle.done()

#12 Colourful Star
from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()


#13 Python program to draw hexagon
# using Turtle Programming
import turtle
polygon = turtle.Turtle()
num_sides = 6
side_length = 70
angle = 360.0 / num_sides
for i in range(num_sides):
	polygon.forward(side_length)
	polygon.right(angle)
turtle.done()


#14 Python program to draw
# Spiral Square Outside In and Inside Out
# using Turtle Programming
import turtle #Outside_In
wn = turtle.Screen()
wn.bgcolor("light green")
wn.title("Turtle")
skk = turtle.Turtle()
skk.color("blue")
def sqrfunc(size):
	for i in range(4):
		skk.fd(size)
		skk.left(90)
		size = size-5
sqrfunc(146)
sqrfunc(126)
sqrfunc(106)
sqrfunc(86)
sqrfunc(66)
sqrfunc(46)
sqrfunc(26)


# 15 Inside_Out
import turtle 
wn = turtle.Screen()
wn.bgcolor("light green")
skk = turtle.Turtle()
skk.color("blue")
def sqrfunc(size):
	for i in range(4):
		skk.fd(size)
		skk.left(90)
		size = size + 5
sqrfunc(6)
sqrfunc(26)
sqrfunc(46)
sqrfunc(66)
sqrfunc(86)
sqrfunc(106)
sqrfunc(126)
sqrfunc(146)


#16 Python program to draw
# Spiral Helix Pattern
# using Turtle Programming
import turtle
loadWindow = turtle.Screen()
turtle.speed(2)
for i in range(100):
	turtle.circle(5*i)
	turtle.circle(-5*i)
	turtle.left(i)
turtle.exitonclick()


#17 Python program to draw
# Rainbow Benzene
# using Turtle Programming
import turtle
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
t = turtle.Pen()
turtle.bgcolor('black')
for x in range(360):
	t.pencolor(colors[x%6])
	t.width(x//100 + 1)
	t.forward(x)
	t.left(59)
