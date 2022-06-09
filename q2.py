import random 
c=random.randint(1,9)
while True:
    i=int(input("Guess a number: "))
    if (i==c):
        print("Well Guessed!")
        break
    else:
        print("Guess Again.")
