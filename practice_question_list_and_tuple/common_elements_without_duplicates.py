list =[1,2,3,4,2]
list2=[2,4,5,6,7]
new=[]
for i in list:
    for j in list2:
        if i==j and i not in new:
            new.append(i)
        else:
            pass    
print(new)        