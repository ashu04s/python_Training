list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
new =[]
for i in list1:
    if i in list1 and  i not in list2:
        new.append(i)
    else:
        pass  
for i in list2:
    if i in list2 and  i not in list1 and i not in new:
        new.append(i)
    else:
        pass    
    
print(new)      