def func(num):
    flag=False
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                # if factor is found, set flag to True
                flag = True
            
                break
    if flag:
        return (False)
    else:
        return(True)

k=func(num=int(input("Enter a number: ")))
if k==False:
    print("Not a prime number")
else:
    print("Prime number")

    

