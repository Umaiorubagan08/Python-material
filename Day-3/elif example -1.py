# Elif problem

Score = int(input())
if(Score<35):
    print("POOR STUDENT")
elif(Score>35 and Score<70):
    print("AVERAGE STUDENT")
elif(Score>70 and Score<100):
    print("GOOD STUDENT")
else:
    print("INVALID STUDENT")
