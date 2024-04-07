#Simple calculator

a=int(input("Enter a number a ="))
b=int(input("Enter a number b ="))
operation=input("add/sub/mul/div:")

if(operation=="add"):
    print("THE ADDITION OF TWO NUMBERS =",a+b)
elif(operation=="sub"):
    print("THE SUBTRACTION OF TWO NUMBERS =",a-b)
elif(operation=="mul"):
    print("THE MULTIPLICATION OF TWO NUMBERS =",a*b)
elif(operation=="div"):
    print("THE DIVISION OF TWO NUMBERS =",a/b)
else:
    print("NO OPERATION WAS FOUND")

# completed the mini calculator
