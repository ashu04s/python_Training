list1=[1,2,3,4,2,1,2]
list2 =[1,2,3,4,12]
list3=[1,2,3,4,5,23,1,21]
new=[]
for i in list1:
    if i in list2 and i in list3 and i not in new:
        new.append(i)
        
print(new)        