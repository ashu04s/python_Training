list =[1,2,3,4,2,3]
list2 =[1,2,4,5]
new =[]
for i in list:
    if i not in list2 and i not in new:
        new.append(i)
print(new)            