t1=(11,2,3,14)
t2=(13,5,22,10)
t3=(12,2,3,10)
if(len(t1)==len(t2) and len(t2)==len(t3)):
    print("(",end=" ")
    for i in range(0,len(t1)):
        print(t1[i]+t2[i]+t3[i],end=" ")
    print(")")
else:
    print("Enter tuples with equal lengths.")
        

