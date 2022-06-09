def func(num):
    sum=0
    while(num>0):
        sum+=num%10
        num//=10
    return sum



if (__name__=="__main__"):
    inp=int(input("Enter a number: "))
    temp=inp
    while temp>0:
        temp=temp-func(temp)
        print(temp)
