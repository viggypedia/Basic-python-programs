# File Name: ascii-chr-versa.py
# Purpose: To convert ascii code to its character and vice-versa
# Input: 1. Users choice 2.Ascii value 3.Character
# Output: 1.character for given ascii code 2.ascii code for given character
# Arguments: None
# Variables: i(users choice),a(ascii code input),b(chracter input)
# Calls :None
# Created By: S.Vignesh Nelakantan
# Creation Date: 30/08/2020
# Last Updated Date: 30/08/2020
# Recent Changes: 


#Menu Driven Program


#Converting ascii to chr and vice versa
d=0
x=0
while d!=10:
    print("To convert ascii code to charecter type 1")
    print("To convert charecter to its rescpective ascii code type 2")
    i=int(input("Enter your choice:-"))
    
    if i==1: #Converts Ascii Code to Equivalent Character
        a=int(input("Enter the ascii code:-"))
        print("The character of the ascii code",a,"is",chr(a))
        s=str(input("To exit type 1, to continue press 2 :-"))
        if s==1 or s==2:
            x=13
            break
            if int(s)==1:
                d=10
                break
            else:
                d!=10
                
                continue
                    
    elif i==2:
        b=str(input("Enter the charecter for which you want to find the ascii code:-"))
        print("The ascii code for the the character",b,"is",ord(b))
        v=input("To exit type 1, to continue press 2 :-")
        if int(v)==1:
            d=10
            break
        else:
            d!=1
        
    
    
