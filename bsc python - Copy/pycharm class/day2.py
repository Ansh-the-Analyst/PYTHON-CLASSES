#(If,Ifelse,elif)
# if
#Q) if the customer purchases above 2000 then give discount of 25% or else print the total bill amount
"""
item_cost=float(input("enter the purchased amount"))
if item_cost >=2000:
    discount=25
    offer=(discount/100)*item_cost
    item_cost=item_cost-offer
    print("the discount amount is",offer,"!!!!")
else:
    print("the total bill is",item_cost)
"""

# if assignment(
"""
scored_marks=int(input("enter the scored marks by the student"))
if scored_marks<50:
    print("the student has failed the test")
if scored_marks>=50:
    print("the student has passed the exam")
"""

# ifelse (no conditions can be given in else)
"""
a=int(input("enter the a"))
if a>=0:
    print("this is a positive number")
else:
    print("this is a negative number")"""

"""I=int(input("enter the number to check"))
if(I%9==0):
    print("this is a multiple of 9")
else:
    print("this is not a multiple of 9")

"""
# ifelse (assignment)
"""
word=(input("enter the word to check if vowel"))
if (word=='a' or word=='e' or word=='i' or word=='o' or word=='u'):
    print("this is a vowel")
else:
    print("this is not a vowel")
"""

# elif
"""
a=int(input("enter the number"))
ifa>0:
    print("this is a positive number")
elif a<0:
    print("this is a negative number")
else:
    print("this is zero")
 """

# elif(assignment)
"""
age=int(input("enter the age"))
if age>=18 and age<25:
    print("you are eligible to vote only")
elif age>=25:
    print("you are eligible to vote and participate in elections")
else:
    print("your are not eligible")
"""

# exercise
"""
year=int(input("enter the number of days in the given year"))
if year%4==0 and year%100 !=0:
    print("the given year is a leap year")
elif year%4==0 and year%100==0 and year%400==0:
    print("the given year is a leap year")
else:
    print("the given year is not a leap year")
"""
# Assignment is given in the gclassroom