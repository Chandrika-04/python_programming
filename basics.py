'''#Basic
print("hello world")'''

#Variable Declartion

#1.Normal declaration
a=2                
b="jermy"          
c=3.05             
d=True
print(type(a))                   #<class 'int'>
print(type(b))                   #<class 'str'>
print(type(c))                   #<class 'float'>
print(type(d))                   #<class 'bool'>

#2.By Specifying DataType

p = str("hello")    
q = int(3)    
r = float(3)

#3.Multi Words Variable Names

#----Camel Case----
# Each word, except the first, starts with a capital letter:
myVariableName = "Scott"
#----Pascal Case----
# Each word starts with a capital letter:
MyVariableName = "Scott"
#----Snake Case-----
# Each word is separated by an underscore character:
my_variable_name = "Scott"

#4.Multiple Variable Declaration
#---one to many---
a=b=c="hello"
print(a,b,c)
#----many to many---
x, y, z="pink", "orange" ,"blue"
d, e, f, g= 1, "hello" ,4.65 ,True
print(x,y,z)
print(d,e,f,g)
#----unpack a collection----
color=["pink","blue","orange"]
x,y,z=color
print(x,y,z)
print(x)
print(y)
print(z)
#if we declare x=y=z=color,and print x,y,z the output will be ["pink","blue","orange"]

#5.Output Variables
x=5
y=7
print(x,y)      #output:5 7
print(x+y)      #output:13 , '+' act as arthmetic operator

a="hello"
b="world"
print(a,b)         #output:hello world
print(a+b)         #output:helloworld, '+'act as concatenation operator 

print(x,a)
#print(x+a) produce type error 

p=35.66           
print(x+p)          #output:40.66

#6.Global Variables-These variables can be used every where both the inside and ouside the functions

#Create a variable outside of a function, and use it inside the function
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()
#Create a variable inside a function, with the same name as the global variable
def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)
#To change the value of a global variable inside a function, refer to the variable by using the global keyword:
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
#To change the value of a global variable inside a function, refer to the variable by using the global keyword:
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

