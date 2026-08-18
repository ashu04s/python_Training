#second larest number in list
list =[1,2,3,5,64,342,23,0]
max=0
secondmax=0
for i in list:
    if i>max:
        max =i
    else:
        pass
for i in list:
    if i<max and i>secondmax:
        secondmax =i
    else:
        pass  
print(f"second largest number in list is {secondmax}")      