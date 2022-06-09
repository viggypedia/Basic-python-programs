s1=str(input("Enter a string: "))
s2=""
for i in range(0,len(s1)):
    if(s1[i].isdigit()==True or s1[i].isalpha()==True or s1[i]==" "):
        s2+=s1[i]
s1=s2
print(s1)
