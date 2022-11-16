"""
count = 0

def first(x):
    global count
    if x == 1:
        count += 1
        print("count=",count)
    else:
        print("count=",count)
    x += 1
def second(x):
    global count
    if x == 1:
        count +=1
        print("count=",count)
    else:
        print("count=",count)
    x += 1
def third(x):
    global count
    if x == 1:
        count += 1
        print("count=",count)
    else:
        print("count=",count)
    x += 1
def fourth(x):
    global count
    if x == 1:
        count += 1
        print("count=",count)
    else:
        print("count=",count)
    x += 1
x = int(input("enter the number"))
first(x)
second(x)
third(x)
fourth(x)
"""

'''x = [1,2,3,4,5,6,7,8,9]
nwlst = [i for i in x if i%2 !=0 ]
print(nwlst)'''

"""Get only numbers in sentences like
'in 1984 there were 13 instances of a protest with over 1000 people attending """
"""
a =  "in 1984 there were 13 instances of a protest with over 1000 people attending"
numdata = [x for x in a if x.isnumeric()]
print(numdata)
"""
"""
a =  "in 1984 there were 13 instances of a protest with over 1000 people attending"
numdata = [x for x in a.split() if x.isnumeric()]
print(numdata)
"""

"""
a =  "in 1984 there were 13 instances of a protest with over 1000 people attending"
numdata = [x for x in a.split() if x.isalpha() and len(x)<4]
print(numdata)
"""
"""
lst = []
for i in range(0,1001):
    n = str(i)
    for j in n:
        if j==3:
            lst.append(int(j))
        else:
            pass
print(lst)
"""
"""
lst1 = ['1','2','3','4','5','6']
lst2 = ['1','4','9','16','25','36']
square = dict(zip(lst1,lst2))
print((square))
print(type(square))
"""

inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}
inventory["pocket"] = {}
inventory["pocket"] = ["seashell","strange berry","lint"]
print(inventory)

inventory["backpack"] = sorted(inventory["backpack"])
print(inventory)

inventory["backpack"].remove("dagger")
print(inventory)

inventory["gold"] = "550"
print(inventory)
