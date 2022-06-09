a=(input("Enter the text: "))
cnt=0
for i in range(0,len(a)):
    if (a[i].isalpha()==True):
        cnt+=1
        

print(f"The number of characters in the given text: {cnt}")

