a=eval(input("Enter a list: "))
cnt=0
for i in range(0,len(a)):
    
    if (type(a[i])!=tuple):
        cnt+=1
    else:
        break
print(f"The count of elements till a tuple occured is {cnt}")
