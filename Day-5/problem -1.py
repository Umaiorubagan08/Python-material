Score = int(input("ENTER THE SCORE PERCENTAGE:"))


if(Score>=70):
    name=str(input("NAME: "))
    department=str(input("DEPARTMENT: "))
    location=str(input("LOCATION: "))
    print((name,department,location),"YOU ARE ELIGIBLE")
else:
    print("YOU ARE NOT ELIGIBLE")
