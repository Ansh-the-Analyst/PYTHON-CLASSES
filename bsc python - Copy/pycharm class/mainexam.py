#finding input prime or not
"""
n=int(input("enter the number you want to find prime or not"))
m= False
if n > 1:
    for i in range(2, n):
        if (n % i) == 0:
            m = True
            break
if m:
    print(n, "is not a prime number")
else:
    print(n, "is a prime number")
"""

#check the numbers from 10-50 which are odd or even
"""
n=10
for i in range(n,n+41):
    if i%2==0:
            print(f"{i} this is an even number")
    else:
        print(f"{i} this is odd number")
"""

#using dictionary add 2 and display the elements
"""
c={1:"cranes"}
c[2]="varsity"
print(c)
"""

#write a program making a pyramid
"""
n=5
for i in range(n+1):
    for j in range(i):
        print(i,end=" ")
    print()
"""

#find the area of the rectangle
"""
def again():
    char=input("enter y to continue and n to stop")
    if char=="y":
        area()
    else:
        print("Thank you for using my area calculator")


def area():
    l=int(input("enter the length of the rectangle"))
    b=int(input("enter the breadth of the rectangle"))
    print("the area of the rectangle is ",l*b)
    again()
area()
"""

