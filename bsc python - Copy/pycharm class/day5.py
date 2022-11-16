 #(quadraticeqns,scope,arguments,fibbonaci,factorial,evenoroddusingfunction)
#everything related to functions
'''
import math
def quad(a,b,c):
    x1 = (-b + math.sqrt(b**2-4*a*c))/(2*a)
    x2 = (-b - math.sqrt(b**2-4*a*c))/(2*a)
    return x1,x2
a=int(input("enter the a"))
b=int(input("enter the b"))
c=int(input("enter the c"))
x1,x2=quad(a,b,c)
print(x1,x2)
'''


#scope of function
'''
k=23
def old():
    a=89
    global k
    k += 1
    print("the a value in old",a)
def new():
    a=90
    print("the a value in new",a)
old()
new()

'''

#whenever we want a global variable we have to declare the variable inside the function using (global)and if we alter it like add or subtract etc it would get updated outside and k will get the updated value.

'''

#default arguments,keyword arguments,positional arguments
#default arguments

def avg(x,y,z):
    return(x+y+z)/3
res=avg(1,2,3)
print(res)#this is the normal method

def avg(x=1,y=2,z=5):
    return(x+y+z)/3
res=avg(1,2,5)#here we need to assign from right to the left.if we change the values in this fn call more priority will be given to this line
print(res)#this is the normal method

def avg(x,y,z):
    return(x+y+z)/3
res=avg(1,2)#we should assign from right to left while fun definition or else we should give it during fn call
print(res)#this is the normal method

'''

#keyword arguments
'''
def ch(x,y,z):
    print("x is",x)
    print("y is",y)
    print("z is",z)
ch(y=3,x=6,z=1)#keywords arguments
'''

#positional arguments
#adding many numbers
'''
def add(*b):
    tem=0
    for i in b:
        tem +=i
    return tem
ans=add(12,16,20,30,45,56,87,44,21)
print(ans)
'''
#2nd example(doubt)
'''
def large(a,*b):
    max=a
    for i in b:
        if i>max:
            max=i
        return max
print(large(12,23,45,67,11,10,456,78,43))
'''
#fibonacci series(interview question)
#fibonacci series it is in the form 0,1,1,2,3,5,8etc..it adds the previous number
'''
def fibo(num):
    a=-1#we need 0 and 1 and when we get a+b its answer will be differrent so we give the a value as -1
    b=1
    for i in range (num):
        c=a+b
        print(c)
        a=b
        b=c
num=int(input('enter the number'))
fibo(num)
'''

#write a program to check the factorial of a number
'''
def factorial():
    a=int(input("enter the number to find factorial"))
    fact=1
    for i in range(1,a+1):
        fact=fact*i
    print("the factorial value of your given number is",fact)
factorial()
'''

#another method
"""
def fn(num):
  if num == 0:
    return 1
  else :
    return num*fn(num-1)
print(fn(int(5)))
"""

#check the given input is even or odd using function
'''
def find():
    a=int(input("enter the value which you want to check even or odd"))
    if a%2 ==0:
        print("the given value is even")
    else:
        print("the given value is odd")
find()
'''
