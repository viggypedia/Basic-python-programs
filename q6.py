a=eval(input("Enter a list of tuple: "))
a2=[]
for i in range(0,len(a)):
    t=()
    if(a[i]!=t):
        a2.append(a[i])
print(f"Ther remaining list of non-empty tuples: {a2}")
