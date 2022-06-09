t=0
#Enter all the elements in the format [1,2,3]
l=eval(input("Enter the elements: "))
n=len(l)
for i in range(0,n-1):
    if (l[i]==l[i+1]):
        t+=1
if t==n-1:
    print("All the values are of same values.")
else: 
    print("All the values are not the same.")
