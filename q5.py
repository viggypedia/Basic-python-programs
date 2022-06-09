r=int(input("Enter number of rows: "))
c=int (input("Enter number of coloumns: "))
a=[]
l=[]
for i in range(0,r):
    for j in range(0,c):
        a.append(i*j)
    l.append(a)
    a=[]
print(l)
