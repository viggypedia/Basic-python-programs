n= int (input("Enter the number of stars: "))
for i in range(0,n+1):
    for j in range(0,i):
        print("*",end=" ")
    print("\n")

for i in range(n-1,0,-1):
    for j in range(0,i):
        print("*",end=" ")
    print("\n")
