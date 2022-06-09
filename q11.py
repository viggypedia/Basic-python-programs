a=eval(input("Enter a list: "))
l=len(a)
def func(a,l):
    for i in range(0,l):
        if a[i]%2==0:
            print(a[i],end=" ")
func(a,l)

