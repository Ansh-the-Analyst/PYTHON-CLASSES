#1st assignment
#2.checking the numbers are multiples of 3,5 ,3 and 5
"""
a=int(input("enter the value"))
if a%3==0 and a%5==0:
    print("the entered value is divisible by both 3 and 5")
elif a%3==0:
    print("the entered value is divisible by 3")
elif a%5==0:
    print("the entered value is divisible by 5")
else:
    print("the entered value is neither divisible by 3 nor 5)
"""

#3.check no divisible by 5 and 11
"""
a=int(input("enter the value"))
if a%5==0:
    print("the entered value is divisible by 5")
elif a%11==0:
    print("the entered value is divisible by 11")
else:
    print("the entered value is neither divisible neither by 5 nor by 11")
"""

#4.to check if square or not by input l and b values
"""
q=int(input("enter the length"))
r=int(input("enter the breadth"))
if q==r:
    print("the user is designing a square")
else:
    print("the user is designing a rectangle")
"""

#6.to find area of triangle
"""
b=int(input("enter the breadth of the triangle"))
h=int(input("enter the height of the triangle"))
print("the area of the triangle is",0.5*b*h)
"""

#7a.converting c to F
'''
c=int(input("enter the celcius value"))
print("the fahrenheit conversion is",(c*9/5)+32)
'''

#7b.converting F to c
"""
f=int(input("enter the fahrenheit value"))
print("the celcius conversion is",(f-32)*5/9)
"""

#5.shop discount based on unit

p=int(input("enter the quantity of units purchased"))
if p >= 10:
      discount_percent=10
      discount=(10/100)*(p*100)
      total_price=(p*100)-discount
      print("the total price is",total_price)
else:
    print("the total bill is",p*100)


#1.Salary bonus if yearofservice >= 5
"""
s=float(input("enter the present salary"))
x=int(input("enter the year of experience"))
if x >= 5:
    bonus=5
    increment=(5/100)*s
    total_salary=s+increment
    print("your total amount this month is",total_salary)
else:
    print("your total amount this month is",s)
"""


      


