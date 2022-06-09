a=eval(input("Enter a list: "))
l=[]
for i in range(0,len(a)):
    if a[i] not in l:
        l.append(a[i])
h=len(l)
print(f"The no of unique values are: {h}")
