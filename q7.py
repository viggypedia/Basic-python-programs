a=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
b=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
c=["$","#","@"]
n=["1","2","3","4","5","6","7","8","9","0"]
z,y,x,t=0,0,0,0
s= str(input("Enter your current password: "))
if(len(s)<6 and len(s)<16):
    print("Not a valid password")
    exit
else:
    for i in range(0,len(s)):
        if (s[i] in a):
            z=1
        if (s[i] in b):
            y=1
        if (s[i]in c):
            x=1
        if (s[i]in n):
            t=1
    if (z==1 and y==1 and x==1 and t==1):
        print("Valid Password.")
        exit
    else:
        print("Not a valid password. ")
