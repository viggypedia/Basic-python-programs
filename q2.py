s1=str(input("Enter string one: "))
s2=str(input("Enter string two: "))
   
if(len(s1) != len(s1)):  
    print("Second string is not a rotation of first string");  
else:  
    try:    
        s1 = s1+ s1;  
          
        if(s1.index(s2)):  
            print("Second string is a rotation of first string");  
    except ValueError:  
            print("Second string is not a rotation of first string");  
