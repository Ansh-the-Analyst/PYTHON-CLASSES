#Day 8
#finding upper digit and space in a string
"""
new=input("enter the string")
print("the length of the given string is",len(new))
upper=0
digit=0
space=0
for j in new:
    if j.isupper()==True:
        upper += 1
    elif j.isdigit() == True:
        digit += 1
    elif j.isspace() == True:
        space += 1
print(f"the upper case are {upper}")
print(f"the digit case are {digit}")
print(f"the space case are {space}")
"""

#split(seperator,max split)Seperator-splits according to the seperator.Max split-how much we want to split.or how much we dont want
#join
"""
a = "cricket*soccer*chess*ludo*kungfu"
res=a.split("*",2)
print(res)
b ="machine learning"
ans = "@".join(b)
print(ans)
"""

#map (function, iterables)
"""
n = [10,20,30,40,50]
ans1 = map(str, n)
print(ans1)#by this we wont get the values in the n so we need to typecast the n
print(list(ans1))#here we typecast n into list so we get the values in list
print(type(ans1))
"""

#Anagram words(same words in alphabetic order)
"""
x1=input("enter the string 1")
x2=input("enter the string 2")
if sorted(x1) == sorted(x2):
    print("this is anagram words")
else:
    print("this is not anagram words")
"""

#order and character
#ord - returns a unicode from given character
#chr - returns the string from unicode
"""
s="l"
print(ord(s))
h=90
print(chr(h))
"""

#Ascii value (practise from ascii value)
"""
new = input("enter the string")
buf = [True]*128
for j in new:
    if buf[ord(j)] == True:
        buf[ord(j)] = False
    else:
        print("duplicate elements are present")
        break
else:
    print("all the elements are unique")
"""
#Panagram sentence(eg:-The quick brown fox jumps over a lazy dog)
"""
data=input('enter the string')
data = data.upper()
tem = [False]*26
for i in data:
    if i.isalpha():
        tem[ord(i)-65]=True
if all(tem):
    print("this is panagram sentence")
else:
    print("this is not a panagram sentence")
"""

#(set)
#set can be of mixed type & its not ordered(unordered) & muttable
#it is denoted by {} and each elements are seperated by commas
#it does not support index & empty set cannot be created
#DOESNOT ALLOW REPETATION OF ELEMENTS
"""
a={8,7,9,4,5,"cat",89.98}#mixed datatype list 
print(type(a))
print()
c={}#empty set but it shows as dict whn checking its type
print(type(c))
k = set()#if we want a set then we have to declare it as a set then we can make an empty set
print(type(k))#this will show a set type
k.update([7,9,23,"dog",23,12])#if we update it gets added to the list
print(k)
k.update("cranes")#here each word gets mixed up with the list.inorder to get it as a string we have to do below code
print(k)
k.update(["cranes"])
print(k)
k.discard(90)#discard shows no error even data is from outside
print(k)
k.remove(90)#will throw error if we enter the value which is not present in the list
print(k)
"""
#set
"""
a={1,2,3,4,5,6,7}
b={9,10,2,5,11,7}
print(a|b)
print(a&b)
print(a-b)
print(b-a)
print(a^b)

"""

#find out non-players from 2 list
"""
students={"anson","ansh","shyam","sidique","mohanlal","mamooty"}
cricket={"mohanlal","ansh","mamooty"}
print("the non player students are",students-cricket)
"""

#find out the allrounders from 2 lst
"""
batsman={"gayle","sachin","anson","ali","samcurran","dhoni"}
baller={"gayle","anson","ali","samcurran",}
print("the all-rounders in your team are",batsman&baller)
"""


# isdisjoint--->returns true if there is null intersection
# issuperset-->returns true if the set contains itself
# issubset---->returns true if the set is derived from the other set
"""
num= {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15}
even={2,4,6,8,10,12,14}
odd={1,3,5,7,9,11,13,15}
print(even.isdisjoint(odd))#it will return true or false.there will be no intersection(even is disjoint of odd
print(num.isdisjoint(even))
print(odd.issuperset(num))#main set.here num is superset of even and odd
print(odd.issuperset(even))
print(num.issubset(odd))
print(even.issubset(num))
"""

