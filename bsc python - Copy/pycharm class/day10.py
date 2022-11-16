#in except block inorder to check the error in the try we are declaring it into a variable t so that we can see the error type present in the try
#same way we declare different errors into differentt variables
#if we have not declared
#EXCEPTION can be used for this.Instead of giving one by one we can assign this one so it will handle all types of error at a time

#nameerror defined
"""
try:
    a = 4
    b = 3
    print(c)
except NameError as t:
    print("error", t)
finally:
    print("hello")
    print("end")
"""


#defining 2 and more errors and EXCEPTION(doubt)
"""

try:
    a = int(input("enter the number a"))
    b = int(input("enter the number b"))
    print(a/b)
    
except ZeroDivisionError as d:
    print("0 cant be given", d)
except ValueError as e:
    print("str not allowed", e)
except Exception as y:
    print("error", y)
"""

#File handling concepts
#in python a file operation takes place in foll order (open a file,read or write,close the file)



#opening a file(following is the order to perform a opening of file)
#if we rerun the program of write (1st prgrm) the previous written text will overwritten the new data will be present in mach.txt
#when we use read the data will be displayed in the console itself
#readline:-it is used to read the 1st line. and the [5] gives the word in that sentence
#readlines:-it will read the data in the file in the form of list and the [2] in the bracket will print the second line in the file if we give [2][6] then prints the 2nd line 6th word
"""
r-open a file for reading.(default)
w-open a file for writing.Creates a new file if it does not exist or truncates the file if it exists(it will only hold a string)
x-open a file for exclusive creation.if the file already exists the operation fails
a-open for appending at the end of the file without truncating it.Creates a new file if it does not exist.
+:-open a file for updating(reading and writing)
"""

"""
try:
    h=open("mach.txt", "w")#w represents write
    print("file has opened successfully")
    res = h.write("today is friday.")#if after running we alter the sentence then it will be overwritten
    print(res)
    h.close()
except:
    print("file has not opened")
"""

"""
try:
    h=open("mach.txt", "r")#r represemts read
    print("file has opened successfully")
    res = h.read()
    print(res)
    h.close()
except:
    print("file has not opened")
"""

"""
try:
    h=open("mach.txt", "r")#r represemts read
    print("file has opened successfully")
    res = h.readline()[3]
    print(res)
    h.close()
except:
    print("file has not opened")
"""

"""
try:
    h=open("mach.txt", "r")#r represemts read
    print("file has opened successfully")
    res = h.readlines()[2]
    print(res)
    h.close()
except:
    print("file has not opened")
"""

"""
try:
    h=open("mach.txt", "r")#r represemts read
    print("file has opened successfully")
    res = h.readlines()[2][3]
    print(res)
    h.close()
except:
    print("file has not opened")
"""


#append and exclusive function(when we need to add a fn and we use write overwritng occurs so we use append function)
#"a" is append mode
#exclusive is used to check the file name which we are giving is not present before.if it is present it would throw a error.only new files while be created.
"""
try:
    g = open("mach.txt","a")
    print("opened successfully")
    for i in range(6):
        res = g.write("this is example line %d\n" %(i+1))
    g.close()
except:
    print("file is not opened")
"""

#exclusive
"""
try:
    c=open("cat.txt", "x")
    print("ok")
except:
    print("error in opening the file")
"""


#Position of cursor or filehandler position (for that tell is used)
"""
try:
    s=open("cat.txt","w")
    print(s.tell())
    info=8719#the no of characters or numbers we give decide the cursor position(inside the file cat.txt)
    s.write(str(info))
    print(info)
    print(s.tell())
    s.close
except:
    print("position of cursor cannot be detected")
"""

#seek function(used to change the position of file handle)
#2 parameters(offset,from_what or whence)
#using seek we give "rb","r+b" (b is binary)

#offset
#whence holds the value 0,1,2 and if we give 3 and above it will give error
#0->beginning of the file,1-->current position of the file,2-->end of the file
#giving 0 and 1 is same both has same output
"""
c=open("cat.txt","r+b")#r+b is used for seek
c.seek(3,0)#here 2 is the whence value.we can give only 0 1 & 2 &(3 is the offset here)
print(c.tell())
print(c.readlines())
print(c.tell())
c.close()
"""

#sys:- sys is used to access the

import sys
try:
c = open("cat.txt" , "r+b")
size = seek(3 , 2)
print(size)
except:
print(sys.exc_info()[0] , sys.exc_info()[1])

#lambda and filter function
#lambda can be used instead
#lambda(argument : single expression)
#lambda (arguments : single expresion)

a = lambda a , b , c:a+b-c
print(a( 6 , 3 , 1))

#filter(function , iterables)
e = [ 9,7,6,5,2,8,4,12]
res = filter(lambda x: x>=6 , e)
print(list(res))
y= [ 9,80,7,56,45,30,20,10]
even = list(filter(lambda y :y%2==0 , y))
double =list(map((lambda y:y+y) , even))
print(even)
print(double)


#filter function filters out the iterables
arr = [ 7 ,8 , (8,9,3)]
print(arr)
print(len(arr))
print(type(arr))
arr.append( 100)
print(arr)
print(len(arr))
k = (13 , 24,67 ,[9 ,4 ,3])
print(type(k))
print(len(k))
#k.append( 7)
#print(k)
k[3][2]= 90
print(k)
k[3].append(200)
print(k)

#program using both



#enumerate(interview question)
#it will have 2 parameters(iterable, start)
#by default it start with 0
n=[8,9,2,3,4,45,89,22,1]
for i in enumerate(n , 10):
    print(i)