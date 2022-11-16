#(List,accesinglistusingindex,slicingandfunctionsoflist(len,sum,max,min),appendinsertextend,popremove,stack,queue,LinearSearch)
#list
#refer cranes varsity video in youtube
#to check the type of the list we use print(type(var_name))
#to check the length of the list we use print(len(var_name))
#list can also be of mixed type

#this list contains only one type of data

'''
a=[67,78,78,]
print(type(a))
print(len(a))
'''

#this type of list also contains one type of data
'''
b=["ram","shyam","manu"]
print(type(b))
print(len(b))
'''

#this list contains mixed type of the data in its list
'''
c=[87,90.0,"hello"]
print(type(c))
print(len(c))
'''

#accessing the list using index
#here we use indexing method as[0,1,2,3,4,]
#negative index also is there and goes from -1 to n whereas other is from 0 to n-1
'''
marks = [12,21,23,32,44,43]
n = len(marks)
print(marks[n-1])
print(marks[-1])
'''

#slicing(extract the 1st 3 elements)
'''
marks = [12,21,23,32,44,43]
print(marks[2 : 5])
'''

# Functions in list
'''
num = [12,45,67,89,43,43,2,3,13]
a = ["Anzi","Bini","Cyra","Desi","Eliya","Sam","Xam"]
mix = [12,45,67,89,43,"Anzi","Bini","Cyra"]

print(len(num))
print(len(a))
print(len(mix))
print(sum(num))
'''
'''
print(sum(a))
print(sum(mix))
'''
'''
m = max(num)
print(f"The largest number in {num} = {m}")
print(max(num))
s =max(a)
print(f"The largest sting in {a} = {s}")
'''

'''
t=max(mix)
print(f"The largest sting in {mix} = {t}")

y = min(num)
print(f"The smallest number in {num} = {y}")

ys = min(a)
print(f"The smallest string in {a} = {ys}")

yes = min(mix)
print(f"The smallest number in {mix} = {yes}")
'''
#adding 2 lists of type string and int
"""
 
d=[2,2,3]
res =d*4
print(res)
"""

#append,insert,extend
"""
adding the elements in list
append(ele)
insert(index,ele)
extend(seq)
"""
'''
new=[1.34,67,89,33,11]
new.append(100)
print(new)
new.append(330)
print(new)
d=[]
for i in range (1,21):
    d.append(i)
print(d)
new.insert(5,1000)
print(new)
new.insert(-3,87)
print(new)
'''

#appending in empty list
"""
d=[]
for i in range(1,21):
    d.append(i)
print(d)
new.insert(5,1000)
print(new)
new.insert(-3,87)
print(new)
a=int(input("enter the number to insert"))
b=[]
for i in range(0, a):
    x = int(input("enter the elements"))
    b.insert(i,x)
print(b)
"""

#extend
'''
a=[8,9,5,6,7]
b=[23,44,55,66]
a.append(b)
print(a)
a.extend(b)
print(a)
'''

#deleting the elements from the list
#pop(index)
#remove(ele)
'''
b=[6,89,80,99,97,67,66,55]
b.pop(3)#it will delete acc to the index 3rd one
print(b) 
b.pop(-5)
print(b)
#b pop(9) error
print(b)
b.remove(66)
'''

#stack
'''
stack=[]
while True:
    ch=input("1.push 2.pop 3.display 4.quit")
    if ch=="1":
        ele = int(input("enter the elements into stack"))
        stack.append(ele)
    elif ch=="2":
        ele = stack.pop()
        print("the deleted element is", ele)
    elif ch=="3":
        print("the stack elements are",stack)
    else:
        break
'''

#implementing a queue using list functions
'''
queue=[]
while True:
    ch=input("1.push 2.pop 3.display 4.quit")
    if ch=="1":
        ele = int(input("enter the elements into queue"))
        queue.append(ele)
    elif ch=="2":
        ele = queue.pop(0)
        print("the deleted element is", ele)
    elif ch=="3":
        print("the queue elements are",queue)
    else:
        break
        
'''

#linear search
#it will search an element in a list one by one
#works in a true or false condition(compare it with the elements in the list)
'''
n=int(input("enter the element"))
arr=[]
for i in range(n):
    print(f'enter the {i} element')
    x = int(input())
    arr.append(x)
print("the elements in arr is" , arr)
key = int(input("enter the elements to find"))
for i in arr:
    if i==key:
        print("the elements is found")
        break
else:
    print("the element is not found")
'''