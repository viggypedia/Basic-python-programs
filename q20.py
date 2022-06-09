a=eval(input("Enter list: "))
print(f"Length of the series: {len(a)}")
print("Elements from last till third last: ")
n=len(a)
sum=0
for i in range(2,n-2):
    print(a[i],end=" ")
for i in range(0,n):
    sum+=a[i]
print("\nSum=",sum)

