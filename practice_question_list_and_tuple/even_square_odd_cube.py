list = [1,2,3,4,2,1,2,6]
for i in range(len(list)):
    if list[i]%2==0:
        list[i]=list[i]**2
    else:
        list[i]=list[i]**3      
        
print(list)        