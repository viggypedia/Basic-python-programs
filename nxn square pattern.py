# File Name: nxn square pattern.py
# Purpose: To print a square block pattern of #
# Input: 1. Users choice 
# Output: 1.character for given ascii code 2.ascii code for given character
# Arguments: None
# Variables: n(users choice),i(loop number one),j(loop number two)
# Calls :None
# Created By: S.Vignesh Nelakantan
# Creation Date: 26/01/2021
# Last Updated Date: 26/01/2021
# Recent Changes: 






n=int(input("Enter the number of rows and columns :-"))
for i in range (0,n):
    #print("\n")
    for j in range (0,n):
        print("#", end="")
    print("")
