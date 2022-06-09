s= str(input("Enter a string: "))
l,d=0,0
for i in range(0,len(s)):
    if (s[i].isalpha()==True):
        l+=1
    elif (s[i].isdigit()==True):
        d+=1
print(f"Letters: {l}\nDigits: {d}")
