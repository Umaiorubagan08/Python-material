SALARY =int(input("ENTER THE SALARY OF THE PERSON: "))
AGE = int(input("ENTER THE AGE OF THE PERSOON: "))


if(SALARY >= 20000) or (AGE <= 25):
    loan=int(input("LOAN AMOUNT:"))
# Nested loop
    if(loan>50000): 
        print("MAXIMUM LOAN AMOUNT IS 50000 ONLY")
    else:
        print("YOU ARE ELIGIBLE FOR LOAN ") 
else:
    print("YOU ARE NOT ELIGIBLE FOR LOAN")


