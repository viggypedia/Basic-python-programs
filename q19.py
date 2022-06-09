def func():
    a=int (input("Enter the number:"))
    b=int(str(a)[::-1])
    c=str(a+b)
    for i in range(0,len(str(c))):
        if(str(c[i]==str(str(c)[-(i+1)]))):
            print(c)
            break
        else: 
            func()
func()
