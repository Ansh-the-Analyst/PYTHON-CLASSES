#1stqn
"""
c=[cranes for cranes  in "cranes"]
print(c)
"""

#2nd qn
"""
c=['Ch','Dh','Eh','cb','Tb','Td','Chb','Tdb']
for i in c:
    if len(i)==2:
        print(i)
    else:
        continue
"""
#3rd
"""
def a(iplist):

   a = [iplist[i] for i in range(len(iplist)-1, -1, -1)]

   return a

iplist = ["python","embedded","automotive"]

print("The original list is - ", iplist)

print("The list after reversal is - ", a(iplist))
"""

# faulty calculator
# some calc should be 45*3=555, 56+9=77, 56/6=4
"""

print("---Faulty Calculator---")
num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
op = input("Enter operator to preform your operation : ")

if op == "+":
    if num1 == 56 and num2 == 9 or num1 == 9 and num2 == 56:
        print("Your addition is : 77")
    else:
        result = num1+num2
        print("Your addition is : "+str(result))

elif op == "*":
    if num1 == 45 and num2 == 3 or num1 == 3 and num2 == 45:
        print("Your multiplication is : 555")
    else:
        result = num1*num2
        print("Your multiplication is : "+str(result))

elif op == "/":
    if num1 == 56 and num2 == 6:
        print("Your division is : 4")
    else:
        result = num1/num2
        print("Your division is : "+str(result))

elif op == "-":
    result = num1-num2
    print("Your subtraction is : "+str(result))

else:
    print("Invalid Operation ! Exiting...")

"""
#with function


def again():
    def again():
        char=input("enter y to continue and n to stop")
        if char=="y":
            cal()
        else:
            print("Thank you for using my calculator")


def cal():
    print("---Faulty Calculator---")
    num1 = int(input("Enter first number : "))
    num2 = int(input("Enter second number : "))
    op = input("Enter operator to preform your operation : ")

    if op == "+":
        if num1 == 56 and num2 == 9 or num1 == 9 and num2 == 56:
            print("Your addition is : 77")
        else:
            result = num1+num2
            print("Your addition is : "+str(result))

    elif op == "*":
        if num1 == 45 and num2 == 3 or num1 == 3 and num2 == 45:
            print("Your multiplication is : 555")
        else:
            result = num1*num2
            print("Your multiplication is : "+str(result))

    elif op == "/":
        if num1 == 56 and num2 == 6:
            print("Your division is : 4")
        else:
            result = num1/num2
            print("Your division is : "+str(result))

    elif op == "-":
        result = num1-num2
        print("Your subtraction is : "+str(result))

    else:
        print("Invalid Operation ! Exiting...")

    again()
cal()



