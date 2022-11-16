#dictionary
#it is unordered collection of data and mutable
#it has key and value pairs and it is denoted by {} and are seperated by commas
#eg---->a={1:"cat", 2:"dog}#the dict should always contain both key and value pairs and it should not be empty

"""
c={1:"cat", "a":"dog"}
print(type(c))
d={}
print(type(d))#both will have class of dict
"""

#adding elements in dict
"""
c[3]= "bat"
print(c)#it will be added at 3
"""

#to add tuple
"""
d.update(da=90,ml=76,dl=45)#dict gets updated to this values and update it can be used for set and dict
print(d)
"""

#pop(here key value acts as index in dict so we should give key value to pop the data)
""" 
c.pop("a")
print(c)
"""

#delete(we give key value to delete)
"""
del d["ml"]
print(d)
"""

#in and not
"""
x={1:1,2:4,3:9,4:8,5:25,6:36}
print(1 in x)
print(25 in x)
print(9 not in x)#not shows true or false value 
print(3 not in x)
print(x[1])
print(x["da"])
"""

#in dict while get ing only key values must be given or else.For set we dont have get attribute.
#new dict=to create a dict with no pair values we can use fromkeys
#pop is a function and delete is key
"""
e = {"apple":"green" , "yellow":"banana", "red":"cherry"}
ans= e.get("blue")#we should search with key and not with the value.for value it shows none
print(ans)
e={"apple","yellow","banana","red","cherry","blue"}
#ans=dict.fromkeys(e)#it will make a list from only values
#print(ans)
value= "fruits"
res1 = dict.fromkeys(e, value)
print(res1)
"""

#checking  the no of characters in a string(doubt)
"""
new = "machine learning projects in data science"
arr={}
for i in new:
    arr[i]= arr.get(i, 0)+1
for key in arr:
    print(key, arr[key])

#inorder to adapt the key and value pair we can use copy function.if we use= then if we delete 2nd dict 1st also gets deleted.
#if we add more elements in the main dict after copy then it wouldnt reflect in the 2nd dict
animal = {"dog":2, "rat":3, "bat":9}
new= animal.copy()
print(animal)
print(new)
new.clear()
print(new)
print(aminal)
animal["hen"]=8
print(animal)
print(new)
"""

#dictionary
#pop() without index cant be used like in stack.we need to use popitem() in dict to delete the last
#data.items #(items) will return us the values of the dict as tuples
"""
city={"karnataka":["bangalore","hampi","mysore"],"andra":["tripathi","vizag","kurnool"],"maharashtra":["mumbai","pune"]}
print(city.keys())
print(city.values())
print(city["karnataka"])
data={1:{"animal":"rabbit","name":"bunny","food":"carrot"},2:{"animal":"dog","name":"scody","food":"bones"},3:{"bird":"parrot","name":"moji","breed":"cukatoo"}}

#access the elements
print(data[1]["animal"])
print(data[2]["food"])
print(data[3]["name"])

#adding the element
data[4]={}#we should make an empty dictionary then we have to add an element in the dictionary
data[4]["bird"] = "eagle"
data[4]["name"] = "peggy"
print(data)

#deleting the elements
data.popitem()
print(data)
data[2].pop("food")
print(data)
del data[3]["bird"]
print(data)
del data[2]
print(data)

#displaying the elements
for i , info in data.items():
    print("\n id:", i)
    for key in info:
        print(key,":", info[key])
"""

#Types of error in python(refer classroom 21th july dict class)
#assert is used to check our condition.whenever conditions are not met then this error
#attribute: whenever we use function we dont have for that particular
#nameerror;undefined variable is tried to access


"""
AssertionError Raised when an assert statement fails.
AttributeError Raised when attribute assignment or reference fails.
EOFError Raised when the input() function hits end-of-file condition.
FloatingPointError Raised when a floating point operation fails.
ImportError Raised when the imported module is not found.
IndexError Raised when the index of a sequence is out of range.
KeyError Raised when a key is not found in a dictionary.
KeyboardInterrupt Raised when the user hits the interrupt key (Ctrl+C or Delete).
NameError Raised when a variable is not found in local or global scope.
OSError Raised when system operation causes system related error.
OverflowError Raised when the result of an arithmetic operation is too large to be represented.
SyntaxError Raised by parser when syntax error is encountered.
IndentationError Raised when there is incorrect indentation.
SystemExit Raised by sys.exit() function.
TypeError Raised when a function or operation is applied to an object of incorrect type.
ValueError Raised when a function gets an argument of correct type but improper value.
ZeroDivisionError Raised when the second operand of division or modulo operation is zero.'''
"""

#try,except & finally
#in try if there is an error then it wont show a error and it would jump to except and then it would jump to finally
#in except we should give proper code or it wont jump to finally
"""
try:
    a = 4
    b = 8
    print(a+b)
except:
    c=90
    d=90
    print(u)
    print("error")
finally:
    print("hello world")
"""