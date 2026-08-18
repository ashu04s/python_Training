# palendrome with using slice
str = input("enter any string")

str2 = ""
for i in str:
    str2 = i+str2
    
if str==str2:
    print("yes")    
    
else:
    print("no")        
            
        
