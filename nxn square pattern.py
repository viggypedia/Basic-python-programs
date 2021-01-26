#printing a square block pattern of #
#Date: -26th-Jan-2021
#Input:- Number of rows and columns




n=int(input("Enter the number of rows and columns :-"))
for i in range (0,n):
    #print("\n")
    for j in range (0,n):
        print("#", end="")
    print("")
