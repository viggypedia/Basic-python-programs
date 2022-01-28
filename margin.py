import math

import os


try:
    import pyfiglet
except ImportError as e:
    os.system("pip install pyfiglet") 
fig=pyfiglet.figlet_format("Attendence Manager")
print(fig)

def calc(no_p,no_a):
    margin=(no_t*(0.75))-(no_t-no_a)
    percent=((no_t-no_a)/no_t)*100
    if(margin<=0):
        print("Your attendece percent is: ",round(percent,2))
        print("The margin is: ",round(margin*(-1)))
    else:
        print("Your attendence percent is: ",round(percent,2))
        print("Yout attendence is below 75%.")

t=0
while(t==0):
    print("------------------------------------------------------")   
    y=["y","Y","Yes","yes","YES"]
    n=["n","N","No","no","NO"]
    no_t=int(input("Enter the total hours: "))
    no_a=int(input("Enter the absent hours: "))
    calc(no_t,no_a)
    print("------------------------------------------------------")

    a=str(input("Do you want to exit(y/n): "))
    if a in y:
        t=1
    else:
        t=0
