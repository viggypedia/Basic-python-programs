a=int(input("Enter a three digit number: "))
b=a%10
c=((a%100)-b)//10
d=a//100

print("All the possible combinations of the given number is: ")
print(f"{b}{c}{d}")
print(f"{c}{d}{b}")
print(f"{d}{b}{c}")
print(f"{b}{d}{c}")
print(f"{c}{b}{d}")
print(f"{d}{c}{b}")


