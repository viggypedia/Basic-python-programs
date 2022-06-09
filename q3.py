import random
n= int(input("Enter a number: "))
s=""
for i in range(0,n):
    s+=str(random.randint(0,1))

print(f"The random binary number generated is: {s}")
