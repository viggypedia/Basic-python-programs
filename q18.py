n=["0", "1","2","3","4","5","6","7","8","9"]
cnt=1
a=int(input("Enter your Phone number: "))
k=str(a)
for i in range(0,len(str(k))):
    if (n[i] not in k):
            print(n[i])
    else: 
        cnt+=1
if (cnt==10):
    print("All the digits are present in your phone number!")

