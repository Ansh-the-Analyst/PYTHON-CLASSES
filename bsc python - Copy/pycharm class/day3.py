  #(while,create table,reverse digit,sum of n numbers,nestered while loop,print 1st 50 natural numbers,For,range)
##ITERATIVE(DAY3)
# infinite loop
"""
x=0
while x<6:
    print(x)
"""

# finite loop
"""
x=3
while x <=15:
    print(x)
    x=x+1
print("stop")
"""

# create table with while
"""
a=int(input("enter the tables you want"))
b=1
while b<=20:
    print('%d*%d=%d'%(a,b,a*b))
    b=b+1
    #b+=1
print("end")
"""

# reverse the digit
"""
x=73921
while x>0:
    tem=x%10
    print(tem,end="")
    x=x//10
    #x//=10
"""

# on different line
"""
x=73921
while x>0:
    tem=x%10
    print(tem)#or /n
    x=x//10
    #x//=10
"""

# sum of n numbers
"""
i=int(input("enter the number"))
add=0
n=1
while n<=i:
    add=add+n
    n=n+1
    #n +=1
print("the addition of i values is",add)
"""

# whileloop inside another whileloop(nestered whileloops)
"""
a=1
b=2
while a<=5:
    while b<=6:
        print(a,b)
        a+=1
        b+=1
"""
# display cranes 5 times using while loop
"""
a=1
while a<=5:
    print("the cranes")
.    a=a+1
"""

# display 1st 50 natural numbers using while loop
"""
a=1
while a<=50:
    print(a)
    a=a+1
"""

# for loop application1
"""
for letters in "bangalore":
    print(letters)
"""

# for loop application2
"""
for num in [8,9,45,9.0,"hi"]:
    print(num)
"""

# for loop application3
"""
a=[5,10,25,90,78,34,20]
add=0
for num in a:
    add=add+num
    #add+=num
print(f'the addition of a is{add}')
"""

# range syntax explanation
"""
range(starts,end,stepsize)
by default stepsize as 1
for i in range(10,0,-2):#it can be started from 0 to 10 also
    print(i)
"""

# range application to find the factorial of the given number
"""
x=int(input("enter the number"))
fact=1
for k in range(1,x+1):
    fact=fact*k
    #fact*=k
print(f'the factorial of the number is{fact}')
"""

# range application to check if divisible by 11 in the string
"""
new=[90,80,22,33,44,70,60,50,40]
for j in new:
    if j%11 ==0:
        print(j)
    else:
        print(0)
"""

# take a list of names and add hello to each name by iterating it with for loop
"""
name=["bean","kaaliya","raju","jaggu","chutki"]
for j in name:
    print(f'Hello {j}')
"""