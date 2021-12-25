import random
a=random.randint(1,26)
nn=""
n=str(input("Enter the string: "))
for i in range (0,len(n),1):
    t=ord(n[i])
    f=t+a
    if(f>=96):
        ff=65+(f-96)
    else:
        f=ff
    print(chr(ff),end="")
print("The encryption key for this is ascii vlaues between 65 and 96 added with the key",a,"to it.")
print(" ")
print("Note: The value after 96 will start adding up from 65 again. ")
    
