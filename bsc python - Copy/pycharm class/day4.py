#(nestered for loop,no pyramid,breakcontinuepass,omitvowels,functions,functioncallinotherfunction,mul add using fun,areaofcircle,areaofrectangle)
#(nestered for loop)
"""
colors=["red","yellow","green"]
fruits=["cherry","banana","apple"]
for i in colors:
    for j in fruits:
        print(i,j)
"""

#making number pyramid using nestered for loops
"""
num=6
for i in range(1,num):
    for j in range(i,num+1):
        print(j,end=" ")
    print()
"""

#making upside down number pyramid using nestered loops
"""
g=7
for i in range(1,g+1):
    for j in range(g-i,0,-1):  #here we use stepsize for the reverse pyramid
        print(j,end=" ")
    print( )
"""

#break,continue,pass
"""
break-stops the execution
continue-skips a part of execution
pass-does nothing or place holder for future codes
"""

#break classwork
"""
toffee=int(input("enter the no of the toffee needed"))
x=1
stock=6
while x<=toffee:
    if x>stock:
        print("out of stock")
        break
    else:
        print(f"here is your{x} no of toffees")
        x=x+1
        #x+=1
"""

#break small eg
"""
data="bangalore"
for i in data:
    if i =="l":
        break
    print(i)
"""

#continue (it skips the given code)
"""
x=10
while x>0:
    if x%2==0:
        x-=1
        #x=x-1
        continue
    print(f"the value of x is{x}")
    x=x-1
"""

#to omit the vowels in the given string
"""
data="python programming projects"
for i in data:
    if(i=="a") or (i=="e") or (i=="i") or (i=="o") or (i=="u"):
        continue
    print(i,end=" ")
"""

#pass
"""
a=90
b=76
if a>b:
    pass
else:
    print("hello")
"""

#functions (it is a group of codes,it avoids the repeatation of the codes)
"""
def functionname():#defining function
    s1
    s2
    s3
functionname()#calling the function
"""
#function classwork
"""
def hello():
    print("hello good morning")
hello()
hello()
"""

#to add anything with the function
"""
def add():
    a=346
    b=456
    c=a+b
    print(c)
    hello()
add()
"""

#write a function for the subtraction and multiplication take input from the user and create the other
#function as multiplication inside this function call subtraction.
"""
def subtraction():
    a=int(input("enter the number"))
    b=int(input("enter the number"))
    print(a-b)
subtraction()#if we wont give this,1st multiplication will be carried out then subtraction will be called.
def multiplication():
    c=int(input("enter the number"))
    d=int(input("enter the number"))
    print(c*d)
    subtraction()
multiplication()
"""

#find largest of two numbers using function (assignment)
"""
def comparison():
    a=int(input("enter the 1st value"))
    b=int(input("enter the 2nd value"))
    if a<b:
        print("1st value is smaller")
    else:
        print("2nd value is smaller")
comparison()
"""

#finding the square of a number using function
"""
def square(a):
    res=a*a
    print(f"the square of {a} is {res}")
a=int(input("enter the a"))
square(a)
#print(print("hi"))
"""

#finding division between 2 numbers using function
"""
def divi(x,y,z):
    return(x+y-z)/3.0
print("hello function")
res=divi(90,30,20)
res1=divi(20,3,1)
print(res)
print(res1)
"""

#find the area of the circle importing math library which has many operations
"""
import math
def area(rad):
    print(math.pi)
    return math.pi*rad*rad
print(area(4))
"""

#to check all the operations done by math
"""
math.
"""

#area of a rectanngle
"""
def area(l,b):
    return(l*b)
l=int(input("enter the length of the rectangle"))
b=int(input("enter the length of the rectangle"))
print(area(l,b))
"""