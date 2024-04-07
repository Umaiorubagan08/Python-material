
a = int(input("NUMBER 1:"))
b = int(input("NUMBER 2:"))
operation=input("CALCULATOR=(add/sub/mul/div/modulus):")

            
if(operation=="add"):
    print(a+b)
elif(operation=="sub"):
    print(a-b)
elif(operation=="mul"):
    print(a*b)
elif(operation=="div"):
    print(a/b)
elif(operation=="modulus"):
    print(a%b)
else:
    print("Invalid operation")
    
