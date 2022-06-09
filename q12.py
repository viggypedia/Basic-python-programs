a=str(input("Enter a string: "))
l=len(a)
def func(a,l):
    cnt=0
    for i in range(0,l):
        if (a[i]==a[-(i+1)]):
            cnt+=1

    if cnt==l:
        print("The given string is a pallindrome.")
    else:
        print("The given string is not a pallindrome.")
func(a,l)
