#normal program to count even

for i in range(1,11):
    if(i%2==0):
        print("EVEN NUMBER = ", i)

for i in range(1,11):
    if(i%2==1):
        print("odd number = ",i)


even_count=0
odd_count=0
for i in range(1,11):
    if(i%2==0):
        even_count=even_count+1
    else:
        odd_count=odd_count+1
print("Even number count =", even_count)
print("odd number count =", odd_count)
