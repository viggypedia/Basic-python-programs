import math


def calc(no_p,no_a):
    margin=(no_t*(0.75))-(no_t-no_a)
    percent=((no_t-no_a)/no_t)*100
    if(margin<=0):
        print("Your attendece percent is: %.2f ",percent)
        print("The margin is: ",margin*(-1))
    else:
        print("Yout attendence is below 75%.")
print("$$$$$$$$$$$$$$$$$$$$")
no_t=int(input("Enter the total hours: "))
no_a=int(input("Enter the absent hours: "))
calc(no_t,no_a)
print("$$$$$$$$$$$$$$$$$$$$")

