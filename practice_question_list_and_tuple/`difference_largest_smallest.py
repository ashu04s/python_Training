list = [1,2,3,4,2,10]
min =999
max =0
for i in list:
    if i>max:
        max =i
    elif i<min:
        min=i
    else:
        pass
  
print(f"max element is {max}")
print(f"min element is {min}")
print(f"difference bettwen both is {max-min}")
         
           