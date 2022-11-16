#day7
"""
b=[4,5,6,7,8,9,12,13,14,4,5,5,5,4]
res=b.index(9)#inbuilt function to find the index number of the input
print(res)
ans=b.count(5)#used to count how much time the input is occuring in the list
print(ans)
city=["bangalore","mumbai","ooty","wayanad","hampi","agra","goa"]
print(sorted(city))#sort according to the alphabetic order
print("reverse",sorted(city,reverse=True))#if we give reverse=true it will print in the descending order of the alphabetic order
city.sort(key=len,reverse=False)#it is sorted according to the len of the string from less tto big
print(city)
city.sort(key=len,reverse=True)#here it prints according to the strng length from big to small
print(city)
"""

#list inside a list
"""
n=[[3,4,5],[2,9,45],[90,80,70]]
print(n[2][1])
print(n[1][0])
print(n[0][0])
total=[]
for i in n:
    total.append(sum(i))
    print(total [-1])#-1 gives it in another lines.try without it too.
print("total list added value is",sum(total))
"""

#zip(it makes tuples and makes pair together)
"""
sno=[1,2,3]
animals=["lion","deer","dog","cat"]
kids=["cub","fawn","puppy","kitten"]
ans=zip(sno,animals,kids)
#print(lis(ans))
#if there are no correct pairs it will omit it
for i in ans:
    print(i)
print(type(ans))
"""

#any and all
# (any:-if anyone of the value is true it  will return true or it will return false)
#(all:-all the value should be true then only it will return true or it will return false)
#inorder to check somme conditions we can use this
"""
print(any([True,True]))
print(any([True,False,False]))
print(any([False,False,False]))
print(all([True,True]))
print(all([True,False,False]))
print(all([False,False,False]))
"""
#eg of any and all
"""
x=[]
y=[]
for i in range(1,11):
    x.append(i)
for i in range(0,10):
    y.append(x[i]%5==0)
print(y)
print(any (y))
print(all(y))
"""

#list comprehension(writing in the short or the reduced format)
#syntax for it is as follows
#expression for items in iterables
"""
a=[3**i for i in range(1,6)] #1st we add into the list
print(a)
b=[x for x in range(1,11)if x%3==0]
print(b)
c=[y if y%2==0 else "odd" for y in range(1,21)]
print(c)


import math
num = [4,9,16,25,36,49,81,64,100,121]
x=[math.sqrt(n) for n in num]
print(x)`
y =[[math.sqrt(n) for n in num if n%5==0]]
print(y)
z=[math.sqrt(n) if n%2==0 else n+1 for n in num]
print(z)
"""

#tuple
"""
#it is similar to list
#it is collection of mixed data types
#it is denoted by () and each and every elements are seperated by commas
#it is ordered and immutable
#() is optional.even if we wont give it interpreter will take it as a tuple
#tuple cannot be assigned a attribute value
c=(8,9,67,56,"python",4.5,2.2)
print(type(c))
#if we give only a number it will take take the value as an integer even if we give it inside a bracket
##to get as a tuple we should give it a comma along the integer
d=(9,)
print(type(d))
"""

#class assignment(write a prgm to access the tuples using the index values
#how to have concatination reptative, tuple slicing
#try index, count functions in tuples.
"""
a=(23,45,63,45,67,35,45)
b=(4,5,6,7,8,9)
#tuples using index value
print(a[2])
print(a.index(63))
#slicing
print(a[2: 5])
#count functions
count=a.count(63)
print(count)
#concatinate
c=a+b
print(c)
#repetation
d = b*5
print(d)

#additional tuple programs
e = (34,67,32,45,89,97,12,45)
print(len(e))
print(e[6])
print(e[3:6])
print(e[:4])
print(e[3:])
print(e[-1])
print(max(e))
print(min(e))
print(sum(e))
"""

#(same qn bini prgrm)
"""
#index values
a = (23,34,4,1,3,67,89,"Hello",3,3,3,3)
print(a.index(67))
#count
print(a.count(3))
b = (34,67,34,"Hi")
#concatenate
c = a + b
print(c)
#repeatation
d = b*5
print(d)
#tuple slicing
e = (34,67,32,45,89,97,12,45)
print(len(e))
print(e[6])
print(e[3:6])
print(e[:4])
print(e[3:])
print(e[-1])
print(max(e))
print(min(e))
print(sum(e))
"""

#Strings(it is a sequence of characters
#it is denoted single quotes or in double quote
#it is stored in unique text formats(utf)       (interview qns)
"""
a="bangalore city"
print(type(a))
#index,count,slicing
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
print(a[5])
print(a[6])
print(a[6])
#count
print(a.count("a"))
#slicing
print(a[3:6])
"""

#string functions
"""
y=" this is BAsic Python cLASS "
print(y.upper())#All converted to uppercase
print(y.lower())#all converted to lowercase
print(y.title())#only starting word is capitilised
print(y.swapcase())#uppercase swapped to lowercase and vice versa
print(y.strip())#removoes the space after and before " in beginning and end
print(y.lstrip())#removes the left side beginning space
print(y.rstrip())#removes the right side end space
print(y.capitalize(y))#upper changed to lower
print(y.replace("A","e"))#replace A to e
"""