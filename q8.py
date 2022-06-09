a=[[(9,15),(7,9)],[(11,1),(22,19)]]
x=[]
z=[]
for l in range(len((a)[0][0])):
    for i in range(len(a)):
        for j in range(len((a)[i])):
            z.append(a[i][j][l])
        x.append(tuple(z))
        z=[]
print(x)
