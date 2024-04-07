salary =int(input("ENTER THE SALARY OF THE PERSON: "))
age = int(input("ENTER THE AGE OF THE PERSOON: "))


if(salary >= 20000) or (age <= 25):
    loan=int(input("loan amount:"))
    if(loan>50000): 
        print("maximum loan amount is 50000 only")
    else:
        print("you are eigible for loan") 
else:
    print("you are not eligible for the loan")


