#3rd assignment
#importing math module and finding sqrt of 13689
'''
import math
def sqroot(a):
    print(math.sqrt(a))
sqroot(13689)
'''

'''

2.First, def a function called distance_from_zero, with one argument
(choose any argument name you like). If the type of the argument is
either int or float, the function should return the absolute value of the
function input. Otherwise, the function should return &quot;Nope&quot;. Check if it
works calling the function with -5.6 and &quot;what?&quot;.
'''
'''
def distance_from_zero(a):
    if type(a) == int or type(a)== float:
        return abs(a) 
    else:
        return ("Nope&quot")

print(distance_from_zero("what"))        
    
'''

#3.Rewrite your pay computation program with time- and-a-half for overtime and create a function called computepay which takes two parameters (hours and rate).


hours = int(input('Enter hours:'))
rate =  int(input('Enter rate:'))
pay = (hours  * rate)+(hours/2)
def computepay(hours,rate):
    pay = (hours * rate)+(hours/2)
    return pay 

print(pay)


#4.Follow the stpes:

# First, def a function called cube that takes an argument called number.
# Make that function return the cube of that number (i.e. that number multiplied by itself and multiplied by itself once again).
# Define a second function called by_three that takes an argument called number. if that number is divisible by 3,by_threeshould call cube(number) and return its result. Otherwise, by_three should return False. -Check if it works.

'''
def cube(number):
    return number*number*number
    

def by_three(number):
    if(number%3 == 0):
        return cube(number)
    else:
        return False

print(by_three(3))
'''

#5. Define a function that accepts 2 values and return its sum, subtraction and multiplication.
'''

def arithematic(a,b):
    a = int(input("Enter value of a: "))
    b = int(input("Enter value of b: "))
    return sum(a,b),subtraction(a,b), multiplication(a,b)
    
def sum(a,b):
    return a+b
def subtraction(a,b):
    return a-b
def multiplication(a,b):
    return a*b
    
