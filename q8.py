for i in range(100,401):
    a=i//100
    b=(i-(a*100))//10
    c=(i-(a*100)-(b*10))
    if (a%2==0 and b%2==0 and c%2==0):
        print(f"{a},{b},{c}")
